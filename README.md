# Search

This package provides a simple script to search for lines in a file that contain a specified term.

## Installation

To install `andre_search`, follow these steps:

```bash
git clone https://github.com/yourusername/andre_search.git
cd andre_search
pip install .
```

## Usage

To use this script, simply pass the path to the input file containing the source text and search term as a command line argument, like so:

```bash
andre_search /path/to/input_file.txt
```

If you would like to run in a docker container use:

```bash
docker build -t andre_search .
docker run --rm andre_search python search.py "/path/to/input_file.txt"
```

## Development
This package includes pre-commit hooks to help ensure code quality. To set up these hooks including pytests, run the following command:
```bash
pre-commit install
```
