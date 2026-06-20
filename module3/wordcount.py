line_count = 0
word_count = 0

with open("poem.txt", "r") as f:
	for line in f:
		line_count += 1
		word_count += len(line.split())

print(f"Number of lines: {line_count}")
print(f"Total number of words: {word_count}")

with open("summary.txt", "w") as f:
	f.write(f"The poem has {line_count} lines and {word_count} words.")


print("\nContents of summary.txt:")
with open("summary.txt", "r") as f:
	print(f.read())
