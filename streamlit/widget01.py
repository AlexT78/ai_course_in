import streamlit as st
import pandas as pd

#text input widget, always use it as variable
name = st.text_input('your name')
if name:
    st.write(f'hello {name}')

#number input
x = st.number_input('numba', min_value= 1, max_value=99, step=1)
st.write(f'the current number is {x}')

st.divider()

#button > if user click the button, return True
clicked = st.button('test')

if clicked:
    st.write(":ghost:" *2)


st.divider()


#checkbox > return true if checked like the button
agree = st.checkbox("i agree")

if agree:
    'great, you are doomed'

checked = st.checkbox("continue", value=True) # the checkbox will be checked by default
if checked:
    ':+1:'*5

df = pd.DataFrame({'name':['anne', 'mario', 'douglas'],
                   'age': [20,23,24]
                   })
if st.checkbox('show data'):
    st.write(df)
st.divider()

#radio button
pets = ["cat", "dog", "fish"]
pet = st.radio("animals", pets, index = 2, key = "your_pet") #will select fish by default in the list
st.write(f'your favorite pet: {pet}')
st.write(f"your fav pet: {st.session_state.your_pet}") #using the key argument on the "pet"

st.divider()

#select
cities = ["london", "berlin", "paris", "madrid"]
city = st.selectbox("your city", cities, index = 2)
st.write(f'you live in {city}')


#slider
y = st.slider("y", value=50, min_value =30, max_value=200, step =10)
st.write(f" y: {y}")

st.divider()

#file uploader
uploaded_file = st.file_uploader("upload file", type = ["txt", "csv", "xlsx"])

if uploaded_file:
    st.write(uploaded_file)
    if uploaded_file.type == "text/plain":
        from io import StringIO
        stringio = StringIO(uploaded_file.getvalue().decode("utf-8"))
        string_data= stringio.read()
        st.write(string_data)
    elif uploaded_file.type == "text/csv":
        import pandas as pd
        df = pd.read_csv(uploaded_file)
        st.write(df)
    else:
        import pandas as pd
        df = pd.read_excel(uploaded_file)
        st.write(df)

st.divider()

#camera input

camera_photo = st.camera_input('take a photo')
if camera_photo:
    st.image(camera_photo)


if st.checkbox("hmmm"):
    st.image('00-026.png')
