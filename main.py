import random

print("_____________________________Ввод данных_____________________________")

l=int(input("Введите кол-во символов:"))
ul=input("Использовать буквы? ")
ud=input("Использовать цифры? ")
us=input("Использовать спецсимволы? ")
sa=" "
if us=="Да" or us=="да":
    sa=input("Введите разрешенные спецсимволы: ")
    
print("___________________________Параметры пароля_________________________")

print("Кол-во символов: ", l)
print('Использование букв: ', ul)
print('Использование цифр: ', ud)
print('Использование спецсимволов: ', us)
    
class PasswordGenerator:
    letters_alphabet = 'AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz'
    digits_alphabet = '0123456789'
    specsymbols_alphabet = sa
    
    if ul=="Да" or ul=="да":
        ul="True"
    elif ul=="Нет" or ul=="нет":
        ul="False"
    if ud=="Да" or ud=="да":
        ud="True"
    elif ud=="Нет" or ud=="нет":
        ud="False"
    if us=="Да" or us=="да":
        us="True"
    elif us=="Нет" or us=="нет":
        us="False"
        
    def __init__(self, length= l, use_letters = ul, use_digits = ud, use_specsymbols = us):
        self.length = length
        self.use_letters = use_letters
        self.use_digits = use_digits
        self.use_specsymbols = use_specsymbols
  
    def generate_password(self):
        alphabet = ''
        if self.use_letters:
            alphabet += self.letters_alphabet
        if self.use_digits:
            alphabet += self.digits_alphabet
        if self.use_specsymbols:
            alphabet += self.specsymbols_alphabet
        if not alphabet:
            print ('!')
        password = ''
        for i in range(self.length):
            password += random.choice(alphabet)
        return password

print ("________________Несколько вариантов пароля пароль______________________")
generator = PasswordGenerator(use_specsymbols = True)
print(generator.generate_password())
print(generator.generate_password())
print(generator.generate_password())
print(generator.generate_password())


