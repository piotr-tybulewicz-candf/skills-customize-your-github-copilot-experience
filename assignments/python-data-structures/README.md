# 📘 Assignment: Data Structures in Python

## 🎯 Objective

Build confidence with Python data structures by using lists, dictionaries, sets, and tuples to organize, analyze, and transform simple classroom data.

## 📝 Tasks

### 🛠️	Working with Lists

#### Description
Create a function named `list_operations(numbers)` that performs common list operations on a list of integers.

#### Requirements
Completed program should:

- Accept a list of integers as input.
- Return a dictionary with these keys: `original`, `sorted`, `reversed`, and `sum`.
- Keep `original` unchanged while creating new transformed versions.
- Example behavior:
  ```python
  list_operations([4, 1, 3, 1])
  # {
  #   "original": [4, 1, 3, 1],
  #   "sorted": [1, 1, 3, 4],
  #   "reversed": [1, 3, 1, 4],
  #   "sum": 9
  # }
  ```

### 🛠️	Working with Dictionaries

#### Description
Create a function named `grade_lookup(records, student_name)` that uses a dictionary to store student names and grades.

#### Requirements
Completed program should:

- Use a dictionary where keys are student names and values are integer grades.
- Return the student grade when the student exists.
- Return `"Student not found"` when the name is not in the dictionary.
- Example behavior:
  ```python
  grade_lookup({"Ava": 92, "Noah": 85}, "Ava")
  # 92
  grade_lookup({"Ava": 92, "Noah": 85}, "Mia")
  # "Student not found"
  ```

### 🛠️	Working with Sets

#### Description
Create a function named `unique_topics(topics)` that uses a set to remove duplicates from a list of topic names.

#### Requirements
Completed program should:

- Accept a list of strings.
- Return a set containing unique topic names only.
- Show that repeated values appear once in the final set.
- Example behavior:
  ```python
  unique_topics(["lists", "tuples", "lists", "sets"])
  # {"lists", "tuples", "sets"}
  ```

### 🛠️	Working with Tuples

#### Description
Create a function named `coordinate_summary(point)` that accepts a tuple in the format `(x, y)` and returns a formatted sentence.

#### Requirements
Completed program should:

- Accept a tuple with exactly two numbers.
- Unpack the tuple into `x` and `y`.
- Return a string formatted as: `"The point is at x=<x>, y=<y>."`
- Example behavior:
  ```python
  coordinate_summary((3, 7))
  # "The point is at x=3, y=7."
  ```
