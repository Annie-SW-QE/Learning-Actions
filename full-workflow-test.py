## Test the full workflow, including using secrets and writing artifacts to a folder
import os
import pandas as pd
# where = os.environ.get('my_var')
where = "theres"

my_array = []
for i in range(0,20,1):
    my_array.append(where)
os.makedirs("artifacts")
my_df = pd.DataFrame(my_array)

my_df.to_excel("artifacts/my_excel.xlsx")
print("Done!!")