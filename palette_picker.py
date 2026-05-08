#%%
import pandas as pd
import random

palettes_import = pd.read_csv('C:\\Users\\BmWoo\\Documents\\GitHub\\Learning\\Palette_list.csv',header=None)

palettes = palettes_import[0].to_list()

#%%

palette_choice = random.choice(palettes)
print("Palette of the day is: ",palette_choice)
# %%
