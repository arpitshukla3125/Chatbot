import requests

# Replace with your actual API key and endpoint
API_KEY = 'your_api_key_here'
API_URL = 'https://api.openai.com/v1/chat/completions'

def get_chatbot_response(user_message):
    headers = {
        'Authorization': f'Bearer {API_KEY}',
        'Content-Type': 'application/json'
    }
    
    payload = {
        'model': 'gpt-3.5-turbo',  # or another model of your choice
        'messages': [{'role': 'user', 'content': user_message}]
    }
    
    response = requests.post(API_URL, headers=headers, json=payload)
    
    if response.status_code == 200:
        reply = response.json()
        return reply['choices'][0]['message']['content']
    else:
        return f"Error: {response.status_code}, {response.text}"

def main():
    print("Welcome to the chatbot! Type 'exit' to end the conversation.")
    
    while True:
        user_input = input("You: ")
        if user_input.lower() == 'exit':
            break
        response = get_chatbot_response(user_input)
        print(f"Chatbot: {response}")

if __name__ == "__main__":
    main()
