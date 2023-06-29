#Standard Implementation:

for n in range(1, 101):
    if n % 3 == 0 and n % 5 == 0:
        print("FizzBuzz")
    elif n%3 == 0:
        print("Fizz")
    elif n%5 == 0:
        print("Buzz")
    else:
        print(n)

#Golfed
[print("Fizz"*(i%3<1)+"Buzz"*(i%5<1)or i)for i in range(1,101)]
