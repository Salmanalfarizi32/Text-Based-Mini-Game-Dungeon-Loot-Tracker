import random

# List loot yang mungkin ditemukan
loot_list = ["Mystic Sword", "Thunder Mace", "Mithril Shirt", "Knight Shield", "Health Potion", "Gold Coins", "Magic Scroll"]

# List buat nyimpen semua loot yang didapat
inventory = []

def opening():
    print("🏰 Selamat datang di Dungeon Loot Tracker!")
    print("Kamu adalah petualang yang mencari harta karun misterius...\n")

def get_random_loot():
    return random.choice(loot_list)

def dungeon_loop():
    while True:
        print("\nKamu memasuki ruangan...")
        pilihan = input("[L]anjut atau [K]eluar? ").lower()

        if pilihan == "k":
            print("\n🏃‍♂️ Kamu memilih keluar dari dungeon.")
            break
        elif pilihan == "l":
            loot = get_random_loot()
            inventory.append(loot)
            print(f"🎁 Kamu menemukan: {loot}")
        else:
            print("❗ Pilihan tidak valid. Coba lagi.")

def show_summary():
    print("\n📦 Loot yang kamu kumpulkan:")
    if inventory:
        for item in inventory:
            print(f"- {item}")
    else:
        print("Kamu tidak mendapatkan apa-apa... sedih 😢")

def main():
    opening()
    dungeon_loop()
    show_summary()

if __name__ == "__main__":
    main()
