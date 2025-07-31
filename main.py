
import sys
from stats import text_count
from stats import number_of_characters
from stats import report
from stats import full_report

def get_book_text(path):
    with open(path) as f:
        return f.read()
def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    book_path = sys.argv[1]
    text = get_book_text(book_path)
    result_count = text_count(text)
    number_of_characters_result = number_of_characters(text)
    result_report = report(number_of_characters_result)
    print(full_report(result_report, result_count, book_path))
    

main()
