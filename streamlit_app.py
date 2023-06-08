import streamlit as st


st.title('🦜🔗 My Web App')


with st.sidebar:
    text = st.text_input('Paste something here:')
    st.success(text)

with st.form('my_form'):
  
    text2 = st.text_area('Enter text prompt:', 'What is the meaning of life the universe and everything?')
    submitted = st.form_submit_button('Submit')

    if submitted :
        st.info(text2)

# streamlit run streamlit_app.py