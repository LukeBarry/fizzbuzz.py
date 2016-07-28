import sys

try:
    limit = int(sys.argv[1])
except (IndexError,ValueError):
    while True:
        try:
            limit = int(input("Please enter a number to play the FizzBuzz game... "))
            break
        except ValueError:
            print("You did not enter a NUMBER.")

print("FizzBuzz is counting up to {}".format(limit))
for y in range(1,limit+1):
    if y % 3 == 0 and y % 5 == 0:
        print('FizzBuzz')
    elif y % 3 == 0:
        print('Fizz')
    elif y % 5 == 0:
        print('Buzz')
    else:
        print(y)