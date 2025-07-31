
def text_count (book):
    num_words = len(book.split())
    return num_words

def number_of_characters(text):
    dict = {}
    words = text.lower()
    for char in words:
        if char in dict:
            dict[char] += 1
        else:
            dict[char] = 1
    return dict      

def sort_on(char):
    return char["num"]


def report(charactersDict):
    sorted_list = []
    for char in charactersDict:
        if char.isalpha(): 
            sorted_list.append({"char": char, "num": charactersDict[char]})
        else:
            sorted_list.append({"char": char, "num": charactersDict[char]})
        sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list
        
def full_report(list, totalCount):
    report = ""

    report += "============ BOOKBOT ============\n"
    report += "Analyzing book found at books/frankenstein.txt...\n"
    report += "Analyzing book found at books/frankenstein.txt...\n"
    report += "----------- Word Count ----------\n"
    report += f"Found {totalCount} total words\n"

    for value in list:
        report += f"{value['char']}: {value['num']} \n"
    report += "============= END ==============="
    return report
    