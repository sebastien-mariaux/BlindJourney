import string
import re


def is_same(first, second):
    if first == second:
        return True

    if first.lower() == second.lower():
        return True

    if transform(first) == transform(second):
        return True


def transform(text):
    text = text.strip()
    text = remove_double_spaces(text)
    text = remove_punctuation(text)
    return text


def remove_punctuation(text):
    return text.translate(str.maketrans('', '', string.punctuation))


def remove_double_spaces(text):
    return re.sub(' +', ' ', text)
