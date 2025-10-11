import pandas as pd
import os
numbers = []

for i in range(0,20,1):
    numbers.append(i)

numbers_df = pd.DataFrame(numbers)
os.mkdir("artifacts")
print("yay nums")
numbers_df.to_excel("artifacts/numarr.xlsx")