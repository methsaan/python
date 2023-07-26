#! /usr/bin/python3

import math
import collections
import time
import random
from tkinter import *

# Process: Define colors, used for graphs
COLORS = ["red", "orange", "yellow", "green", "blue", "purple", "white", "aqua", "pink", "teal", "gray", "brown"]

# Input: Get calculator mode option
def get_option():
    option = ""
    while option not in ['b', 'g', 'd', 'q', 'quit']:
        option = input("Choose your mode - (b)asic calculator, (g)raph identifier, (d)ata analyser, (q)uadratics calculator, 'quit' to quit: ")
        if option not in ['b', 'g', 'd', 'q', 'quit']:
            print("Please enter a valid option.")
    return option

# Input: Get operation for basic calculator
def get_basic_operation():
    option = ""
    operations = ['+', '-', 'x', '/', '^', 'sqrt', 'min', 'max', 'gcf', 'lcm']
    while option not in operations:
        option = input("Enter operation (+, -, x, /, ^, sqrt, min, max, gcf, lcm): ")
        if option not in operations:
            print("Please enter a valid operation.")
    return option

# Input: Get operands for operation in basic calculator
def get_operands(n):
    numbers = []
    for i in range(n):
        temp = None
        while temp == None:
            try:
                temp = float(input("Enter operand " + str(i+1) + ": "))
                numbers.append(temp)
            except ValueError:
                print("Please enter a numerical value.")
    return numbers

# Process: Calculate GCF
def gcf(a, b):
    gcf = 0
    for i in range(a, 0, -1):
        if a % i == 0 and b % i == 0:
            gcf = i
            break
    return gcf

# Process: Calculate LCM
def lcm(a, b):
    lcm = a
    while lcm % b != 0:
        lcm += a
    return lcm

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

# Process: Calculate factorial of a number, used to calculate coefficient from constant degree
def factorial(n):
    result = n
    for i in range(n-1, 0, -1):
        result *= i
    return result

# Process: Calculate constant difference of function, return constant difference and degree
def finite_differences(yvalues):
    temp = yvalues
    differences = []
    degree = 0
    while temp.count(temp[0]) != len(temp):
        for i in range(1, len(temp)):
            differences.append(temp[i]-temp[i-1])
        temp = differences[:]
        differences = []
        degree += 1
        if len(temp) == 1:
            return None, 0
    return temp[0], degree

# Input: Get data management calculation option
def get_data_option():
    option = ""
    operations = ['mean', 'median', 'mode', 'line-graph', 'bar-graph', 'pi-chart', 'histogram']
    while option not in operations:
        option = input("Enter operation (mean, median, mode, line-graph, bar-graph, pi-chart, histogram): ")
        if option not in operations:
            print("Please enter a valid operation.")
    return option

# Input: Get data set
def get_data():
    d = []
    temp = None
    while temp != 'Done':
        temp = None
        while temp == None:
            temp = input("Enter next data point 'Done' to quit: ")
            if temp == 'Done':
                break
            try:
                temp = float(temp)
                d.append(temp)
            except:
                print("Please enter a numerical value.")
    return d

# Input: Get data and labels to create bar graphs or pi-charts
def get_data_and_labels():
    data = {}
    temp = None
    temp2 = None
    while temp != 'q':
        temp = input("Enter label ('q' to quit): ")
        temp2 = None
        while temp2 == None and temp != 'q':
            try:
                temp2 = float(input("Enter data: "))
                data[temp] = temp2
            except:
                print("Please enter a numerical value.")
    return data

# Process: Calculate mean of data set
def mean(data):
    return sum(data)/len(data)

