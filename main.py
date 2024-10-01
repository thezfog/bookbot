def main():
    book_title = "Frankenstein"
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    word_count = count_words(text)
    char_count = count_chars(text)
    ordered_char_count = order_dictionary(char_count)
    ordered_char_count.sort(key=sort_on, reverse=True)

    print("--- Begin report of books/frankenstein.txt ---")
    print()
    print(f"{word_count} words in {book_title}")
    print()
    print_dictionaries(ordered_char_count)
    print()
    print("--- End report ---")

def get_book_text(path):
    with open(path) as f:
        return f.read()

def count_words(text):
    words = text.split()
    return len(words)

def count_chars(text):
    characters = {}
    lower_case_words = text.lower()
    for letter in lower_case_words:
        if letter.isalpha():
            characters[letter] = characters.get(letter, 0) + 1
            
    return characters

def sort_on(dictionary):
    return dictionary["num"]

def order_dictionary(dictionary):
    new_dictionary = []
    for index in dictionary:
        new_entry = {"char": index, "num": dictionary[index]}
        new_dictionary.append(new_entry)
    return new_dictionary

def print_dictionaries(dict_list):
    for entry in dict_list:
        char = entry["char"]
        num = entry["num"]
        print(f"The '{char}' character was found {num} times")

main()