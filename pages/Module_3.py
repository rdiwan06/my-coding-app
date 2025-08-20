import streamlit as st
import random
import time as tm
st.set_page_config(page_title="Learn Python: Module 3", page_icon="🚀")

# Title
st.title("🚀 Learn to Code: Module 3 – For Loops")
st.markdown("Welcome back, space explorer! Today we’ll learn how to **repeat code** using for loops.")

# Section 1: Learning
st.header("👩‍🏫 1. Learn")
st.markdown("""
A **for loop** lets you repeat code multiple times.

Example:
```python
for i in range(5):
    print("Blast off in", i)
📝 What’s happening:

for i in range(5): → repeats the block of code 5 times

i takes values from 0, 1, 2, 3, 4

The code inside the loop runs once for each value of i

This is how computers can do repetitive tasks without you typing the same line over and over.
""")

st.subheader("🎥 Watch a Quick Explainer")
st.video("https://www.youtube.com/watch?v=KWgYha0clzw")

st.divider()

st.header("💻 2. Demo")
with st.expander("Show Demo Code"):
   st.code("""for i in range(3):
    print("Hello")""", language="python")
st.markdown("👉 This prints 'Hello, world!' three times.")

if st.button("▶️ Run Demo"):
    demo_output = "\n".join(["Hello, world!" for i in range(3)])
    st.text(demo_output)

st.divider()

st.header("✏️ 3. Try It Yourself!")
user_code3 = st.text_area("Write a for loop that prints the numbers from 1 to 5.")

if st.button("👾 Submit Code"):
    # Normalize input
    code = user_code3.lower().replace(" ", "").replace('"', "'")


    # Check conditions
    has_for = "for" in code and "inrange(1,6)" in code
    has_print = "print(i)" in code

    if has_for and has_print:
        st.balloons()
        st.success("Nice work! You wrote a for loop that counts from 1 to 5 🚀")
    else:
        st.error("Check your code – did you use a for loop with range(1,6) and print(i)?")

st.divider()

# Section 4: Interactive Coding Game
# Section 4: Interactive Coding Game
st.header("🎮 4. Coding Challenge Game!")

st.markdown("""
Welcome to the **Loop Builder Game!**
Your goal: Help the robot print all the stars ⭐ using a for loop.
""")
st.session_state.score = 0
# Keep track of score
if "score" not in st.session_state:
    st.session_state.score = 0

# Challenge 1
st.subheader("Level 1: Fill in the missing code")
st.markdown("Complete the loop so it prints stars ⭐ five times!")

code_guess = st.text_area("Your code:",
"""for i in _____:
    print("⭐")""")

if st.button("✅ Check Code"):
    code = code_guess.lower().replace(" ", "").replace('"', "'")
    has_for = "for" in code and "inrange(5)" in code
    has_print = "print('⭐')" in code or "print('star')" in code

    if has_for and has_print:
        st.success("🌟 Great job! You helped the robot collect 5 stars!")
        st.session_state.score += 1
        st.balloons()
        st.progress(100)
    else:
        st.error("Not quite! Make sure your loop uses `for i in range(5):` and prints a ⭐.")

# Show current score
st.markdown(f"**Your Score:** {st.session_state.score} ⭐")

st.divider()

st.subheader("Level 2: Build a Star Pyramid")
st.markdown(
    "Complete the code to build a pyramid of stars ⭐.\n\n"
   "Example for 5 rows:\n\n"
    "```\n"
    "    ⭐\n"
    "   ⭐⭐\n"
    "  ⭐⭐⭐\n"
    " ⭐⭐⭐⭐\n"
    "⭐⭐⭐⭐⭐\n"
    "Hint: Use a nested loop!"
)

pyramid_code = st.text_area("Your code:",
"""rows = 5
for i in range(1, _____):
    print('⭐' * i)""", key="level3")

if st.button("✅ Check Pyramid"):
    code = pyramid_code.lower().replace(" ", "").replace('"', "'")
    has_rows = "rows=5" in code
    has_for = "fori" in code and "inrange(1,6)" in code
    has_print = "print('⭐'*i)" in code or "print('star'*i)" in code

    if has_rows and has_for and has_print:
        st.success("🎉 Amazing! You built the star pyramid!")
        st.session_state.score += 1
        st.balloons()
        st.progress(100)
        
        # Show the pyramid visually
        st.markdown("Here’s your pyramid:")
        pyramid = ""
        for i in range(1, 6):
            pyramid += " " * (5 - i) + "⭐" * i + "\n"
        st.markdown(f"```\n{pyramid}```")
    else:
        st.error(
            "Not quite! Make sure you:\n"
            "- Set `rows = 5`\n"
            "- Loop with `for i in range(1, 6)`\n"
            "- Print stars multiplied by `i`"
        )

# Show current score
st.markdown(f"**Your Score:** {st.session_state.score} ⭐")

st.divider()
# Final feedback
if st.session_state.score >= 3:
    st.success("🎉 You beat the game! Amazing work with loops!")
