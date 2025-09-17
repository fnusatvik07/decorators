def outer_function(original_function):

    def wrapper_function():
        print("Hi I am Wrapper Function")
        print("This is Decorator Running")

        return original_function()
    
    return wrapper_function


@outer_function
def display():
    print("This is Display Function running")

@outer_function
def display_info(name,age):
    print(f"Display info function ran with values {name} and {age}")

display_info("John",30)