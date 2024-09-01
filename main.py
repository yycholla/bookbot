def main():
    path = "books/frankenstein.txt"
    text = get_text(path)
    num_words = get_words(text)
    num_chars = get_chars_dict(text)
    chars_sorted_list = chars_dict_to_sorted_list(num_chars)
    print(f"--- Begin report of {path} ---")
    print(f"{num_words} words found in the document")
    for item in chars_sorted_list:
        print(f"The {item["char"]} character was found {item["num"]} times")


def get_text(path):
    with open(path) as f:
        return f.read()


def get_words(string):
    return len(string.split())


def sort_on(dict):
    return dict["num"]


def get_chars_dict(text):
    chars = {}
    for c in text:
        lowered = c.lower()
        if lowered in chars:
            chars[lowered] += 1
        else:
            chars[lowered] = 1
    return chars


def chars_dict_to_sorted_list(num_chars_dict):
    sorted_list = []
    for ch in num_chars_dict:
        sorted_list.append({"char": ch, "num": num_chars_dict[ch]})
    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list


main()
