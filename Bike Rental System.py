class bikeshop: 
    def __init__(self,stock): 
        self.stock = stock 
    def displayBike(self): 
        print(f"Total Bikes: {self.stock}") 
    def rent_for_bike(self,quantity): 
        if quantity <= 0: 
            print("Enter the positive value or greater than Zero") 
        elif quantity > self.stock: 
            print("Enter the value less than or equal to stock")  
        else: 
            total_price = quantity * 100
            self.stock -= quantity
            print(f"Total price: {total_price} ") 
            print(f"Total Bikes {self.stock} ") 
            return total_price
while True:  
    object = bikeshop(100) 
    user_input = input(''' 
    1 Display Bike 
    2 Rent A bike  
    Enter your choice: ''')                   
    try:
        if user_input == '1': 
            object.displayBike() 
        elif user_input == '2': 
            n = int(input("Enter the quantity:___")) 
            object.rent_for_bike(n) 
        elif user_input == '3': 
            print("Thank you for using our bike rental system.") 
            break 
        else: 
            print("Invalid input. Please enter a number between 1 and 3.")
    except ValueError:
        print("Invalid input. Please enter a valid number.")
    except ValueError:
        print("Invalid input. Please enter a valid number.")

    

 
