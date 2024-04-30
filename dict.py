print(":::: Example of dict data type ::::")
marks2024 = {
    "idilpur": [85, 37, 37, 32, 95, 73, 95, 43, 67],
    "kodalpur": [35, 35, 48, 78, 28, 50, 38, 53]
}

marks2024["Haturia"] = [83, 83, 24]
# print(marks2024)
print(marks2024.get("haturia"))  # best practice for error handling
print(marks2024.items())
print(marks2024.values())
print(marks2024.keys())
