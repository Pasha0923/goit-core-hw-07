# 📒 Contact Book (Address Book) — Console Assistant Bot

A simple command-line contact book assistant bot written in **Python 3.13**, using **object-oriented programming** principles.

This console bot helps you manage contacts: add, edit, delete, and search for phone numbers.
 Contacts can have multiple phone numbers, and each phone number is validated (must be exactly 10 digits). Additionally, contacts can store a birthday date, which is validated and used to track upcoming birthdays and send timely greetings.

 ---

## 🧠 Features

- Interactive console assistant bot interface  
- Add and remove contact records  
- Edit and find phone numbers  
- Support multiple phone numbers per contact  
- Validate phone numbers (only 10-digit numeric values)  
- Store and validate birthdays in format DD.MM.YYYY  
- Retrieve contacts with birthdays in the next 7 days, including adjusted greeting dates if birthdays fall on weekends  
- Pretty string representation of records and the address book  
---
## 🛠 Technologies
* Python 3.13 
* OOP principles  
* Standard library (collections,datetime)  
---
## ⚡ Installation

1. Make sure you have **Python 3.13** installed  
2. Clone the repository:
```bash
git clone https://github.com/YOUR_USERNAME/YOUR_REPO_NAME.git 
```
3. Navigate to the project folder:
```bash
cd YOUR_REPO_NAME
```
4. (Optional) Create a virtual environment:
python -m venv venv
source venv/bin/activate  # Linux/macOS
venv\Scripts\activate     # Windows