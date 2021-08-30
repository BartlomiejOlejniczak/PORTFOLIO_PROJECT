import pandas

morse_code = pandas.read_csv('morse.csv')
mc_letter_list = morse_code.letter.to_list()
mc_code_list = morse_code.code.to_list()
word_list = []
'''get_word = input('dej litiere: \n').upper()
for l in get_word:
    for letter in mc_letter_list:
        if l == letter:
            print(mc_code_list[mc_letter_list.index(letter)])
    word_list.append(mc_code_list[mc_letter_list.index(l)])'''


print(morse_code.letter('P'))
