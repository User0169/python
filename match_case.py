# match case
hari = input("masukan hari: ").lower()

match hari:
    case "senin" | "selasa" | "rabu" | "kamis" | "jumat":
        print("hari kerja")
    case "sabtu" | "minggu":
        print("hari libur")
    case _:
        print("masukan hari dengan benar")