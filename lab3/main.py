name_text1 = input('Введите название первого файла с расширением: ')
name_text2 = input('Введите название второго файла с расширением: ')

def detrasher(text):
    text = text.lower()
    text = text.replace('/n', '')
    text = list(text)
    return list(filter(lambda x: ord(x) <= 122 and ord(x) >= 97, text))
    
original_text1 = open(f'{name_text1}', 'r')
mode_text1 = detrasher(original_text1.read())

original_text2 = open(f'{name_text2}', 'r')
mode_text2 = detrasher(original_text2.read())

letters_count = min(len(mode_text1), len(mode_text2))

match_count = 0
for i in range(letters_count):
    if mode_text1[i] == mode_text2[i]:
        match_count += 1
print(match_count/letters_count*100)
