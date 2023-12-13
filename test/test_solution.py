from unittest import TestCase
from src.solution import correct_text, count_elements


class TestSolution(TestCase):

    def test_correct_text(self):
        bad_brackets = 'some {name, in big text'
        bad_key = 'Some awesome text, {Name}. some more {services}'
        good_txt = '''{name}, ваша запись изменена:
            ⌚ {day_month} в {start_time}
            👩 {master}
            Услуги:
            {services}
            управление записью {record_link}'''
        
        with self.assertRaises(ValueError) as ctx:
            correct_text(bad_brackets)
            self.assertEqual('brackets dont match', ctx.exception)
        with self.assertRaises(ValueError) as ctx:
            correct_text(bad_key)
            self.assertEqual('one or more keys are not accepted', ctx.exception)
        self.assertEqual(good_txt, correct_text(good_txt))

    def test_count_elements(self):
        l = [
            ['665587', 2],
            ['669532', 1],
            ['669537', 2],
            ['669532', 1],
            ['665587', 1]
        ]
        expected = [
            ['665587', 2, 1],
            ['669532', 1, 2],
            ['669537', 2, 1],
            ['665587', 1, 1]
        ]
        self.assertEqual(expected, count_elements(l))