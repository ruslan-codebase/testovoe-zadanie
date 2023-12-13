import re

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
