#1 Create two variables – one with your name and one with your age

name = input("What is your name?: ").strip()
age = int(input("How old are you?: ").strip())

#2 Create a function which prints your data as one string

def get_name_and_year(name, age):
    print(name, age)
get_name_and_year(name, age)    

#3 Create a function which prints ANY data (two arguments) as one string

def get_string(x, y):
    print(str(x) + str(y))
get_string("hello", "world")   

#4 Create a function which calculates and returns the number of decades you already lived (e.g. 23 = 2 decades)

def get_decades(age):
    decade = age//10
    print(decade)
get_decades(age)    


 