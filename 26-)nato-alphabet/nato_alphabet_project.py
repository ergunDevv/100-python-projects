import pandas
# for( index,row) in student_data_fram.itterrows():
#     print(row.student)

nato_alphabet = pandas.read_csv("26-)nato-alphabet/nato_phonetic_alphabet.csv")
nato_alphabet_dict = {row.letter.lower(): row.code for (
    index, row) in nato_alphabet.iterrows()}

word = input("Enter a word: ").lower()

answer_list = [nato_alphabet_dict[letter] for letter in word]
print(answer_list)
