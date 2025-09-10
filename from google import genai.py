
from openai import OpenAI

client = OpenAI(
    api_key="AIzaSyANkQYKC3FruAyHCX2pniGynOaUVt7yAAI",
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
)

system_prompt = """
You are Prabhas, a soft-spoken, humble Indian actor known for your roles in epic action films like Baahubali and Salaar. You keep your answers grounded, calm, and respectful.

Examples:
input: "How was your experience working with director Prashanth Neel?"
output:"In my 21 years in the industry, I’ve never felt this level of connection with a director"
"""

response = client.chat.completions.create(
    model="gemini-2.5-flash",
    messages=[
        {"role": "system", "content": system_prompt},
        {
            "role": "user",
            "content": "how do you make good movies?"
        }
    ]
)

print(response.choices[0].message.content)
