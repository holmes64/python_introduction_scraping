import pandas as pd

'''
    Source: https://www.e-stat.go.jp/
'''

df = pd.read_csv("FEH_00200524_200816200444.csv", index_col="全国・都道府県", encoding="shift_jis")
print(len(df))
print(df.columns.values)
