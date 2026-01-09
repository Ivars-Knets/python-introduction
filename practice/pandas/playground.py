import pandas as pd

# Series
groceries = pd.Series(data=[30, 6, "y", "n"], index=["egg", "apple", "milk", "bread"])
new_groceries = groceries.drop('apple')
# print(groceries)
# print(new_groceries)
groceries.drop('milk', inplace=True)
# print(groceries)



# DataFrame
items = {
    'Coleen': pd.Series([2,4,6,8], index=['a','c','d','e']),
    'Colton': pd.Series([1,3,7], index=['b','c','f']),
}
frame = pd.DataFrame(items)
print(frame)

frameRow = frame[]