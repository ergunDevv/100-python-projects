# In Python, a scope is a region of the program where a variable is accessible. There are four types of scopes in Python:

# Global scope: This is the outermost scope in a Python program. Variables declared in the global scope are accessible from anywhere in the program.
# Local scope: This is the scope of a function or a class. Variables declared in the local scope are only accessible from within the function or class where they are declared.
# Enclosing scope: This is the scope of the outer function or class from which a function or class is called. Variables declared in the enclosing scope are accessible from within the function or class where they are called.
# Built-in scope: This is the scope of the built-in functions and variables in Python. These variables are always accessible from anywhere in the program.
# The Python interpreter uses the LEGB rule to determine the scope of a variable. The LEGB rule stands for:

# Local
# Enclosing
# Global
# Built-in

# Example 1
def outer_function():
    a = 10  # a is a local variable in outer_function()

    def inner_function():
        b = 20  # b is a local variable in inner_function()
        print(a)  # a is visible in inner_function() because of enclosing scope

    inner_function()


outer_function()


enemies = 1


def increase_enemies():
    # If you wanna modify global variable you can use --->
    global enemies
    # BUT NEVER MODIFY THE GLOBAL VARIABLES
    # Beacuse its prone to bugs and it is really hard to debug.
    # There is just one use case for global and it is for constants like pi or urls
    enemies = 2
    print(f"enemies inside function: {enemies}")


increase_enemies()
print(f"enemies outside function: {enemies}")
