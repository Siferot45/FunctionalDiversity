
# Задание 1: Lambda-функция > список совпадения букв в той же позиции
from random import choice


first = 'Мама мыла раму'
second = 'Рамена мало было'

result = list(map(lambda f, s : f == s, first, second))

print(result)

# Задание 2: Замыкание
def get_advanced_writer(file_name):
    
    def write_everything(*data_set):
        
        with open(file_name, 'a') as file:
            
            for data in data_set:
                file.write(str(data))
        
    return write_everything
    
write = get_advanced_writer('example.txt')
write('Это строчка', ['А', 'это', 'уже', 'число', 5, 'в', 'списке'])


# Задание 3: Класс MysticBall > 
# случайный выбор слова с одинаковой вероятностью для каждого данного в коллекции 
class MysticBall:
    def __init__(self, *words):
        self.words = words

    def __call__(self):
        return choice(self.words)

first_ball = MysticBall('Да', 'Нет', 'Наверное')

print(first_ball())
print(first_ball())
print(first_ball())
