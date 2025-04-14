import streamlit as st

st.set_page_config(page_title="multilingual virtual assistant")

st.markdown("<h3 style='text-align: center; color:BLUE;'>multilingual tasky!!!🤩</h3>",unsafe_allow_html=True)

help_1, help_2 = st.columns(2)
with help_1:
    with st.expander("ABOUT APP"):
        st.markdown('''
        - A simple translator which supports 85 lamguages
        - Type in the user input box to initiate the bot.
        - search for your language from the dropdown menu
        - The available text is converted to its translated language 
        - you can also listen to the audio and download it.
        - A simple ChatBot example using Python Streamlit Framework.
        - No Chatbot module OR library used. Q&A is handled through dictionary of Questions and Answers.  
        - This is just a proof of concept with regards to building a chatbot without any additional module so might not anwser all questions.
        
        - Type exit or quit in the user input box to terminate the bot.
        ''')

with help_2:
    with st.expander("Thanks to"):
        st.markdown('''
        - TNCpl :https://www.guvi.in/mlp/tncpl
        - Naan mudhalvan : https://portal.naanmudhalvan.tn.gov.in/login
        - Anna University : https://www.annauniv.edu/        
        - guvi : https://www.guvi.in/
        ''')


st.markdown("""
<style>
     [data-testid=stSidebar] {
             background-color: #00008b    
     }
</style>
""",unsafe_allow_html=True)
