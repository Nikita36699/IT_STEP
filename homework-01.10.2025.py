# Завдання 1
# Напишіть програму для збереження даних про музичні
# групи у вигляді словника, де ключ – назва групи, значення –
# список альбомів.
# Напишіть функціонал:
#  додати новий гурт
#  додати новий альбом
#  зберегти дані через json
#  зберегти дані через pickle
#  завантажити дані через json
#  завантажити дані через pickle
import json
import pickle



def save_new_band(bands: dict):
    user_band = input('add band name').capitalize().strip()
    user_band_album = input('add album name').capitalize().strip()

    if user_band not in bands:
        bands[user_band] = [user_band_album]
    else:
        print('this band already  added')


def add_new_album(bands: dict):
    user_band = input('add band name').capitalize().strip()
    user_band_album = input('add album name').capitalize().strip()
    if user_band not in bands:
        bands[user_band] = [user_band_album]
    else:
        bands[user_band].append(user_band_album)


def save_json(bands: dict, filename='bands.json'):
    with open(filename, 'w', encoding='utf-8') as file:
        json.dump(bands, file, indent=4)
    print(f'Data saved to {filename}')


def load_json(filename='bands.json'):
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            return json.load(file)
    except FileNotFoundError:
        print('JSON file not found')
        return {}


def save_pickle(bands: dict, filename='bands.pkl'):
    with open(filename, "wb") as f:
        pickle.dump(bands, f)
    print(f"Data saved to {filename}")


def load_pickle(filename="bands.pkl") -> dict:
    try:
        with open(filename, "rb") as f:
            return pickle.load(f)
    except FileNotFoundError:
        print("Pickle file not found")
        return {}


def show_bands(bands: dict):
    if not bands:
        print("No bands yet!")
        return
    for band, albums in bands.items():
        print(f"{band}: {', '.join(albums)}")


def main():
    bands = {}

    while True:
        print("\nMenu:")
        print("1 - Add new band")
        print("2 - Add new album")
        print("3 - Show all bands")
        print("4 - Save to JSON")
        print("5 - Load from JSON")
        print("6 - Save to Pickle")
        print("7 - Load from Pickle")
        print("0 - Exit")

        choice = input("Choose an option: ").strip()

        if choice == "1":
            save_new_band(bands)
        elif choice == "2":
            add_new_album(bands)
        elif choice == "3":
            show_bands(bands)
        elif choice == "4":
            save_json(bands)
        elif choice == "5":
            bands = load_json()
        elif choice == "6":
            save_pickle(bands)
        elif choice == "7":
            bands = load_pickle()
        elif choice == "0":
            print("Goodbye!")
            break
        else:
            print("Invalid choice, try again.")


main()
