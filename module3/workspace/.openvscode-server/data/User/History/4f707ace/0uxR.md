<p align="center">
  <img src="../../vyoma.png" alt="Vyoma Systems" width="200"/>
</p>

# Module 02 — Git & Version Control · Submission

> Fill in the sections below. For each task, paste the exact commands you ran and add a
> screenshot to the `screenshots/` folder, then reference it as shown. Replace the placeholder
> text and image names with your own.

---

## Task 1 — Publish your first repository

### Commands I used

```bash
mkdir learn_git && cd learn_git
git init
git branch -m main
echo "Hello Git" > notes.txt
git add .
git commit -m "Initial commit"
git remote add origin https://github.com/adzmir32/learn_git.git
git remote -v
git push -u origin main
```

### Link to my GitHub repository

https://github.com/adzmir32/learn_git
`<your repository URL>`

### Screenshot

<!-- Save your screenshot in the screenshots/ folder, e.g. screenshots/task1.png -->
![Task 1 — repository on GitHub](screenshots/task1.png)

---

## Task 2 — Branch, modify, and merge

### Commands I used

```bash
git checkout -b feature
echo "Learning Git branching" >> notes.txt
git add .
git commit -m "Add branching note"
git checkout main
cat notes.txt
git merge feature
cat notes.txt
git log --oneline --graph --all
git push
```

### Screenshot

![Task 2 — git log graph](screenshots/task2.png)

---

## Optional stretch goal — fork & pull request

<!-- If you completed the stretch goal, paste your pull request link here. Otherwise, delete this section. -->
`https://github.com/adzmir32/assignment1-adzmir32/pull/new/my-feature`
