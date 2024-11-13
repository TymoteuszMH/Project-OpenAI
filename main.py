from openai import OpenAI
from key import api_key
import os

os.environ["OPENAI_API_KEY"] = api_key

def main():
    client = OpenAI(api_key=os.environ.get("OPENAI_API_KEY"))
    file = open("artykul.txt", 'r')

    message = f"Please refactor this text using HTML tags, only as content within <body> tag (but do not use <body> tag itself). Make sure that all letters will be correct in Polish alphabet and UTF-8 encoding. Paste images with <img src='placeholder.jpg' alt='alt-text'> where you think it suitable. Do not use css nor js. Do not use block code as response. Text: {file.read()}"
    # print(message)
    response = client.chat.completions.create(
        messages=[{
            "role": "user",
            "content": message,
        }],
        model="gpt-4o-mini",
    )

    file.close()

    # print(response.choices[0].message.content)
    art = open('artykul.html', 'w', encoding='utf-8')
    art.write(response.choices[0].message.content)
    art.close()

    print("file created!")

if __name__ == "__main__":
    main()