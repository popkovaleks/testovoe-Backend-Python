from random import randint


class SearchPoint():
    '''Класс искомой точки'''
    def __init__(self, w, h):
        '''инициализация случайных координат искомой точки'''
        self.__x = randint(0, w)
        self.__y = randint(0, h)
    def where_is_point(self, x, y):
        '''Описывает положение искомой точки относительно текущей.
        Возможные варианты: "R", "RU", "RD", "L", "LU", "LD", "U", "D" , ""
        '''
        print(x, y)
        pos_x = pos_y = ''
        if x > self.__x:
            pos_x = 'L'
        elif x < self.__x:
            pos_x = 'R'
        if y > self.__y:
            pos_y = 'D'
        elif y < self.__y:
            pos_y = 'U'
        return pos_x+pos_y


def main():

    w = int(input("Введите ширину сетки: "))
    h = int(input("Введите высоту сетки: "))
    # Создание точки:
    SP = SearchPoint(w, h)

    x = int(input("Начальная x-координата: "))
    y = int(input("Начальная y-координата: "))

    x_old = 0
    y_old = 0

    position = '_'

    while position != '':
        # сравнение текущей точки(x,y) с искомой
        position = SP.where_is_point(x,y)

        if position == 'R':
            x = x + 2
        elif position == 'L':
            x = x - 1
        elif position == 'U':
            y = y + 1
        elif position == 'D':
            y = y - 2
        elif position =='RU':
            x = x + 2
            y = y + 1
        elif position == 'RD':
            x = x + 2
            y = y - 2
        elif position == 'LU':
            x = x - 1
            y = y + 1
        elif position == 'LD':
            x = x - 1
            y = y - 2


if __name__ == '__main__':
    main()
