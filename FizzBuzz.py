n=100
for x in range(1,n):
    if x% 15==0:
        print("fizzBuzz")
    elif x% 3==0:
        print('Fizz')
    elif x% 5==0:
        print("Buzz")
    else:
        print(x)