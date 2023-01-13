def asterisk(number):
    i = 1
    blank = " "
    asterik = "* "
    b = number - 1
    while i < number:
        print(blank * b, asterik * i)
        i += 1
        b -= 1

    i = 1
    blank = " "
    b = 2
    c = number - 2
    while i <= c:
        print(blank * b, "* " * c)
        c -= 1
        b += 1


asterisk(10)
