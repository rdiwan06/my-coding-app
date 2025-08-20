import streamlit as st
st.subheader("Module 4: If/Else Statements for Beginners")

# --------------------
# Explanation Section
# --------------------
st.markdown("""
### 🧠 Understanding If/Else Statements in Python

**What Are Conditional Statements?**

Conditional statements let your program **make decisions**. Think of it like a fork in the road: depending on the sign, you go left or right.

**The Basics: `if`, `elif`, and `else`**
- `if`: Asks a question. If the answer is "yes" (True), it does something.
- `elif`: Short for "else if". If the first condition was "no", it asks another question.
- `else`: If all previous questions were "no", it does something else.

**Example:**
```python
age = 12

if age >= 13:
    print("You're a teenager!")
elif age >= 6:
    print("You're a child!")
else:
    print("You're a toddler!")
Visualizing the Flow:
This chart shows how the program checks each condition in order and executes the corresponding block of code.
""")

st.image("https://www.tutorialspoint.com/python/images/if_else_statement.jpg", caption="If/Else Flowchart")

st.markdown("""
Real-Life Analogy:
Imagine you're deciding what to wear based on the weather:

If it's raining, wear a raincoat.

If it's sunny, wear sunglasses.

Otherwise, wear a regular jacket.

This is exactly what if, elif, and else do in programming.
""")

st.markdown("### 🎥 Watch and Learn")
st.video("https://www.youtube.com/watch?v=-BOBedcjySI")

st.markdown("""🧪 Try It Yourself: Fill in the blanks and enter any number to test your conditional logic!
""")

code_guess = st.text_area(
"Fill in the blanks for the if and elif conditions: ",
"""if _____:
print('Positive')
elif _____:
print('Negative')
else:
print('Zero')"""
)

user_number = st.number_input("Enter a number:", value=0)

if st.button("✅ Check Code"):
    code = code_guess.replace(" ", "")
    if ">" in code and "<" in code:
        st.success("🎉 Correct! Your conditional logic works!")
# Dynamically run the logic on the number they entered
    if user_number > 0:
        st.write("Output:", "Positive")
    elif user_number < 0:
        st.write("Output:", "Negative")
    elif user_number == 0:
        st.write("Output:", "Zero")
    else:
        st.error("❌ Not quite. Make sure your conditions check for positive and negative numbers correctly.")

