from sys import argv, exit
from stats import get_word_count, get_chars_count, sort_dictionary


def main() -> None:
    if len(argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        exit(1)

    print("============ BOOKBOT ============")

    file_path = argv[1]
    text = get_book_text(file_path)
    counts = sort_dictionary(get_chars_count(text))
    for item in counts:
        if item.isalpha():
            print(f"{item}: {counts[item]}")

    print("============= END ===============")


def get_book_text(path: str) -> str:
    print(f"Analyzing book found at {path}...")

    with open(path) as file:
        file_contents = file.read()

    print("----------- Word Count ----------")
    print(f"Found {get_word_count(file_contents)} total words")

    return file_contents


if __name__ == "__main__":
    main()
