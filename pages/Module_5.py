import streamlit as st

st.subheader("Module 5: While Loops")
st.markdown("""
### 🧠 Understanding While Loops in Python

**What is a While Loop?**

A `while` loop lets your program **repeat an action multiple times** until a condition is no longer true. Think of it like a game that keeps going until you lose all your lives.

**The Basics:**
```python
i = 1
while i <= 5:
    print(i)
    i += 1
i = 1 → start counter

while i <= 5: → keeps looping as long as the condition is True

i += 1 → increases the counter so the loop eventually stops
""")

st.markdown("Real-Life Analogy:")
st.markdown("""
Imagine you are stacking blocks. You keep adding blocks while you still have blocks left in your pile. Once your pile is empty, you stop.
""")

st.markdown("### 🎥 Watch and Learn")
st.video("https://www.youtube.com/watch?v=6iF8Xb7Z3wQ") # Example Python while loop video

st.markdown("""

🧪 Try It Yourself
Fill in the blanks to make the loop print ⭐ five times!
""")

#--------------------
#Interactive Try-It-Yourself Section
#--------------------

code_guess = st.text_area(
"Fill in the blanks for the while loop:",
"""i = 1
while _____:
print('⭐')
i += 1""")

#user_count = st.number_input("Enter how many stars to print:", value=5, min_value=1)

if st.button("✅ Check Code"):
    code = code_guess.replace(" ", "")
    
    if "<=" in code or "<" in code:  # ✅ Now inside the button block
        st.success("🎉 Correct! Your while loop prints stars dynamically.")
        # Dynamically show stars
        st.code('\n'.join(['⭐']*5))
    else:
        st.error("❌ Not quite. Make sure your while loop has a proper condition (like i <= 5).")
