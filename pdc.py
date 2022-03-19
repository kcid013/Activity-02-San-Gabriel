import random

print("""
Sample Problem

A Lv. 90 Charizard (Fire/Flying, Sp. Atk: 205) attacks a Lv. 95
Feraligatr (Water, Sp. Def: 188) with Fire Blast, a Fire-type move
with a Power of 110 and gains a same-type attack bonus.. It hits
the target normally but deals a not very effective damage. The
weather on the field is normal. Given the following conditions,
determine how much damage Charizard’s attack will deal.

""")
level = 90
power = 110
attack = 205
defense = 188

print(f"""Level: {level}
Name: Charizard
Type: Flying/Fire
Sp. Attack: {attack}
Power Move: Fire Blast ({power})


Enemy Level:95
Name: Feraligatr
Type: Water
Sp. Defense: {defense}
""")

modifiers = {
    "target": 1,
    "weather": 1,
    "badge": 1,
    "crit": 1,
    "rand": random.uniform(0.85, 1.00),
    "stab": 1.5,
    "types": random.uniform(0.25, 0.50),
    "burn": 1,
    "other": 1
}
totalMods = 1
print("Modifiers:")
for i in modifiers:
    print(f"{i}: {modifiers[i]}")
    totalMods *= modifiers[i]

damage = ((((((2 * level) / 5) + 2) * power * (attack/defense)) / 50) + 2)

print(f"""
Total Modifiers: {totalMods}
Total Damage: {damage}
Final Damage inflicted to enemy: {damage*totalMods}
""")