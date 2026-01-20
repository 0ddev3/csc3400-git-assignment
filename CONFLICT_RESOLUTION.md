# COnflict Resolution Documentation

## Overview
This document explains how I resolved a merge conflict in calculator.py.

## What Caused the Conflict
 - The main branch changed the add() function.
 - The hotfic branch also changed the same function.
 - Git could not authomatically merge these changes.

## How I Resolved It
1. I ran "git merge origin/hotfix/readme-update"
2. Git reported a conflict in calculator.py
3. Opened the file and saw conflict markers:
<<<<<<<< HEAD
========
>>>>>>>>>>> origin/hotfix/readme-update
4. Edited the function to create a final merged version
5. Saved the file, staged it, and committed the merge

## Final Result
The conflict was resolved and the merged version of calculator.py now contains the final logic.
