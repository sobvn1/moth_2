input_user = input('Введите слово:').lower()
d = {'Буквы':0}
vowels = 0
consonants = 0
for i in input_user:
    if i.isalpha():
        d['Буквы'] += 1
    letter = i.lower()
    if letter == "a" or letter == "e" or\
       letter == "i" or letter == "o" or\
       letter == "u" or letter == "y" or\
       letter == "а" or letter == "я" or\
       letter == "я" or letter == "у" or\
       letter == "у" or letter == "ю" or\
       letter == "о" or letter == "е" or\
       letter == "э" or letter == "и" or\
       letter == "ы":
        vowels += 1
    else:
        consonants += 1
        a = vowels
        b = consonants


print('Количество слов:', d['Буквы'])
print('Сколько гласных:', vowels)
print('Сколько согласных :', consonants)




