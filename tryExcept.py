print(":::: try and except In Python ::::")


try:
    num = int(input("Enter a Number: "))
    print(num % 2)
# except:
#     print(" Somthing was Wrong \n please input a valid number !")
except Exception as e:
    print(" Somthing was Wrong \n please input a valid number !! \n", e)