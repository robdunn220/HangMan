day = int(raw_input('Day (0-6)? '))

if day < 7:
    if day == 0:
        print 'Sunday'
    if day == 1:
        print 'Monday'
    if day == 2:
        print 'Tuesday'
    if day == 3:
        print 'Wednesday'
    if day == 4:
        print 'Thursday'
    if day == 5:
        print 'Friday'
    if day == 6:
        print 'Saturday'

elif day < 0:
        print 'Error, please input a number 0-6.'

else:
    print 'Error, please input a number 0-6.'
