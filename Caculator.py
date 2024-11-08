num1=float(input("Enter the first number :" ))
while True:
    num2=float(input("Enter the second number : "))
    operation=str(input("Select any operation you want to done + , - , * , / , % : "  ))
    if operation == '+':
        result=num1+num2
        print(f"The sum of {num1} and {num2} is ",result)
    elif operation=='-':
        result=num1-num2
        print(f"The subtraction of {num1} and {num2} is ",result)
    elif operation =='*':
        result=num1*num2
        print(f"The sum of {num1} and {num2} is ",result)
    elif operation=='/':
        result=num1/num2
        if num2==0:
            print("A number cannot divided by zero")
        else:    
            print(f"The sum of {num1} and {num2} is ",result)
    elif operation=='%':
        result=num1%num2
        print(f"The sum of {num1} and {num2} is ",result)
    else:
        print("Invalid Operator!")     
    print("Select the option \n 1 --> continue \n 0 --> Exit ")
    i=int(input("Enter the option : "))
    if i==1:
        num1=result
    elif i==0:
        break    

           


    
    