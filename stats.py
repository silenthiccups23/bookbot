def text_count (book):
    num_words = len(book.split())
    return f"{num_words} words found in the document"

def number_of_characters(text):
    dict = {}
    words = text.lower()
    for word in words:
        if word in dict:
            dict[word] += 1
        else:
            dict[word] = 1
    return dict 

def sort_on(char): 
    return char['nums']

def report(charactersDict, totalCount):
    sorted_list = []
    for char in charactersDict: 
        sorted_list.append({"char": char, "num": charactersDict[char]})
    print(sorted_list)