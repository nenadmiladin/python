def float_range(start, stop, step):
  while start < stop:
    yield float(round(start, 2))
    start += step

lista = list(float_range(0, 180, 0.01))

def sun_angle(time):
    time = time.split(':')
    if time[0][0] == '0' and time[1][0] == '0':
        hours = int(time[0][1])
        minutes = int(time[1][1])
    else:
        hours = int(time[0])
        minutes = int(time[1])
    
    angle = ((hours - 6) * 60 + minutes) / 4
    return angle if angle in lista  else "I don't see the sun!"

if __name__ == '__main__':
    print("Example:")
    print(sun_angle("07:00"))
#    print(lista)
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert sun_angle("12:15") == 93.75
    assert sun_angle("18:01") == "I don't see the sun!"
    assert sun_angle("18:00") == 180
    assert sun_angle("07:00") == 15
    assert sun_angle("01:23") == "I don't see the sun!"
    print("Coding complete? Click 'Check' to earn cool rewards!")


