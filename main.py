import streamlit as st
st.title('Storybook Creator')
st.markdown("Welcome to the story book creator, a place where AI technology can make any person on the planet the main character! Don't believe me? Give it a shot for yourself!")
"---"
tab_INI, tab_AI, tab_BS, tab_DS = st.tabs(["Initial Story Elements", "AI Story Builder", "Build Summary", "Download Story"])

with tab_INI:
        with st.form('Story elements Form'):
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
                        
                submitted_elements = st.form_submit_button('Pull Initial Elements')
#Will need to update this data dump instead to an ai
                if submitted_elements:
                        st.success("We've collected and submitted the information you provided, pop over to the next tab (AI Story builder) to see the AI at work!")
                        with tab_AI: st.write(f"I'd like you to create a story about my {relation}, {name_of_loved}. The story's Genre will be: {genre}, with a setting as: {setting}. A supporting character will be: {supporting_character}, with a plot element of: {plot_elements}. The theme of the story is: {theme}, a magical object, included somewhere in the story is a: {magical_objects}, and the tone will be: {tone} ")
                        with tab_AI: st.image
with tab_AI:
        st.write('ai chat will receive the elements inputs')

with tab_BS:
        col_PGodd, col_PGeven = st.columns(2)
        st.write("Your story book's title:")
        st.title('Title placeholder')
        '---'
        st.write("Your storybook's narrative and pages in order:")
        '---'
        st.subheader("Related data")
        '---'
        "---"
        with col1:
            st.write("stuff in 1")
        with col2:
            val = st.slider('slider in col 2', 1, 50)
        st.markdown(f'<div style="text-align: center">Very long winded way of saying value is: {val}</div>', unsafe_allow_html=True)
        st.markdown('----')
        
        st.write('post')

#'AI Story Builder', 'Build Summary', 'Download Story'
