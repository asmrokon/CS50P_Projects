text = input("Input: ").strip()

aliases = {
    ":1st_place_medal:": "🥇",
    ":thumbsup:": "👍",
    ":earth_asia:": "🌏",
    ":candy:": "🍬",
    ":ice_cream:": "🍨",
}

for emoji in aliases.keys():
    if emoji in text:
        text = text.replace(f"{emoji}", f"{aliases[emoji]}")
        print(text)
