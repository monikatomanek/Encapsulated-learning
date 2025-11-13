# Python Patterns for Data Analysis

This guide is part of the `Encapsulated-learning` repository by [Monika Tomanek](https://github.com/monikatomanek).
It includes clean, beginner-friendly Python patterns commonly used in real-world data analysis workflows using pandas.

Each pattern includes:

* ✅ When to use it
* ✍️ What to replace
* 🧠 A mental sentence (to help remember what it *does*, not just what it *says*)

---

## 1. Load a Dataset

```python
df = pd.read_csv('filename.csv')
```

**Use when:** You want to read a CSV file and start analysing it.
**Replace:** 'filename.csv' → your actual file name
**Mental sentence:** 'Bring my spreadsheet into Python and call it df'.

---

## 2. Count Values in a Column (Frequency)

```python
df['ColumnName'].value_counts()
```

**Use when:** You want to know how many times each value appears.
**Replace:** 'ColumnName' → your actual column name
**Mental sentence:** 'How often does each unique value appear in this column?'.

---

## 3. Count Values as Percentages

```python
df['ColumnName'].value_counts(normalize=True) * 100
```

**Use when:** You want to see percentages instead of raw counts.
**Mental sentence:** 'What percent of the total is each value in this column?'.

---

## 4. Filter the Dataset by Condition

```python
filtered_df = df[df['ColumnName'] == 'SomeValue']
```

**Use when:** You only want rows that match a certain value.
**Mental sentence:** 'Give me only the rows where this column has this value'.

---

## 5. Get Top Value from a Count

```python
top_result = df['ColumnName'].value_counts().head(1)
top_name = top_result.index[0]
top_value = top_result.values[0]
```

**Use when:** You want the most common category and how often it appears.
**Mental sentence:** 'What's the most frequent value in this column?'.

---

## ✧ BONUS: Print the Result with Formatting

```python
print(f"\n[message here] {variable_name:.2f}%")
```

**Use when:** You want a clean, readable output using variables.
**Mental sentence:** 'Say this sentence and plug in my number using 2 decimal places'.

---

## ✦ Example Application: Percentage of Women

```python
percentage_women = df['Gender'].value_counts(normalize=True)['Female'] * 100
print(f"\nPercentage of women: {percentage_women:.2f}%")
```

---

## 6. Filter by Boolean Column

```python
df[df['ColumnName'] == True]  # or False
```

**Use when:** You want only rows where a Boolean column is True or False.
**Mental sentence:** 'Give me the rows where this is True or False'.

---

## 7. If / Elif / Else Logic

```python
if condition:
    # do this
elif another_condition:
    # do that
else:
    # do something else
```

**Use when:** You want to make decisions based on logic.
**Mental sentence:** 'If this is true, do one thing. Otherwise, check something else'.

---

## 8. Loop Through a List or Column

```python
for item in list:
    print(item)
```

**Use when:** You want to repeat something for each item.
**Mental sentence:** 'For each thing in this group, do something to it'.

---

## 9. Create a New Column Using Logic

```python
def custom_function(row):
    if row['Column'] == 'something':
        return 'A'
    else:
        return 'B'

df['NewColumn'] = df.apply(custom_function, axis=1)
```

**Use when:** You want a new column based on custom logic per row.
**Mental sentence:** 'Look at each row, decide something, and store the result'.

---

## 10. Calculate Stats by Group (GroupBy)

```python
df.groupby('Column')['AnotherColumn'].mean()
```

**Use when:** You want averages/sums by category.
**Example:** Average monthly spend by region.
**Mental sentence:** 'Group by this column, then calculate a stat'.

---

## Summary Table

| Purpose               | Code Template                                | Notes                         |
| --------------------- | -------------------------------------------- | ----------------------------- |
| Load CSV              | `pd.read_csv('file.csv')`                    | First step                    |
| Count values          | `df['Col'].value_counts()`                   | Shows raw counts              |
| Count as %            | `df['Col'].value_counts(normalize=True)*100` | Shows percentages             |
| Filter data           | `df[df['Col'] == 'Value']`                   | Returns a smaller dataset     |
| Top value from column | `.value_counts().head(1)` with `.index[0]`   | Get name + count              |
| Print nicely          | `print(f"... {var:.2f}%")`                   | Format variables into strings |
| Filter True/False     | `df[df['Col'] == True]`                      | Boolean filtering             |
| Conditional logic     | `if / elif / else:`                          | Control flow                  |
| Loop through items    | `for item in list:`                          | Repeat for each value         |
| Apply logic per row   | `df.apply(function, axis=1)`                 | Custom calculations           |
| Group stats           | `df.groupby('Col')['OtherCol'].mean()`       | Averages/sums by group        |

---

> Authored and maintained by Monika Tomanek
