from textwrap import dedent

def d(string):
    string_without_its_first_line = string[string.find('\n') + 1:]
    return dedent(string_without_its_first_line)
