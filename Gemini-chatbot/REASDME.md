# Simple Chatbot using Streamlit and Google Generative AI

👉 [Demo](https://mini-projects-gemini-chatbot.streamlit.app/)

This project is a simple chatbot application built with Streamlit, powered by Google’s Generative AI. Users can interact with the chatbot by entering prompts, and the bot will respond based on the input. The application is designed for ease of use and provides a straightforward interface for users to communicate with the AI model.

### Features
**Chat Interface:** Users can send messages and receive responses in real-time.
**Session History:** The conversation history is maintained throughout the session, allowing users to refer back to previous messages.
**Environment Variable Configuration:** The application uses environment variables to securely manage the API key.

### Requirements
To run this application, you will need the following:

- Python 3.x
- Streamlit
- Google Generative AI library (google.generativeai)
- python-dotenv

You can install the required libraries using pip:

```
pip install streamlit google-generativeai python-dotenv
```

### Setting Up the Environment
1. Create a .env File: In the root directory of your project, create a file named .env and add your Google API key as follows:
```
env
GOOGLE_API_KEY=your_google_api_key_here
```
2. Replace your_google_api_key_here with your actual Google API key.

### How to Run the App
1. Clone this repository or download the script.
2. Navigate to the directory where the script is located.
3. Run the following command in your terminal:

```
streamlit run app.py
```
4. Open your web browser and go to http://localhost:8501 to access the chatbot.

### Usage Instructions
1. Enter your prompt in the text input field.
2. Click the "Send" button to submit your message.
3. The chatbot will respond with an answer, which will be displayed below your message.
4. You can continue the conversation by entering new prompts.

### Troubleshooting
If you encounter any issues, please ensure that:

- You have installed all required libraries.
- Your API key is set correctly in the .env file.
If the issue persists, check the error message displayed in the app for more information.

---

## 🔗 More Projects

Check out more of my projects on GitHub:

- 🤖 [Gemini Chatbot](https://github.com/mj-awad17/Mini-Projects/tree/main/Gemini-chatbot)
- 🖼️ [BGRemover](https://github.com/mj-awad17/Mini-Projects/tree/main/Remove-background)
- 🧮 [Calculator](https://github.com/mj-awad17/Mini-Projects/tree/main/Calculator)

## 👨‍💼 Connect with Me
- 🌐 [LinkedIn](https://www.linkedin.com/in/muhammad-jawad-86507b201/)
