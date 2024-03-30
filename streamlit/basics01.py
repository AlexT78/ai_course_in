import streamlit as st
import pandas as pd

st.title('hello streamlit word :100:')

#display data on the screen:
#1. st.write()
#2. Magic

st.write("hello there+")


l1 = [1,2,3, "bob"]
st.write(l1)


l2 = list("abc")
d1 = dict(zip(l1,l2))
st.write(d1)

# using magic

'Displaying using magic :smile:'

df = pd.DataFrame({
    'first_column': [1,2,3],
    'second_column': [432,5,3]
})

df #would be the same if st.write(df)