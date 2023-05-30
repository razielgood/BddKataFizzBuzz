class FizzBuzz:
    @staticmethod
    def calculates(num):
        num = int(num)  # Convert the variable to an integer
        if num % 3 == 0 and num % 5 == 0:
            return "FizzBuzz"
        elif num % 3 == 0:
            return "Fizz"
        elif num % 5 == 0:
            return "Buzz"
        else:
            return str(num)
