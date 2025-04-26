from stats import count_words, count_char, sort_dict 
import sys

def get_book_text(path_to_file):
    with open(path_to_file) as f:
        file_contents = f.read()
    return file_contents

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    book = sys.argv[1]
    text = get_book_text(book)
    num_words = count_words(text)
    list_result = sort_dict(count_char(text))

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for i in list_result:
        if i['char'].isalpha():
            print(f"{i['char']}: {i['num']}")
    print("============= END ===============")


main()
