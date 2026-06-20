
</p>

# Module 01 — Linux Essentials · Submission

> Fill in the sections below. For each task, paste the exact commands you ran and add a
> screenshot to the `screenshots/` folder, then reference it as shown. Replace the placeholder
> text and image names with your own.

---

## Task 1 — Build a project workspace

### Commands I used


```bash

## create linux_lab

vsysuser@uptickpro-pod-333-iitmshakti:~$ mkdir linux_lab
vsysuser@uptickpro-pod-333-iitmshakti:~$ cd linux_lab
vsysuser@uptickpro-pod-333-iitmshakti:~/linux_lab$ pwd
/home/vsysuser/workspace/linux_lab

## create notes & scripts

vsysuser@uptickpro-pod-333-iitmshakti:~/linux_lab$ mkdir notes scripts
vsysuser@uptickpro-pod-333-iitmshakti:~/linux_lab$ ls
notes  scripts
<<<<<<< Updated upstream

vsysuser@uptickpro-pod-333-iitmshakti:~/linux_lab$ echo "Day 1: learned mkdir and cd" > notes/day1.txt
=======
vsysuser@uptickpro-pod-333-iitmshakti:~/linux_lab$ echo "Day 1: learned mkdir and cd" > notes/day1.txt
>>>>>>> Stashed changes
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
<<<<<<< Updated upstream
vsysuser@uptickpro-pod-333-iitmshakti:~/linux_lab$ find . -name "sample.log"
vsysuser@uptickpro-pod-333-iitmshakti:~/linux_lab$ cat > sample.log << 'EOF'
2026-06-15 09:00:01 INFO Application started
2026-06-15 09:01:12 WARNING Disk usage at 75%
2026-06-15 09:02:45 ERROR Failed to connect to database
2026-06-15 09:03:10 INFO Retrying connection
2026-06-15 09:03:30 Error Temporary network issue
2026-06-15 09:04:22 WARNING High memory usage detected
2026-06-15 09:05:01 ERROR User authentication failed
2026-06-15 09:06:17 INFO Background job completed
2026-06-15 09:07:40 warning Cache nearing capacity
2026-06-15 09:08:55 ERROR Unable to write to log file
2026-06-15 09:09:20 INFO Application shutdown initiated
EOF
vsysuser@uptickpro-pod-333-iitmshakti:~/linux_lab$ find . -name "sample.log"
./sample.log
vsysuser@uptickpro-pod-333-iitmshakti:~/linux_lab$ grep "ERROR" sample.log > errors.txt
vsysuser@uptickpro-pod-333-iitmshakti:~/linux_lab$ cat errors.txt
2026-06-15 09:02:45 ERROR Failed to connect to database
2026-06-15 09:05:01 ERROR User authentication failed
2026-06-15 09:08:55 ERROR Unable to write to log file
vsysuser@uptickpro-pod-333-iitmshakti:~/linux_lab$ grep -i "WARNING" sample.log
2026-06-15 09:01:12 WARNING Disk usage at 75%
2026-06-15 09:04:22 WARNING High memory usage detected
2026-06-15 09:07:40 warning Cache nearing capacity
vsysuser@uptickpro-pod-333-iitmshakti:~/linux_lab$ ^C
vsysuser@uptickpro-pod-333-iitmshakti:~/linux_lab$
vsysuser@uptickpro-pod-333-iitmshakti:~/linux_lab$ grep "ERROR" sample.log
2026-06-15 09:02:45 ERROR Failed to connect to database
2026-06-15 09:05:01 ERROR User authentication failed
2026-06-15 09:08:55 ERROR Unable to write to log file
vsysuser@uptickpro-pod-333-iitmshakti:~/linux_lab$ grep -c "ERROR" sample.log
3
vsysuser@uptickpro-pod-333-iitmshakti:~/linux_lab$ grep -i "ERROR" sample.log > errors.txt
vsysuser@uptickpro-pod-333-iitmshakti:~/linux_lab$ grep -i "WARNING" sample.log
2026-06-15 09:01:12 WARNING Disk usage at 75%
2026-06-15 09:04:22 WARNING High memory usage detected
2026-06-15 09:07:40 warning Cache nearing capacity
=======
find . -name "sample.log"
grep "ERROR" sample.log
grep -c "ERROR" sample.log
grep "ERROR" sample.log > errors.txt
grep -i "WARNING" sample.log
>>>>>>> Stashed changes
```

### Number of ERROR lines found

<!-- Write the count from grep -c here -->
`3`

### Screenshot

<img width="856" height="240" alt="Screenshot" src="https://github.com/user-attachments/assets/d8d4953c-0816-462e-bbed-c8da0c6f903c" />


![Task 2 — grep results](screenshots/task2.png)
