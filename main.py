import streamlit as st
st.title('Storybook Creator')
st.markdown("Welcome to the story book creator, a place where AI technology can make any person on the planet the main character! Don't believe me? Give it a shot for yourself!")

with st.form.expander('Story elements Form'):
        options = ['Initial story Elements','AI Story Builder', 'Build Summary', 'Download Story']
        radio_cols = st.columns([.25,10])
        step = radio_cols[1].radio(label='', label_visibility='collapsed', options=options, horizontal=True, index=0)
        if step == 'Initial story Elements':
                st.markdown("Let's get started, please fill out the following fields:")
                'upload a pciture of a loved one here:'
                uploaded_img = st.file_uploader("Upload a picture of the person/pet you'd like on a card, board, or coloring page", type=['png', 'jpg', 'jpeg', 'gif'])
                if uploaded_img is not None:
                        from PIL import Image
                        image = Image.open(uploaded_img)
                else:
                        st.warning('Please upload at least one image of your loved one')
                lmnt_cols = st.columns(2)
                with lmnt_cols[0]:
                        name_of_loved = st.text_input('Name of loved one')
                        genre = st.selectbox(
                        "Choose the Genre:",
                        options=["Adventure", "Fairy Tale", "Animal Story", "Space Exploration", "Magical Fantasy", "surprise me"]
                )
                        supporting_character = st.selectbox(
                        "Choose A Supporting Character:",
                        options=["Wise Owl", "Funny Clown", "Talking Robot", "Friendly Dragon", "Mischievous Monkey", "surprise me"],
                )
                        theme = st.selectbox(
                        "Choose the Theme:",
                        options=["Friendship", "Courage", "Kindness", "Discovery", "Teamwork", "surprise me"]
                )
                        tone = st.selectbox(
                        "Choose the Tone/Mood:",
                        options=["Joyful", "Exciting", "Mysterious", "Playful", "Heartwarming", "surprise me"]
                )
                with lmnt_cols[1]:
                        relation = st.text_input('Relation to loved one')
                        setting = st.selectbox(
                        "Choose the Setting:",
                        options=["Enchanted Forest", "Outer Space", "Kingdom", "Under the Sea", "Mystical Mountain", "surprise me"]
                )
                        plot_elements = st.selectbox(
                        "Choose Plot Elements:",
                        options=["A Hidden Treasure", "A Grand Festival", "A Magic Spell", "A Daring Rescue", "A Secret Door", "surprise me"]
                )
                        magical_objects = st.selectbox(
                        "Choose Magical Objects:",
                        options=["Magic Wand", "Enchanted Mirror", "Golden Key", "Flying Carpet", "Invisible Cloak", "surprise me"]
                )
                        
        submitted = st.form_submit_button('Pull Initial Elements')
        if submitted:
                st.write(f"I'd like you to create a story about my {relation}, {name_of_loved}. The story's Genre will be: {genre}, with a setting as: {setting}. A supporting character will be: {supporting_character}, with a plot element of: {plot_elements}. The theme of the story is: {theme}, a magical object, included somewhere in the story is a: {magical_objects}, and the tone will be: {tone} ")
        if step == 'AI Story Builder':
                st.write('ai chat will receive the elements inputs')

#'AI Story Builder', 'Build Summary', 'Download Story'
