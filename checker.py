import re

def check_password(pw):
    score = 0
    tips = []
    if len(pw) >= 12: score += 2
    elif len(pw) >= 8: score += 1
    else: tips.append("Use at least 8 characters (12+ is better)")
    if re.search(r"[A-Z]", pw): score += 1
    else: tips.append("Add an uppercase letter")
    if re.search(r"[a-z]", pw): score += 1
    else: tips.append("Add a lowercase letter")
    if re.search(r"\d", pw): score += 1
    else: tips.append("Add a number")
    if re.search(r"[^\w]", pw): score += 1
    else: tips.append("Add a symbol like @ or #")
    if pw.lower() in ["password", "123456", "qwerty", "admin"]:
        score = 0
        tips.append("This is a very common password")
    levels = ["Very weak", "Weak", "Weak", "Medium", "Strong", "Strong", "Very strong"]
    return levels[min(score, 6)], tips

pw = input("Enter password: ")
level, tips = check_password(pw)
print("Strength:", level)
for t in tips:
    print("-", t)
