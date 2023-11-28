#! /usr/bin/python3


# Input: Get y-values from x=-4 to x=4
def get_graph_y():
    yvalues = []
    for i in range(-4, 5):
        temp = None
        while temp == None:
            try:
                temp = float(input("Enter y value at x = " + str(i) + ": "))
                yvalues.append(temp)
            except:
                print("Please enter a numerical value.")
    return yvalues


# Graph identifier
print("---------------- GRAPH IDENTIFIER ----------------")
print("Enter coordinates of a polynomial function. Maximum degree: 7")
# Process: Initialize function
function = "y = "
a = None
# Process: Loop until function can be detected
while a == None:
    # Input: Get y values corresponding to x values from -4 to 4
    y = get_graph_y()
    # Process: Determine value of constant finite difference and degree of function
    constant, degree = finite_differences(y)
    # Process: Calculate leading coefficient of function
    try:
        a = constant/factorial(degree)
    except ZeroDivisionError:
        a = constant
    except TypeError:
        # Output: Print error if function cannot be detected
        print("Error: Your graph either has a degree above 7 or is not a polynomial function. Please try again.")

# Process: Add term to function given coefficient and degree
if a != 0:
    function += ("" if a > 0 else "-") + (('%g' % abs(a)) if a != 1 else "") + "x" + ("^" + str(degree) if degree != 0 else "")
# Process: Loop until all terms are added
while not(degree == 0):
    # Process: Store y coordinates of function after added terms are removed
    y = [y[x]- a*(x-4)**degree for x in range(len(y))]
    # Process: Determine value of constant finite difference and degree of function
    constant, degree = finite_differences(y)
    # Process: Calculate leading coefficient of function
    try:
        a = constant/factorial(degree)
    except:
        a = constant
    # Process: Add term to function given coefficient and degree
    if a != 0:
        function += (" + " if a > 0 else " - ") + (('%g' % abs(a)) if abs(a) != 1 else "") + "x" + ("^" + str(degree) if degree != 0 else "")

# Output: Print function
print(function)

