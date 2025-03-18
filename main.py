from stats import word_num, lower_letter_count
def get_book_text(file_path):
    with open(file_path) as f:
        contents = f.read()
        return contents

def main():
    path = "books/frankenstein.txt"
    book_text = get_book_text(path)
    word_count = word_num(book_text)
    letter_count = lower_letter_count(book_text)
# Using a completely different approach to format the string
    message = str(word_count) + " words found in the document"
    print(message)
    print(f"{lower_letter_count(book_text)}")

main()