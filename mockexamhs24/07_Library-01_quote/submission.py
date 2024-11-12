from urllib.parse import quote


def encode(s):
    return quote(s)