from random import randint, choice 
from random_word import RandomWords 
import time 
 
start_time = time.time() 
 
file = open("random words2.txt", "w") 
 
for i in range(10000): 
    word = RandomWords().get_random_word() 
    file.write(f'{word} ') 
 
end_time = time.time() 
elapsed_time = end_time - start_time 
print(f"Время выполнения: {elapsed_time} секунд.")