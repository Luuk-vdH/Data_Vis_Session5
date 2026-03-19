import streamlit as st

st.title("Counter App")

# Initialize session state
if "count" not in st.session_state:
    st.session_state.count = 0

# Input box for step size (Extra 3)
step = st.number_input("Enter a number (X)", min_value=1, value=1, step=1)

# Show current count
st.write(f"### Current count: {st.session_state.count}")

# Buttons side by side
col1, col2, col3 = st.columns(3)

with col1:
    if st.button("Increase"):
        st.session_state.count += step

with col2:
    if st.button("Decrease"):
        st.session_state.count -= step

with col3:
    if st.button("Reset"):
        st.session_state.count = 0

# Show updated count
st.write(f"### Updated count: {st.session_state.count}")

# Extra 2: special message when count reaches 10
if st.session_state.count == 10:
    st.success("🎉 Special message: The counter reached 10!")
