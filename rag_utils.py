MAX_QUESTION_CHARS = 1000
MAX_HISTORY_ENTRY_CHARS = 2000


def clean_question(text: str) -> str:
    cleaned = " ".join(text.split())
    if not cleaned:
        raise ValueError("Please enter a question.")
    if len(cleaned) > MAX_QUESTION_CHARS:
        raise ValueError(f"Questions are limited to {MAX_QUESTION_CHARS} characters.")
    return cleaned


def history_entry(role: str, text: str) -> str:
    # Keeps prompt size bounded as the conversation grows.
    return f"{role}: {text[:MAX_HISTORY_ENTRY_CHARS]}"
