names=['tima','alina','peter ']
words=['kfc', 'school', 'dog']
def up_letter(word: str):
    return word.title()

def last_letter(word: str):
    return word.title()

def show_names(lst, funs):
    for i in lst:
        print(funs(i))

show_names(names, up_letter)
show_names(words, last_letter)