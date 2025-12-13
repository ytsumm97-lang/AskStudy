import csv

DATA_PATH = "../data/study_data.csv"


def load_data():
    data = []
    with open(DATA_PATH, newline="", encoding="utf-8") as file:
        reader = csv.DictReader(file)
        for row in reader:
            data.append(row)
    return data


def show_menu():
    print("=== AskStudy ===")
    print("1. Lihat semua soal")
    print("2. Keluar")


def main():
    data = load_data()

    while True:
        show_menu()
        choice = input("Pilih menu (1/2): ")

        if choice == "1":
            for i, item in enumerate(data, start=1):
                print(f"\nSoal {i}:")
                print(item["question"])
        elif choice == "2":
            print("Terima kasih sudah belajar ✨")
            break
        else:
            print("Pilihan tidak valid.")


if __name__ == "__main__":
    main()


