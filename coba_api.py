import urllib.request
import json

urls = [
    "http://api.open-notify.org/astros.json",
    "http://httpbin.org/get",
    "https://jsonplaceholder.typicode.com/posts" 
 ]

for url in urls:
    try:
        print(f"mencoba {url}...")
        response = urllib.request.urlopen(url, timeout=5)
        data = json.loads(data_json)
        print("berhasil\n")



        if "astros" in url:
            print(f"astronaut di ISS: {data['numbe']} orang")
            for astronaut in data['people']:
                print(f" - {astronaut['name']}")
        elif"httpbin" in url:
           print(f"Origin ip: {data['origin']}")
        elif "jsonplaceholdr" in url:
            print("contoh judul:",data[0]["title"])
        break 
    except Exception as e:
        print(f"Gagal: {e}\n")
else:
      # Jika semua URL gagal
    print("❌ Semua URL gagal. Gunakan data lokal.")
    data = [
        {"title": "Belajar API"}, 
        {"title": "Error Handling"}, 
        {"title": "Logging"}
    ]
    print("\nData lokal:")
    for i, post in enumerate(data, start=1):
        print(f"{i}. {post['title']}")