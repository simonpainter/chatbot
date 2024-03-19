import json
import os
from openai import OpenAI

client = OpenAI(api_key=os.environ["OPENAI_API_KEY"])

# Load API credentials from environment variables

# Load JSON data from file
json_file_path = "data.json"
with open(json_file_path, "r") as file:
    data = json.load(file)

def send_message(message, max_retries=3, backoff_factor=2):
    retries = 0
    while retries < max_retries:
        try:
            response = client.chat.completions.create(model="gpt-3.5-turbo",
            messages=[
                {
                    "role": "system",
                    "content": f"You are a helpful assistant that only answers questions related to the dog breeds provided in the following JSON data:\n\n{json.dumps(data)}\n\nIf the user asks a question that is not related to the dog breeds in the data, respond with 'I apologize, but I can only answer questions related to the dog breeds in my dataset. Please ask a question about the specific dog breeds I have information on.'"
                },
                {"role": "user", "content": message}
            ])
            return response.choices[0].message.content.strip()
        except openai.RateLimitError:
            retries += 1
            if retries < max_retries:
                wait_time = backoff_factor ** retries
                print(f"Rate limit exceeded. Retrying in {wait_time} seconds...")
                time.sleep(wait_time)
            else:
                raise

# Example usage
while True:
    user_input = input("User: ")
    if user_input.lower() in ["quit", "exit"]:
        break

    response = send_message(user_input)
    print(f"Assistant: {response}")