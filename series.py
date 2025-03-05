import pandas as pd


def solve(data, index):
    my_series = pd.Series(data, index=index, name="my_series")
    my_series.index.name = "my_index"
    return my_series.head(10)

def solve1(series, new_indexes):
    return series.reindex(new_indexes, fill_value="Unknown")

def solve2(series):
    return f"{series.max() - series.min()}/{series.value_counts().index.values[0]}/{series.abs().sum()}"

print(solve2(pd.Series([1,1,1, 2,10])))