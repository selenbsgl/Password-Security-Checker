def parola_kontrol(parola):
    mesajlar = []

    if len(parola) < 8:
        mesajlar.append("Parola çok kısa (min. 8 karakter olmalı)")
    if not any(char.isupper() for char in parola):
        mesajlar.append("En az bir büyük harf içermeli")
    if not any(char.islower() for char in parola):
        mesajlar.append("En az bir küçük harf içermeli")
    if not any(char.isdigit() for char in parola):
        mesajlar.append("En az bir rakam içermeli")
    if not any(char in "!@#$%^&*()-_=+[]{};:'\",.<>?/" for char in parola):
        mesajlar.append("En az bir özel karakter içermeli")

    if not mesajlar:
        return "Parola güçlü!"
    else:
        return "\n".join(mesajlar)

# Kullanıcıdan parola al
parola = input("Parolanızı girin: ")
print(parola_kontrol(parola))
