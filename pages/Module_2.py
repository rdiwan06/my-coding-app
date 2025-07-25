import streamlit as st
st.set_page_config(page_title="Learn Python: Module 2", page_icon="👾")

# Title and welcome
st.title("👾 Learn to Code: Module 2 – Python Inputs")
st.markdown("Welcome, young coder! Today we’ll learn how to prompt for user input in python!")

# Section 1: Learning
st.header("👩‍🏫 1. Learn")
st.markdown("""
To ask someone for input, we use the **`input()`** function.

Here’s how it works:
```python
name = input("What’s your name? ")
print("Hello, " + name)
📝 What’s happening:

input() asks a question

The answer is stored in a variable like name

print() uses that name to greet the user
""")
st.image("https://media.giphy.com/media/3ohzdQ1IynzclJldUQ/giphy.gif", caption="The alien wants to know your name! 👽")

st.divider()

st.header("💻 2. Demo")
with st.expander("Show Demo Code"):
    st.code('name = input("What’s your name? ")\nprint("Hello, " + name)', language="python")

name_input = st.text_input("Simulate input: What’s your name?")
if name_input:
    st.success(f'👋 Hello, {name_input}!')

st.divider()

st.header("✏️ 3. Try It Yourself!")
user_code2 = st.text_area("Write the code to ask a name and print a greeting.")

if st.button("👾 Submit Code"):
    # Normalize code formatting
    code = user_code2.lower()
    code = code.replace("’", "'").replace("“", '"').replace("”", '"')
    code = code.replace('"', "'")  # convert double quotes to single for matching
    code = " ".join(code.split())  # remove extra spaces

    # Check for input() asking for name
    has_input = "input(" in code and "name" in code

    # Check for print greeting using + and hello
    has_print = "print(" in code and "'hello" in code and "+" in code

    if has_input and has_print:
        st.balloons()
        st.success("🎉 Amazing work! You used input and print like a pro!")
    else:
        st.error("⚠️ Oops! Try again. Make sure you're using both `input()` and `print()` to ask for and greet the user.")

st.divider()

