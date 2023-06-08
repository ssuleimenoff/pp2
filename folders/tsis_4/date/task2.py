from datetime import date, timedelta
yesterday = date.today() - timedelta(1)
tomorrow = date.today() + timedelta(1)
print('Current Date :', date.today())
print('Yesterday was :', yesterday)
print('Tomorrow will be:', tomorrow)