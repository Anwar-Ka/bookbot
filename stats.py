def get_no_of_words(book_text):
    words = book_text.split()
    no_of_words = len(words)
    return no_of_words

def get_no_of_characters(book_text):
    char_count = {}
    for char in book_text:
        char = char.lower()
        if char not in char_count:
            char_count[char] = 1
        else:
            char_count[char] += 1
    return char_count
            
