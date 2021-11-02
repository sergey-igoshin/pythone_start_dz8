"""
Создайте собственный класс-исключение, обрабатывающий ситуацию деления на ноль. Проверьте его работу на данных, вводимых
пользователем. При вводе нуля в качестве делителя программа должна корректно обработать эту ситуацию и не завершиться
с ошибкой.
"""


class OwnError(Exception):
    def __init__(self, text):
        self.text = text


user_answer = (input("Делимое: "), input("Делитель: "))
try:
    divisible, divider = user_answer
    if int(divider) == 0:
        raise OwnError('На ноль делить нельзя!')
except (OwnError, ValueError) as e:
    print(e)
else:
    print(f'Частное: {round(int(divisible) / int(divider), 2)}')
