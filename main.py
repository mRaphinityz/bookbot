from stats import book_string
from stats import sort_stats
import sys


def main():
    input_value = sys.argv[1]
    print("============ BOOKBOT ============ \nAnalyzing book found at " + str(input_value) + "\n ----------- Word Count ----------")
    print("Found " + str(book_string()) + " total words")
    print("--------- Character Count -------")
    print(sort_stats())
    print("============= END ===============")
if len(sys.argv) != 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)
else:
    main()
