from stats import get_no_of_words, get_no_of_characters

def get_book_text(file_path):
    with open (file_path) as f:
        book_text = f.read()
    return book_text

def main(file_path):
    book_text = get_book_text(file_path)
    no_of_words = get_no_of_words(book_text)
    char_count = get_no_of_characters(book_text)
    print(f"{no_of_words} words found in the document")
    for char in char_count:
        print(f"'{char}': {char_count[char]}")

main("./books/frankenstein.txt")