import streamlit as st

def demo_DS():
    st.header("Trial Data Science")
    st.markdown("""
    Try out my little project of Data Science for the prime number
    """)
    #st.subheader("Predict if this number is prime")
    number = st.number_input("Enter the number:", value=0)
    if number <= 1:
        st.warning("This number is **Not Prime**")
    else:
        for i in range (2,number):
            if number % i == 0:
                st.warning("This number is **Not Prime**")
        else:
            st.success("This number is **Prime**")