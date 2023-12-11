import streamlit as st

st.write('Hello fools!')

with st.form('Story_form'):
    with st.expander('',expander=True):

    options = ['Initial story Elements','AI Story Builder', 'Build out Summary', 'download']
    radio_cols = st.columns([.25,10])
    step = radio_cols[1].radio(label='', label_visibility='collapsed', options=options, horizontal=True, index=0)
    if step == 'Initial story Elements':
      st.markdown("Let's get started, please fill out the following fields:")
      lmnt_cols = st.columns(2)
      lmnt_cols[0].text_input('relation')
      lmnt_cols[1].text_input('Name')

      submitted = st.form_submit_button('Pull Elements')



# def Elements_pool():
#   st.file_uploader(), st.file_uploader()

