import wikipedia
wikipedia.set_lang("pl")

Olsztyn = wikipedia.summary("Olsztyn")

print(Olsztyn.upper())
