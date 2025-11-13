import random

racas = ["humano", "goblin", "Orc", "Gigante", "anao"]
classes = ["espadachim", "mago", "ladrao", "arqueiro"]

nome = ["Assuna ", "KLIN ", "CARLOS ", "Kirito ", "Yui "]
sobrenome = ["pagodinho", "xin", "CALIN", "Nascimento"]

print("⚔️ --BEM VINDO AO SOWRD ART ONLINE-- ⚔️")
print("SEU PERSONAGEM JÁ ESTÁ SENDO CRIADO...")

# --- Correção aplicada aqui ---
raca_heroi = random.choice(racas)
classe_heroi = random.choice(classes)
# --- Fim da correção ---

nome_heroi = f"{random.choice(nome)}{random.choice(sobrenome)}"

itens_iniciais = ["poçao de cura", "Pao", "Maça", "Mapa do tesourro"]
mochila_heroi = []

for _ in range(3):
    item = random.choice(itens_iniciais)
    mochila_heroi.append(item)


ficha_final = {
    "Nome": nome_heroi,
    "Raça": raca_heroi,
    "Classe": classe_heroi,
    "Força": random.randint(3, 20),
    "Inteligencia": random.randint(3, 20),
    "Destreza": random.randint(3, 20),
    "Carisma": random.randint(3, 20),
    "Inventario": mochila_heroi
}


print("\n🎉 --FICHA PRONTA, NASÇA HERÓI!!!-- 🎉")
print(f"**Nome:** {ficha_final['Nome']}")
print(f"**Raça:** {ficha_final['Raça']}")
print(f"**Classe:** {ficha_final['Classe']}")
print("\n-- STATUS, APAREÇAM A ESTE GRANDE HERÓI! --")
print(f"**Força:** {ficha_final['Força']}")
print(f"**Inteligência:** {ficha_final['Inteligencia']}")
print(f"**Destreza:** {ficha_final['Destreza']}")
print(f"**Carisma:** {ficha_final['Carisma']}")
print("\n-- INVENTÁRIO --")
print(f"**Inventário:** {ficha_final['Inventario']}")
