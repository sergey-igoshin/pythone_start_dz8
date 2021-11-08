"""
Начните работу над проектом «Склад оргтехники». Создайте класс, описывающий склад. А также класс «Оргтехника», который
будет базовым для классов-наследников. Эти классы — конкретные типы оргтехники (принтер, сканер, ксерокс). В базовом
классе определите параметры, общие для приведённых типов. В классах-наследниках реализуйте параметры, уникальные для
каждого типа оргтехники.
Продолжить работу над первым заданием. Разработайте методы, которые отвечают за приём оргтехники на склад и передачу в
определённое подразделение компании. Для хранения данных о наименовании и количестве единиц оргтехники, а также других
данных, можно использовать любую подходящую структуру (например, словарь)
Продолжить работу над вторым заданием. Реализуйте механизм валидации вводимых пользователем данных. Например, для
указания количества принтеров, отправленных на склад, нельзя использовать строковый тип данных
"""


def print_color(arg):
    format_color = {
        'GREEN': '\x1b[38;5;46m',
        'RED': '\x1b[38;5;160m',
        'END': '\x1b[0m',
    }
    return format_color[arg]


RED = print_color('RED')
GREEN = print_color('GREEN')
END = print_color('END')


def print_error(text):
    return RED + text + END


def print_action(text):
    print()
    print(GREEN + text + END)


def valid_del_product(len_product, num_product):
    try:
        num = int(num_product)
        if num <= len_product:
            return num
    except (OwnError, Exception):
        return None


class OwnError(Exception):
    def __init__(self):
        self.warehouse = int(len(Warehouse().action[1]))
        self.office_eq = int(len(Warehouse().office_eq))
        self.check = [self.office_eq, self.warehouse]
        self.value = print_error('Ошибка!')

    def validate(self, num, check):
        try:
            num = int(num)
            if num <= self.check[check]:
                return num
        except (OwnError, Exception):
            return None

    def valid_price(self, title):
        while True:
            try:
                num = int(input(f'{title}: '))
                return num
            except (OwnError, Exception):
                print(self.value, 'Вы ввели не число')


class Step:
    def __init__(self):
        self.w = Warehouse()
        self.err = OwnError()
        self.office_eq = [Printer(), Scanner(), Xerox()]

    def input_action(self, n, title, action):
        print_action(title)
        num = self.w.num_next(n)
        print(self.w)
        count = self.err.validate(input(f'{action}: '), num)
        return count

    def step(self):
        while True:
            count = self.input_action(0, 'Программа склад', 'Укажите склад')
            if count == 0:
                break

            if count is not None:
                self.step_2(count)
            else:
                print(self.err.value, 'Не верный аргумент')

    def step_2(self, score):
        while True:
            count = self.input_action(1, self.w.office_eq[score - 1], 'Выберите действие')
            if count == 0:
                break
            elif count is not None:
                if count == 1:
                    print_action(str(self.w.action[1][count - 1] + ' ' + self.w.office_eq[score - 1]))
                    print(self.office_eq[score - 1])
                elif count == 2:
                    print_action(str(self.w.action[1][count - 1] + ' ' + self.w.office_eq[score - 1]))
                    self.add_product(score)
                elif count == 3:
                    self.del_product(score, count)
            else:
                print(self.err.value, 'Не верный аргумент')

    def add_product(self, score):
        self.office_eq[score - 1].product.append([
            f'"{input("Наименование: ")}"',
            f'{self.err.valid_price("Цена"):0,} руб'.replace(',', ' '),
            f'{self.err.valid_price("Кол-во")} ед.',
        ])

    def del_product(self, score, count):
        self.office_eq[score - 1].check = True
        while True:
            print_action(str(self.w.action[1][count - 1] + ' ' + self.w.office_eq[score - 1]))
            print(self.office_eq[score - 1])
            len_product = len(self.office_eq[score - 1].product)
            if len_product == 0:
                self.office_eq[score - 1].check = False
                break
            else:
                num_product = input(f'Выберите товар который надо удалить: ')
                count_del = valid_del_product(len_product, num_product)
                if count_del is not None:
                    if count_del == 0:
                        self.office_eq[score - 1].check = False
                        break
                    self.office_eq[score - 1].product.pop(count_del - 1)
                else:
                    print(self.err.value, 'Не верный аргумент')


class Warehouse:
    def __init__(self):
        self.office_eq = ['"Принтер"', '"Сканер"', '"Ксерокс"']
        self.action = [self.office_eq,
                       ['Показать товар на складе', 'Добавить товар на склад', 'Удалить товар со склада']]
        self.back = ['Выход', 'Назад']
        self.num = 0

    def __str__(self):
        return str('\n'.join([': '.join([str(item), i]) for item, i in enumerate(self.action[self.num], 1)] +
                             [f'0: {self.back[self.num]}']))

    def num_next(self, num):
        self.num = num
        return num


class OfficeEquipment:
    def __init__(self):
        self.product = []
        self.null_product = 'Склад пустой'
        self.check = False

    def __str__(self):
        if len(self.product) == 0:
            return self.null_product
        elif len(self.product) != 0 and self.check:
            return str('\n'.join(
                [': '.join([str(key), val]) for key, val in enumerate([', '.join(i) for i in self.product], 1)] +
                [f'0: {Warehouse().back[1]}']))
        else:
            return str('\n'.join([', '.join(i) for i in self.product]))


class Printer(OfficeEquipment):
    pass


class Scanner(OfficeEquipment):
    pass


class Xerox(OfficeEquipment):
    pass


if __name__ == '__main__':
    s = Step()
    s.step()
    print_action("Программа склад завершена")
