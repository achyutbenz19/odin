from routellm.controller import Controller

def stream_response():
    client = Controller(
        routers=["mf"],
        strong_model="gpt-4-1106-preview",
        weak_model="groq/llama3-8b-8192",
        progress_bar=True,
    )

    response = client.chat.completions.create(
        model="router-mf-0.11593",
        messages=[{"role": "user", "content": """hey"""}],
        stream=True,
        temperature=0
    )

    for i, chunk in enumerate(response):
        if i == 0:
            model_prefix = f"[{chunk.model}]\n"
            yield model_prefix

        content = chunk.choices[0].delta.content
        if content:
            yield content

for token in stream_response():
    print(token, end='', flush=True)