import streamlit as st
import re

st.set_page_config(page_title="Password Stength Checker", page_icon="🔒")

st.title("🔒 Password Stength Checker")
st.markdown("""
            ## Welcome to the Ultimate Password Stength Checker! 👋 
            Use this simple tool to check the strenght of your password and get suggestions on how to make it stronger,
            we will give you helpful tips to create a **Strong Password** 🔒""")

password = st.text_input("Enter Your Password: ", type = "password")

instructions = []

score = 0

if password:
    if len(password) >= 9:
        score += 1
    else:
        instructions.append(" ❌ Password Should be at least 9 Characters Long")
    
    if re.search(r"[A-Z]", password) and re.search(r"[a-z]", password):
        score += 1
    else:
        instructions.append("❌ Password Should be contain both upper and lower case characters")
    
    if re.search(r"\d", password):
        score += 1
    else:
        instructions.append("❌ Password Should be contain at least oen digit")
    
    if re.search(r"[!@#$%&*]", password):
        score += 1
    else:
        instructions.append("❌ Password should contain at least one special character (!@#$%&*)")

    if score == 4:
        instructions.append("✅ Your Password is Strong!🎉")

    elif score == 3:
        instructions.append("🟡 Your Password is in Medium Strength. It could be stronger!")

    else:
        instructions.append("🔴 Your Password is weak. Please make it stronger!")

    if instructions:
        st.markdown("## Improvement Suggestions")
        for line in instructions:
            st.write(line)

else:
    st.info("Please Enter your password to get starting") 

