# Number Name Converter

As part of my Python programming practice, I developed a number-to-words and words-to-number converter that can translate numeric values in both directions. The program uses dictionaries to map numbers to their word forms and vice versa, and processes values in chunks (hundreds, thousands, millions) to construct or decode numerical expressions. It also accounts for special cases like zero, and runs in a continuous input loop with error handling for invalid entries. This project demonstrates my ability to work with data structures, string manipulation, loops, and control logic to build an interactive Python tool.

## Features
- Converts numbers to word form (ex., `123` → `one hundred twenty-three`)
- Converts word form to numbers (ex., `one hundred twenty-three` → `123`)
- Handles large numbers (thousands, millions, billions)
- Accounts for special cases like zero and negative numbers
- Continuous input loop for user interaction
- Error handling for invalid entries

## Skills Demonstrated
- Data usage (dictionaries for mapping)
- String manipulation and parsing
- Looping
- Input validation and error handling

## How to Use
1. Clone this repository.
2. Run the converter:
3. Enter a number or its word form to convert. The program will continuously prompt for input until you exit.

**Example:**
```
Enter number or words (or 'exit' to quit): 100000
One Hundred Thousand
Enter number or words (or 'exit' to quit): One Hundred Thousand
100000
Enter number or words (or 'exit' to quit): exit
```
