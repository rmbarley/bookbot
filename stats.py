def get_num_words(corpus):
    return len(corpus.split())

def get_char_frequency(corpus):
    result = {}
    for c in corpus:
        test = c.lower()
        if test in result:
            result[test] += 1
        else:
            result[test] = 1
    return result

def sorted_on(item):
    return item[1]


def print_report(char_dict):
    sorted_dict = dict(sorted(char_dict.items(), key=sorted_on, reverse=True))
    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
    print("----------- Word Count ----------")
    print(f"Found 75767 total words")
    print("--------- Character Count -------")
    for c in sorted_dict:
        if c.isalpha():
            print(f"{c}: {sorted_dict[c]}")
    print("============= END ===============")


