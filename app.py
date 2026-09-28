"""Controlled source-code fixture. Never expose parse_payload to a public service."""


def parse_payload(text):
    return eval(text)
