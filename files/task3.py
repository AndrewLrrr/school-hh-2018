"""
Раздели карту
Ограничение времени 1 секунда
Ограничение памяти  64Mb
Ввод                стандартный ввод или input.txt
Вывод               стандартный вывод или output.txt

Представьте, что карта задана следующим прямоугольником:
........
..o.....
...o....
........
где о - это местоположение вакансии. Необходимо разделить карту на N равных прямоугольных частей так, чтобы в каждой 
была одна вакансия. В случае, если решения нет - ничего выводить не нужно.
Порядок частей в ответе должен быть сверху вниз, слева направо, т.е. по положению левой верхней точки региона.
Если решений несколько - нужно выбрать решение с максимальной шириной первого элемента.

Примеры:
1) Выбор из нескольких решений:
.o......
......o.
....o...
..o.....

Для этой карты мы можем найти 3 решения:
Решение 1 (горизонтальное разделение):
.o......

......o.
 
....o...
 
..o.....

Решение 2 (вертикальное разделение):
.o
..
..
..

..
..
..
o.

..
..
o.
..

..
o.
..
..

Решение 3:
.o..
....

....
..o.

....
..o.

o...
....

Правильным решением будет первое, т.к. оно имеет наибольшую ширину первого элемента.

2) Решение с частями разной формы:
.o.o....
........
....o...
........
.....o..
........

Решение:
.o
..
..
..
..
..

.o....
......
 
..o...
......
 
...o..
......

Несмотря на то, что части имеют разную форму, они все - одной площади.

3) Пример входных данных, для которых решения не существует:
.o.o....
.o.o....
........
........
........
........

В данном случае не нужно ничего выводить в ответ

Формат ввода
........
..o.....
...o....
........
Формат вывода
........
..o.....

...o....
........

Примечания:
Размер карты по горизонтали и по вертикале не превышает 100.
Количество вакансий всегда больше 1 и меньше 10
Каждая часть должна быть прямоугольником
Равные прямоугольные части - это части, равные по площади, хотя их формы могут быть разными
Части в ответе должны быть упорядочены по координатам своей левой верхней точки. Из двух частей в ответе раньше должна 
идти та, верхняя левая точка которой находится выше. Если левые верхние точки обеих частей находятся на одной высоте, 
то первой должна быть та часть, верхняя левая точка которой находится левее.
Из всех возможных решений задачи следует выбрать решение с максимальной шириной первого элемента. Если у нескольких 
возможных решений первый элемент имеет одинаковую ширину, то следует выбрать решение с максимальной шириной второго 
элемента и т.д.
"""

# Алгоритм решения задачи основывается на поиске с возвратом:
# 1. Определяем количество вакансий (n) и общую площадь (S);
# 2. От кол-ва вакансий (n) и общей площади определяем минимальную площадь на одну вакансию (s = S/n);
# 3. Если n = 0 или площадь не соответствует кол-ву вакансий,значит посчитать равные площади не
#    является возможным, возвращаем None
# 4. В противном случае, генерируем список всех возможных площадей от y=1, x=max (s0) до y=max, x=1 (si),
#    каждый раз уменьшая x в 2 раза и увеличивая y в 2 раза;
# 5. Проходим по каждой вакансии и генерим для нее список доступных площадей от s0 до si с учетом
#    соседних вакансий от площади с наибольшей шириной до площади с наименьшей шириной;
# 6. Берем вакансию, выбираем у нее площадь которая не пересекается с площадью предыдущих вакансий
# 7. Рекурсивно повторяем шаг 6 пока не дойдем до последней вакансии
# 8. Если у последней вакансии площадь не пересекается с одной предыдущих, то задача решена, возвращаем
#    прямоугольники
# 9. В противном случае, возвращаемся к ближайшей вакансии, где есть пересечение и выбираем следующую площадь
# 10.Если после всех итераций площади все равно пересекаются, значит посчитать равные площади не является
#    возможным, возвращаем None


def is_input_data_correct(S, n):
    """
    Проверяет, что входящие данные корректные:
    - количество вакансий > 0
    - площадь соответсвует количеству вакансий
    :param S: int
    :param n: int
    :return: bool
    """
    return n != 0 and S % n == 0


