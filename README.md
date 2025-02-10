# Text and Number Analyzer

This Python project analyzes user-inputted text or numbers to extract key statistics. It provides insights into sentence and word structure for text or basic statistical analysis for numbers.

## Features

### Text Analysis
- Counts total characters, words, and sentences.
- Finds the most frequent word.
- Calculates the average word length.
- Determines the average sentence length.

### Number Analysis
- Counts total numbers.
- Computes the sum and range of numbers.
- Identifies the most frequent number.
- Calculates the average value.

## Installation

Ensure you have Python installed, then clone the repository and run the script:

```sh
python analysis.py
```

## Usage

1. Run the script and choose between text or number analysis.
2. Input text to analyze its structure.
3. Input a list of numbers to get statistical results.

## Example

### Text Analysis
**Input:**
```sh
Enter 'numbers' to process numbers (0,1,2,etc.) or 'text' to process alphameric text: text
Enter the text you want to analyze:
This is a test. This is only a test!
```
**Output:**
```sh
Text analysis results
---------------------
Total characters: 31
Total words: 8
Total sentences: 2
Most frequent word: 'test'
Avg word length: 3.9 letters
Avg sentence length: 4.0 words
```

### Number Analysis
**Input:**
```sh
Enter 'numbers' to process numbers (0,1,2,etc.) or 'text' to process alphameric text: numbers
Enter a list of numbers separated by a space:
1 2 2 3 4 4 4 5
```
**Output:**
```sh
Number analysis results
---------------------
Total numbers: 8
Sum of numbers: 25
Range of numbers: 4
Most frequent number: 4
Total Average: 3.1
```

## Requirements

- Python 3.x
- No external dependencies (uses built-in libraries)

## License

This project is licensed under the MIT License.

## Author

Sean Anih

