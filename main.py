def main():
    with open("books/frankenstein.txt") as f:
        book = f.read()
        print(book)

        word_count = count_words(book)
        print(word_count)

        character_count = count_characters(book)
        print(character_count)


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


main()
