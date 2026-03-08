# ATM Management System

A simple command-line ATM simulation built with Python that demonstrates Git collaboration and merge conflict resolution.

## 🎯 Project Overview

This ATM system provides essential banking operations including balance checking, deposits, withdrawals, PIN management, transaction history, and account information display.

## ✨ Features

- **Check Balance** - View current account balance
- **Deposit Money** - Add funds to your account
- **Withdraw Money** - Withdraw funds from your account
- **Change PIN** - Update your security PIN
- **Transaction History** - View all your transactions (Added by Developer 1)
- **Account Information** - Display account holder details (Added by Developer 2)
- **Secure PIN Authentication** - PIN verification before access

## 🚀 Getting Started

### Prerequisites

- Python 3.x installed on your system
- Git installed

### Installation

1. Clone the repository:
```bash
git clone https://github.com/rohitnegi106/Git-Project-Submission.git
cd Git-Project-Submission
```

2. Run the ATM application:
```bash
python atm.py
```

### Default Credentials

- **PIN**: `1234`
- **Initial Balance**: ₹5000
- **Account Holder**: John Doe
- **Account Number**: XXXX-XXXX-1234

## 📸 Screenshots

### Initial Setup & Repository Creation

![Initial Commit]()
*Screenshot: Initial repository setup and first commit*

### Developer 1 - Transaction History Feature

![Developer 1 Branch]()
*Screenshot: Creating and working on developer1 branch*

### Developer 2 - Account Info Feature

![Developer 2 Branch]()
*Screenshot: Creating and working on developer2 branch*

### Merge Conflict Resolution

![Merge Conflict]()
*Screenshot: Merge conflict in atm.py*

![Conflict Resolution]()
*Screenshot: Successfully resolved merge conflict*

### Final Push

![Final Push]()
*Screenshot: Pushing merged changes to GitHub*

## 🔧 Git Commands Used

### Initial Setup
```bash
# Initialize repository
git init

# Add files to staging
git add .

# Create initial commit
git commit -m "Initial commit - ATM project with 5 functions"

# Add remote repository
git remote add origin https://github.com/rohitnegi106/Git-Project-Submission.git

# Push to GitHub
git push -u origin main
```

### Developer 1 Workflow (Transaction History Feature)
```bash
# Create and switch to developer1 branch
git checkout -b developer1

# Make changes to atm.py (add transactions list and transaction_history function)

# Stage changes
git add atm.py

# Commit changes
git commit -m "developer1 - added transaction history function"

# Push to remote
git push origin developer1

# Switch back to main
git checkout main

# Merge developer1 branch
git merge developer1
```

### Developer 2 Workflow (Account Info Feature)
```bash
# Create and switch to developer2 branch
git checkout -b developer2

# Make changes to atm.py (add account holder info and account_info function)

# Stage changes
git add atm.py

# Commit changes
git commit -m "developer2 - added account information function"

# Push to remote
git push origin developer2

# Switch back to main
git checkout main

# Merge developer2 branch (this creates a conflict!)
git merge developer2
```

### Merge Conflict Resolution
```bash
# Check status to see conflicts
git status

# View the conflict in the file
cat atm.py

# Resolve conflicts manually by editing atm.py
# Keep both features: transactions + account info

# Stage the resolved file
git add atm.py

# Complete the merge
git commit -m "Merge branch 'developer2'"

# Push merged changes
git push origin main
```

### Useful Git Commands
```bash
# Check repository status
git status

# View commit history
git log --oneline

# View all branches
git branch -a

# View differences
git diff

# Pull latest changes
git pull origin main
```

## 📁 Project Structure

```
atm_project/
│___ screenshots     # screensots with steps
├── atm.py           # Main ATM application
├── .gitignore       # Git ignore file
└── README.md
     # Project documentation
```

## 🤝 Collaboration Workflow

This project demonstrates a typical Git collaboration workflow:

1. **Main Branch** - Contains stable, production-ready code
2. **Developer Branches** - Individual developers work on features
3. **Merge Conflicts** - Handled when multiple developers modify the same code
4. **Conflict Resolution** - Manual resolution keeping both features
5. **Final Integration** - Merged code pushed to main branch

## 🎓 Learning Outcomes

- Git branching and merging
- Handling merge conflicts
- Collaborative development workflow
- Version control best practices
- Feature integration

## 👥 Contributors

- **Developer 1** - Transaction History Feature
- **Developer 2** - Account Information Feature

## 📝 License

This project is created for educational purposes to demonstrate Git workflows and Python programming.

## 🐛 Known Issues

None at the moment. Feel free to report any issues!

## 🔮 Future Enhancements

- Add database integration for persistent data
- Implement multiple user accounts
- Add transaction limits and daily withdrawal limits
- Generate transaction receipts
- Add interest calculation feature
- Implement account statement generation

---

