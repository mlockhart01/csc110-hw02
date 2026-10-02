#Malia Lockhart
# Task 1.1:
#  Complete the function "read_two_ints" below:
def read_two_ints():
    """Read two numbers from the user and return them as integers."""
   #I have to convert the strings into integers since they are in quotes
    x_string = input("give me x: ")
    x = int(x_string)
    
    y_string = input("give me y: ")
    y = int(y_string)
    
    return x, y
    # ADD a Docstring for this function
    # the return shown below is a placeholder to make sure this runs
    # TODO: complete the function instead of the line shown below
    

# Task 2.1:
#  Complete the function "compute_multadd" below:
def compute_multadd(a, b):
    """Calculate and return (a * b) / (a + b)."""
    #by adding the docstring it will calculate what I told it to do without popping up in the shell, same with all the other docstrings.
    mult_result = a * b
    print("mult result:", mult_result)
    
    add_result = a + b
    print("add result:", add_result)
    
    return mult_result / add_result
    # ADD a Docstring for this function
    # the pass shown below is a placeholder to make sure this runs
    # TODO: complete the function instead of the line shown below
    pass

# Task 3.1:
#  Complete the function "print_fancy" below:
def print_fancy(a, b, ab_multadd):
    """Print the input numbers and multadd result in a fancy format."""
    
    print("*" * 16)
    print("RESULTS:")
    print("first number:", a)
    print("second number:", b)
    print("multadd result:", ab_multadd)
    print("=" * 16)
    # ADD a Docstring for this function
    # the pass shown below is a placeholder to make sure this runs
    # TODO: complete the function instead of the line shown below
    pass

def main ():


    
    #for the other .2 sections you have to add this into the main otherwise it won't understand where to go and it won't print out the results with all of the other functions
    # ADD a Docstring for this function
    # Task 1.2:
    #  Add one line below to call read_two_ints (note that it returns two values)
    #  the call should provide no arguments
    #  store the returned values into two variables: x and y

    x, y = read_two_ints()

    # Task 2.2:
    #  Add one line below to call multadd (note that it returns one value)
    #  the call should provide the arguments x, and y you obtained above;
    #  store the returned value in a variable called xy_multadd

    xy_multadd = compute_multadd (x, y)

    # Task 3.2:
    #  Complete The line below to call print_fancy
    #  the call should provide the arguments x, y, and xy_multadd you obtained above;

    print_fancy(x, y, xy_multadd)


    # Do not modify this final print statement
    print("The End")

# Do not modify these two lines
if __name__ == "__main__":
    main()
