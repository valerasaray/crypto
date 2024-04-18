from random import randint as r

file = open('random letters 2.txt', 'w')
for i in range(50000):
    file.write(chr(r(97, 122))) # unicode коды сиволов "a" и "z"