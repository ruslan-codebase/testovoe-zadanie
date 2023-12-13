from unittest import TestCase
from src.solution import correct_text, count_elements, json_diff


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
    
    def test_json_diff(self):
        old = {
            'company_id': 111111,
            'resource': 'record',
            'resource_id': 406155061,
            'status': 'create',
            'data': {
                'id': 11111111,
                'company_id': 111111, 
                'services': [
                    {
                        'id': 9035445,
                        'title': 'Стрижка',
                        'cost': 1500,
                        'cost_per_unit': 1500,
                        'first_cost': 1500,
                        'amount': 1
                    }
                ],
                'goods_transactions': [],
                'staff': {
                    'id': 1819441,
                    'name': 'Мастер'
                },
                'client': {
                    'id': 130345867,
                    'name': 'Клиент',
                    'phone': '79111111111',
                    'success_visits_count': 2,
                    'fail_visits_count': 0
                },
                'clients_count': 1,
                'datetime': '2022-01-25T11:00:00+03:00',
                'create_date': '2022-01-22T00:54:00+03:00',
                'online': False,
                'attendance': 0,
                'confirmed': 1,
                'seance_length': 3600,
                'length': 3600,
                'master_request': 1,
                'visit_id': 346427049,
                'created_user_id': 10573443,
                'deleted': False,
                'paid_full': 0,
                'last_change_date': '2022-01-22T00:54:00+03:00',
                'record_labels': '',
                'date': '2022-01-22 10:00:00'
            }
        }
        new = {
            'company_id': 111111,
            'resource': 'record',
            'resource_id': 406155061,
            'status': 'create',
            'data': {
                'id': 11111111,
                'company_id': 111111,
                'services': [
                    {
                        'id': 22222225,
                        'title': 'Стрижка',
                        'cost': 1500,
                        'cost_per_unit': 1500,
                        'first_cost': 1500,
                        'amount': 1
                    }
                ],
                'goods_transactions': [],
                'staff': {
                    'id': 1819441,
                    'name': 'Мастер'
                },
                'client': {
                    'id': 130345867,
                    'name': 'Клиент',
                    'phone': '79111111111',
                    'success_visits_count': 2,
                    'fail_visits_count': 0
                },
                'clients_count': 1,
                'datetime': '2022-01-25T13:00:00+03:00',
                'create_date': '2022-01-22T00:54:00+03:00',
                'online': False,
                'attendance': 2,
                'confirmed': 1,
                'seance_length': 3600,
                'length': 3600,
                'master_request': 1,
                'visit_id': 346427049,
                'created_user_id': 10573443,
                'deleted': False,
                'paid_full': 1,
                'last_change_date': '2022-01-22T00:54:00+03:00',
                'record_labels': '',
                'date': '2022-01-22 10:00:00'
            }
        }
        diff_list = ['services', 'staff', 'datetime']
        expected = {
            'services': [
                {
                    'id': 22222225,
                    'title': 'Стрижка',
                    'cost': 1500,
                    'cost_per_unit': 1500,
                    'first_cost': 1500,
                    'amount': 1
                }
            ],
            'datetime': '2022-01-25T13:00:00+03:00',
        }
        self.assertEqual(expected, json_diff(old, new, diff_list))