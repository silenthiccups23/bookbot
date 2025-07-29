def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    print(text)
    result = text_count(text)
    print(result)

def get_book_text(path):
    with open(path) as f:
        return f.read()


def text_count (book):
    num_words = 0
    words = book.split()
    for word in words:
        num_words += 1
    return f"{num_words} words found in the document"

main()
