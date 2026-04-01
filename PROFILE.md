# How to Merge Two DataFrames in Pandas

In pandas, you can merge two DataFrames using the `merge()` function.

## Basic Merge

```python
import pandas as pd

df1 = pd.DataFrame({'key': ['A', 'B', 'C'], 'value1': [1, 2, 3]})
df2 = pd.DataFrame({'key': ['B', 'C', 'D'], 'value2': [4, 5, 6]})

# Inner merge (default) - only keeps rows with matching keys in both DataFrames
result = pd.merge(df1, df2, on='key')
```

## Types of Merges

| `how` parameter | Description |
|---|---|
| `'inner'` | Returns only rows with matching keys in both DataFrames (default) |
| `'left'`  | Returns all rows from the left DataFrame, with NaN for non-matches |
| `'right'` | Returns all rows from the right DataFrame, with NaN for non-matches |
| `'outer'` | Returns all rows from both DataFrames, with NaN for non-matches |

## Examples

```python
# Left merge
result = pd.merge(df1, df2, on='key', how='left')

# Right merge
result = pd.merge(df1, df2, on='key', how='right')

# Outer merge
result = pd.merge(df1, df2, on='key', how='outer')

# Merging on multiple columns
result = pd.merge(df1, df2, on=['key1', 'key2'])

# Merging on columns with different names
result = pd.merge(df1, df2, left_on='id', right_on='user_id')
```

## Using `join()` Method

Alternatively, you can use the `join()` method which merges on index by default:

```python
result = df1.join(df2, how='inner')
```

## Using `concat()` for Stacking DataFrames

To stack DataFrames vertically or horizontally:

```python
# Stack rows (vertically)
result = pd.concat([df1, df2], ignore_index=True)

# Stack columns (horizontally)
result = pd.concat([df1, df2], axis=1)
```
