import sys
import csv
import argparse

parser = argparse.ArgumentParser(description='CSV column merge')
parser.add_argument('merge_columns', nargs='+', help='Columns to be merged', type=int)
parser.add_argument('--ignore-empty', action='store_true', help='Will not join the particular cell if it is completely empty')
parser.add_argument('-d', '--delimiter', help='The delimiter that will be used between merged cells', default=' ')
arguments = parser.parse_args()
merge_columns = [i - 1 for i in arguments.merge_columns]
delimiter = arguments.delimiter

def include(cell):
	if arguments.ignore_empty:
		return cell
	else:
		return True

def merged_generator(source, *to_merge):
	for row in source:
		merged_columns = delimiter.join([row[i] for i in to_merge if include(row[i])])
		row[to_merge[0]] = merged_columns
		yield [column for (i, column) in enumerate(row) if not (i in to_merge[1:])]
		

reader = csv.reader(iter(sys.stdin.readline, ''))
generator = merged_generator(reader, *merge_columns)
writer = csv.writer(sys.stdout)
for row in generator:
	writer.writerow(row)
