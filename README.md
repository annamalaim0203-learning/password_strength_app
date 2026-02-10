# 🔐 Password Strength Analyzer (Streamlit App)

This is a simple web application that helps you check how strong a password is.

The app analyzes a password based on:
- Length
- Use of uppercase letters
- Use of numbers
- Use of special characters
- Overall randomness (entropy)

⚠️ **Important:**  
Your password is **never stored, logged, or sent anywhere**.  
All analysis happens instantly and locally inside the app.

---

## 🧠 How the App Works (In Simple Words)

1. You enter a password
2. The app checks how complex it is
3. It calculates a **strength level**:
   - Weak
   - Medium
   - Strong
4. It shows suggestions to improve your password

---

## 📂 Project Files Explained

### `app.py`
This is the **main application file**.

It:
- Creates the web interface using Streamlit
- Takes password input securely
- Calculates password entropy
- Displays strength results and suggestions
- Generates a secure SHA-256 hash (one-way, not reversible)

---

### `strength_model.py`
This file contains the **password strength logic**.

It:
- Uses simple scoring rules
- Classifies passwords as Weak, Medium, or Strong
- Does NOT use heavy machine-learning libraries
- Is fully compatible with modern Python versions

---

### `requirements.txt`
This file lists what the app needs to run.

It only requires:
- `streamlit`

No complex or unsafe dependencies are used.

---

## ▶️ How to Run the App Locally

Make sure Python is installed.

1. Install dependencies:
```bash
pip install -r requirements.txt
