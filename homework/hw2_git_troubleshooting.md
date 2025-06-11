# HW2: Git Troubleshooting Lab

**Due Date:** [To be announced]  
**Points:** 100  
**Submission:** Upload your written report to bCourses

---

## Overview

In this assignment, you'll practice essential Git troubleshooting skills by fixing a deliberately broken repository. Real-world Git usage often involves recovering from mistakes, so this lab will prepare you for common scenarios you'll encounter as a developer.

## Learning Objectives

By completing this assignment, you will:
- Practice Git recovery and troubleshooting techniques
- Understand how to fix common Git mistakes
- Learn to navigate Git history and recover lost work
- Gain confidence in Git operations through hands-on problem solving

## Assignment Setup

### Getting Started
1. Accept the GitHub Classroom assignment: `[GitHub Classroom Link - TBD]`
2. Clone your assigned repository to your local machine:
   ```bash
   git clone [your-assigned-repo-url]
   cd [repo-name]
   ```
3. **IMPORTANT**: Create a backup copy before starting work:
   ```bash
   cd ..
   cp -r [repo-name] [repo-name]-backup
   cd [repo-name]
   ```

### The Broken Repository
The repository you'll receive contains a student project with these intentional problems:
- **Deleted files**: Critical `important_data.txt` file has been removed
- **Detached HEAD state**: Repository is not properly on a branch
- **Poor commit messages**: Recent commits have unclear messages like "WIP", "temp", "asdf"
- **Unresolved merge conflict**: A merge between `main` and `feature-branch` was left incomplete
- **Staging issues**: Files may be in incorrect staging states
- **Branch problems**: Unnecessary or broken branches need cleanup

### Repository Structure
The project should contain:
- `README.md` - Project overview and instructions
- `important_data.txt` - Critical project data (MISSING - needs recovery)
- `student_code.py` - Python script for data analysis
- `config.json` - Configuration file
- `notes.txt` - Project notes and meeting records

## Tasks to Complete

### Task 1: File Recovery (20 points)
**Problem**: Important project files have been accidentally deleted.
- **Find**: Locate and recover the deleted `important_data.txt` file
- **Recover**: Restore the file to the working directory
- **Document**: Explain the commands you used and why

### Task 2: Fix Detached HEAD (20 points)
**Problem**: The repository is in a detached HEAD state.
- **Identify**: Confirm the current state of HEAD
- **Fix**: Return to a proper branch state
- **Document**: Explain what detached HEAD means and how you resolved it

### Task 3: Rewrite Commit Messages (20 points)
**Problem**: Recent commits have unclear or incorrect messages.
- **Find**: Identify commits with poor messages (look for "WIP", "temp", "asdf", etc.)
- **Rewrite**: Update at least 3 commit messages to be descriptive and professional
- **Document**: Explain the importance of good commit messages

### Task 4: Resolve Merge Conflict (20 points)
**Problem**: There's an unresolved merge conflict preventing progress.
- **Identify**: Find the conflicted files
- **Resolve**: Fix the merge conflict appropriately
- **Complete**: Successfully complete the merge
- **Document**: Explain the conflict resolution process

### Task 5: Clean Up Repository State (20 points)
**Problem**: The repository has various issues with staging and branch management.
- **Staging**: Fix any files stuck in inappropriate staging states
- **Branches**: Clean up any unnecessary or broken branches
- **Status**: Ensure `git status` shows a clean working directory
- **Document**: Describe the cleanup process and final repository state

## Submission Requirements

### Written Report
Create a report that includes:

1. **Introduction** (5 points)
   - Brief overview of the problems you encountered
   - Your approach to troubleshooting

2. **Task Solutions** (15 points each × 5 tasks = 75 points)
   For each task, include:
   - **Problem Description**: What was wrong?
   - **Solution Process**: Step-by-step commands used
   - **Command Explanations**: Why you chose these specific commands
   - **Screenshots**: Before and after states (optional but recommended)

3. **Reflection** (5 points)
   - What did you learn about Git troubleshooting?
   - Which problems were most challenging and why?
   - How will this knowledge help you in future development work?

4. **Final Repository State** (15 points)
   - Screenshot of final `git status`
   - Screenshot of `git log --oneline --graph`
   - Confirmation that all problems are resolved

### Code Submission
- Push your fixed repository to your GitHub fork
- Include the URL to your fixed repository in your report

## Grading Rubric

| Component | Points | Criteria |
|-----------|--------|----------|
| Task Completion | 75 | All 5 tasks properly completed |
| Command Understanding | 10 | Demonstrates understanding of Git commands |
| Documentation Quality | 10 | Clear explanations and proper formatting |
| Final State | 5 | Repository is properly cleaned and functional |

## Tips for Success

1. **Read the entire assignment before starting** - Understanding all problems helps you plan your approach
2. **Use `git status` frequently** - Always know your current repository state
3. **Make incremental progress** - Fix one problem at a time
4. **Document as you go** - Take notes and screenshots during the process
5. **Use `git log` and `git reflog`** - These are essential for understanding repository history
6. **Don't panic** - Git is designed to help you recover from mistakes

## Useful Commands for This Assignment

```bash
# Investigation commands
git status
git log --oneline --graph --all
git reflog
git branch -a

# Recovery commands
git checkout <file>
git reset <file>
git revert <commit>
git cherry-pick <commit>

# Advanced troubleshooting
git fsck
git clean -n  # (dry run before cleaning)
git stash list
```

## Academic Integrity

- You may discuss general Git concepts with classmates
- You may use Git documentation and online resources
- You must write your own solutions and report
- Cite any external resources you use beyond course materials

## Getting Help

- Git documentation: https://git-scm.com/docs
- If you're completely stuck, document your attempt and explain where you got stuck

---

**Remember**: This assignment simulates real-world scenarios. The goal is to learn problem-solving skills that will serve you throughout your development career. Take your time, think through each problem systematically, and don't hesitate to ask for help if needed.

---
