# Read in the file of sequences 
# Find all of the possible subsequences within the lists provided of min_len = 2
# For each list (sequence of labels)
	# Find all of the possible subsequences of length 2 or greater
	# For each of the possible subsequences
		# If it is not alredy included in the dictionary of subsequences
			# Add to the dictionary of subsequences
		# Else 
			# Increase the counter for that specific sequence

# Output the dictionary and its related counters to a file

import re
import argparse
from collections import Counter

def extract_labels(line):
	labels = []
	pattern = re.compile(r"\(\s*([^\s()]+)")
	matches = pattern.findall(line)

	return matches

def all_subsequences(seq, min_len=2):
	n = len(seq)
	for start in range(n):
		for end in range(start + min_len, n+1):
			yield tuple(seq[start:end])

def count_subsequences(input_file, min_len=2):
	counts = Counter()
	
	with open(input_file, 'r', encoding='utf-8') as f:
		for line in f:
			line = line.strip()
			if not line:
				continue
	
			labels = extract_labels(line)

			for subseq in all_subsequences(labels, min_len=min_len):
				counts[subseq] += 1
	return counts

def write_counts(counts, output_file):
	with open(output_file, 'w', encoding='utf-8') as f:
		for subseq, count in counts.items():
			subseq_str = " ".join(subseq)
			f.write(f"{subseq_str}\t{count}\n")
def print_top_n(counts, n):
	print(f"\nTop {n} most common subsequences:\n")
	for subseq, count in counts.most_common(n):
		subseq_str = " ".join(subseq)
		print(f"{subseq_str} --> {count}")

def main():
	parser = argparse.ArgumentParser(description="Count subsequences in label sequences.")
	parser.add_argument("input_file", help="Input file containing the labeled input sentences")
	parser.add_argument("output_file", help="Output file for subsequence counts")
	parser.add_argument("--min_len", type=int, default=2, help="Minimum subsequence length (default=2)")
	parser.add_argument("--top_n", type=int, default=0, help="Print the N most common subsequences (default = 0)")

	args = parser.parse_args()

	counts = count_subsequences(args.input_file, min_len=args.min_len)
	write_counts(counts, args.output_file)

	if args.top_n > 0:
		print_top_n(counts, args.top_n)


if __name__ == "__main__":
	main()
