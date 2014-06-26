CSV merge utility
-----------------
Utility will read csv from std input and output combined columns to stdout.  All cells will be joined into the first cell of the list.  So for instance merging column 1 2 3 will result in a csv file where the merged columns end up in column 1 and columns 2 and 3 will be dropped from the output.

Usage
-----
merge_csv_columns.py [--ignore_empty] columns [columns]

The columns must be integers with the first column in the csv being column 1
--ignore_empty flag can be used if you don't want to join a cell that has no content.  This may be desirable when you don't want something like first_name  last_name because the middle name column is empty.

Example
-------
cat my.csv | python merge_csv_columns.py 1 2 3 > output.csv