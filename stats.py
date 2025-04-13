def get_word_count(text: str) -> int:
    return len(text.split())


def get_chars_count(text: str):
    print("--------- Character Count -------")
    char_counts_dict = {}
    for char in text:
        char = char.lower()
        if char in char_counts_dict:
            char_counts_dict[char] += 1
        else:
            char_counts_dict[char] = 1

    return char_counts_dict


def sort_dictionary(data: dict[str, int]):
    return dict(sorted(data.items(), key=lambda item: item[1], reverse=True))
