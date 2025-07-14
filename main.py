from stats import number_of_words, get_chars_dict, sorted_list_of_dicts
import sys


def get_book_text(book_path):
    with open(book_path) as f:
        return f.read()


def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    book_path = sys.argv[1]
    text = get_book_text(book_path)
    num_words = number_of_words(text)
    chars_dict = get_chars_dict(text)
    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for char in sorted_list_of_dicts(chars_dict):
        print(f"{char['char']}: {char['num']}")


main()
