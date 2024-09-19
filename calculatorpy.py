print("1-add")
print("2-subtract")
print("3-multiply")
print("4-divide")
option=int(input("choose an operation"))
if(option in [1,2,3,4]):
    num1=int(input("enter first number:"))
    num2=int(input("enter scond number:"))
    if(option==1):
        result= num1 + num2
        print("the result of the operation is", result)
    elif(option==2):
        result = num1 - num2
        print("the result of the operation is", result)
    elif(option==3):
        result = num1 * num2
        print("the result of the operation is", result)
    elif(option==4):
        result = num1 // num2
        print("the result of the operation is", result)
    else:
        print("invalid operation entered:")
        1


