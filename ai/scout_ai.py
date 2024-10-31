from g4f.client import Client
def ai_search(alias):
    prompt = f"Tell me everything you know about {alias}, if you do not know anything please say 'NFOUND'"
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}],
    )
    gpt_response = str(response.choices[0].message.content)
    if not "NFOUND" in gpt_response:
        found_info = gpt_response
    else:
        found_info = "N/A"