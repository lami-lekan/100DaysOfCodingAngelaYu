# student_dict = {
#     "student": ["Angela", "James", "Lily"], 
#     "score": [56, 76, 98]
# }

#Looping through dictionaries:
# for (key, value) in student_dict.items():
#     #Access key and value
#     pass

import pandas
# student_data_frame = pandas.DataFrame(student_dict)

#Loop through rows of a data frame
# for (index, row) in student_data_frame.iterrows():
    #Access index and row
    #Access row.student or row.score
    #pass

# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}

df = pandas.read_csv("nato_phonetic_alphabet.csv")
#TODO 1. Create a dictionary in this format:
nato_phonetic_dict = {row.letter:row.code for (index, row) in df.iterrows()}
# print(nato_phonetic_dict)
# print(nato_phonetic_dict.keys())

#TODO 2. Create a list of the phonetic code words from a word that the user inputs.
correct_ans = True
while correct_ans:
    user_input = input("Give a message: ").upper()
    try:
        nato_words = [nato_phonetic_dict[letter] for letter in user_input]

    except KeyError:
        print("Sorry, only letters int the alphabet please")
    else:
        print(nato_words)
        correct_ans = False
