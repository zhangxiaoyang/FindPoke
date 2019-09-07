import sys

poke_name = sys.argv[1]

poke_dict = {
    "皮卡丘": "Pikachu https://wiki.52poke.com/wiki/皮卡丘",
    "小火龙": "Charmander https://wiki.52poke.com/wiki/小火龙"
}

value = poke_dict[poke_name]
print(poke_name + ": " + value)