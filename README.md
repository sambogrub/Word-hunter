# Word-hunter
 Word Hunter is a simple word-guessing game built with Python and Tkinter. Players have up to 5 attempts to guess a randomly selected 5-letter word from a predefined word list.

## Requirements

- Python version **3.11.0 or later**
- A file named **`word_list`** containing 5-letter words, located in the same directory as the script.

## Installation and Setup

1. **Ensure Python is installed:**
   - Download and install Python [here](https://www.python.org/).
   - Verify installation by running:
     ```bash
     python --version
     ```

2. **Prepare the `word_list` file:**
   - You may use the file 'word_list' from this repository or create your own.
   - Make sure the file named `word_list` is in the same directory as the script.
   - Populate it with a list of 5-letter words, each on a new line. For example:
     ```
     apple
     mango
     lemon
     grape
     berry
     ```

3. **Run the script:**
   - Execute the script with the following command:
     ```bash
     python word_hunter.py
     ```

## How to Play

1. Enter a 5-letter word into the input box and click "Check your word."
2. After each guess:
   - **Green background**: Correct letter in the correct position.
   - **Yellow background**: Correct letter in the wrong position.
   - **Gray background**: Incorrect letter.
3. Use up to 5 attempts to guess the word.
4. If you guess the word correctly, you'll see a "Correct!" message.

## Notes

- If the `word_list` file is missing or improperly formatted, the program will not function.
- Only 5-letter words are valid guesses.

Feel free to customize the word list and enjoy the game!