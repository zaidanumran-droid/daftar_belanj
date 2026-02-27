# ================= DATABASE =================
NAMA_FILE = "data.txt"
import json
import os

FILE_DATA = "data_belanja.json"

def baca_data():
    if os.path.exists(FILE_DATA):
        with open(FILE_DATA, "r") as file:
            return json.load(file)
    return []

def tulis_data(data):
    with open(FILE_DATA, "w") as file:
        json.dump(data, file, indent=4)
def baca_data():
    try:
        with open(NAMA_FILE, "r") as file:
            return file.read().splitlines()
    except FileNotFoundError:
        return []
    except json.JSONDecodeError:
        print("file data rusak,membuat file baru")
    return []
print("error tidak terduga saat membaca: {e}")


def tulis_data(daftar):
    with open(NAMA_FILE, "w") as file:
        for item in daftar:
            file.write(item + "\n")

def baca_data():
    with open("data.txt","r") as file:
        return file.read().splitlines()
    
    