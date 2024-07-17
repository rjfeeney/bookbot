def print_report():
    file_path = "books/frankenstein.txt"
    with open(file_path) as f:
        file_contents = f.read()
    count = wordcount(file_contents)
    characters = charactercount(file_contents)
    print(f"--- Begin report of {file_path} ---")
    print(f"{count} words found in the document")

    for char, count in characters:
        print(f"The '{char}' letter was found {count} times")
    
    print("--- End report ---")

def wordcount(frankenstein):
    words = frankenstein.split()
    return len(words)

def charactercount(frankenstein):
    character_dict = {}
    lowered_string = frankenstein.lower()
    for char in lowered_string:
        if char.isalpha():
            if char not in character_dict:
                character_dict[char] = 0
            character_dict[char] += 1
    char_list = [(char, count) for char, count in character_dict.items()]
    char_list.sort(key=lambda x: x[1], reverse=True)
    return char_list


print_report()