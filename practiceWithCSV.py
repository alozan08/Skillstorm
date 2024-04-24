import csv

''' Using the following Customer class, create a CSV file containing at 
    least five rows of customer data. Write a function that parses the 
    CSV file and returns a list of Customer objects. Call this function 
    and print the data for each object to the console.
'''

class Customer:
    name: str
    email: str
    balance: int

    def __init__(self, name, email, balance):
        self.name = name
        self.email = email
        self.balance = balance


def parse_file(filename):
    with open(filename) as file:
        user_list = []
        reader = csv.reader(file, delimiter=',')
        row = 1
        for list in reader:
            if row != 1:
                customer = Customer(list[0] + " " + list[1], list[2], list[3])
                user_list.append(customer)
                row += 1
            else:
                row += 1
    return user_list

users = parse_file('users.csv')
for user in users:
    print(f'Name: {user.name}, Email: {user.email}, Balance: {user.balance}')