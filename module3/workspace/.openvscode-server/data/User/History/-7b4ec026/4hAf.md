<p align="center">
  <img src="../../vyoma.png" alt="Vyoma Systems" width="200"/>
</p>

# Module 03 — Python Programming · Submission

> Fill in the sections below. For each task, paste your code and add a screenshot to the
> `screenshots/` folder, then reference it as shown. Replace the placeholder text and image
> names with your own.

---

## Task 1 — Interactive greeting script

### My code (`greeting.py`)

name = input("What is your name? ")
age = int(input("How old are you? "))

print(f"Hello {name}, welcome to RISC-V training!")
print(f"Next year you will be {age + 1} years old.")

for i in range(1, 6):
    print(f"Day {i}")

### Screenshot

<!-- Save your screenshot in the screenshots/ folder, e.g. screenshots/task1.png -->
![Task 1 — greeting.py running](screenshots/task1.png)

---

## Task 2 — File word counter

### My code (`wordcount.py`)

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


### Result (line and word counts)

<!-- Write the counts your program reported -->
`<lines>` lines, `<words>` words

### Screenshot

![Task 2 — wordcount.py output and summary.txt](screenshots/task2.png)
