# ---
# jupyter:
#   jupytext:
#     formats: py:hydrogen
#     text_representation:
#       extension: .py
#       format_name: hydrogen
#       format_version: '1.3'
#       jupytext_version: 1.5.0
#   kernelspec:
#     display_name: Python 3
#     language: python
#     name: python3
# ---

# %% [raw] slideshow={"slide_type": "skip"}
# # Intended to be presented as a RISE slide deck
# # NOTE: As of August 2020, RISE still is not compatible with JupyterLab,
# # so make sure you have the RISE extension installed and run with: jupyter notebook

# %% [markdown] slideshow={"slide_type": "slide"}
# # Accessing Datasets in Python
#
# ### Different Tools for Different Use Cases

# %% [markdown] slideshow={"slide_type": "slide"}
# ##### Learning Objectives for this unit:
#
# * Perform basic file I/O operations: `open`, `csv` package, `json` package
#
# * Perform basic file I/O operations using NumPy
#
# * Work with datasets from `statsmodels` and `scikit-learn` 
#
#

# %% [markdown] slideshow={"slide_type": "slide"}
# ### Core Python File I/O: `open()`

# %% [markdown] slideshow={"slide_type": "fragment"}
# `open('path/to/file/', mode='r')` instantiates an object that is connected to a file, in read mode (which is the default).

# %% slideshow={"slide_type": "fragment"}
file_obj = open('../data/lorem-ipsum.txt', mode = 'r')

# %% [markdown] slideshow={"slide_type": "slide"}
# ### Commonly used methods:
#
# * `.read()` / `.readlines()` 
# * `.write()` / `.writelines()`
# * `.close()`

# %% slideshow={"slide_type": "fragment"}
content_string = file_obj.read()
list_of_content_strings = file_obj.readlines()

# %% slideshow={"slide_type": "fragment"}
content_string[:200]

# %% slideshow={"slide_type": "subslide"}
file_obj.write('some str to be written to disk')
file_obj.writelines(['some', 'strs', 'in', 'list'])

# %% [markdown] slideshow={"slide_type": "slide"}
# ### Things to watch out for:
#
# * Specifying the `mode` 
#     - Common modes: read: `'r'`, write: `'w'`, text file type: `'t'`, binary file type: `'b'`
#     - `mode = 'rt'` is the default
#         * `file_obj.write()` errored as a way to protect us from accidentally corrupting a file.
#  

# %% [markdown] slideshow={"slide_type": "slide"}
# ### Things to watch out for:
# * Reading a file iterates through it, so scanning through contents a second time requires opening a new connection.
#

# %% slideshow={"slide_type": "fragment"}
print(list_of_content_strings)

# %% [markdown] slideshow={"slide_type": "fragment"}
# (all of the contents in our file were read into `content_string` above, leaving nothing for `list_of_content_strings`)

# %% [markdown] slideshow={"slide_type": "slide"}
# ### Things to watch out for:
# * You need to **close your connection** to a file when you are done interacting with it.
#     - `.close()` method works. (But you have to remember to do it!)
#     - More common, use a `with` block:

# %% slideshow={"slide_type": "fragment"}
with open('../data/lorem-ipsum.txt', mode = 'r') as new_file_obj:
    new_list_of_content_strings = new_file_obj.readlines()

# %% slideshow={"slide_type": "fragment"}
print('file_obj is closed:', file_obj.closed)
print('new_file_obj is closed:', new_file_obj.closed)

# %% slideshow={"slide_type": "subslide"}
# so let's close that first one now:
file_obj.close()

# %% [markdown] slideshow={"slide_type": "slide"}
# #### `open()` advice:
# * Make sure you are clear on which `mode` you need.
# * Reading/Writing should usually take place inside a `with` block.
# * `.readlines()` / `.writelines()` convenient when working with rows of data.

# %% [markdown] slideshow={"slide_type": "slide"}
# ### Reading/Writing Specific File Types
# * Many file I/O packages are part of the Python Standard Library. We'll focus on:
#  - csv, (Comma Separated Values)
#  - json, (JavaScript Object Notation)
# * Also see Pandas: `pd.read_csv` / `dataframe.to_csv` and `pd.read_json` / `dataframe.to_json`

