# 5. Программа запрашивает у пользователя строку чисел, разделенных пробелом. При нажатии Enter должна выводиться сумма
# чисел. Пользователь может продолжить ввод чисел, разделенных пробелом и снова нажать Enter. Сумма вновь введенных чисел
# будет добавляться к уже подсчитанной сумме. Но если вместо числа вводится специальный символ, выполнение программы
# завершается. Если специальный символ введен после нескольких чисел, то вначале нужно добавить сумму этих чисел к
# полученной ранее сумме и после этого завершить программу.

q = ''
sum_number = 0
while q != 'Q':
    s = map(int,input('Введите список чисел через пробел: ').split())
    sum_number += sum(s)
    print(f'\nТекущая сумма чисел: {sum_number}')
    q = input('Для продолжения ввода нажмите "ENTER"\nДля завершения программы введите Q\n').upper()