def minimum_skipped_number(a):
    s = set()  # Множество куда будем сохранять элементы для проверки

    for n in a:
        # Отбрасываем все ненатуральные числа
        if n <= 0:
            continue
        s.add(n)

    cur_n = 1
    for _ in range(len(s)):
        if cur_n not in s:
            return cur_n
        cur_n += 1

    return cur_n


print(minimum_skipped_number(map(int, input().split())))
