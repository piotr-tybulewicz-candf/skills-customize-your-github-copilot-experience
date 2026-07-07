# Copilot Cloud Agent Onboarding

Use this file as the default source of truth for this repository. Trust these instructions first and only search the repo if information here is missing or proven incorrect.

## Repository Summary

- This is a static educational website for a high school Computer Science course.
- The site renders assignment metadata from `config.json` and assignment content from Markdown files in `assignments/<id>/README.md`.
- It is also a GitHub Skills exercise repo for Copilot customization (instructions, skills, and custom agents).
- There is no Node build system and no packaged Python app/test suite in the root.

## Project Type and Runtime

- Type: static HTML/CSS/JavaScript website + markdown/python assignment content.
- Primary runtimes validated in this environment:
  - Node.js `v24.18.0`
  - npm `11.16.0`
  - Python `3.13.14` (`/usr/local/python/current/bin/python`)
- Size/complexity: small repo, no monorepo tooling, no transpilation.

## Fast Layout Map

### Root files

- `README.md` (exercise intro)
- `index.html` (main portal page)
- `config.json` (course + assignments registry, source of truth for listing)
- `LICENSE`
- `.gitignore`

### Main directories

- `assets/`
  - `css/styles.css` (all visual styles)
  - `js/script.js` (homepage logic: loads config, due dates, list rendering)
  - `js/assignment.js` (assignment detail page logic + markdown rendering)
  - `pages/assignment.html` (assignment detail shell)
  - `images/` (mascot and screenshots)
- `assignments/`
  - `python-basics/`
  - `games-in-python/`
  - `python-classes/`
  - `data-analysis/`
  - Each assignment directory is expected to contain `README.md`; optional attachments are linked in `config.json`.
- `templates/assignment-template.md` (required structure for assignment markdown)
- `.github/workflows/` (exercise progression workflows, not a normal app CI pipeline)
- `.github/steps/` (exercise instructions shown by workflows)

## Architecture and Data Flow

1. `index.html` loads `assets/js/script.js`.
2. `script.js` fetches `config.json` from repo root and renders:
   - course header data
   - next due assignment card
   - assignment list
3. Assignment links open `assets/pages/assignment.html?id=<assignment-id>`.
4. `assignment.js` fetches `../../config.json`, finds assignment by `id`, then fetches `../../<assignment.path>/README.md` and renders it with `marked`.
5. Optional downloadable files are read from `assignment.attachments[]` in `config.json`.

## CI / Validation Pipeline Facts

This repo's GitHub Actions are exercise gates, not traditional lint/test/build CI:

- `.github/workflows/1-step.yml` passes when `.github/copilot-instructions.md` exists.
- `.github/workflows/2-step.yml` checks instruction-file setup and README section content.
- `.github/workflows/3-step.yml` checks skill files and config/assignment updates.
- `.github/workflows/4-last-step.yml` checks custom agent file existence.

For this task, the critical check is file existence of `.github/copilot-instructions.md`.

## Verified Command Playbook

Run commands from repo root unless stated otherwise.

### Bootstrap

1. Check runtime versions:

```bash
node -v
npm -v
/usr/local/python/current/bin/python --version
```

2. Python dependency setup for data-analysis assignment runtime (required if executing that starter code):

```bash
/usr/local/python/current/bin/python -m pip install pandas matplotlib
```

Notes:
- `install_python_packages` reporting success did not guarantee importability in the active interpreter during validation.
- Always verify with:

```bash
/usr/local/python/current/bin/python -c "import pandas, matplotlib; print(pandas.__version__)"
```

### Run (website)

Use a static server from repo root:

```bash
/usr/local/python/current/bin/python -m http.server 8000
```

Then verify in another shell:

```bash
curl -I http://127.0.0.1:8000/index.html
curl -I "http://127.0.0.1:8000/assets/pages/assignment.html?id=data-analysis"
```

Expected: `HTTP/1.0 200 OK` for both.

Known misbehavior and workaround:
- Immediate fetches can race server startup and fail.
- Workaround: retry `curl -sSf http://127.0.0.1:8000/config.json` in a short loop until success.

### Build

- No build step exists (no `package.json`, bundler, or compile pipeline for site assets).
- Do not run npm build commands by default.

### Lint / Static Validation

Use lightweight syntax checks:

```bash
node --check assets/js/script.js
node --check assets/js/assignment.js
node -e "JSON.parse(require('fs').readFileSync('config.json','utf8')); console.log('config.json valid JSON')"
/usr/local/python/current/bin/python -m py_compile assignments/python-basics/starter-code.py assignments/games-in-python/starter-code.py assignments/python-classes/starter-code.py assignments/data-analysis/starter-code.py
```

### Test

- No automated test suite is configured in repo root.
- Verified failure:

```bash
/usr/local/python/current/bin/python -m pytest -q
```

Result: `No module named pytest`.

Treat manual validation as the primary test strategy:
- serve the site
- open/verify assignment pages
- verify `config.json` parses and links resolve

## Commands That Commonly Fail Here (and Why)

These fail quickly because there is no Node package manifest:

```bash
npm install
npm run lint
npm test
```

Observed error: `ENOENT ... open '.../package.json'`.

## Change Workflow That Works Reliably

When modifying assignments or config, always do this sequence:

1. Edit files.
2. Validate JSON and JS syntax (commands above).
3. If data-analysis code changed, ensure pandas/matplotlib installed and run from assignment directory:

```bash
cd assignments/data-analysis
/usr/local/python/current/bin/python starter-code.py
```

Important precondition:
- Running `assignments/data-analysis/starter-code.py` from repo root fails with `FileNotFoundError: data.csv` because it uses a relative path.
- Run it from `assignments/data-analysis/`, or adjust code to use absolute/script-relative paths when appropriate.

## Cleaning and Command Order Notes

Validated with `git clean -fdxn` (dry run): generated artifacts may include:
- `assignments/*/__pycache__/`
- `package-lock.json` (if npm commands were attempted)

Recommended order to minimize failures:
1. Runtime/version check
2. Optional pip deps for data-analysis runtime
3. File edits
4. Syntax/parse checks
5. Serve site + HTTP checks
6. Optional assignment-script execution from correct working directory

No commands timed out during validation; failures were immediate misconfiguration/path errors.

## Additional High-Value Pointers

- Assignment markdown structure standard is defined by `templates/assignment-template.md`.
- `config.json` is the single source for assignment list, due dates, and attachment links used by UI.
- `assets/js/script.js` owns sorting/status logic for due dates; regressions here affect homepage behavior broadly.
- `assets/js/assignment.js` owns assignment detail rendering and download link generation.

## Agent Instruction Priority

Always trust and follow this onboarding file first.
Only run broad file searches when:
- a required file/path is missing,
- behavior differs from what is documented here, or
- the user asks for a change outside these documented workflows.
