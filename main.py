from stats import text_count
from stats import number_of_characters
from stats import report

def get_book_text(path):
    with open(path) as f:
        return f.read()
def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    result_count = text_count(text)
    number_of_characters_result = number_of_characters(text)
    resutl_report = report(number_of_characters_result, result_count)
    print(resutl_report)



main()
