import pyaici.server as aici
    
async def main():
    prompt = "Can you give me a list of theorems in probability theory?"
    await aici.FixedTokens(prompt)
    marker = aici.Label()
    await aici.FixedTokens("\n")
    for i in range(1,6):
        await aici.FixedTokens(f"{i}.")
        await aici.gen_text(stop_at = "\n")
    await aici.FixedTokens("\n")

await aici.FixedTokens("\n")