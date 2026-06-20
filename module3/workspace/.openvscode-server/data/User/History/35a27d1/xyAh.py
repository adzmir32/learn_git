line_count = 0
word_count = 0

with open("poem.txt", "r") as f:
	for line in f:
		line_count += 1
		word_count += len(line.split())

print(f"Number of lines: {line_count}")
