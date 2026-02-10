import streamlit as st
import math
import hashlib
import re

from strength_model import predict_strength

# ------------------ Utility Functions ------------------

def calculate_entropy(password: str) -> float:
    charset = 0
    if re.search(r"[a-z]", password):
        charset += 26
    if re.search(r"[A-Z]", password):
        charset += 26
    if re.search(r"[0-9]", password):
        charset += 10
    if re.search(r"[^\w]", password):
        charset += 32

    if charset == 0:
        return 0.0

    return round(len(password) * math.log2(charset), 2)


def sha256_hash(password: str) -> str:
    return hashlib.sha256(password.encode("utf-8")).hexdigest()


# ------------------ Streamlit UI ------------------

st.set_page_config(
    page_title="Password Strength Analyzer",
    page_icon="🔐",
    layout="centered"
)

st.title("🔐 Password Strength Analyzer")
st.caption("Pure-Python | Secure | Python 3.13 Compatible")

password = st.text_input(
    "Enter a password to analyze",
    type="password",
    help="Passwords are processed locally and never stored."
)

if password:
    length = len(password)
    upper = bool(re.search(r"[A-Z]", password))
    lower = bool(re.search(r"[a-z]", password))
    digit = bool(re.search(r"[0-9]", password))
    special = bool(re.search(r"[^\w]", password))
    entropy = calculate_entropy(password)

    strength = predict_strength(
        length, upper, lower, digit, special, entropy
    )

    st.subheader("🔍 Analysis Results")
    st.metric("Entropy (bits)", entropy)
    st.metric("Strength Classification", strength)

    st.subheader("🔑 Password Hash (SHA-256)")
    st.code(sha256_hash(password))

    st.subheader("🛡️ Security Feedback")

    if length < 12:
        st.warning("Use at least 12 characters.")
    if not upper:
        st.warning("Add an uppercase letter.")
    if not digit:
        st.warning("Add a number.")
    if not special:
        st.warning("Add a special character.")

    if strength == "Strong":
        st.success("This password is suitable for high-security use.")

st.divider()
st.caption("⚠️ No passwords are stored, logged, or transmitted.")
