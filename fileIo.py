print(":::: File In Python ::::")

# text = " there are many river in bangladesh !"
#
# with open("test.txt", "w") as f:  # 3 mode read write append
#     f.write(text)


with open("test.txt", "r") as f:
   result = f.read()
   print(result)



with open("test.txt", "a") as f:
   f.write("yes , you can do this.")