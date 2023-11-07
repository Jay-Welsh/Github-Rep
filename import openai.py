import openai

# Set your API key (replace 'key' with your actual API key)
openai.api_key = "('YOUR_API_KEY')"

# Define a function for basic text generation
def BasicGeneration(userPrompt):
    completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
              {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": userPrompt}
    ]
 )
    return completion.choices[0].message.content

# Define the prompt
prompt = "explain python programming in 2 sentences"

# Generate a response using your function
response = BasicGeneration(prompt)

# Print the response
print(response)