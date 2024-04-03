# Файл: test_word_counter.py

import pytest
from main import count_words_and_sentences

@pytest.mark.parametrize("file_path, expected_result", [
    ("D:\Уник\TestMkr2\mkr.txt", (71, 4)),

])
def test_count_words_and_sentences(file_path, expected_result):
    assert count_words_and_sentences(file_path) == expected_result
