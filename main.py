import sys
from stats import print_report, get_num_words, get_char_frequency

def get_book_text(filepath):
    with open(filepath) as f:
        return f.read()

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    corpus = get_book_text(sys.argv[1])
    char_dict = get_char_frequency(corpus)
    print_report(char_dict)


main()
