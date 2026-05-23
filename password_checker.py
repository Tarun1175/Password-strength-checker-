import re

print("=== Password Strength Checker ===") password = input("Enter a password: ")

strength = 0 feedback = []

Length check

if len(password) >= 8: strength += 1 else: feedback.append("Use at least 8 characters")

Uppercase check

if re.search(r"[A-Z]", password): strength += 1 else: feedback.append("Add an uppercase letter")

Lowercase check

if re.search(r"[a-z]", password): strength += 1 else: feedback.append("Add a lowercase letter")

Number check

if re.search(r"[0-9]", password): strength += 1 else: feedback.append("Add a number")

Special character check

if re.search(r"[!@#$%^&*(),.?":{}|<>]", password): strength += 1 else: feedback.append("Add a special character")

Result

print("\n=== Result ===")

if strength == 5: print("Strong Password") elif strength >= 3: print("Medium Password") else: print("Weak Password")

if feedback: print("\nSuggestions:") for item in feedback: print("-", item)
