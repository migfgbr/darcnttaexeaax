meme_dict = {
    "gankado": "ter sido alvo de um ataque surpresa ou emboscada",
    "lore": "história",
    "hype": "entusiasmo",
    "easter egg" : "mensagem ou recurso escondido",
    "rage": "pessoa entra em estado de fúria e frustração"
}
print(meme_dict)
doubt = input("qual dessas palavras você quer saber?")
if doubt == "gankado":
    print(meme_dict["gankado"])
elif doubt == "lore":
    print(meme_dict["lore"])
elif doubt == "hype":
    print(meme_dict["hype"])
elif doubt == "easter egg":
    print(meme_dict["easter egg"])
elif doubt == "rage":
    print(meme_dict["rage"])
else:
    print("não conheço essa palavra :| ")
