

with open("Input/Letters/starting_letter.txt") as letter:
    letter_copy = letter.read()
    with open("Input/Names/invited_names.txt") as names:
        names_copy = names.readlines()
        for name in names_copy:
            stripped_name = name.strip()
            replaced_letter = letter_copy.replace("[name]", stripped_name)
            file_name = f"Output/Ready_to_send/letter_for_{stripped_name}.txt"
            with open(file=file_name, mode="w") as new_letter:
                new_letter.write(replaced_letter)