# %% [markdown] slideshow={"slide_type": "slide"}
# #### CSV library usage: reading

# %% slideshow={"slide_type": "fragment"}
import csv
with open('../data/some_tabular_data.csv', newline='') as csvfile:
    csvdata_reader = csv.reader(csvfile, delimiter=',')
    rows = [row for row in csvdata_reader]

# %% [markdown] slideshow={"slide_type": "fragment"}
# * Note the `delimiter` keyword. Default is a comma, but CSV library also works with other special characters separating values in a row.
# * The [docs](https://docs.python.org/3/library/csv.html?highlight=csv#csv.reader) state: 'If csvfile is a file object, it should be opened with `newline=''`' (to better deal with any quoted values containing multiple lines)
# * [See also](https://docs.python.org/3/library/csv.html) `csv.DictReader`

# %% slideshow={"slide_type": "subslide"}
len(rows)

# %% slideshow={"slide_type": "fragment"}
rows[0]

# %% [markdown] slideshow={"slide_type": "fragment"}
# * CSV works with strings by default, so would need to convert these values to floats

# %% [markdown] slideshow={"slide_type": "slide"}
# #### CSV library usage: writing

# %% slideshow={"slide_type": "fragment"}
with open('../data/some_copy_of_tabular_data.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerows(rows)

# %% [markdown] slideshow={"slide_type": "slide"}
# #### JSON library usage: reading

# %% slideshow={"slide_type": "fragment"}
import json
with open('../data/yelp_reviews_sf.json') as jsonfile:
    yelp_reviews = json.load(jsonfile)

# %% [markdown] slideshow={"slide_type": "fragment"}
# * JSON formatting uses key-value pairing, so naturally fits into Python dictionaries, or often, lists of dicts.

# %% slideshow={"slide_type": "subslide"}
type(yelp_reviews)

# %% slideshow={"slide_type": "fragment"}
len(yelp_reviews)

# %%
yelp_reviews[0]

# %% [markdown] slideshow={"slide_type": "slide"}
# #### JSON library usage: writing

# %% slideshow={"slide_type": "fragment"}
with open('../copy_of_yelp_reviews_sf.json', 'w') as jsonout:
    json.dump(yelp_dict, jsonout)

# %% [markdown] slideshow={"slide_type": "fragment"}
# * [Also see:](https://docs.python.org/3/library/json.html) `json.loads`/`json.dumps`. Similar functionality but acts on strings in JSON format, rather than on file objects.

# %% [markdown] slideshow={"slide_type": "slide"}
# #### CSV/JSON: a note from personal experience
# * Since CSV files have a naturally tabular structure they tend to be paired with Pandas DataFrames, so `pd.read_csv` / `dataframe.to_csv` gets more use than the `csv` library.
# * In contrast, JSON files can have complicated nesting structures that are not easily parsed into tabular DataFrames, so the `json` library is often used rather than `pd.read_json`.

# %% [markdown] slideshow={"slide_type": "slide"}
# ### NumPy, text-based and binary [I/O utilities:](https://numpy.org/doc/stable/reference/routines.io.html)
#
# Read to and write from NumPy arrays:
# * Text files: `np.loadtxt` / `np.savetxt` 
# * Binary files: `np.load` / `np.save` use [.npy format](https://numpy.org/doc/stable/reference/generated/numpy.lib.format.html#module-numpy.lib.format) for saving individual arrays.

# %% [markdown] slideshow={"slide_type": "slide"}
# #### Load csv file to NumPy array

# %% slideshow={"slide_type": "fragment"}
import numpy as np
arr = np.loadtxt('../data/some_tabular_data.csv', delimiter = ',')

# %% [markdown] slideshow={"slide_type": "fragment"}
# * `np.loadtxt` (and others) accept either a file path *string*, or a file connection *object* instantiated with `open('file/path/')`.
# * Unlike with `csv` the `delimiter=` keyword is NOT a comma by default.

# %% slideshow={"slide_type": "subslide"}
arr.shape

# %% slideshow={"slide_type": "fragment"}
arr[:3, :]

# %% [markdown] slideshow={"slide_type": "fragment"}
# * Same data as with `csv` library, but easier to work with as NumPy array rather than list of lists.

# %% [markdown] slideshow={"slide_type": "slide"}
# #### Save array in binary format

# %% slideshow={"slide_type": "fragment"}
np.save('../data/some_tabular_data.npy', arr)

# %% slideshow={"slide_type": "fragment"}
# Compare file sizes:
!ls -l ../data/some_tabular_data*

# %% [markdown] slideshow={"slide_type": "slide"}
# #### Notes on `.npy` format:
# * `.npy` works with a single array, to save multiple arrays use `np.savez` which saves each array as an individual `.npy` file and then zips everything together into a `.npz` file (which can be read with `np.load`).
# * `np.load` can also read Pickle files.

# %% [markdown] slideshow={"slide_type": "slide"}
# ## Loading hosted datasets
#
# * **scikit-learn** datasets
# * **statsmodels** datasets

# %% [markdown] slideshow={"slide_type": "slide"}
# ### scikit-learn
# * Toy datasets come with package, and are available with `datasets.load_` functions:

# %% slideshow={"slide_type": "fragment"}
from sklearn import datasets
bos_data = datasets.load_boston()

# %% [markdown] slideshow={"slide_type": "fragment"}
# * Real world datasets can be downloaded with `datasets.fetch_` functions:

# %% slideshow={"slide_type": "fragment"}
ca_housing_data = datasets.fetch_california_housing()

# %% [markdown] slideshow={"slide_type": "slide"}
# #### scikit datasets datatype:

# %% slideshow={"slide_type": "fragment"}
type(bos_data)

# %% slideshow={"slide_type": "fragment"}
# inspect its contents
dir(bos_data)

# %% slideshow={"slide_type": "fragment"}
# peek at the data
bos_data['data']

# %% [markdown] slideshow={"slide_type": "slide"}
# ##### Simulate data 
# * You can also use scikit-learn to simulate data with `datasets.make_` functions, e.g.:

# %% slideshow={"slide_type": "fragment"}
regress_data = datasets.make_regression()
type(regress_data)

# %% [markdown] slideshow={"slide_type": "subslide"}
# #### Observed/predictive data vs target data
# * Traditionally in machine learning observed data matrix is labeled `X` and target vector is `y`

# %% slideshow={"slide_type": "fragment"}
X, y = regress_data
type(X)

# %% slideshow={"slide_type": "fragment"}
print('X', X.shape)
print('y', y.shape)

# %% [markdown] slideshow={"slide_type": "slide"}
# ### Statsmodels datasets
#
# * The statsmodels library also has dataset loading functionality, with each dataset within the `datasets` package structured as a module.
#     - Each of these dataset modules will have functions and attributes in common.
# * More details on [the web](https://www.statsmodels.org/dev/datasets/index.html).

# %% slideshow={"slide_type": "fragment"}
# standard way of importing statsmodels
import statsmodels.api as sm

# %% slideshow={"slide_type": "subslide"}
# hit tab at the end of this line will bring up list of dataset modules
sm.datasets.sunspots

# %% slideshow={"slide_type": "fragment"}
# grab one and check its description:
print(sm.datasets.longley.DESCRLONG)

# %% [markdown] slideshow={"slide_type": "slide"}
# #### Loading statsmodels data
# * Use `.load_pandas`. 
#     - Another option you will see is: `.load` (houses data with different datatypes), but this will be deprecated in the future. 

# %% slideshow={"slide_type": "fragment"}
longley_data = sm.datasets.longley.load_pandas()
type(longley_data)

# %% slideshow={"slide_type": "fragment"}
type(longley_data.data)

# %% [markdown] slideshow={"slide_type": "slide"}
# * As with `scikit-learn` most of the `statsmodels` datasets are suited for predictive models. 
# * However, the machine learning and statistics communities often use different terms for the same thing.
#     - The observed/predictive and target data of ML is the known as exogenous and endogenous data in stats.

# %% slideshow={"slide_type": "fragment"}
# Split up data into an X matrix and y vector, as we did with the sklearn data:
X_longley, y_longley = longley_data.exog, longley_data.endog

# %% slideshow={"slide_type": "fragment"}
print('X', X_longley.shape)
print('y', y_longley.shape)

# %% [markdown] slideshow={"slide_type": "fragment"}
# (If you are used to the ML terminology, just remember that the *eXogenous* data goes in the *X* matrix.)
