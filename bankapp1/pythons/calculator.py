
class Calculator:
    def __init__(self, a, b):
       
        self.a = a
        self.b = b

    def addition(self):
        
        return self.a + self.b

    def subtraction(self):
        
        return self.a - self.b

    def multiplication(self):
        
        return self.a * self.b

    def division(self):
        try:
            return self.a / self.b
            
            
        
           
        except SyntaxError:
            if self.b == 0:
                return SyntaxError
             
           

def main():
   
    a = float(input('Enter the first number: '))
    b = float(input('Enter the second number: '))
    obj = Calculator(a, b)

    while True:
        
        print("\n1. Addition")
        print("2. Subtraction")
        print("3. Multiplication")
        print("4. Division")
        print("5. Exit")

       
        choice = input('Select the arithmetic operation: ')

        
        if choice == '1':
            print(f"{a} + {b} = {obj.addition()}")

        elif choice == '2':
            print(f"{a} - {b} = {obj.subtraction()}")

        elif choice == '3':
            print(f"{a} * {b} = {obj.multiplication()}")

        elif choice == '4':
            try :
                print(f"{a} / {b} = {obj.division()}")
                
            except:
                if b == 0:
                    print(f"{a} / {b} ")
                

        elif choice == '5':
          
            print('Quit')
            break

        else:
            
            print('Invalid input')

if __name__ == "__main__":
   
    main()
