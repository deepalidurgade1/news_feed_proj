###########       Call one python file from another ##################

# from subprocess import call
#
# print("Calling test6 from test7")
# call(["python", "test6.py"])
# print("Done with execution")


##############    Python Methods  #########################
# We can also define a function inside a Python class. A Python Function defined inside a class is called a method.

import requests
# create a class
class Room:
    length = 0.0
    breadth = 0.0

    # method to calculate area
    def calculate_area(self):
        area = self.length * self.breadth
        return area

class GeekforGeeks:

    # default constructor
    def __init__(self, x):
        self.geek = x

    # a method for printing data members
    def print_Geek(self, p):
        print("In class 'GeekforGeeks'")
        print(self.geek)
        print(p)

class NewGeeks:

    # class with no constructor

    # a method for printing data members
    def print_str(self):
        print("In class 'NewGeeks'")
        print(self)


class FetchUrl:

    # default constructor
    def __init__(self, x):
        self.url = x

    # a method for printing data members
    def fetch_url(self):
        print("Fetching Requested URL...........")
        r1 = requests.get(self.url)  # Request
        print("Status Code: ", r1.status_code)

