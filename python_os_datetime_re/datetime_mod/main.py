from datetime import datetime, date, timedelta
import pytz

# print(datetime.datetime.now(tz=pytz.timezone('Europe/Moscow')))
# print(datetime.datetime.today())

# timedate = datetime.datetime(2020, 1, 1, 0, 0, 0)
# today = datetime.datetime.today()
# s = today-timedate
# print(s.days)

# today = datetime.datetime.today()

# abonement = today + timedelta(seconds=180)

# print(abonement)

# print(date.today())

# print(date(2020, 4, 1))

# print(date.today() + timedelta(days=10))

# news_pub_date = datetime(2020, 6, 8, 10, 10, 0)

# print(news_pub_date)
# aylar = {
#     'January': 'Yanvar',
#     'February': 'Fevral',
#     'June': 'Iyun'
# }
# current_ay = datetime.strftime(news_pub_date, '%B')
# print(current_ay)
# print(aylar.get(current_ay, 'Bele bir ay movcud deyil'))
# print(datetime.strftime(news_pub_date, '%d %B, %Y'))

# input_date  = '8 Jun/2020 10:10:10'

# datetime_input_date = datetime.strptime(input_date, '%d %b/%Y %H:%M:%S')


# print(datetime_input_date+timedelta(days=10))