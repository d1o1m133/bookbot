def word_num(text):
    words = text.split()
    return len(words)

def chars_to_sorted_list(char_dict):
    # Create an empty list to hold our dictionaries
    chars_list = []
    
    # Convert each character and count into a dictionary and add to list
    for char, count in char_dict.items():
        char_info = {"char": char, "count": count}
        chars_list.append(char_info)
    
    # Define a helper function for sorting
    def sort_on(dict):
        return dict["count"]
    
    # Sort the list in descending order by count
    chars_list.sort(reverse=True, key=sort_on)
    
    return chars_list

def convert_lower(text):
    lower_text = text.lower()
    return lower_text

def lower_letter_count(text):
    letter_dict = {}
    for l in text.lower():
        if l.strip() == "":  # Ignore spaces and empty lines entirely
            continue
        if l not in letter_dict:
            letter_dict[l] = 0
        letter_dict[l] += 1
    return letter_dict