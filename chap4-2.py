import pandas as pd

'''
    Source: https://www.post.japanpost.jp/zipcode/dl/kogaki-zip.html
'''

df = pd.read_csv("13TOKYO.CSV", header=None, encoding="shift_jis")

results = df[df[2] == 1600006]
print(results[[2, 6, 7, 8]])

results = df[df[8].str.contains("四谷")]
print(results[[2, 6, 7, 8]])
