N = 10
def my_function():
    N = 1000 # a new local variable 'N' is created and used, global N is not used
    print("local N: ", N)


def my_function_global():
    #global keyword tells python to refer the glocal variable  
    # and not to create a local variable
    global N  
    N = 500 # now a global 'N' will be used
    print("global N: ", N)    

i = 0

def test_function():
    global i
    i = i + 1
    print('i: ', i)
    

test_function()

my_function()
my_function_global()

print("Global N outside function: ", N)