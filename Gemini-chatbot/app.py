# libraries
import streamlit as st
import google.generativeai as genai
import os
from dotenv import load_dotenv  # Correct import statement

# Load environment variables from .env file
load_dotenv()

# Access the API key from environment variables
GOOGLE_API_KEY = os.getenv('GOOGLE_API_KEY')

# GOOGLE_API_KEY = "AIzaSyCNGgh3q7Nkh0Oa0_G-QR87qhGJJqXTcVQ"

# Google_API configuration
if GOOGLE_API_KEY:
    genai.configure(api_key=GOOGLE_API_KEY)
else:
    st.error("API key not found. Please set your GOOGLE_API_KEY in the environment variables.")

# initialize generative AI model
# Ensure the model is initialized correctly after the API key is configured
def get_model():
    try:
        return genai.GenerativeModel('gemini-1.5-flash')
    except Exception as e:
        st.error(f"Error initializing the model: {e}")
        return None

model = get_model()

# function to get response from model
def get_response(prompt):
    if model:
        try:
            response = model.generate_content(prompt)
            return response.text
        except Exception as e:
            st.error(f"Error generating response: {e}")
            return "Sorry, I couldn't process that."
    else:
        return "Model is not initialized."

# streamlit interface
st.set_page_config(page_title="Simple ChatBot!", layout='centered')
st.title("Simple Chatbot 🤖")
st.write("Powered by Muhammad Jawad.")

# Initialize session state for chat history if not present
if "history" not in st.session_state:
    st.session_state["history"] = []

with st.form(key="chat-form", clear_on_submit=True):
    # prompt input text using streamlit
    prompt = st.text_input("", max_chars=2000)
    # send button
    submit_button = st.form_submit_button("Send")
    # condition if text_input is not empty
    if submit_button:
        if prompt:
            response = get_response(prompt)
            # append conversation to chat history
            st.session_state.history.append((prompt, response))
        else:
            st.warning("Please enter a prompt.")

# display chat history
for user_msg, bot_msg in st.session_state.history:
    st.markdown(f"""
                <div style="
                    background-color: #d1d3e0;
                    border-radius: 15px;    
                    padding: 10px 15px;
                    margin: 5px 0;
                    max-width: 70%;
                    text-align: left;
                    display: inline-block;
                    color:black;
                ">
                <p style="margin:0; font-size: 16px; line-height: 1.5"><b>You: </b>{user_msg}</p>
                </div>
                """, unsafe_allow_html=True)
    
    st.markdown(f"""
                <div style="
                    background-color: #e1ffc7;
                    border-radius: 15px;
                    padding: 10px 15px;
                    margin: 5px 0;
                    max-width: 70%;
                    text-align: left;
                    display: inline-block;
                    color: black;
                ">
                <p style="margin:0; font-size: 16px; line-height: 1.5"><b>Bot: </b>{bot_msg}</p>
                </div>
                """, unsafe_allow_html=True)

# prompt = input("Enter your prompt = ")
# output = get_response(prompt)
# print(output)
