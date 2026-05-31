from openai import AsyncOpenAI

client = AsyncOpenAI(
    api_key="YOUR_API_KEY",
    base_url="https://dashscope.aliyuncs.com/compatible-mode/v1"
)

async def ask_qwen(message):
    response = await client.chat.completions.create(
        model="qwen-omni-turbo",
        messages=[{"role": "user", "content": message}]
    )
    return response.choices[0].message.content
