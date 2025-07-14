def number_of_words(text):
    return len(text.split())


def get_chars_dict(text):
    chars = {}
    for c in text:
        lowered = c.lower()
        if lowered in chars:
            chars[lowered] += 1
        else:
            chars[lowered] = 1
    return chars


def sort_on(items):
    return items["num"]


def sorted_list_of_dicts(chars_dict):
    list = []
    for char, count in chars_dict.items():
        list.append({"char": char, "num": count})

    return sorted(list, reverse=True, key=sort_on)
