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
