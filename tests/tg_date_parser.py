import re
from datetime import datetime

text = """🎫 Знайдено талони 🏛️ ТСЦ МВС № 4841 м. Миколаїв, пров. Транспортний, 1а/1
💼 На послугу: 🚗 Практичний іспит (транспортний засіб навчального закладу)
✅ Талони наявні на наступні дати :
📆 2.5.2024 - 1 🎫 талон
📆 24.4.2024 - 1 🎫 талон 
📆 30.9.2024 - 1 🎫 талон 
"""

matches = re.findall(r'📆 \d+\.\d+\.\d+ - \d+ 🎫 талон', text)

dates = []
for match in matches:
    date_str = re.search(r'\d+\.\d+\.\d+', match).group()
    date_obj = datetime.strptime(date_str, '%d.%m.%Y')
    dates.append((date_str, date_obj))

sorted_dates = sorted(dates, key=lambda x: x[1])
first_date = sorted_dates[0][1].strftime('%Y-%m-%d')
print(first_date)
