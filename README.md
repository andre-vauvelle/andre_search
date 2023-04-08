# Search

This package provides a simple script to search for lines in a file that contain a specified term.





## Installation

To install `andre_search`, follow these steps:

```bash
git clone https://github.com/andre-vauvelle/andre_search.git
cd andre_search
pip install .
```

## Usage

To use this script, simply pass the path to the input file containing the source text and search term as a command line argument, like so:

```bash
andre_search /path/to/input_file.txt
```

## Input File Format

The input file should be a plain text file containing the source text and the search term. The source text consists of multiple lines, each representing a single line of text. The search term should be placed on the last line of the input file.

Example:
```text
This is the first line of the source text.
This is the second line of the source text.
This is the third line of the source text.
search term
```

In this example, the first three lines make up the source text, and the last line contains the search term "search term". The search tool will look for the search term in the source text and return any matching lines.


## Development
This package includes pre-commit hooks to help ensure code quality. To set up these hooks including pytests, run the following command:
```bash
pre-commit install
```
