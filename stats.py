def get_no_of_words(book_text):
    words = book_text.split()
    no_of_words = len(words)
    return no_of_words

def get_no_of_characters(book_text):
    char_count = {}
    for char in book_text:
        if char.isalpha():
            char = char.lower()
            if char not in char_count:
                char_count[char] = 1
            else:
                char_count[char] += 1
    return char_count

def sort_on(list_of_characters):
        return list_of_characters["num"]

def sort_characters(char_count):
    list_of_characters = []
    for char in char_count:
        list_of_characters.append({"char": char, "num": char_count[char]})
    
    list_of_characters.sort(key=sort_on, reverse=True)
    return list_of_characters