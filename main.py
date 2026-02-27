import backend
import logger


# ================== HANDLER ==================

def tambah_item_handler():
    item = input("Nama item: ")
    if item.strip() == "":
        print("Nama item tidak boleh kosong.")
        return

    pesan = backend.tambah_item(item)
    logger.tulis_log(f'Tambah item: nama: "{item}"')
    print(pesan)


def lihat_semua_handler():
    daftar = backend.semua_item()
    logger.tulis_log("Melihat semua item")

    if not daftar:
        print("📭 Daftar belanja kosong.")
    else:
        print("\n🛒 Daftar Belanja:")
        for i, nama in enumerate(daftar, start=1):
            print(f"   {i}. {nama}")


def hapus_item_handler():
    daftar = backend.semua_item()

    if not daftar:
        print("📭 Tidak ada item untuk dihapus.")
        return

    for i, nama in enumerate(daftar, start=1):
        print(f"   {i}. {nama}")

    try:
        no = int(input("Nomor item yang akan dihapus: "))
        pesan = backend.hapus_item(no)
        logger.tulis_log(f"Hapus item nomor: {no}")
        print(pesan)
    except ValueError:
        print("⚠️ Masukkan angka.")


def edit_item_handler():
    daftar = backend.semua_item()

    if not daftar:
        print("Tidak ada item untuk diedit.")
        return

    for i, nama in enumerate(daftar, start=1):
        print(f"   {i}. {nama}")

    try:
        no = int(input("Nomor item yang akan diedit: "))
        nama_baru = input("Nama baru: ")

        if nama_baru.strip() == "":
            print("Nama baru tidak boleh kosong.")
            return

        pesan = backend.edit_item(no, nama_baru)
        logger.tulis_log(f'Edit item nomor: {no}, nama_baru: "{nama_baru}"')
        print(pesan)

    except ValueError:
        print("Masukkan angka.")


def cari_item_handler():
    kata = input("Masukan kata kunci: ")

    if kata.strip() == "":
        print("Kata kunci tidak boleh kosong.")
        return

    hasil = backend.cari_item(kata)
    logger.tulis_log(f'Cari item dengan kata kunci: "{kata}"')

    if not hasil:
        print("Tidak ada item yang cocok.")
    else:
        print("\n🔍 Hasil pencarian:")
        for i, item in enumerate(hasil, start=1):
            print(f"   {i}. {item}")


def hitung_total_handler():
    total = backend.hitung_total_item()
    logger.tulis_log("Menghitung total item")
    print(f"Total item saat ini: {total}")


# ================== MENU ==================

def tampilkan_menu():
    print("\n=== APLIKASI DAFTAR BELANJA ===")
    print("1. Tambah item")
    print("2. Lihat semua item")
    print("3. Hapus item")
    print("4. Edit item")
    print("5. Cari item")
    print("6. Hitung jumlah item")
    print("7. Keluar")


def main():
    logger.tulis_log("Program dimulai")

    while True:
        tampilkan_menu()
        pilihan = input("Pilih menu (1-7): ")

        if pilihan == '1':
            tambah_item_handler()

        elif pilihan == '2':
            lihat_semua_handler()

        elif pilihan == '3':
            hapus_item_handler()


        elif pilihan == '4':
            edit_item_handler()

        elif pilihan == '5':
            cari_item_handler()

        elif pilihan == '6':
            hitung_total_handler()

        elif pilihan == '7':
            logger.tulis_log("Program selesai")
            print("Terima kasih dan sampai jumpa.")
            break

        else:
            print("Pilihan tidak valid.")


if __name__ == "__main__":
    main()