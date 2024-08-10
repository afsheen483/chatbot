import google.generativeai as genai
import streamlit as st

# Configure the Google API key
GOOGLE_API_KEY = ""
genai.configure(api_key=GOOGLE_API_KEY)

# Initialize the generative model
model = genai.GenerativeModel('gemini-1.5-flash')

# Function to get response from the model
def get_response_from_model(user_input):
    response = model.generate_content(user_input)
    return response.text

# Streamlit app
st.title("First Chatbot")
st.write("This chatbot uses Google's Generative AI API.")

# Create a text input field for the user prompt
user_input = st.text_input("Enter your prompt:")

# If the user enters a prompt, generate the response
if user_input:
    output = get_response_from_model(user_input)
    st.write("Response from the model:")
    st.write(output)


