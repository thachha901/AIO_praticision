import streamlit as st 
import hugchat
from hugchat.login import Login


def generate_response(prompt_in, email, password):
    #Login
    sign = Login(email, password)
    cookies = sign.login()
    
    # Create chatbot
    chatbot = hugchat.Chatbot(cookies=cookies.get_dict())
    
    return chatbot.chat(prompt_in)

if __name__ == "__main__":
    st.title('Chatbot')
    
    with st.sidebar:
        st.title('HuggingFace Login')
        email = st.text_input('Email')
        password = st.text_input('Password', type = 'password')
        
    if 'messages' not in st.session_state.keys():
        st.session_state.messages = [{'role': 'assistant', 'content': 'How may I help you ?'}]
    
    for message in st.session_state.messages:
        with st.chat_message(message['role']):
            st.write(message['content'])
            
    if prompt := st.chat_input(disabled = not(email and password)):
        st.session_state.messages.append({'role': 'user', 'content': prompt})
        with st.chat_message('user'):
            st.write(prompt)
            
    if st.session_state.messages[-1]['role'] != 'assistant':
        with st.chat_message('assistant'):
            with st.spinner('Thinking...'):
                response = generate_response(prompt, email, password)
                st.write(response)
        
        message = {'role': 'assistant', 'content': response}
        st.session_state.messages.append(message)
    