import re
from collections import Counter


# 1
def correct_text(txt: str) -> str:
    if txt.count('{') != txt.count('}'):
        raise ValueError('brackets dont match')
    accepted_vals = [
        '{name}',
        '{day_month}',
        '{day_of_week}',
        '{start_time}',
        '{end_time}',
        '{master}',
        '{services}',
        '{record_link}'
    ]
    for val in re.findall(r'\{.*?\}', txt):
        if val not in accepted_vals:
            raise ValueError('one or more keys are not accepted')
    return txt

# 2
def count_elements(l: list) -> list:
    counts = Counter([f'{i[0]}+{i[1]}' for i in l])
    return [[i.split('+')[0], int(i.split('+')[1]), j] for i,j in counts.items()]


# 3
def json_diff(old, new, diff_list):
    diffs = {}
    for key in diff_list:
        if old.get('data').get(key) != new.get('data').get(key):
            diffs[key]=new.get('data').get(key)
    return diffs