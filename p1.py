import google.generativeai as genai
API_KEY ="AIzaSyC7tXRQ9mF5aGF0x1CD9PDTPqHQHRWf-h4"
genai.configure(api_key = API_KEY)
model = genai.GenerativeModel("gemini-2.0-flash")
chat = model.start_chat()
print("Talk with AI .... Enter Quit to exit")
while True:
    user = input("you:")
    if user.lower() == "quit":
        break
    response =chat.send_message(user)
    print("Gemini:",response.text)