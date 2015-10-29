def tokenize(source):
    def is_blank(char):
        return char in (' ', '\n')

    def is_delimiter(char):
        return char in ('(', ')')

    def next_token():
        nonlocal head
        while head < len(source) and is_blank(source[head]):
            head += 1

        begin = head

        if head >= len(source):
            return None

        if is_delimiter(source[head]):
            head += 1
            return source[head - 1]
        else:
            while head < len(source) and not is_blank(source[head]) and not is_delimiter(source[head]):
                head += 1
            return source[begin:head]

    tokens = []
    head = 0

    t = next_token()
    while t is not None:
        tokens.append(t)
        t = next_token()

    return tokens
