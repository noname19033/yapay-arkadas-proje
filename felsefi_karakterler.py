def felsefi_sohbet():
    filozoflar = {
        "Sokrates": "Bildiğim tek şey, hiçbir şey bilmediğimdir.",
        "Nietzsche": "Beni öldürmeyen şey, beni güçlendirir.",
        "Kant": "Aklını kullanma cesaretini göster!"
    }
    
    print("Hoş geldin! Bir filozof seç:")
    for i, filozof in enumerate(filozoflar.keys(), 1):
        print(f"{i}. {filozof}")
    
    secim = input("Seçimini yap (1-3): ")
    
    if secim in ["1", "2", "3"]:
        secilen_filozof = list(filozoflar.keys())[int(secim)-1]
        print(f"{secilen_filozof} diyor ki: {filozoflar[secilen_filozof]}")
    else:
        print("Geçersiz seçim, lütfen 1-3 arasında bir sayı gir.")

# Fonksiyonu çalıştır
felsefi_sohbet()
