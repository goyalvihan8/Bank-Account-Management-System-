# 🏦 Bank Account Management System Using Python

## 📌 Project Overview

The **Bank Account Management System** is a console-based Python application designed to manage bank accounts and perform basic banking operations efficiently.

It allows users to create accounts, deposit money, withdraw money, check account balances, view transaction history, and save account information using file handling.

This project demonstrates **Object-Oriented Programming (OOP)** concepts, data structures, exception handling, and persistent data storage in Python.

## 🚀 Features

- **Create Accounts:** Create bank accounts with a unique account number, account holder name, and initial balance.
- **Deposit Money:** Deposit money into an existing bank account.
- **Withdraw Money:** Withdraw money after checking the available balance.
- **Check Balance:** Display the current balance of a bank account.
- **Transaction History:** View previous deposits and withdrawals.
- **Save Records:** Store account details and transaction history in `account.txt`.
- **Load Records:** Load previously saved account records when the application starts.
- **Duplicate Prevention:** Prevent creating accounts with duplicate account numbers.
- **Input Validation:** Prevent invalid transaction amounts and negative initial balances.

## 🛠️ Technologies Used

- **Programming Language:** Python 3
- **Programming Paradigm:** Object-Oriented Programming (OOP)
- **Data Structures:** Python Lists
- **Storage:** Text File (`account.txt`)
- **Interface:** Command-Line Interface (CLI)
- **Exception Handling:** `try` and `except`

## 🧠 OOP Concepts Implemented

| Concept | Implementation |
|---|---|
| Abstraction | Abstract base class and abstract methods for account operations |
| Encapsulation | Account attributes such as account number, account holder name, and balance |
| Inheritance | `SavingAccount` inherits from the `Account` class |
| Polymorphism | Derived classes can implement shared account methods |

## 📂 Project Structure

```text
Bank-Account-Management-System/
│
├── bank_management.py
├── account.txt
└── README.md
```

`account.txt` stores bank account details and transaction records.

## ⚙️ Installation and Setup

**Step 1: Clone the repository**

```bash
git clone https://github.com/USERNAME/Bank-Account-Management-System.git
```

**Step 2: Navigate to the project folder**

```bash
cd Bank-Account-Management-System
```

**Step 3: Run the application**

```bash
python bank_management.py
```

Replace `USERNAME` with your GitHub username and use your actual Python filename.

No external Python libraries are required.

## 💻 Program Menu

```text
====== Bank Account Management System ======

1. Create Account
2. Deposit Money
3. Withdraw Money
4. Check Balance
5. Transaction History
6. Save Records
7. Exit

Enter Your Choice:
```

## 💳 Example Bank Account Record

```text
Account Number: 101
Account Holder Name: Rahul
Account Balance: 5000.0
```

## 💰 Example Banking Operations

### Deposit Money

```text
Enter Account Number: 101
Enter Deposit Amount: 2000

Amount Deposited Successfully...
Current Balance: 7000.0
```

### Withdraw Money

```text
Enter Account Number: 101
Enter Withdrawal Amount: 1500

Amount Withdrawn Successfully...
Current Balance: 5500.0
```

### Transaction History

```text
Account Number: 101

Transaction History:
1. Initial Balance: 5000.0
2. Deposited: 2000.0
3. Withdrawn: 1500.0

Current Balance: 5500.0
```

## 💾 File Storage

The application stores bank account information in `account.txt`.

An example of a possible record format is:

```text
101,Rahul,5500.0,Deposited:2000|Withdrawn:1500
102,Priya,8000.0,Deposited:3000
103,Aman,4000.0,Withdrawn:1000
```

Each record contains:

`Account_Number,Account_Holder_Name,Account_Balance,Transaction_History`

The application maintains account information using Python objects and lists.

## 🔄 How the Application Works

1. The application starts and attempts to load previously saved account records from `account.txt`.
2. The user selects an operation from the main menu.
3. The system identifies the bank account using its unique account number.
4. Account details are stored as Python objects.
5. When money is deposited, the account balance increases.
6. When money is withdrawn, the system checks whether sufficient funds are available.
7. Successful transactions are added to the transaction history.
8. The user can save account records for future use.

## 🏗️ Classes Used

### 1. Account Class

The `Account` class represents a bank account and stores important account information.

**Attributes:**
- Account Number
- Account Holder Name
- Account Balance
- Transaction History

**Responsibilities:**
- Store account details.
- Manage account information.
- Maintain transaction records.

### 2. SavingAccount Class

The `SavingAccount` class inherits from the `Account` class.

**Responsibilities:**
- Represent a savings account.
- Reuse account properties and methods.
- Implement account-specific functionality.

### 3. Bank_Account_Management Class

The `Bank_Account_Management` class manages the banking system.

**Responsibilities:**
- Create bank accounts.
- Search existing accounts.
- Deposit and withdraw money.
- Check account balances.
- Display transaction history.
- Save and load account records.

## 📚 Python Concepts Practiced

- Classes and Objects
- Object-Oriented Programming
- Abstract Base Classes (`ABC`), if used
- Abstract Methods (`@abstractmethod`), if used
- Encapsulation
- Inheritance
- Polymorphism
- Getter and Setter Methods
- Lists and Loops
- Conditional Statements
- Exception Handling
- File Handling
- Input Validation
- Persistent Data Storage

## 🎯 Learning Objectives

- Apply Object-Oriented Programming concepts in a practical project.
- Understand bank account management operations.
- Implement deposit and withdrawal functionality.
- Manage multiple bank accounts using Python lists.
- Maintain transaction history.
- Practice saving and loading account records.
- Handle invalid inputs and insufficient balances.
- Improve Python programming and problem-solving skills.

## 🔮 Future Enhancements

- Integrate SQLite or MySQL for database storage.
- Develop a graphical user interface using Tkinter.
- Implement secure account authentication.
- Add fund transfers between accounts.
- Generate bank statements.
- Support different account types.
- Add transaction timestamps.
- Implement advanced transaction searching.

## ⚠️ Disclaimer

This project is developed for **educational purposes only**. It is not intended for real banking transactions or the storage of sensitive financial information.

## ⭐ Support

If you find this project helpful, consider giving the repository a star ⭐ on GitHub.
