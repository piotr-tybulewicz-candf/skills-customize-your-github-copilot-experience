# 📘 Assignment: Hangman Game Challenge

## 🎯 Objective

Build the classic word-guessing game using Python strings, loops, and user input. You'll practice string manipulation, loops, conditionals, and random selection by creating an interactive Hangman game.

## 📝 Tasks

### 🛠️ Game Setup and Word Selection

#### Description
Create the foundational structure of the Hangman game, including a word list and the ability to randomly select a word to guess.

#### Requirements
Completed program should:

- Define a list of words to choose from
- Randomly select a word from the list
- Initialize game variables (attempts remaining, guessed letters)
- Display the initial hidden word state (_ _ _ format)

### 🛠️ Letter Guessing and Progress Tracking

#### Description
Implement the main game loop that accepts letter guesses and updates the game state accordingly.

#### Requirements
Completed program should:

- Accept letter guesses from the user
- Show current progress with guessed letters revealed and unguessed letters hidden
- Track incorrect guesses and decrement attempts remaining
- Prevent duplicate guesses (optional enhancement)

### 🛠️ Win/Lose Conditions and Game End

#### Description
Complete the game by implementing win and lose conditions with appropriate end-game messages.

#### Requirements
Completed program should:

- End the game when the word is completely guessed (win)
- End the game when attempts reach zero (lose)
- Display clear win/lose messages with the final word revealed
- Allow players to play again or exit
