from stats import text_count
from stats import number_of_characters
from stats import report
from stats import full_report

def get_book_text(path):
    with open(path) as f:
        return f.read()
def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    result_count = text_count(text)
    number_of_characters_result = number_of_characters(text)
    result_report = report(number_of_characters_result)
    print(full_report(result_report, result_count))
    



main()
