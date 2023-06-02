with open(r"24-)mail-merge\mail-merge\Names\invited_names.txt") as file:
    names_txt = file.read()
with open(r"24-)mail-merge\mail-merge\Letters\starting_letter.txt") as file:
    letter_template = file.read()

names = names_txt.splitlines()
print(names[0])
print(letter_template)


for name in names:
    with open(f"24-)mail-merge\mail-merge\Output\ReadyToSend\letter_for_{name}.txt", mode="w") as file:
        file.write(letter_template.replace("[name]", name))
