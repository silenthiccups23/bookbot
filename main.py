from stats import text_count
from stats import number_of_characters

def get_book_text(path):
    with open(path) as f:
        return f.read()
def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    result = text_count(text)
    print(result)
    number_of_characters_result = number_of_characters(text)
    print(number_of_characters_result)


main()
