def greet():
    print('Hello my name is bryan.')
    print('May i know ur name please')

    username = input()

    print("Hello Bryan, My name is ", username)
    print('How are you today?')
greet()

class Student():
    #propeties
    name = ''
    age = 12
    year = 7
    house = 'red'
    class_teacher = 'Mrs Harrowwood'
    
    #constructor
    def __init__(self):
        print('making a new student')

    #another fuctuon
    def change_details(self):
        print('Please enter your age: ')
        self.age = int(input())
        print('Please enter the name of the student: ')
        self.name = input()

    #another function
    def show_details(self):
        print('The details of student are: ')
        print(self.name)
        print(self.age)
        print(self.year)
        print(self.house)
        print(self.class_teacher)

Blake = Student()
Thomas = Student()
#jack = Student.change_details()