def get_init_rectangles(x, y, s):
    """
    Определяет пропорции первого и последнего прямоугольника
    для заданной площади
    :param x: int
    :param y: int
    :param s: int
    :return: tuple
    """
    while s % x != 0:
        x -= 1
    while s % y != 0:
        y -= 1
    return (x, s // x), (s // y, y)


def get_all_ratios_of_rectangle(first, last, s):
    """
    Определяет пропорции всех прямоугольников между первым и последним
    :param first: tuple
    :param last: tuple
    :param s: int
    :return: list
    """
    from math import sqrt
    res = []
    max_x, min_y = first
    min_x, max_y = last
    res_x = []

    for y in range(1, int(sqrt(s) + 1)):
        if s % y == 0:
            x = s // y
            if max_x >= x >= min_x:
                res_x.append((x, y))
                res.append((x, y))

    for y, x in reversed(res_x):
        if max_y >= y >= min_y and y != x:
            res.append((x, y))

    return res


def is_vacancy_in_rectangle(v, r):
    """
    Проверяет, что вакансия внитри прямоугольника
    :param v: tuple
    :param r: tuple
    :return: bool
    """
    (x1, x2), (y1, y2) = r
    x, y = v
    if x1 <= x < x2 and y1 <= y < y2:
        return True
    return False


def is_rectangles_intersect(r1, r2):
    """
    Проверяет, что прямоугольники пересекаются
    :param r1: tuple
    :param r2: tuple
    :return: bool
    """
    (x_min1, x_max1), (y_min1, y_max1) = r1
    (x_min2, x_max2), (y_min2, y_max2) = r2

    return all([x_min1 < x_max2,
                x_min2 < x_max1,
                y_min1 < y_max2,
                y_min2 < y_max1])


def get_base_rectangle(v, r):
    """
    Создает прямоугольник заданного размера, сдвинутый 
    максимально влево и вверх относительно вакансии
    :param v: tuple
    :param r: tuple
    :return: tuple
    """
    w, h = r
    x, y = v
    x1 = y1 = 0
    if x + 1 - w >= 0:
        x1 = x + 1 - w
    if y + 1 - h >= 0:
        y1 = y + 1 - h
    return (x1, x1 + w), (y1, y1 + h)


def move_rectangle_to_right(r):
    """
    Перемещает прямоугольник вправо
    :param r: tuple
    :return: tuple
    """
    w, h = r
    x1, x2 = w
    return (x1 + 1, x2 + 1), h


def move_rectangle_to_bottom(r):
    """
    Перемещает прямоугольник вниз
    :param r: tuple
    :return: tuple
    """
    w, h = r
    y1, y2 = h
    return w, (y1 + 1, y2 + 1)


def is_rectangle_correct(vacancies, i, r, lim_x, lim_y):
    """
    Проверяет, что прямоугольник содержит текущую вакансию,
    не содержит других вакансий и не выходит за пределы поля.
    Возвращает значения:
    1  - прямоугольник корректный
    0  - в прямоугольнике чужая вакансия, но можно продолжать 
         генерировать другие прямоугольники на его основе
    -1 - в прямоугольнике нет его вакансии или он вышел за пределы
         карты, останавливаем дальнейшие генерации
    :param vacancies: list
    :param i: int
    :param r: tuple
    :param lim_x: int
    :param lim_y: int
    :return: int
    """
    w, h = r
    x1, x2 = w
    y1, y2 = h
    if x2 > lim_x + 1:
        return -1
    if y2 > lim_y + 1:
        return -1
    if x1 < 0 or y1 < 0:
        return -1
    if not is_vacancy_in_rectangle(vacancies[i], r):
        return -1
    for j in range(len(vacancies)):
        if j == i:
            continue
        if is_vacancy_in_rectangle(vacancies[j], r):
            return 0
    return 1


def generate_rectangles_for_vacancy(vacancies, i, ratios, lim_x, lim_y):
    """
    Генерирует все возможные прямоугольники для вакансии
    :param vacancies: list
    :param i: int
    :param ratios: list
    :param lim_y: int
    :param lim_x: int
    :return: list
    """
    from collections import deque
    q = deque([])
    res = []
    visited = set()

    for ratio in ratios:
        r = get_base_rectangle(vacancies[i], ratio)
        q.append(r)
        while q:
            r = q.popleft()
            r_status = is_rectangle_correct(vacancies, i, r, lim_x, lim_y)
            if r_status != -1:
                if r_status == 1 and r not in visited:
                    res.append(r)
                    visited.add(r)
                q.append(move_rectangle_to_right(r))
                q.append(move_rectangle_to_bottom(r))
    return res


def split_map(m):
    """
    Разделяет карту карту на N равных прямоугольных частей так,
    чтобы в каждой была одна вакансия.
    :param m: list
    :return: list
    """
    # Список координат вакансий, он нам еще понадобится
    vacancies = []

    # Определяем количество вакансий (n) и общую площадь (S)
    h = len(m)
    w = len(m[0])
    S = h * w
    for y in range(h):
        for x in range(w):
            if m[y][x] == 'o':
                vacancies.append((x, y))

    # Проверяем что вакансии есть и их можно разделить на
    # прямоугольники, иначе возвращаем пустой список
    n = len(vacancies)
    if not is_input_data_correct(S, n):
        return []

    # Необходимая площадь для каждой вакансии
    s = S // n

    # Генерируем все возможные размерности
    ratios = get_all_ratios_of_rectangle(*get_init_rectangles(w, h, s), s=s)

    rectangles = []
    for i in range(len(vacancies)):
        gen = generate_rectangles_for_vacancy(vacancies, i, ratios, w-1, h-1)
        # Если для вакансии не получилось сгенерировать ни одного прямоугольника
        # значит дальше искать их бессмысленно, возвращаем пустой список
        if not gen:
            return []
        rectangles.append(gen)

    result = []

    # С помощью поиска с возвратом пытаемся найти прямоугольники
    def backtracking_vacancies_rectangles(v_idx=0, stack=None):
        stack = stack if stack is not None else []
        if v_idx == len(vacancies):
            result.extend(stack)
            return True, -1  # Второй параметр в данном случае не нужен
        intersects = set()
        for r in rectangles[v_idx]:
            # Проходим по предыдущим прямоугольникам в обратном направлении,
            # Чтобы вернуться к ближайшему в случае пересечения
            r_status = True
            for j in range(len(stack)-1, -1, -1):
                if is_rectangles_intersect(r, stack[j]):
                    r_status = False
                    intersects.add(j)
                    break

            # Если нет возможности поставить прямоугольник,
            # сразу переходим к следующему
            if not r_status:
                continue

            stack.append(r)
            status, idx = backtracking_vacancies_rectangles(v_idx+1, stack)
            stack.pop()
            if not status:
                if idx != v_idx:
                    return False, idx
            else:
                # Останавливаем цикл, считаем, что решение найдено
                return True, -1
        if intersects:
            # В случае наличия пересечений, возвращаемся
            # к ближайшему прямоугольнику где было пересечение
            return False, max(intersects)
        return True, -1

    backtracking_vacancies_rectangles()

    return result


def print_result(rectangles, m):
    """
    Выводит результаты в заданном порядке
    :param rectangles: list
    :param m: list
    :return: None
    """
    rectangles.sort(key=lambda r: (r[1][0], r[0][0]))
    for r in rectangles:
        (x1, x2), (y1, y2) = r
        for i in range(y1, y2):
            for j in range(x1, x2):
                print(m[i][j], end='')
            print()
        print()


inp = []

while True:
    try:
        line = input().strip()
        if line:
            inp.append(line)
    except EOFError:
        break

print_result(split_map(inp), inp)


#
# """
# oo.....o
# ...o.o..
# ...o...o
# ....o...
# """
#
# """
# ........
# ........
# ...o....
# ........
# .o......
# ........
# """
#
#
# if __name__ == '__main__':
#     source = """
#     .o...o.o
#     ..o.....
#     ........
#     oo..o..o
#     """
#
#     inp = []
#
#     for l in map(lambda t: t.strip(), source.split('\n')):
#         if l:
#             inp.append(list(l))
#
#     import timeit
#     print(timeit.timeit("split_map(inp)", setup="from __main__ import split_map, inp", number=1))
#     print_result(split_map(inp), inp)
#     print()
#
#     source2 = """
#     .o.o....
#     ........
#     ....o...
#     ........
#     .....o..
#     ........
#     """
#
#     inp2 = []
#
#     for l in map(lambda t: t.strip(), source2.split('\n')):
#         if l:
#             inp2.append(list(l))
#
#     print(timeit.timeit("split_map(inp2)", setup="from __main__ import split_map, inp2", number=1))
#     print_result(split_map(inp2), inp2)
#
#     source3 = """
#     .o.o....
#     .o.o....
#     ........
#     ........
#     ........
#     ........
#     """
#
#     inp3 = []
#
#     for l in map(lambda t: t.strip(), source3.split('\n')):
#         if l:
#             inp3.append(list(l))
#
#     # split_map(inp)
#     print(timeit.timeit("split_map(inp3)", setup="from __main__ import split_map, inp3", number=1))
#     print_result(split_map(inp3), inp3)
