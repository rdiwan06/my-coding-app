import streamlit as st
st.title("👋 Welcome to Learn to Code!")
#st.markdown("Click a module on the left sidebar to get started!")

# Set the page config
st.set_page_config(page_title="Learn Python: Module 1", page_icon="👾")

# Title and welcome
st.title("👾 Learn to Code: Module 1 – Intro to Python")
st.markdown("Welcome, young coder! Today we’ll learn how to print a message in Python.")

# Section 1: Learning
st.header("👩‍🏫 1. Learn")
st.markdown("""
Python is a popular and easy-to-read programming language.

Let’s look at the most basic command: `print()`.

Rules to remember:
1. Use print() to make the computer talk
2. Put text inside double quotes "like this"
3. Always use parentheses after print

### 👇 This tells the computer to say something.
```python
print("Hello, world!")""")
st.image("https://media.giphy.com/media/3o7qE1YN7aBOFPRw8E/giphy.gif", caption="👽 Hello from your alien friend!")

st.divider()

st.header("💻 2. Demo")
st.markdown("Here’s how the code works:")

with st.expander("Show Python Code"):
    st.code('print("Hello, world!")')

if st.button("▶️ Run Demo"):
    st.success("Output: Hello, world! 👽")

st.divider()

st.header("✏️ 3. Try It Yourself!")
st.markdown("Type the code below and see if you can get it right!")

user_code = st.text_area("Your code goes here:", height=100)

if st.button("🚀 Submit Code"):
# Clean and check user input
    cleaned_code = user_code.strip()
    correct_code = 'print("Hello, world!")'

    if cleaned_code == correct_code:
        st.balloons()
        st.success("Woohoo! You printed your first message. Great job! 👾")
    else:
        st.error("Hmm... that's not quite right. Try again! Hint: Make sure everything matches exactly, including the quotes.")
    
    
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
    if ('input("What’s your name?")' in user_code2 or 'input("What’s your name? ")' in user_code2 or 'input( "What’s your name?  ")' in user_code2) and 'print("Hello, " + name)' in user_code2.replace("'", '"'):
        st.balloons()
        st.success("Amazing work! You used input and print like a pro! 🧠")
    else:
        st.error("Check your code – did you ask for a name and say hello?")

st.divider()
