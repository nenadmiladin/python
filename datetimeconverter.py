def date_time(time: str) -> str:
    month = {'01' : 'January', '02' : 'February', '03' : 'March', '04' : 'April', '05' : 'May', '06' : 'June',
             '07' : 'July', '08' : 'August', '09' : 'September', '10' : 'October', '11' : 'November', '12' :
             'December' 
        }
    x = time.split(' ')
    split1 = x[0].split('.')
    split2 = x[1].split(':')
    d, m, y = split1[0], split1[1], split1[2]
    h, mi = split2[0], split2[1]
    
    return ('{day} {month} {year} year {hour} {hours} {minute} {minutes}'.format(
        day = (lambda d: d if int(d[0]) >= 1 else d[1])(d),
        month = month[m],
        year = y,
        hour = (lambda h: h if int(h[0]) >= 1 else h[1])(h),
        hours = (lambda h: 'hour' if int(h) == 1 else 'hours' )(h),
        minute = (lambda mi: mi if int(mi[0]) >= 1 else mi[1])(mi),
        minutes = (lambda mi: 'minute' if int(mi) == 1 else 'minutes' )(mi))
        )

if __name__ == '__main__':
    print("Example:")
    print(date_time('01.01.2000 00:00'))

    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert date_time("01.01.2000 00:00") == "1 January 2000 year 0 hours 0 minutes", "Millenium"
    assert date_time("09.05.1945 06:30") == "9 May 1945 year 6 hours 30 minutes", "Victory"
    assert date_time("20.11.1990 03:55") == "20 November 1990 year 3 hours 55 minutes", "Somebody was born"
    print("Coding complete? Click 'Check' to earn cool rewards!")
