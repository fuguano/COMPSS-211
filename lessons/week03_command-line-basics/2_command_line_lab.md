# 🛠 Lab: Practical Bash for Computational Social Science

**Goal:** gain confidence using the command line to quickly inspect, transform, and organize files without needing Python for every task.

**What you’ll need:**
- Your terminal (mac/Linux, or WSL on Windows)
- A folder `bash_lab/` with:
  - `data/` (10–20 small `.csv` files, some `.json`)
  - `logs/` (`app_YYYY.log` with some lines containing `ERROR`, `WARN`)
  - `docs/` (`.md` files with `http:` links, some `https:`)
  - Some files with spaces in names

### Part 1: Navigation + inspection
1. Print your current directory path.
2. List all files in `data/` showing sizes in human-readable format.
3. Count the number of `.csv` files in `data/`.
4. Count total lines across all `.csv` files in `data/`.

### Part 2: Searching + filtering  
5. Find all lines containing "ERROR" (case-insensitive) in `logs/*.log`.
6. Count how many lines contain "ERROR" in all log files.
7. Search for "ERROR" with line numbers shown.

### Part 3: Safe batch operations
8. Find all files with spaces in their names under `docs/`.
9. Rename them to use underscores (preview first, then apply).
10. Replace `http:` with `https:` in all `.md` files in `docs/`.

### Part 4: Automation
11. Create a simple script that counts lines in all `.csv` files.
12. Find all `.json` files and pass them to `xargs echo` to see the list.

**Live Check-off:**
- A text file `lab_commands.txt` with the exact commands you ran, in order.
- Short comments (`# like this`) explaining why you used each command.
