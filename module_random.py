import random
import secrets
import string as s


random = secrets.SystemRandom()
random.seed(1)
number_random_int = random.randint(1, 100)
number_random_range = random.randrange(1, 50, 2)
number_random_float_range = random.uniform(1_000_000.0, 1_000_000.9)

print(f'\
Random Interger: {number_random_int} \n\
Random Range: {number_random_range} \n\
Random Float: {number_random_float_range:,.2f}')

list_exemple = ['Francisco', 'Leonardo', 'Monteiro', 'Paiva']
weight = [1,2,1,10]

shuffle = random.shuffle(list_exemple)
choice = random.choice(list_exemple)
sample = random.sample(list_exemple, k=3)
choices = random.choices(list_exemple, k=3, weights= weight)

print('Shuffle: ', list_exemple)
print('Choice: ',choice)
print('Sample:', sample)
print('Choices: ', choices)

# Trecho de código para gerar senha segura (senha aleatória).
print(''.join(random.choices(s.ascii_letters + s.digits + s.punctuation, k=7)))
