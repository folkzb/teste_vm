import openai

openai.api_key = "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"

resposta= openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[
            {"role" : "user", "content": "quem foi floriano peixoto?"}
    ]
)

print(resposta["choices"][0]["message"]["content"])


