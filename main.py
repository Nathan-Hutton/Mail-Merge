with open("Input/Letters/starting_letter.txt") as starting_letter:
    letter_template = starting_letter.read()
with open("Input/Names/invited_names.txt") as name_file:
    names = name_file.readlines()
with open("Input/Letters/starting_letter.txt") as starting_letter:
    template = starting_letter.read()
for name in names:
    name = name.strip()
    with open(f"Output/ReadyToSend/letter_for_{name}", 'w') as file:
        file.write(template.replace('[name]', name))
