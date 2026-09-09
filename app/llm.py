import json
import httpx

async def ask(base_url: str | None, api_key: str | None, model: str | None, question: str) -> str:
    if not (base_url and model): return "LLM is not configured. Set LLM_BASE_URL and LLM_MODEL in .env."
    url = base_url.rstrip("/") + "/chat/completions"
    headers = {"Authorization": f"Bearer {api_key}"} if api_key else {}
    payload = {"model": model, "messages": [{"role":"system","content":"You assist with authorized bug-bounty notes. Do not provide instructions for unauthorized access, credential theft, malware, persistence, or bypassing access controls."},{"role":"user","content":question}], "temperature":0.2}
    async with httpx.AsyncClient(timeout=60) as client:
        r = await client.post(url, headers=headers, json=payload)
        r.raise_for_status()
        data=r.json()
    return data["choices"][0]["message"]["content"]
