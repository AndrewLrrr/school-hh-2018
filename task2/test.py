import unittest

from task2.main import (
    get_init_rectangles,
    get_all_ratios_of_rectangle,
    is_point_in_rectangle,
    is_input_data_correct,
    is_rectangle_in_map,
    get_rectangle_vacancy,
    get_vertex_rectangle,
    is_rectangles_intersect,
)


class TestUnits(unittest.TestCase):
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

    def test_is_point_in_rectangle(self):
        r = ((0, 2), (0, 2))
        self.assertTrue(is_point_in_rectangle(r, (0, 0)))
        self.assertTrue(is_point_in_rectangle(r, (0, 1)))
        self.assertFalse(is_point_in_rectangle(r, (0, 2)))
        self.assertFalse(is_point_in_rectangle(r, (2, 0)))

    def test_is_rectangle_in_map(self):
        lim_x = 4
        lim_y = 3
        self.assertTrue(is_rectangle_in_map(((0, 4), (1, 2)), lim_x, lim_y))
        self.assertTrue(is_rectangle_in_map(((1, 5), (1, 2)), lim_x, lim_y))
        self.assertTrue(is_rectangle_in_map(((0, 5), (0, 4)), lim_x, lim_y))
        self.assertFalse(is_rectangle_in_map(((2, 6), (1, 2)), lim_x, lim_y))
        self.assertFalse(is_rectangle_in_map(((1, 2), (-1, 3)), lim_x, lim_y))
        self.assertFalse(is_rectangle_in_map(((1, 2), (1, 5)), lim_x, lim_y))
        self.assertFalse(is_rectangle_in_map(((-1, 2), (1, 3)), lim_x, lim_y))

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

    def test_get_rectangle_vacancy(self):
        """
        o.o..
        .o...
        .....
        .o...
        """
        vacancies = [(0, 0), (2, 0), (1, 1), (1, 3)]
        self.assertEqual((0, 0), get_rectangle_vacancy(((0, 2), (0, 1)), vacancies))
        self.assertIsNone(get_rectangle_vacancy(((0, 2), (0, 3)), vacancies))
        self.assertIsNone(get_rectangle_vacancy(((0, 3), (0, 3)), vacancies))
        self.assertIsNone(get_rectangle_vacancy(((1, 2), (0, 1)), vacancies))
        self.assertEqual((2, 0), get_rectangle_vacancy(((1, 3), (0, 1)), vacancies))
        self.assertEqual((2, 0), get_rectangle_vacancy(((2, 4), (0, 2)), vacancies))
        self.assertEqual((1, 1), get_rectangle_vacancy(((1, 2), (0, 2)), vacancies))
        self.assertEqual((1, 3), get_rectangle_vacancy(((0, 2), (2, 4)), vacancies))
        self.assertIsNone(get_rectangle_vacancy(((1, 2), (1, 4)), vacancies))

    def test_get_vertex_rectangle(self):
        self.assertEqual(((0, 3), (0, 2)), get_vertex_rectangle((0, 0), (3, 2)))
        self.assertEqual(((1, 5), (2, 5)), get_vertex_rectangle((1, 2), (4, 3)))


if __name__ == '__main__':
    unittest.main()
