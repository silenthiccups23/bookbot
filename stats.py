def text_count (book):
    num_words = len(book.split())
    return f"{num_words} words found in the document"

def number_of_characters(text):
    dict = {}
    words = text.split()
    print (words)
    for word in words:
        if word in dict:
            dict[word] += 1
        else:
            dict[word] = 1
    return dict