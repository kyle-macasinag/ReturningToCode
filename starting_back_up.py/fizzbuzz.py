#Below is the famous FizzBuzz problem.  Hope you enjoy my solution!


def fizzbuzz():
    for n in range(1,101):
        if (n % 3 == 0) and (n % 5 == 0):
            print ("FizzBuzz")
        elif n % 3 == 0:
            print ("Fizz")
        elif n % 5 == 0:
            print ("Buzz")
        else:
            print (n)


fizzbuzz()