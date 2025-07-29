def text_count (book):
    num_words = len(book.split())
    return f"{num_words} words found in the document"

def number_of_characters(text):
    dict = {}
<<<<<<< HEAD
    words = text.split()
    print (words)
=======
    words = text.lower().split()
>>>>>>> ef7b6a028b04197e6180b51b88b2f0c8403ccaf5
    for word in words:
        if word in dict:
            dict[word] += 1
        else:
            dict[word] = 1
    return dict