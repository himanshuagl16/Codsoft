num1 = float(input("Enter the First number: "))
num2 = float(input("Enter the Second number: "))
operator = input("Select an operation (+, -, *, /, ^) ->> ")

if operator == "+" :
    print(num1, "+", num2, "=", num1 + num2)

elif operator == "-":
    print(num1, "-", num2, "=", num1 - num2)

elif operator == "*":
    print(num1, "*", num2, "=", num1 * num2)

elif operator == "/":
    if num2 == 0.0 :
        print("Cannot divide by 0")
    else:
        print(num1, "/", num2, "=", num1 / num2)

elif operator == "^":
    print(num1, "^", num2, "=", num1 ** num2)
 
else:
    print("Invalid operation.")        

