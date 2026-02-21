import pandas as pd

#Creating a manual DataFrame from a dictionary

students = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David'],
    'Marks': [24, 22, 23, 21],
    'Grade': ['A', 'B', 'B', 'C']
}
df = pd.DataFrame(students)

# print(df)

# print("\nData types of each column:")
# print(df.dtypes)    

# print("\nShape of the DataFrame:")
# print(df.shape)

# print("\nFirst two rows of the DataFrame:")
# print(df.head(2))

# print("\nLast two rows of the DataFrame:")
# print(df.tail(2))

# print("\nStatistical summary of the DataFrame:")
# print(df.describe())

# print("\nInformation about the DataFrame:")
# print(df.info())   

# print("\nColumn names in the DataFrame:")
# print(df.columns)

# print("\nIndex of the DataFrame:")
# print(df.index)

# print("\nValues in the DataFrame:")
# print(df.values) 

# print("\nTransposed DataFrame:")
# print(df.T)   
 
print("\n adding a new column 'Passed' to the DataFrame:")
df['Passed'] = [True, True, True, False]
print(df)

# print("\nSorting the DataFrame by 'Marks' in descending order:")
# print(df.sort_values(by='Marks', ascending=False))

# print("\nFiltering the DataFrame for students with Marks greater than 22:")
# print(df[df['Marks'] > 22]) 

# print("\nGrouping the DataFrame by 'Grade' and calculating the mean Marks:")
# print(df.groupby('Grade')['Marks'].mean())

# print("\nIterating over the DataFrame rows:")
# for index, row in df.iterrows():
#     print(f"Index: {index}, Name: {row['Name']}, Marks: {row['Marks']}, Grade: {row['Grade']}")

# print("\nApplying a function to increase Marks by 2:")
# df['Marks'] = df['Marks'].apply(lambda x: x + 2)
# print(df)   

# print("\nHandling missing data by filling NaN values with 0:")
# df_with_nan = df.copy()
# df_with_nan.loc[1, 'Marks'] = None
# print(df_with_nan.fillna(0))

# print("\nMerging two DataFrames:")
# df2 = pd.DataFrame({
#     'Name': ['Eve', 'Frank'],
#     'Marks': [20, 19],
#     'Grade': ['C', 'D']
# })
# merged_df = pd.concat([df, df2], ignore_index=True)
# print(merged_df)

# print ("\nPivoting the DataFrame:")
# pivot_df = df.pivot_table(values='Marks', index='Grade', aggfunc='mean')
# print(pivot_df) 

# print("\nCreating a copy of the DataFrame:")
# df_copy = df.copy()
# print(df_copy)  

print("\nDropping the 'Passed' column from the DataFrame:")
df_dropped = df.drop(columns=['Passed'])
print(df_dropped)

print("\nRenaming the 'Marks' column to 'Scores':")
df_renamed = df.rename(columns={'Marks': 'Scores'})
print(df_renamed)   

print("\nResetting the index of the DataFrame:")
df_reset = df.reset_index(drop=True)
print(df_reset)

print("/n Setting "Name" as the index of the DataFrame:")
df_set_index = df.set_index('Name')
print(df_set_index) 

print("/n Removing duplicate rows from the DataFrame:")
df_duplicates = pd.DataFrame({
    'Name': ['Alice', 'Bob', 'Alice', 'David'],
    'Marks': [24, 22, 24, 21],
    'Grade': ['A', 'B', 'A', 'C']
})
df_no_duplicates = df_duplicates.drop_duplicates()
print(df_no_duplicates)  



##Exporting the DataFrame to a CSV file
# df.to_csv("students_data.csv", index=False)

##Exporting the DataFrame to a JSON file
# df.to_json("students_data.json", orient="records")
    
