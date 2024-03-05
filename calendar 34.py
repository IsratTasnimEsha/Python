#BISMILLAHIR RAHMANIR RAHIM

print()

import calendar
oct=calendar.month(2000, 10)
print('Calendar of oct, 2000:\n\n', oct, '\n')

print('1900 is a leap year:', calendar.isleap(1900))
print('2016 is a leap year:', calendar.isleap(2016), '\n')

print('Days in 2.2000:', calendar._monthlen(2000, 2))
print('Days in 4, 2012:', calendar._monthlen(2012, 4), '\n')

print('Total leap year between 1900-2000:', calendar.leapdays(1900, 2000), '\n')

days_of_week=['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
print('12.10.2000 is:', days_of_week[calendar.weekday(2000, 10, 12)], '\n')