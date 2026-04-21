import streamlit as st

st.set_page_config(page_title="Calculator", layout="centered")

# Custom CSS
st.markdown("""
<style>
.main {
    background-color: #0E1117;
}
.title {
    text-align: center;
    color: #ff;
    font-size: 40px;
    font-weight: bold;
}
.result-box {
    background-color: #1c1f26;
    padding: 15px;
    border-radius: 10px;
    color:White;
    text-align: center;
    font-size: 20px;
}
</style>
""", unsafe_allow_html=True)

# Title
st.markdown('<div class="title"> Simple Calculator</div>', unsafe_allow_html=True)

# Inputs
col1, col2 = st.columns(2)

with col1:
    first_number = st.number_input("Enter first number")

with col2:
    second_number = st.number_input("Enter second number")

operators = st.selectbox("Select operator", ["+", "-", "//", "%", "*"])

# Button
if st.button("Calculate"):
    try:
        if operators == "+":
            result = first_number + second_number
        elif operators == "-":
            result = first_number - second_number
        elif operators == "//":
            result = first_number // second_number
        elif operators == "%":
            result = first_number % second_number
        elif operators == "*":
            result = first_number * second_number

        st.markdown(f'<div class="result-box">Result: {result}</div>', unsafe_allow_html=True)

    except:
        st.error("Error in calculation")
