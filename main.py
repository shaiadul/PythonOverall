import pandas as pd

# Create sample data
data = {
        'Name': ['Shaiadul', 'Bashar', 'Bappy'],
        'Age': [25, 30, 35],
        'City': ['Dhaka', 'Khulna', 'Shylet'],
        'occupation': ['Web Developer', 'Python', 'Flutter']
        }

# Create a DataFrame
makeDF = pd.DataFrame(data)

# Export DataFrame to Excel
makeDF.to_excel('data.xlsx', index=False)

# show data on console
df = pd.read_excel("data.xlsx")

print("::::: Your Data Successfully Visualized :::::")
print(df)