import os, asyncio

async def main():
    key = os.getenv("GROQ_API_KEY", "")
    print("1) Key visible to Python?", "YES (" + key[:8] + "...)" if key else "NO  <-- THIS is your problem")
    if not key:
        return
    import openai
    client = openai.AsyncOpenAI(api_key=key, base_url="https://api.groq.com/openai/v1")
    try:
        models = await client.models.list()
        names = [m.id for m in models.data]
        print("2) Key is VALID ✅  Models your key can use:")
        for n in names: print("   -", n)
    except Exception as e:
        print("2) Key REJECTED ❌:", e)
        return
    for model in ["llama-3.3-70b-versatile", "llama-3.1-8b-instant", "llama-3.1-70b-versatile"]:
        if model in names:
            r = await client.chat.completions.create(
                model=model,
                messages=[{"role": "user", "content": "Reply with exactly: GROQ_WORKS"}],
                max_tokens=10, temperature=0)
            print(f"3) Chat test ({model}):", r.choices[0].message.content)
            print("\n✅ All good. If the site STILL shows generic places, your server is running the OLD main.py.")
            return
    print("3) ❌ None of my model names exist for your key. Open main.py and change MODEL_NAME to one of the names printed above.")

asyncio.run(main())