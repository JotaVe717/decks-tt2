import json
import os
import requests

# Token de aplicacao ativo da GameHive
TOKEN = os.getenv("GH_APP_TOKEN", "cd880d55-80c3-44cf-9857-e4ab5ccdaa0a")
URL = "https://tt2-public.gamehivegames.com/raid/clan_data"

headers = {
    "accept": "application/json",
    "Content-Type": "application/json",
    "API-Authenticate": TOKEN
}

# Propriedades oficiais aceites pela GameHive
payload = {
    "player_token": TOKEN,
    "properties": [
        "name",
        "player_code",
        "role",
        "max_stage",
        "player_raid_level",
        "total_card_level",
        "weekly_ticket_count",
        "cards",
        "titan_cards"
    ]
}

try:
    print("A contactar o servidor oficial da GameHive...")
    resposta = requests.post(URL, headers=headers, json=payload, timeout=30)
    
    if resposta.status_code != 200:
        print(f"Erro da GameHive (Codigo {resposta.status_code}): {resposta.text}")
        resposta.raise_for_status()

    dados = resposta.json()

    with open("cla.json", "w", encoding="utf-8") as f:
        json.dump(dados, f, indent=2, ensure_ascii=False)

    print("cla.json gerado com sucesso!")
except Exception as erro:
    print(f"Falha na sincronizacao: {erro}")
    exit(1)