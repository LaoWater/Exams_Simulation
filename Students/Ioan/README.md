# Git Branching & Pull Request Guide

This guide helps you create a new branch and open a pull request for your work.

## 1. Create and Switch to a New Branch

```
git checkout -b my-feature-branch
```
Replace `my-feature-branch` with a descriptive name for your work.

## 2. Make Your Changes
- Edit, add, or delete files as needed.

## 3. Stage and Commit Your Changes

```
git add .
git commit -m "Describe your changes here"
```

## 4. Push Your Branch to GitHub

```
git push origin my-feature-branch
```

## 5. Open a Pull Request
- Go to your repository on GitHub.
- Click **Compare & pull request** for your branch.
- Add a title and description, then click **Create pull request**.

---

**Tips:**
- Always pull the latest changes from `main` before starting:
  ```
  git checkout main
  git pull origin main
  ```
- Keep your branch up to date with `main`:
  ```
  git fetch origin
  git merge origin/main
  ```
