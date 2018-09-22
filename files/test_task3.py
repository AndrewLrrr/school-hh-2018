import unittest

from files.task3 import (
    get_init_rectangles,
    get_all_ratios_of_rectangle,
    is_vacancy_in_rectangle,
    get_base_rectangle,
    is_rectangle_correct,
    is_input_data_correct,
    is_rectangles_intersect,
)


class TestUtils(unittest.TestCase):
    def test_is_input_data_correct(self):
        self.assertTrue(is_input_data_correct(32, 4))
        self.assertTrue(is_input_data_correct(36, 4))
        self.assertFalse(is_input_data_correct(37, 5))
        self.assertTrue(is_input_data_correct(40, 4))
        self.assertFalse(is_input_data_correct(40, 0))
        self.assertTrue(is_input_data_correct(40, 1))

    def test_get_init_rectangles(self):
        self.assertEqual(
            ((5, 1), (1, 5)), get_init_rectangles(5, 5, 5))
        self.assertEqual(
            ((3, 2), (2, 3)), get_init_rectangles(3, 3, 6))
        self.assertEqual(
            ((1, 6), (1, 6)), get_init_rectangles(1, 6, 6))
        self.assertEqual(
            ((6, 1), (6, 1)), get_init_rectangles(6, 1, 6))
        self.assertEqual(
            ((2, 4), (1, 8)), get_init_rectangles(2, 8, 8))
        self.assertEqual(
            ((8, 1), (4, 2)), get_init_rectangles(8, 2, 8))
        self.assertEqual(
            ((4, 2), (4, 2)), get_init_rectangles(7, 2, 8))
        self.assertEqual(
            ((4, 2), (4, 2)), get_init_rectangles(6, 2, 8))
        self.assertEqual(
            ((2, 5), (2, 5)), get_init_rectangles(3, 6, 10))
        self.assertEqual(
            ((20, 3), (6, 10)), get_init_rectangles(20, 10, 60))

    def test_get_all_ratios_of_rectangle(self):
        expected = [(4, 1), (2, 2), (1, 4)]
        self.assertEqual(
            expected, get_all_ratios_of_rectangle(expected[0], expected[-1], 4))
        expected = [(10, 1), (5, 2), (2, 5), (1, 10)]
        self.assertEqual(
            expected, get_all_ratios_of_rectangle(expected[0], expected[-1], 10))
        expected = [(12, 3), (9, 4), (6, 6), (4, 9), (3, 12)]
        self.assertEqual(
            expected, get_all_ratios_of_rectangle(expected[0], expected[-1], 36))
        self.assertEqual(
            [(12, 3)], get_all_ratios_of_rectangle(*[(12, 3), (12, 3)], 36))
        expected = [(12, 1), (6, 2), (4, 3), (3, 4), (2, 6), (1, 12)]
        self.assertEqual(
            expected, get_all_ratios_of_rectangle(expected[0], expected[-1], 12))
        expected = [(20, 3), (15, 4), (12, 5), (10, 6), (6, 10)]
        self.assertEqual(expected, get_all_ratios_of_rectangle(*[(20, 3), (6, 10)], 60))

    def test_is_vacancy_in_rectangle(self):
        r = ((0, 1), (0, 2))
        self.assertTrue(is_vacancy_in_rectangle((0, 0), r))
        self.assertTrue(is_vacancy_in_rectangle((0, 1), r))
        self.assertFalse(is_vacancy_in_rectangle((0, 2), r))
        self.assertFalse(is_vacancy_in_rectangle((1, 0), r))

    def test_is_rectangles_intersect(self):
        r1 = ((1, 3), (1, 4))
        r2 = ((0, 6), (2, 3))
        self.assertTrue(is_rectangles_intersect(r1, r2))
        self.assertTrue(is_rectangles_intersect(r2, r1))
        r2 = ((0, 2), (2, 3))
        self.assertTrue(is_rectangles_intersect(r1, r2))
        self.assertTrue(is_rectangles_intersect(r2, r1))
        r2 = ((2, 6), (2, 3))
        self.assertTrue(is_rectangles_intersect(r1, r2))
        self.assertTrue(is_rectangles_intersect(r2, r1))
        r2 = ((2, 6), (3, 4))
        self.assertTrue(is_rectangles_intersect(r1, r2))
        self.assertTrue(is_rectangles_intersect(r2, r1))
        r2 = ((3, 6), (2, 3))
        self.assertFalse(is_rectangles_intersect(r1, r2))
        self.assertFalse(is_rectangles_intersect(r2, r1))
        r2 = ((0, 6), (0, 1))
        self.assertFalse(is_rectangles_intersect(r1, r2))
        self.assertFalse(is_rectangles_intersect(r2, r1))
        r2 = ((2, 6), (4, 5))
        self.assertFalse(is_rectangles_intersect(r1, r2))
        self.assertFalse(is_rectangles_intersect(r2, r1))
        r2 = ((0, 1), (3, 4))
        self.assertFalse(is_rectangles_intersect(r1, r2))
        self.assertFalse(is_rectangles_intersect(r2, r1))
        r1, r2 = (((0, 8), (2, 3)), ((0, 4), (2, 4)))
        self.assertTrue(is_rectangles_intersect(r1, r2))
        self.assertTrue(is_rectangles_intersect(r2, r1))

    def test_get_base_rectangle(self):
        v = (1, 1)
        self.assertEqual(((0, 4), (1, 2)), get_base_rectangle(v, (4, 1)))
        self.assertEqual(((0, 2), (0, 2)), get_base_rectangle(v, (2, 2)))
        self.assertEqual(((1, 2), (0, 4)), get_base_rectangle(v, (1, 4)))
        v = (4, 0)
        self.assertEqual(((1, 5), (0, 1)), get_base_rectangle(v, (4, 1)))
        self.assertEqual(((3, 5), (0, 2)), get_base_rectangle(v, (2, 2)))
        self.assertEqual(((4, 5), (0, 4)), get_base_rectangle(v, (1, 4)))
        v = (2, 3)
        self.assertEqual(((0, 4), (3, 4)), get_base_rectangle(v, (4, 1)))
        self.assertEqual(((1, 3), (2, 4)), get_base_rectangle(v, (2, 2)))
        self.assertEqual(((2, 3), (0, 4)), get_base_rectangle(v, (1, 4)))

    def test_is_rectangle_correct(self):
        vacancies = [(0, 0), (2, 0), (1, 1), (1, 3)]
        i = 2
        lim_x = 4
        lim_y = 3
        rectangle_status = [
            (((0, 4), (1, 2)), 1),
            (((1, 5), (1, 2)), 1),
            (((2, 6), (1, 2)), -1),
            (((0, 4), (0, 1)), -1),
            (((0, 4), (2, 3)), -1),
            (((0, 2), (0, 2)), 0),
            (((1, 3), (0, 2)), 0),
            (((2, 4), (0, 2)), -1),
            (((0, 2), (1, 3)), 1),
            (((1, 3), (1, 3)), 1),
            (((1, 2), (0, 4)), 0),
            (((1, 2), (-1, 3)), -1),
            (((0, 1), (0, 4)), -1),
            (((2, 3), (0, 4)), -1),
        ]
        for r, s in rectangle_status:
            self.assertEqual(s, is_rectangle_correct(vacancies, i, r, lim_x, lim_y))


if __name__ == '__main__':
    unittest.main()
