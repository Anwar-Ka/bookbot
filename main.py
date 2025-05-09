import sys
from stats import get_no_of_words, get_no_of_characters, sort_characters

def get_book_text(file_path):
    with open (file_path) as f:
        book_text = f.read()
    return book_text

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    else:
        file_path = sys.argv[1]

    book_text = get_book_text(file_path)
    no_of_words = get_no_of_words(book_text)
    char_count = get_no_of_characters(book_text)
    character_count = sort_characters(char_count)

    print(f"""============ BOOKBOT ============
    Analyzing book found at {file_path}
    ----------- Word Count ----------
    Found {no_of_words} total words
    --------- Character Count -------""")
    for char in character_count:
        print(f"{char['char']}: {char['num']}")
    
    print("============= END ===============")

    
main()