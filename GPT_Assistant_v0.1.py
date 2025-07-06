import openai
openai.api_key="your-api-key-here"
def chat_with_gpt(prompt):
    response=openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
        {
            "role": "system","content": "you are AI Assistant",
            "role": "user","content": "prompt"
        }
        ]
            
     )
    return response["choices"][0]["message"]["content"]
prompt=input("Ask your AI Assistant:")
print(chat_with_gpt(prompt))