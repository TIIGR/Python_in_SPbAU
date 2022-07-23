

def de_en_code(text):
    code = ''
    if len(text) == 0:
        return print('Текстовый файл пуст!')
    elif ord(text[0]) == 1425:
        for Ord in range(1, len(text)):
            if ord(text[Ord]) < 1424:
                code += chr((ord(text[Ord]) + ((-1) ** Ord) * Ord) % 1424)
            else:
                return print('Присутствуют недопустимые символы! Один из таких:', text[Ord])
    else:
        for Ord in range(0, len(text)):
            if ord(text[Ord]) < 1424:
                code += chr((ord(text[Ord]) + ((-1) ** Ord) * (Ord + 1)) % 1424)
            else:
                return print('Присутствуют недопустимые символы! Один из таких:', text[Ord])
        code = chr(1425) + code
    with open(Directory, 'w+', encoding='utf-8') as txt:
        txt.write(code)
    if len(text) < len(code) :
        return print('Текст зашифрован!')
    else:
        return print('Текст расшифрован!')


Directory = str(input('Укажите полный путь к текстовому файлу: '))
TxtFile = open(Directory, 'r', encoding='utf-8')
de_en_code(TxtFile.read())