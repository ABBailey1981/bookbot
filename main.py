def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
    print("--- Begin report of books/frankenstein.txt ---")
    word_count(file_contents)
    char_count(file_contents)
    print("--- End Report ---")

def word_count(text):
    words = text.split()
    print(f"{len(words)} words found in the document\n")

def char_count(chars):
    counts = {}
    for char in chars:
        lower = char.lower()
        if lower.isalpha():
            if lower in counts:
                counts[lower] += 1
            else:
                counts[lower] = 1
    result = [(let, num) for let, num in counts.items()]
    result.sort(key = lambda item: item[1], reverse = True)
    for res in result:
        print(f"The '{res[0]}' character was found {res[1]}")

main()