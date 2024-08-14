import pandas as pd

def find(arr, element):
    for i in range(len(arr)):
        if element == arr.iloc[i, 2]:
            return i+2

df_read = pd.read_excel("doctors_DoctorNext.xlsx")

print(len(df_read))
seen = []
for i in range(len(df_read)):

    if df_read.iloc[i, 2] not in seen:
        seen.append(df_read.iloc[i, 2])
    else:
        loc = find(df_read, df_read.iloc[i, 2])
        print('duplicate: ', i+2, loc, df_read.iloc[i, 2])


