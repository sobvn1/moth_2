data_tuple = ('h', 6.13, 'C', 'e', 'T', True, 'k', 'e', 3, 'e', 1, 'g')
letters = ()
numbers =()
for i in data_tuple :
    letters = ['h','C','e','T',True,'k','e','e','g']
    letters[4], letters[-1] = letters[-1], letters[4]
    letters[4], letters[0] = letters[0], letters[4].title()
    letters[6], letters[1] = letters[1], letters[6]
    letters[6], letters[3] = letters[3], letters[6]
    letters[6], letters[4] = letters[4], letters[6]
    letters[7], letters[5] = letters[5], letters[7]
    letters[3], letters[6] = letters[6], letters[3].lower()
    letters[7], letters[3] = letters[3], letters[7]

    numbers = [6.13,3*3,1*1]
    del numbers[0]
    numbers.insert(1, 2*2)
    numbers.sort()

print(tuple(letters))
print(tuple(numbers))
