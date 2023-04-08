import argparse
import re
import subprocess
from typing import Iterable, List, Tuple


def parse_input(file_path: str) -> Tuple[Iterable[str], str]:
    """
    Parse the input file and return the source text and search term.

    Args:
        file_path: The path to the input file.

    Returns:
        A tuple containing the source text (an iterable of strings) and
         the search term (a string).
    """

    last_line = (
        subprocess.check_output(["tail", "-1", file_path])
        .decode("utf-8")
        .rstrip()
    )
    if not last_line:
        raise ValueError(f"The file {file_path} is empty.")
    non_word_pattern = re.compile(r"[^a-zA-Z]+")
    search_term = re.sub(non_word_pattern, " ", last_line).strip()

    def source_text_gen():
        with open(file_path, "r") as file:
            for i, line in enumerate(file):
                if line.rstrip() != last_line:
                    yield re.sub(non_word_pattern, " ", line.strip()).strip()
                elif i == 0:
                    raise ValueError(
                        f"The file {file_path} has only one line (search term)"
                    )

    return source_text_gen(), search_term


def find_matching_lines(
    source_text: Iterable[str], search_term: str
) -> List[str]:
    """
    Find all lines in the source text that contain the search term.

    Args:
        source_text: An iterable of strings representing the source text.
        search_term: The term to search for.

    Returns:
        A list of strings containing the matching lines.

    """
    matching_lines = []

    for line in source_text:
        if search_term in line:
            matching_lines.append(line)

    return matching_lines


def main(file_path: str = None) -> None:
    """
    Parse the input file, find all lines that contain the search term, and
     print them.

    Args:
        file_path: The path to the input file. If None, the file path will
         be read from the command line.

    """
    if file_path is None:
        args_p = parse_args()
        file_path = args_p.file_path
    source_text, search_term = parse_input(file_path)
    matching_lines = find_matching_lines(source_text, search_term)

    for line in matching_lines:
        print(f"[{line}]")


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Search for a term in a source text file."
    )
    parser.add_argument(
        "file_path",
        help=(
            "Path to the input file containing the source text and search"
            " term."
        ),
    )

    args_p = parser.parse_args()
    return args_p
