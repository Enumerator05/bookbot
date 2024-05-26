def main():
    book_path = "books/frankenstein.txt"
    book_text = get_book(book_path)
    print_book_report(book_text)

 
def sort_on(dict):
    return dict["num"]


def print_book_report(text):
    print("--- Begin report of books/frankenstein.txt ---")
    num_words = get_word_count(text)
    print(f"{num_words} words found in the document")
    char_count_dict = get_char_count(text)
    char_count_list = char_dict_to_sorted_list(char_count_dict)
    for item in char_count_list:
        if not item["char"].isalpha():
            continue
        print("The '{}' character was found  {} times".format(item["char"], item["num"]))
    

def get_book(path):
    with open(path) as f:
        return f.read()


def get_word_count(input):
    return len(input.split())


def get_char_count(input):
    dict = {}
    for c in input.lower():
        if c in dict:
            dict[c] += 1
        else:
            dict[c] = 1
    return dict


def char_dict_to_sorted_list(dict):
    sorted_list = []
    for ch in dict:
        sorted_list.append({"char": ch, "num": dict[ch]})
    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list


main()
