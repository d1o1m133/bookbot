def word_num(text):
    words = text.split()
    return len(words)

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