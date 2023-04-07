from unittest.mock import MagicMock, patch

import pytest

from src.search import find_matching_lines, main, parse_input


@pytest.fixture
def sample_input_file(tmpdir):
    sample_content = """this is one
908^)-234 923this-++-23is./<.";][}"another-=&^5
this is one
another
"""
    file = tmpdir.join("sample_input.txt")
    with open(file, "w") as f:
        f.write(sample_content)

    return file


def test_parse_input(sample_input_file):
    source_text, search_term = parse_input(sample_input_file)
    source_text_list = list(source_text)  # Convert the generator to a list
    assert len(source_text_list) == 3
    assert search_term == "another"


def test_find_matching_lines():
    source_text, search_term = parse_input("tests/example.txt")
    expected_output = ["to get very", "by her sister"]
    result = find_matching_lines(source_text, search_term)

    assert result == expected_output


def test_empty_input_file(tmpdir, capsys):
    empty_file = tmpdir.join("empty_input.txt")
    with open(empty_file, "w"):
        pass

    with patch(
        "argparse.ArgumentParser.parse_args",
        return_value=MagicMock(file_path=str(empty_file)),
    ):
        with pytest.raises(SystemExit):
            main()

    captured = capsys.readouterr()
    assert "Error: The file" in captured.out


def test_matching_lines_format(sample_input_file, capsys):
    with patch(
        "argparse.ArgumentParser.parse_args",
        return_value=MagicMock(file_path=str(sample_input_file)),
    ):
        main()

    captured = capsys.readouterr()
    expected_output = "[this is another]\n"
    assert captured.out == expected_output
