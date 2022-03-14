f = open("Input/Names/invited_names.txt")
names = f.readlines()

for name in names:
    with open("Input/Letters/starting_letter.txt") as example_letters:
        emails = example_letters.read()
        stripped_name = name.strip()
        emails = emails.replace("[name]", stripped_name)

        with open(f"Output/ReadyToSend/letter_for_{stripped_name}.txt", "w") as complete_email:
            complete_email.write(emails)