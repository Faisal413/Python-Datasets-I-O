## Python Datasets I/O

### Part 1

**Objective:** The objective of this part is to write a Python script (not IPython notebook) that reads in a JSON file, extracts/summarizes relevant data, and saves the data summary as a CSV file. To write this script, follow the below steps.

1. Write a function to load `coffee-tweets.json` into a list of Python dictionaries.
    - *Hint*: If you encounter an error when reading in the contents of `coffee-tweets.json`, note that the `json` library is set up to work with a *a single JSON object* at a time. Using a command line tool, such as `less`, (or using a text editor) take a peek at the contents of `coffee-tweets.json`. -- Does this file consist of one JSON object?

2. Familiarize yourself with how the tweet data are structured, in terms of the keys used and how things are nested within the dictionaries.
    - If you choose to do your examination in an interactive session (such as in a Notebook), then be sure to import your loading function and call it from the session, rather than copying the code from your script.

3. Write a function that extracts and summarizes numerical data from a tweet into a list. The list should (at minimum) include the tweet id, the user's id, the user's number of followers, whether the user's account is verified, the number of favorites and retweets the tweet received, the number of hashtags it contained, whether it mentioned another user, and the number of times coffee-related words (espresso, latte, etc.) appeared in the tweet text.

    - Your function should return this tweet data and optionally a list of the element/column names. For example, `[['tweet_id', 'user_id', 'follower_count', ...], [123456789, 123456, 100, ...]]`.
    - Hint: Check the key "entities" to find the number of hashtags a tweet contained and whether a tweet mentioned another user. 

4. Write a function that uses the function you wrote in step 3 to aggregate data from all the tweets and saves the data in a CSV file. Add a parameter to your function that specifies whether to write out the column names as a header for the CSV file.

5. Tie everything together so that calling your script from the command-line writes out a CSV file, as specified.
    - **Optional Extra Credit:** Use the `argparse` library to take input and output file paths as command line arguments.


### Part 2

**Objective:** The objective of this part is to write a Python script (not IPython notebook) that loads a dataset from the scikit-learn or statsmodels libraries and saves the data as a NumPy binary file (`.npy` or `.npz`). Follow the below steps.

1. Choose a dataset from the `datasets` modules of either scikit-learn or statsmodels. (You may use an interactive session to explore the dataset options and the data they contain.)

2. After exploring the dataset of your choice, make a plan to save the data using NumPy's IO tools. Most of the datasets are split between predictive/target (a.k.a. exogenous/endogenous) data, so don't forget to include the target data in your files. Also, since much of NumPy's speed and power comes from requiring an array to consist of a single datatype, you will need to think about how to keep track of meta-data like column labels.

3. Write a function that downloads your dataset from sklearn/statsmodels, and (if necessary) converts the data to NumPy arrays.

4. Write a function that saves the separate predictive and target NumPy arrays in a `.npz` file. Also save the column names of the predictive data as part of this file, or separately.

(Note that the statsmodels datasets and real world datasets in sklearn are saved as files on your computer, so in practice this pipeline isn't all that useful. Also, both libraries include convenience functions for deleting these files that you might want to run: `.clear_data_home()` when you are done.)
