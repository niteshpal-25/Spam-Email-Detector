from utils import clean_text


def test_clean_text():

    text = "Hello!!! WORLD@@"

    result = clean_text(text)

    assert result == "hello world"


def test_empty_text():

    text = ""

    result = clean_text(text)

    assert result == ""