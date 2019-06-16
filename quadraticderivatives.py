#calculating the slope at any point in a quadratic function

print("The form of a quadratic function isy = ax^2 + bx + c")
a_value = input("Enter the 'a' value: ")
a_value = int(a_value)

b_value = input("Enter the 'b' value: ")
b_value = int(b_value)

c_value = input("Enter the 'c' value: ")
c_value = int(c_value)

a_derivative = a_value * 2
b_derivative = b_value * 1

print(f'The equation for the slop is {a_derivative}x + {b_derivative}')
x_value = input("For which x value do you want to find the slope?: ")
x_value = float(x_value)

slopei = (a_derivative * x_value)
slope = slopei + b_derivative

print(f'The slope when x is {x_value} is {slope}')
input('Press ENTER to exit')
