#1
Number=(input('Enter a number: '))
New=2*int(Number)
print('Multiplied by two, your number is '+str(New)+'.')
#2
A=input('Enter a Number:')
if int(A)%2==0:
    print('Your number is even!')
else:
    print('Your number is odd!')
#3
import turtle
tim=turtle.Turtle()
number=(input('Enter one more number: '))
for i in range(4):
    tim.forward(int(number))
    tim.right(90)
print('The number you entered was the side length of the square the turtle drew')
