import random
simbols = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
user_input = int(input('Введите длину пароля'))
password = ''
for i in range(user_input):
    password += random.choice(simbols)
print(password)

