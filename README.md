# My Gemini API Console Chatbot

## 📜 Project Description

This project is a simple, interactive console application that demonstrates how to use the **Google Gemini API** to create a conversational chatbot. It serves as a foundational example for anyone looking to integrate the Gemini model into their own command-line tools or scripts.

The chatbot maintains context throughout the conversation, allowing for a natural and continuous dialogue.

## ✨ Features

- **Interactive Console Interface:** A command-line interface for real-time conversation.
- **Persistent Chat Context:** The chat history is maintained, allowing the Gemini model to provide context-aware responses.
- **Easy-to-Understand Code:** A simple and clean Python script, perfect for beginners.
- **Secure API Key Management:** Uses environment variables to securely handle the API key, preventing exposure in the code.

## ⚙️ Prerequisites

Before you get started, make sure you have the following:

- **Python 3.x**
- An **API Key** from Google's Gemini API.

## 🛠️ Installation & Setup

1.  **Clone the repository:**
    ```bash
    git clone [https://github.com/your-username/your-repository-name.git](https://github.com/your-username/your-repository-name.git)
    cd your-repository-name
    ```
2.  **Install the required dependencies:**
    ```bash
    pip install -r requirements.txt
    ```
3.  **Set up your API Key:**
    - The project uses an environment variable for the API key.
    - On Windows, use:
      ```bash
      set GEMINI_API_KEY="YOUR_API_KEY_HERE"
      ```
    - On macOS/Linux, use:
      ```bash
      export GEMINI_API_KEY="YOUR_API_KEY_HERE"
      ```
      Replace `YOUR_API_KEY_HERE` with your actual key.

## 🚀 Usage

To run the chatbot, simply execute the main script from your terminal:

```bash
python p1.py
Type your message and press Enter. To exit the chat, type quit.
