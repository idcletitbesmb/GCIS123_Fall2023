'''def name():
    name = input('What is your name? ')
    surname = input('surname? ')
    date_of_birth = input('when were you born? ')
    return 'You are', name, surname, 'born', date_of_birth

def calculation():
    x = int(input('Enter first var '))
    sign = input('Enter operation ')
    y = int(input('Enter second var '))

    if sign == '+':
        return str('The answer is ' + str(x + y))
    if sign == '-':
        return str('The answer is ' + str(x - y))
    if sign == '*':
        return str('The answer is ' + str(x * y))
    if sign == '/':
        return str('The answer is ' + str(x / y))
    if sign == '//':
        return str('The answer is ' + str(x // y))
    if sign == '%':
        return str('The answer is ' + str(x % y))
    if sign == '**':
        return str('The answer is ' + str(x ** y))
    
def main():
    print(name())
    print(calculation())

main()'''




from turtle import *

def stickman():
    r = 5
    rt(120)
    fd(30*r)
    backward(30*r)
    lt(60)
    fd(30*r)
    backward(30*r)
    lt(150)
    fd(60*r)
    rt(90)
    circle(50)
    exitonclick()


def square(my_size):
    angle = 90
    fillcolor('blue')
    begin_fill()
    fd(my_size)
    lt(90)
    fd(my_size)
    lt(90)
    fd(my_size)
    lt(90)
    fd(my_size)
    end_fill()
    exitonclick()





def draw_circle(x, y, radius, color):
    up()
    goto(x, y)
    down()
    fd(radius)
    lt(90)
    fillcolor(color)
    begin_fill()
    circle(radius)
    end_fill()

def main():
    draw_circle(10, 10, 100, 'yellow')
    exitonclick()


main()





















































