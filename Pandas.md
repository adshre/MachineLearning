# Pandas
Pandas is an open source, BSD-licensed(Berkeley Software Distribution)
library providing high-performance, easy-to-use data structures and data analysis tools for the Python programming language.

# Data Structure
Here is a basic tenet to keep in mind: data alignment is intrinsic. The link between labels and data will not be broken unless done so explicitly by you.

## Series
Series is a one-dimensional labeled array capable of holding any data type (integers, strings, floating point numbers, Python objects, etc.). The axis labels are collectively referred to as the index.

S = pd.Series(data, index=index) \
* data can be python dict, ndarray, scalar values
* index is list of axis label

*Note : pandas supports non-unique index values. If an operation that does not support duplicate index values is attempted, an exception will be raised at that time.*

**Series is like ndarray-like**
* Series acts very similarly to a ndarray, and is a valid argument to most NumPy functions. However, operations such as slicing will also slice the index.
* Like a NumPy array, a pandas Series has a dtype.
* Series.array will always be an ExtensionArray. Briefly, an ExtensionArray is a thin wrapper around one or more concrete arrays like a numpy.ndarray.
Pandas knows how to take an ExtensionArray and store it in a Series or a column of a DataFrame.

**Series is like dict-like**
* A Series is like a fixed-size dict in that you can get and set values by index label
* If a label is not contained, an exception is raised:

**Series name attribute**
Series can also have a name attribute and you can aslo rename it

**Vectorized operations and label alignment with Series**
* When working with raw NumPy arrays, looping through value-by-value is usually not necessary.
* A key difference between Series and ndarray is that operations between Series automatically align the data based on label. 
Thus, you can write computations without giving consideration to whether the Series involved have the same labels.

## DataFrame
DataFrame is a 2-dimensional labeled data structure with columns of potentially different types. You can think of it like a spreadsheet or SQL table, or a dict of Series objects. It is generally the most commonly used pandas object. Like Series, DataFrame accepts many different kinds of input:
* Dict of 1D ndarrays, lists, dicts, or Series
* 2-D numpy.ndarray
* Structured or record ndarray
* A Series
* Another DataFrame

Along with the data, you can optionally pass index (row labels) and columns (column labels) arguments. \
If axis labels are not passed, they will be constructed from the input data based on common sense rules.\


* You can treat a DataFrame semantically like a dict of like-indexed Series objects.
* DataFrame has an assign() method that allows you to easily create new columns that are potentially derived from existing columns.

* Indexing/ Slicing :

| Operation   |      Syntax      |  Result |
|------------:|------------------|-------- |
| Select column| df[col].        | Series |
| Select row by label | df.loc[label] | Series |
| Select row by integer location | df.iloc[loc] | Series |
| Slice row | df[5:10] |DataFrame |
| Select row by boolean vector | df[boo_vec] | DataFrame|

* Data alignment between DataFrame objects automatically align on both the columns and the index (row labels). Again, the resulting object will have the union of the column and row labels.
