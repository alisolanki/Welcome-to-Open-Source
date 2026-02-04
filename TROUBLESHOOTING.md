# 🔧 Troubleshooting Guide

This guide helps you solve common issues when contributing to this repository.

## 📋 Table of Contents
- [Common Git Errors](#common-git-errors)
- [Fork & Clone Issues](#fork--clone-issues)
- [Pull Request Problems](#pull-request-problems)
- [Installation Issues](#installation-issues)
- [Still Need Help?](#still-need-help)

---

## Common Git Errors

### ❌ Error: "Permission denied (publickey)"

**Problem:** You don't have SSH keys set up or GitHub can't access them.

**Solution:**
```bash
# Check if you have SSH keys
ls -al ~/.ssh

# If no keys exist, generate new ones
ssh-keygen -t ed25519 -C "your_email@example.com"

# Add SSH key to ssh-agent
eval "$(ssh-agent -s)"
ssh-add ~/.ssh/id_ed25519

# Add the SSH key to your GitHub account
cat ~/.ssh/id_ed25519.pub
# Copy the output and add it to GitHub: Settings → SSH and GPG keys → New SSH key
```

**Alternative:** Use HTTPS instead of SSH:
```bash
git remote set-url origin https://github.com/YOUR_USERNAME/Welcome-to-Open-Source.git
```

---

### ❌ Error: "fatal: not a git repository"

**Problem:** You're not in a git repository directory.

**Solution:**
```bash
# Navigate to your cloned repository
cd Welcome-to-Open-Source

# Or initialize a new repository if needed
git init
```

---

### ❌ Error: "Your branch is behind 'origin/master'"

**Problem:** Your local branch is outdated.

**Solution:**
```bash
# Pull latest changes
git pull origin master

# Or if you have local changes
git stash          # Save your changes temporarily
git pull origin master
git stash pop      # Restore your changes
```

---

### ❌ Error: "fatal: refusing to merge unrelated histories"

**Problem:** Trying to merge repositories with no common commit history.

**Solution:**
```bash
git pull origin master --allow-unrelated-histories
```

---

## Fork & Clone Issues

### ❌ Can't Find "Fork" Button

**Problem:** Not logged into GitHub or viewing the wrong page.

**Solution:**
1. Make sure you're logged into your GitHub account
2. Visit: https://github.com/alisolanki/Welcome-to-Open-Source
3. Look for the "Fork" button in the top-right corner
4. Click it and wait for the fork to complete

---

### ❌ Cloning Takes Forever or Fails

**Problem:** Network issues or large repository size.

**Solution:**
```bash
# Try shallow clone (faster)
git clone --depth 1 https://github.com/YOUR_USERNAME/Welcome-to-Open-Source.git

# Or use GitHub CLI
gh repo clone YOUR_USERNAME/Welcome-to-Open-Source
```

---

### ❌ Error: "Repository not found"

**Problem:** Wrong URL or repository is private.

**Solution:**
```bash
# Check your fork URL (replace YOUR_USERNAME)
https://github.com/YOUR_USERNAME/Welcome-to-Open-Source

# Verify the remote URL
git remote -v

# Update if needed
git remote set-url origin https://github.com/YOUR_USERNAME/Welcome-to-Open-Source.git
```

---

## Pull Request Problems

### ❌ Can't Create Pull Request

**Problem:** Haven't pushed changes or pushing to wrong branch.

**Solution:**
1. Make sure you've committed your changes:
   ```bash
   git status                    # Check status
   git add .                     # Stage all changes
   git commit -m "Your message"  # Commit
   ```

2. Push to YOUR fork:
   ```bash
   git push origin master
   ```

3. Go to the original repository and create PR from there

---

### ❌ PR Shows Too Many Commits

**Problem:** You're comparing against the wrong branch or haven't updated your fork.

**Solution:**
```bash
# Update your fork
git remote add upstream https://github.com/alisolanki/Welcome-to-Open-Source.git
git fetch upstream
git checkout master
git merge upstream/master
git push origin master
```

---

### ❌ Merge Conflicts

**Problem:** Your changes conflict with other updates.

**Solution:**
```bash
# Update from upstream
git fetch upstream
git merge upstream/master

# Fix conflicts manually in your editor
# Look for markers like: <<<<<<<, =======, >>>>>>>

# After fixing:
git add .
git commit -m "Resolve merge conflicts"
git push origin master
```

---

### ❌ PR Not Following Format

**Problem:** Your contribution doesn't match the required format.

**Solution:**
1. Read the [CONTRIBUTING.md](CONTRIBUTING.md) file carefully
2. For this repo, make sure to:
   - Add yourself to the contributors table in README.md
   - Use the correct HTML format
   - Include your GitHub profile link
   - Use your GitHub avatar image
3. Follow the exact format shown in examples

---

## Installation Issues

### ❌ Git Not Installed

**Problem:** `git` command not found.

**Solution:**

**Windows:**
- Download from: https://git-scm.com/download/win
- Or use: `winget install Git.Git`

**Mac:**
```bash
# Install Homebrew if needed
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"

# Install Git
brew install git
```

**Linux:**
```bash
# Ubuntu/Debian
sudo apt-get update
sudo apt-get install git

# Fedora
sudo dnf install git
```

---

### ❌ Git Configuration Issues

**Problem:** Git doesn't know who you are.

**Solution:**
```bash
# Set your name and email
git config --global user.name "Your Name"
git config --global user.email "your_email@example.com"

# Verify configuration
git config --list
```

---

## Still Need Help?

### 📚 Additional Resources

- [GitHub Docs](https://docs.github.com/)
- [Git Documentation](https://git-scm.com/doc)
- [Pro Git Book](https://git-scm.com/book/en/v2)
- [GitHub Skills](https://skills.github.com/)

### 💬 Get Support

1. **Check existing issues:** [Issues Page](https://github.com/alisolanki/Welcome-to-Open-Source/issues)
2. **Ask in discussions:** [Discussions](https://github.com/alisolanki/Welcome-to-Open-Source/discussions)
3. **Create a new issue:** Describe your problem in detail

### 🎓 Beginner-Friendly Tutorials

- [First Contributions](https://github.com/firstcontributions/first-contributions)
- [How to Contribute to Open Source](https://opensource.guide/how-to-contribute/)
- [GitHub Learning Lab](https://lab.github.com/)

---

## 📝 Common Questions

**Q: How long does it take for my PR to be reviewed?**  
A: Usually within a few days. Be patient and make sure you followed all requirements.

**Q: Can I make multiple contributions?**  
A: Yes! You can contribute multiple times, but each PR should be separate.

**Q: What if I made a mistake in my PR?**  
A: You can push new commits to the same branch to update your PR.

**Q: Do I need to know programming?**  
A: No! This repository is beginner-friendly. You just need to add your name.

---

**Happy Contributing! 🎉**

If this guide helped you, consider giving the repository a ⭐!
