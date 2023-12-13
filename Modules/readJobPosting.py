def preprocessPostingText(text):
    if text is None:
        return []
    #words = findall(r'\b(?:[A-Za-z]+|[A-Za-z]\+[A-Za-z]+|\w+\.\w+|\w+\.\w+\.?\w*)\b', text)
    words = text.split()
    textOut = [word.lower().rstrip('.,;') for word in words]

    return textOut