file = open('results.txt', 'w', encoding='UTF-8')
import random
number = int(input("Введите загаданное вами число в диапазоне [0-100]: "))
with open('file.txt', 'a') as file:
    file.write(f'Введите загаданное вами число в диапазоне [0-100]:{number}\n')
    x = 0
    y = 100
    tries = 1
    computer_number = random.randrange(x, y+1)
    while x != y:
        with open('file.txt', 'a') as file:
            file.write(f'Ваше число равно,больше или меньше:э', computer_number)
        z = input()
        if 'больше' in z.lower():
            x = computer_number
            computer_number = random.randrange(x, y)
            tries += 1
            with open('results.txt', 'a') as file:
                file.write(f'больше: {tries}\n')
        elif 'меньше' in z.lower():
            y = computer_number
            computer_number = random.randrange(x, y)
            tries += 1
            with open('results.txt','a') as file:
                file.write(f'меньше:{tries}\n')
        elif 'равно' in z.lower():
            break
print('Ваше число:', number, ' ,а число найденное компьютером: ', computer_number, 'кол-во попыток:', tries)
