#!/usr/bin/python3
def fizzbuzz():
    for number in range(100):
        number = number + 1
        string = ""
        if (number % 15) == 0:
            string += "FizzBuzz"
        elif (number % 3) == 0:
            string += "Fizz"
        elif (number % 5) == 0:
            string += "Buzz"
        if string == "":
            string = str(number)
        print("{} ".format(string), end="")
