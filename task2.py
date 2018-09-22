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
#    является возможным, возвращаем None;
# 4. В противном случае, генерируем список всех возможных площадей от y=min, x=max (максимально
#    широкий прямоугольник) до y=max, x=min (максимально высокий прямоугольник);
# 5. Берем крайнюю левую вершину (0, 0);
# 6. Выбираем для нее наиболее оптимальный прямоугольник,который содержит строго одну вакансию и
#    не выходит за пределы карты;
# 7. Выбираем следующую крайнюю левую свободную вершину и возвращаемся в пункт 6;
# 8. Если прямоугольник не содержит вакансий или вакансий больше одной или он выходит за пределы
#    карты, то выбираем следующий, более узкий прямоугольник;
# 9. Если ни один прямоугольник не подошел, значит возращаемся в пункт 6 предыдущей свободной вершины
#    и выбираем следующий прямоугольник;
# 10.Если для последней свободной вершины мы нашли прямоугольник соответствующий всем необходимым
#    критериям, значит задача решена, возвращаем прямоульники;


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


def is_point_in_rectangle(r, point):
    """
    Проверяет, что точка внитри прямоугольника
    :param r: tuple
    :param point: tuple
    :return: bool
    """
    (x1, x2), (y1, y2) = r
    x, y = point
    if x1 <= x < x2 and y1 <= y < y2:
        return True
    return False


def is_rectangle_in_map(r, lim_x, lim_y):
    """
    Проверяет, что прямоугольник не выходит за переделы карты
    :param r: tuple
    :param lim_x: int
    :param lim_y: int
    :return: bool
    """
    (x1, x2), (y1, y2) = r
    if x2 > lim_x + 1:
        return False
    if y2 > lim_y + 1:
        return False
    if x1 < 0 or y1 < 0:
        return False
    return True


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


def get_rectangle_vacancy(r, vacancies):
    """
    Возвращает координаты вакансии внутри данного прямоугольника
    или None в случае, если вакансий нет или > 1
    :param r: tuple
    :param vacancies: list
    :return: tuple|None
    """
    point = None
    for j in range(len(vacancies)):
        if is_point_in_rectangle(r, vacancies[j]):
            if point is None:
                point = vacancies[j]
            else:
                return None
    return point


def get_vertex_rectangle(vertex, ratio):
    """
    Создает прямоугольник заданного размера, начинающийся в
    заданной вершине
    :param vertex: tuple
    :param ratio: tuple
    :return: tuple
    """
    w, h = ratio
    x, y = vertex
    return (x, x + w), (y, y + h)


def split_map(m):
    """
    Разделяет карту карту на N равных прямоугольных частей так,
    чтобы в каждой была одна вакансия
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

    result = []

    # С помощью поиска с возвратом пытаемся найти прямоугольники
    def backtracking_vacancies_rectangles(rectangles=None, y=0):
        rectangles = rectangles if rectangles is not None else []

        if len(rectangles) == len(vacancies):
            result.extend(rectangles)
            return True
        for i in range(y, h):
            for j in range(w):
                vertex = (j, i)
                v_status = True
                for r in rectangles:
                    if is_point_in_rectangle(r, vertex):
                        v_status = False
                if not v_status:
                    continue
                for ratio in ratios:
                    rectangle = get_vertex_rectangle(vertex, ratio)
                    if not is_rectangle_in_map(rectangle, w-1, h-1):
                        continue
                    vacancy = get_rectangle_vacancy(rectangle, vacancies)
                    if not vacancy:
                        continue
                    r_status = True
                    for r in rectangles:
                        if is_rectangles_intersect(r, rectangle):
                            r_status = False
                            break
                    if not r_status:
                        continue
                    rectangles.append(rectangle)
                    status = backtracking_vacancies_rectangles(
                        rectangles,
                        i if rectangle[0][1] < w else i+1,
                    )
                    rectangles.pop()
                    if status:
                        return True
                return False

    backtracking_vacancies_rectangles()

    return result


def print_result(rectangles, m):
    """
    Выводит результаты в заданном порядке
    :param rectangles: list
    :param m: list
    :return: None
    """
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
