def main():
    with open("books/frankenstein.txt") as f:
        book = f.read()

        word_count = count_words(book)

        character_count = count_characters(book)

        print("--- Begin report of books/frankenstein.txt ---")
        print(f"{word_count} words was found in the document")

        char_list = []
        for char in character_count:
            if char.isalpha():
                char_list.append({"character": char, "count": character_count[char]})

        char_list.sort(reverse=True, key=sort_on)

        for char in char_list:
            print(
                f"The '{char["character"]}' character was found {char["count"]} times"
            )
        print("--- End report ---")


def count_words(book: str) -> int:
    words = book.split()
    return len(words)


def count_characters(book: str) -> dict[str, int]:
    book = book.lower()
    character_count = {}
    for char in book:
        if char in character_count:
            character_count[char] += 1
        else:
            character_count[char] = 1
    return character_count


def sort_on(dict):
    return dict["count"]


main()
