import pytest

from rag_utils import MAX_HISTORY_ENTRY_CHARS, MAX_QUESTION_CHARS, clean_question, history_entry


def test_clean_question_collapses_whitespace():
    assert clean_question("  what   is\nRAG? ") == "what is RAG?"


@pytest.mark.parametrize("value", ["", "   \n\t"])
def test_clean_question_rejects_blank_input(value):
    with pytest.raises(ValueError):
        clean_question(value)


def test_clean_question_rejects_oversized_input():
    with pytest.raises(ValueError, match="limited"):
        clean_question("x" * (MAX_QUESTION_CHARS + 1))


def test_history_entry_is_bounded_and_prefixed():
    entry = history_entry("Assistant", "y" * (MAX_HISTORY_ENTRY_CHARS + 500))

    assert entry.startswith("Assistant: ")
    assert len(entry) == len("Assistant: ") + MAX_HISTORY_ENTRY_CHARS
