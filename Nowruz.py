import datetime

new_year = datetime.date(2025, 3, 21)
date_object = datetime.date.today()
o = new_year - date_object
print(o)
if o == 0:
    print('tabrik')
