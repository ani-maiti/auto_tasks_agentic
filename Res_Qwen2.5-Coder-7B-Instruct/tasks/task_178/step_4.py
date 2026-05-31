import pandas as pd

data = {
    'Directory': [line.split()[1] for line in open('output.txt')],
    'Size': [int(line.split()[0].replace('M', '')) for line in open('output.txt')]
}

df = pd.DataFrame(data)
df_sorted = df.sort_values(by='Size', ascending=False)

print(df_sorted.to_string(index=False))