import json
import os
import requests

# Puxa o seu token seguro que voce salvou nos Secrets do GitHub
TOKEN = os.getenv("TITANTECH_TOKEN")

# Monta o endereco completo com a sua chave
URL = f"https://titantech.silical.dev/{TOKEN}"

try:
    print(f"Buscando dados em: {URL}")
    resposta = requests.get(URL, timeout=20)
    resposta.raise_for_status()

    # Tenta ler a resposta como dados em formato JSON
    dados = resposta.json()

    # Salva os dados atualizados dentro do cla.json
    with open("cla.json", "w", encoding="utf-8") as f:
        json.dump(dados, f, indent=2, ensure_ascii=False)

    print("Arquivo cla.json atualizado com sucesso!")
except Exception as erro:
    print(f"Ocorreu um erro ao atualizar: {erro}")
    exit(1)