import streamlit as st

st.title("Build Your Own Adventure Project")
st.markdown("""
Welcome! In this module, you'll **build your own text-based adventure game**.
Follow the instructions, write your code in the window below, and use hints if you get stuck.
You'll combine **input/output, if/else statements, for loops, and while loops** to create your game.
""")

# --------------------
# Instructions
# --------------------
st.subheader("General Instructions")
st.markdown("""
1. Use `input()` to get choices from the player.
2. Use `print()` to describe scenes and outcomes.
3. Use `if/elif/else` to handle decisions.
4. Use `for` loops for repeating actions like collecting items.
5. Use `while` loops for challenges until the player succeeds.
6. Start small and build your game step by step.
7. Use the **Show Hint** button if you get stuck (10 hints are available).
""")

# --------------------
# Coding Window
# --------------------
st.subheader("Your Coding Window")
user_code = st.text_area("Type your adventure game code here:", height=400)

# --------------------
# Hint System
# --------------------
if 'hint_counter' not in st.session_state:
    st.session_state.hint_counter = 0

hints = [
    "Step 1: Get the player's name: player_name = input('Enter your name: ')",
    "Step 2: Greet the player using print(): print(f'Welcome {player_name}!')",
    "Step 3: Ask for first choice: choice1 = input('Go left or right? ').lower()",
    "Step 4: Conditional logic: if choice1 == 'left': ... elif choice1 == 'right': ... else: ...",
    "Step 5: For loop to collect 3 items: for i in range(3): item = input('Enter item: ')",
    "Step 6: While loop challenge: guess = 0; while guess != secret_number: guess = int(input(...))",
    "Step 7: Reward message: print('You guessed it!')",
    "Step 8: Final decision: final_choice = input('Take treasure or leave it? ').lower(); if final_choice == 'take': ...",
    "Step 9: Loop through collected items: for item in collected_items: print(item)",
    "Step 10: Ending message: print(f'Thanks for playing, {player_name}!')"
]

if st.button("Show Hint"):
    if st.session_state.hint_counter < len(hints):
        st.info(hints[st.session_state.hint_counter])
        st.session_state.hint_counter += 1
    else:
        st.warning("No more hints available!")

# --------------------
# Run User Code
# --------------------
if st.button("✅ Run Your Game"):
    try:
        # Replace input() calls in user code with st.text_input equivalents
        safe_code = user_code.replace("input(", "st.text_input(")
        local_namespace = {"st": st}
        exec(safe_code, {}, local_namespace)
    except Exception as e:
        st.error(f"Error in your code: {e}")
st.markdown("""
### Tips:
- Replace placeholders or blanks in your code with actual logic.
- Start with small sections and test frequently.
- Use hints to guide you but try to code as much as you can yourself.
- Have fun and be creative with your adventure story!
""")