# Process: Calculate median of data set
def median(data):
    return sorted(data)[len(data)//2+1] if len(data) % 2 != 0 else (sorted(data)[len(data)//2] + sorted(data)[len(data)//2-1]) / 2

# Process: Calculate mode of data set
def mode(data):
    return max(set(data), key=data.count)

# Process: Return values of axes to create histogram
def histogram(data, intervals, minimum, maximum):
    histogram = dict((i, 0) for i in range(minimum-(minimum%intervals), maximum+(intervals-maximum%intervals), intervals))
    for i in data:
        interval = i - i%intervals
        histogram[interval] += 1
    return collections.OrderedDict(sorted(histogram.items()))

# Output: Draw bar graph, given data and labels
def make_bar_graph(x, y, xlabel, ylabel, title):
    tk = Tk()
    canvas = Canvas(tk, width=600, height=600)
    canvas.create_rectangle(100, 100, 500, 400, width=2)
    for i in range(len(x)*2+1):
        canvas.create_line(100+400/(len(x)*2+1)*i, 100, 100+400/(len(x)*2+1)*i, 400, fill="gray")
    for i in range(0, int(max(y)*1.2), int(max(y)*1.2/20) if int(max(y)*1.2/20) > 0 else 1):
        canvas.create_line(100, 400-300/int(max(y)*1.2)*i, 500, 400-300/int(max(y)*1.2)*i, fill="gray")
        canvas.create_text(70, 400-300/int(max(y)*1.2)*i, text=str(i))
    cnt = 0
    for i in range(1, len(x)*2, 2):
        canvas.create_rectangle(100+400/(len(x)*2+1)*i, 400-y[cnt]*300/int(max(y)*1.2), 100+400/(len(x)*2+1)*(i+1), 400, fill=random.choice(COLORS))
        canvas.create_text(100+400/(len(x)*2+1)*(i+0.25), 410+len(x[cnt])*6.5, text=x[cnt], anchor="nw", angle=90)
        cnt += 1
    canvas.create_text(300, 575, text=xlabel, font=("helvetica", 20))
    canvas.create_text(30, 300, text=ylabel, font=("helvetica", 20), anchor="nw", angle=90)
    canvas.create_text(300, 50, text=title, font=("helvetica", 25))
    canvas.pack()
    canvas.mainloop()

# Output: Draw histogram, given data and labels
def make_histogram(histogram, xlabel, ylabel, title):
    tk = Tk()
    canvas = Canvas(tk, width=600, height=600)
    canvas.create_rectangle(100, 100, 500, 400, width=2)
    for i in range(max(histogram.values())+1):
        canvas.create_line(100, 100+300/(max(histogram.values())+1)*i, 500, 100+300/(max(histogram.values())+1)*i, fill="gray")
        canvas.create_text(70, 400-300/(max(histogram.values())+1)*i, text=str(i))
    for i in range(len(histogram)*2+1):
        canvas.create_line(100+400/(len(histogram)*2+1)*i, 100, 100+400/(len(histogram)*2+1)*i, 400, fill="gray")
    cnt = 0
    interval = list(histogram.items())[1][0] - list(histogram.items())[0][0]
    for i in range(1, len(histogram)*2, 2):
        canvas.create_rectangle(100+400/(len(histogram)*2+1)*i, 400-list(histogram.items())[cnt][1]*300/(max(histogram.values())+1), 100+400/(len(histogram)*2+1)*(i+1), 400, fill=random.choice(COLORS))
        label = str(list(histogram.items())[cnt][0]) + "-" + str(list(histogram.items())[cnt][0]+interval)
        canvas.create_text(100+400/(len(histogram)*2+1)*(i+0.25), 410+len(label)*6.5, text=label, anchor="nw", angle=90)
        cnt += 1
    canvas.create_text(300, 500, text=xlabel, font=("helvetica", 20))
    canvas.create_text(30, 300, text=ylabel, font=("helvetica", 20), anchor="nw", angle=90)
    canvas.create_text(300, 50, text=title, font=("helvetica", 25))
    canvas.pack()
    canvas.mainloop()

# Output: Draw pi chart, given data and labels
def make_pi_chart(piChart, title):
    tk = Tk()
    canvas = Canvas(tk, width=600, height=600)
    st = 0
    cnt = 0
    canvas.pack()
    colShuffle = random.sample(COLORS, len(COLORS))
    for i in list(piChart.keys()):
        tempst = st
        canvas.create_arc(50, 70, 550, 570, start=st, extent=piChart[i]*3.6, fill=colShuffle[cnt%12])
        st += piChart[i]*3.6
        cnt += 1
        temptxt = canvas.create_text(300, 320, text=str(i)+" ("+str(round(piChart[i], 2))+"%)", font=("helvetica", 15), anchor="c", angle=(st+tempst)/2)
        xMove = math.sin(math.radians((st+tempst)/2+90))*125
        yMove = math.cos(math.radians((st+tempst)/2+90))*125
        canvas.move(temptxt, xMove, yMove)
        tk.update()
    canvas.create_text(300, 50, text=title, font=("helvetica", 25))
    canvas.mainloop()

# Output: Draw line graph, given data and labels
def make_line_graph(y, timeInterval, start, xlabel, ylabel, title):
    tk = Tk()
    canvas = Canvas(tk, width=600, height=600)
    canvas.create_rectangle(100, 100, 500, 400, width=2)
    for i in range(len(y)+1):
        canvas.create_line(100+400/(len(y)+1)*i, 100, 100+400/(len(y)+1)*i, 400, fill="gray")
    for i in range(0, int(max(y)*1.2), int(max(y)*1.2/20) if int(max(y)*1.2/20) > 0 else 1):
        canvas.create_line(100, 400-300/int(max(y)*1.2)*i, 500, 400-300/int(max(y)*1.2)*i, fill="gray")
        canvas.create_text(70, 400-300/int(max(y)*1.2)*i, text=str(i))
    cnt = 0
    for i in range(1, len(y)):
        canvas.create_line(100+400/(len(y)+1)*i, 400-y[cnt]*300/int(max(y)*1.2), 100+400/(len(y)+1)*(i+1), 400-y[cnt+1]*300/int(max(y)*1.2), width=2)
        canvas.create_text(100+400/(len(y)+1)*(i-0.1), 410+len(str(timeInterval*cnt+start))*6.5, text=str(timeInterval*cnt+start), anchor="nw", angle=90)
        cnt += 1
    canvas.create_text(100+400/(len(y)+1)*(len(y)-0.1), 410+len(str(timeInterval*cnt+start))*6.5, text=str(timeInterval*cnt+start), anchor="nw", angle=90)
    canvas.create_text(300, 575, text=xlabel, font=("helvetica", 20))
    canvas.create_text(30, 300, text=ylabel, font=("helvetica", 20), anchor="nw", angle=90)
    canvas.create_text(300, 50, text=title, font=("helvetica", 25))
    canvas.pack()
    canvas.mainloop()

# Input: Get quadratic equation conversion option
def get_quadratic_option():
    option = ""
    operations = ['standard-vertex', 'vertex-standard', 'standard-factored']
    while option not in operations:
        option = input("Enter conversion type (standard-vertex, vertex-standard, standard-factored): ")
        if option not in operations:
            print("Please enter a valid conversion type.")
    return option

# Input: Get standard form coefficients
def get_standard():
    coefficients = []
    variables = ["a", "b", "c"]
    for i in range(3):
        temp = None
        while temp == None:
            try:
                temp = float(input("Enter " + str(variables[i]) + ": "))
                coefficients.append(temp)
            except:
                print("Please enter a numerical value.")
    return coefficients[0], coefficients[1], coefficients[2]

# Input: Get vertex form variables
def get_vertex():
    coefficients = []
    variables = ["a", "h", "k"]
    for i in range(3):
        temp = None
        while temp == None:
            try:
                temp = float(input("Enter " + str(variables[i]) + ": "))
                coefficients.append(temp)
            except:
                print("Please enter a numerical value.")
    return coefficients[0], coefficients[1], coefficients[2]

# Process: Return string of factored form equation given coefficients of standard form equation
def standard_to_factored(a, b, c):
    discriminant = b**2 - 4*a*c
    print(discriminant)
    x = None
    if discriminant < 0:
        x = "No real roots"
    elif discriminant == 0:
        x = "x(x - " + str(round(-b / (2*a), 2)) + ")"
    else:
        print((-b - math.sqrt(discriminant)) / (2*a))
        print((-b + math.sqrt(discriminant)) / (2*a))
        x = "(x - " + str(round((-b - math.sqrt(discriminant)) / (2*a), 2)) + ")(x - " + str(round((-b + math.sqrt(discriminant)) / (2*a), 2)) + ")"
    return x

# Process: Return string of standard form equation given coefficients of vertex form equation
def vertex_to_standard(a, h, k):
    aStandard = a
    bStandard = -h*2*a
    cStandard = k+a*h**2
    return str(aStandard) + "x^2 + " + str(bStandard) + "x + " + str(cStandard)

# Process: Return string of vertex form equation given coefficients of standard form equation
def standard_to_vertex(a, b, c):
    aVertex = a
    hVertex = -b/(2*a)
    kVertex = a*hVertex**2 + b*hVertex + c
    return str(aVertex) + "(x - " + str(hVertex) + ")^2 + " + str(kVertex)

# Basic calculator
def basic_calc():
    print("---------------- BASIC CALCULATOR ----------------")
    # Input: Get operation choice
    operation = get_basic_operation()
    # Process/output: Perform operation and print result
    if operation == '+':
        operands = get_operands(2)
        answer = operands[0] + operands[1]
        print(operands[0], "+", operands[1], "=", answer)
    elif operation == '-':
        operands = get_operands(2)
        answer = operands[0] - operands[1]
        print(operands[0], "-", operands[1], "=", answer)
    elif operation == "x":
        operands = get_operands(2)
        answer = operands[0] * operands[1]
        print(operands[0], "x", operands[1], "=", answer)
    elif operation == "/":
        answer = None
        operands = []
        while answer == None:
            operands = get_operands(2)
            try:
                answer = operands[0] / operands[1]
            except:
                print("Cannot divide by 0.")
        print(operands[0], "/", operands[1], "=", answer)
    elif operation == "^":
        operands = get_operands(2)
        answer = operands[0] ** operands[1]
        print(operands[0], "^", operands[1], "=", answer)
    elif operation == "sqrt":
        answer = None
        while answer == None:
            operands = get_operands(1)
            try:
                answer = math.sqrt(operands[0])
            except:
                print("Cannot square root negative number.")
        print("sqrt(" + str(operands[0]) + ") =", answer)
    elif operation == "min":
        operands = get_operands(2)
        answer = min(operands[0], operands[0])
        print("Minimum:", answer)
    elif operation == "max":
        operands = get_operands(2)
        answer = max(operands[0], operands[0])
        print("Maximum:", answer)
    elif operation == "gcf":
        operands = get_operands(2)
        answer = gcf(int(operands[0]), int(operands[1]))
        print("GCF(" + str(int(operands[0])) + ", " + str(int(operands[1])) + ") =", answer)
    elif operation == "lcm":
        operands = get_operands(2)
        answer = lcm(int(operands[0]), int(operands[1]))
        print("LCM(" + str(int(operands[0])) + ", " + str(int(operands[1])) + ") =", answer)

# Graph identifier
def graph_identify():
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

# Data analyser
def data_analyser():
    print("---------------- DATA ANALYSER ----------------")
    # Input: Get operation choice
    o = get_data_option()
    if o == "mean":
        # Input: Get data
        print("Enter data:")
        d = get_data()
	# Process: Calculate mean
        m = mean(d)
	# Output: Print result
        print("Mean:", m)
    elif o == "median":
        # Input: Get data
        print("Enter data:")
        d = get_data()
	# Process: Calculate mean
        m = median(d)
	# Output: Print result
        print("Median:", m)
    elif o == "mode":
        # Input: Get data
        print("Enter data:")
        d = get_data()
	# Process: Calculate mean
        m = mode(d)
	# Output: Print result
        print("Mode:", m)
    elif o == "line-graph":
        # Input: Get data and graph information
        print("Enter data:")
        d = get_data()
        s = None
        while s == None:
            try:
                s = int(input("Enter starting time (as a number): "))
            except:
                print("Please enter an integer.")
        i = None
        while i == None:
            try:
                i = int(input("Enter time interval (as a number): "))
                if i <= 0:
                    print("Please enter a positive interval.")
                    i = None
            except:
                print("Please enter an integer.")
        t = input("Enter title: ")
        xaxislabel = input("Enter x-axis label: ")
        yaxislabel = input("Enter y-axis label: ")
        # Process/output: Create line graph
        make_line_graph(d, i, s, xaxislabel, yaxislabel, t)
    elif o == "bar-graph":
        # Input: Get data and graph information
        print("Enter data:")
        labeledData = get_data_and_labels()
        d = list(labeledData.values())
        l = list(labeledData.keys())
        t = input("Enter title: ")
        xaxislabel = input("Enter x-axis label: ")
        yaxislabel = input("Enter y-axis label: ")
        # Process/output: Create bar graph
        make_bar_graph(l, d, xaxislabel, yaxislabel, t)
    elif o == "pi-chart":
        # Input: Get data and graph information
        print("Enter data:")
        labeledData = None
        while labeledData == None:
            labeledData = get_data_and_labels()
            if sum(1 for i in list(labeledData.values()) if i < 0) > 0:
                print("Please enter positive values only.")
                labeledData = None
        labeledData = {list(labeledData.keys())[i] : labeledData[list(labeledData.keys())[i]]/sum(list(labeledData.values()))*100 for i in range(len(labeledData))}
        t = input("Enter title: ")
        # Process/output: Create pi chart
        make_pi_chart(labeledData, t)
    elif o == "histogram":
        # Input: Get data and graph information
        print("Enter data:")
        d = get_data()
        i = None
        while i == None:
            try:
                i = int(input("Enter interval length: "))
            except:
                print("Please enter an integer.")
        maxData = None
        while maxData == None:
            try:
                maxData = int(input("Enter maximum value to graph: "))
            except:
                print("Please enter an integer.")
        minData = None
        while minData == None or minData > maxData:
            try:
                minData = int(input("Enter minimum value to graph: "))
                if minData > maxData:
                    print("Minimum must be less than maximum.")
            except:
                print("Please enter an integer.")
        t = input("Enter title: ")
        xaxislabel = input("Enter x-axis label: ")
        yaxislabel = input("Enter y-axis label: ")
        # Process: Store axes for histogram
        h = histogram(d, i, minData, maxData)
        # Output: Create histogram
        make_histogram(h, xaxislabel, yaxislabel, t)

# Quadratic calculator
def quadratic_calc():
    print("---------------- QUADRATIC CALCULATOR ----------------")
    # Input: Get conversion choice
    o = get_quadratic_option()
    # Process: Perform form conversion
    if o == "standard-vertex":
        a, b, c = get_standard()
        equation = standard_to_vertex(a, b, c)
        print("Vertex form:", equation)
    elif o == "vertex-standard":
        a, h, k = get_vertex()
        equation = vertex_to_standard(a, h, k)
        print("Standard form:", equation)
    else:
        a, b, c = get_standard()
        equation = standard_to_factored(a, b, c)
        print("Factored form:", equation)

# Main program

# Run until user chooses to quit
while True:
    # Input: Get calculator mode choice
    calcOption = get_option()
    # Process: Run calculator of choice
    if calcOption == 'b':
        basic_calc()
    elif calcOption == 'g':
        graph_identify()
    elif calcOption == 'd':
        data_analyser()
    elif calcOption == 'q':
        quadratic_calc()
    else:
        # Process: Quit if user chooses to quit
        break
