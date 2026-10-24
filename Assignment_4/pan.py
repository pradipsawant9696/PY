

# Question 1: Write a program to demonstrate DataFrames in Pandas.

import pandas as pd
data = {
 "Name": ["Amit", "Priya", "Rahul"],
 "Age": [21, 22, 20],
 "Marks": [85, 90, 78]
}
df = pd.DataFrame(data)
print("Student DataFrame:")
print(df)



# Question 2: Write a program to demonstrate reading a CSV file in Pandas.

import pandas as pd

# Create a sample CSV file
data = {
 "Name": ["Amit", "Priya", "Rahul"],
 "Marks": [85, 90, 78]
}
df = pd.DataFrame(data)
df.to_csv("students.csv", index=False)
# Read the CSV file
data_frame = pd.read_csv("students.csv")
print("Data read from CSV file:")
print(data_frame)



# Question 3: Write a program to demonstrate reading a JSON file in Pandas.

import pandas as pd
# Create a sample JSON file
data = [
 {"Name": "Amit", "Age": 21},
 {"Name": "Priya", "Age": 22},
 {"Name": "Rahul", "Age": 20}
]
pd.DataFrame(data).to_json("students.json", orient="records", indent=4)
# Read the JSON file
df = pd.read_json("students.json")
print("Data read from JSON file:")
print(df)



# Question 4: Write a program to demonstrate removing duplicates in Pandas.

import pandas as pd
data = {
 "Name": ["Amit", "Priya", "Amit", "Rahul", "Priya"],
 "Marks": [85, 90, 85, 78, 90]
}
df = pd.DataFrame(data)
print("Original DataFrame:")
print(df)
# Remove rows that are exact duplicates
clean_df = df.drop_duplicates()
print("\nDataFrame after removing duplicates:")
print(clean_df)


