from random import choice

first = 'Мама мыла раму'
second = 'Рамена мало было'

funk = lambda x,y: x == y
print(list(map(funk, first, second)))

def get_advanced_writer(file_name):

    def write_everything(*data_set):
        with open(file_name, "a", encoding='utf-8') as f:
            data_write = []
            for i in data_set:
                if isinstance(i, str):
                    data_write.append(i)
                elif isinstance(i, int):
                    data_write.append(str(i))
                else:
                    data_write.extend(i)
            for item in data_write:
                f.write(str(item))
                f.write("\n")

    return write_everything

write = get_advanced_writer('example.txt')
write('Это строчка', ["'А', 'это', 'уже', 'число', 5, 'в', 'списке'"])


class MysticBall:
    def __init__(self, *words):
        self.words = words

    def __call__(self):
        return choice(self.words)

first_ball = MysticBall('Да', 'Нет', 'Наверное')
print(first_ball())
print(first_ball())
print(first_ball())