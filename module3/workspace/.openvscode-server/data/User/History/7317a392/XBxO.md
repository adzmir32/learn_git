<img width="540" height="222" alt="Task 1_ls -R output" src="https://github.com/user-attachments/assets/396ff79d-6a93-49f0-9580-4101ff619154" /><p align="center">
  <img src="../../vyoma.png" alt="Vyoma Systems" width="200"/>
</p>

# Module 01 — Linux Essentials · Submission

> Fill in the sections below. For each task, paste the exact commands you ran and add a
> screenshot to the `screenshots/` folder, then reference it as shown. Replace the placeholder
> text and image names with your own.

---

## Task 1 — Build a project workspace

### Commands I used

```bash
vsysuser@uptickpro-pod-333-iitmshakti:~$ mkdir linux_lab
vsysuser@uptickpro-pod-333-iitmshakti:~$ cd linux_lab
vsysuser@uptickpro-pod-333-iitmshakti:~/linux_lab$ mk di notes scripts
bash: mk: command not found
vsysuser@uptickpro-pod-333-iitmshakti:~/linux_lab$ mk dir notes scripts
bash: mk: command not found
vsysuser@uptickpro-pod-333-iitmshakti:~/linux_lab$ pwd
/home/vsysuser/workspace/linux_lab
vsysuser@uptickpro-pod-333-iitmshakti:~/linux_lab$ mkdir notes scripts
vsysuser@uptickpro-pod-333-iitmshakti:~/linux_lab$ ls
notes  scripts
vsysuser@uptickpro-pod-333-iitmshakti:~/linux_lab$ echo "Day 1: learned mkdir and cd" > notes/day1.txt
vsysuser@uptickpro-pod-333-iitmshakti:~/linux_lab$ cat day1.txt
cat: day1.txt: No such file or directory
vsysuser@uptickpro-pod-333-iitmshakti:~/linux_lab$ cat notes/day1.txt
Day 1: learned mkdir and cd
vsysuser@uptickpro-pod-333-iitmshakti:~/linux_lab$ echo "Day 1: also learned ls" >> notes/day1.txt
vsysuser@uptickpro-pod-333-iitmshakti:~/linux_lab$ cat notes/day1.txt
Day 1: learned mkdir and cd
Day 1: also learned ls
vsysuser@uptickpro-pod-333-iitmshakti:~/linux_lab$ nano notes/day2.txt
vsysuser@uptickpro-pod-333-iitmshakti:~/linux_lab$ rm notes/day2.txt
vsysuser@uptickpro-pod-333-iitmshakti:~/linux_lab$ nano notes/day2.txt
vsysuser@uptickpro-pod-333-iitmshakti:~/linux_lab$ cp notes/day1.txt scripts/
vsysuser@uptickpro-pod-333-iitmshakti:~/linux_lab$ ls
notes  scripts
vsysuser@uptickpro-pod-333-iitmshakti:~/linux_lab$ ls scripts/
day1.txt
vsysuser@uptickpro-pod-333-iitmshakti:~/linux_lab$ ls -R
.:
notes  scripts

./notes:
day1.txt  day2.txt

./scripts:
day1.txt
```

### Screenshot

<!-- Save your screenshot in the screenshots/ folder, e.g. screenshots/task1.png -->

<img width="540" height="222" alt="Task 1_ls -R output" src="https://github.com/user-attachments/assets/0ea779af-ff08-4bc7-b945-2a808765d709" />

![Task 1 — ls -R output](screenshots/task1.png)

---

## Task 2 — Log hunting

### Commands I used

```bash
find . -name "sample.log"
grep "ERROR" sample.log
grep -c "ERROR" sample.log
grep "ERROR" sample.log > errors.txt
grep -i "WARNING" sample.log
```

### Number of ERROR lines found

<!-- Write the count from grep -c here -->
`3`

### Screenshot

<img width="917" height="677" alt="Task 2_grep results" src="https://github.com/user-attachments/assets/4962c5bf-0386-47bc-b23c-77808b900282" />

![Task 2 — grep results](screenshots/task2.png)
