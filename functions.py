
#def statement defines a funciton
#every function has a return value.  If your function doesnt have a return statement the default return value is None.



def hello(name):
    print('Hello ' + name)
    print('Hello has ' + str(len('hello')) + " letters in it")
    
   
hello('Alice')
hello('Bob')


def plusOne(number):
    return number +1

newNumber = plusOne(5)
print(newNumber)


