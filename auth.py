user = input("user: ").strip()
pwd = input("parola: ").strip()

ok = (user == "admin" and pwd == "1234")
msg = "Autentificat" if ok else "Credențiale invalide"
print(msg)

