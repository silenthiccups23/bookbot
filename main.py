from stats import text_count

def get_book_text(path):
    with open(path) as f:
        return f.read()
def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    print(text)
    result = text_count(text)
    print(result)


main()
