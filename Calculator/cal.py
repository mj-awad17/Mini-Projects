import streamlit as st

def main():
    st.title("Calculator 🧮")
    
    # input fields
    num1 = st.number_input("Enter first number", min_value=None, max_value=None, value=0.0)
    num2 = st.number_input("Enter second number", min_value=None, max_value=None, value=0.0)
    
    # operations using selectbox
    operations = st.selectbox("Select Operation:", ["Addition", "Subtraction", "Multiplication", "Division","Exponent"])
    
    # performing operations
    if operations == "Addition":
        result = num1 + num2
    elif operations == "Subtraction":
        result = num1 - num2
    elif operations == "Multiplication":
        result = num1 * num2
    elif operations == "Division":
        if num2 != 0:
            result = num1 / num2
        else:
            result = "Error: Division by zero is not allowed"
    elif operations == "Exponent":
        result = num1 ** num2
    # display the result
    st.write("Result:", result)
    
if __name__ == "__main__":
    main()