import random
difficulty = 3
health = 50
potion_health = int(random.randint(25, 50) / difficulty)

total_health = health + potion_health


print(f"My Health is: {health:.0f}")
print(f"My total health is: {total_health:.0f}")
print(f"My Potion health is: {potion_health:.0f}")

