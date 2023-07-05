try:
    x=int(input("numero 1:"))/int(input("numero 2:"))
except Exception as ex:
    print(f"errore: {ex}")
finally:
    print("ora puoi fare altro")
print("fine")