def outer_function(original_function):

    def wrapper_function():
        print("Hi I am Wrapper Function")
        print("This is Decorator Running")

        return original_function()
    
    return wrapper_function


@outer_function
def display():
    print("This is Display Function running")


display()

# p=outer_function(display)

# p()












