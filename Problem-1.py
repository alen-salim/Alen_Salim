# Problem-1: Create a small calculator which performs operations such as Addition, Subtraction, Multiplication and Division using class.
#   Calculator inputs :> ‘a’, ‘b’ and ‘type of operation’
#   Datatype :> ‘a’ = double, ‘b’ = double, ‘type of operation’ = string

class Calculator:
    def __init__(self,a:float,b:float):
        self.a = a
        self.b = b
    
    def add(self):
        return self.a + self.b
    
    def subtract(self):
        return self.a - self.b
    
    def multiply(self):
        return self.a * self.b
    
    def divide(self):
        return self.a / self.b
    
def main():
    
    a:float = float(input("Enter the first digit:"))
    b:float = float(input("Enter the second:"))

    numbers = Calculator(a,b)


    while True:
        print("2choose an operation")
        print("1. add")
        print("2. subtract")
        print("3. multiply")
        print("4. divide")
        print("5. Exit the operation")
        choice = input("Enter your choice : ")
        

        match choice:
            case "1":
                print(numbers.add())
            case "2":
                print(numbers.subtract())
            case "3":
                print(numbers.multiply())
            case "4":
                print(numbers.divide())
            case "5":
                print("Ended.")
                break
            case _:
                print("Invalid Choice")


if __name__ == "__main__":
    main()
