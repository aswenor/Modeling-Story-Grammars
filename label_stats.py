import re
import sys
from collections import Counter

def extract_labels(s):
	tokens = re.findall(r'\(|\)|[^\s()]+', s)
	all_labels, word_labels = [], []

	def parse_node(i):
		i += 1
		label = tokens[i]
		all_labels.append(label)
		i += 1
		if tokens[i] == '(':
			while tokens[i] != ')':
				if tokens[i] == '(':
					i = parse_node(i)
				else: 
					word_labels.append(label)
					i += 1
			i += 1
		elif tokens[i] == ')':
			i += 1
		else:
			word_labels.append(label)
			i += 2
		return i

	i = 0
	while i < len(tokens):
		i = parse_node(i)
	return all_labels, word_labels

def count_labels(list):
	
	label_counts = Counter(list)
	return label_counts

def main():
	if len(sys.argv) != 5:
		print("Usage: python label_stats.py <input_file> <all_labels_out> <word_labels_out> <label_counts_out>")
		sys.exit(1)

	input_file, all_out, word_out, counts_out = sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4]
	all_labels_total, word_labels_total, sequences = [], [], []

	with open(input_file, 'r', encoding='utf-8') as f:
		for line in f:
			line = line.strip()
			if not line:
				continue
			sequences.append(line)
			all_labels, word_labels = extract_labels(line)
			all_labels_total.extend(all_labels)
			word_labels_total.extend(word_labels)

	with open(all_out, 'w', encoding='utf-8') as f:
		f.write('\n'.join(all_labels_total))

	with open(word_out, 'w', encoding='utf-8') as f:
		f.write('\n'.join(word_labels_total))

	all_label_counts = count_labels(all_labels_total)
	word_label_counts = count_labels(word_labels_total)

	with open(counts_out, 'w', encoding='utf-8') as f:
		f.write(f"Counts for all labels...\n")
		for label, count in sorted(all_label_counts.items()):
			f.write(f"{label}\t{count}\n")
		f.write(f"\nCounts for word labels...\n")
		for label, count in sorted(word_label_counts.items()):
			f.write(f"{label}\t{count}\n")

if __name__ == "__main__":
	main()
			
