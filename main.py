from stats import word_num, lower_letter_count, chars_to_sorted_list
import sys

def get_book_text(file_path):
    with open(file_path) as f:
        contents = f.read()
        return contents

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    script_name = sys.argv[0]
    path_to_book = sys.argv[1]

    book_text = get_book_text(path_to_book)
    word_count = word_num(book_text)
    letter_dict = lower_letter_count(book_text)
    
    # Get sorted list of letter counts
    sorted_letters = chars_to_sorted_list(letter_dict)
    
    # Print report in the required format
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path_to_book}...")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")
    
    # Print only alphabetical characters
    for item in sorted_letters:
        char = item["char"]  # Make sure this matches the key in your chars_to_sorted_list function
        count = item["count"]  # Make sure this matches the key in your chars_to_sorted_list function
        if char.isalpha():
            print(f"{char}: {count}")
    
    print("============= END ===============")

if __name__ == "__main__":
    main()