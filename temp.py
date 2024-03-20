# Adınız, soyadınız, öğrenci numaranız ve notunuzu belirten fonksiyon
def bilgi_ver():
    ad = "Beyza"
    soyad = "Ucak"
    ogrenci_no = "211220032"
    notum = "hello world"

    print("Ad:", ad)
    print("Soyad:", soyad)
    print("Öğrenci Numarası:", ogrenci_no)
    print("Not:", notum)

# Kendisine gönderilen karakterin bir harf olup olmadığını bulan fonksiyon
def harf_mi(karakter):
    return karakter.isalpha()

# Kendisine gelen harfi (büyükse) küçük harfe çeviren fonksiyon
def kucuk_harf_yap(harf):
    return harf.lower()

# Kendisine gönderilen metinde harflerin kullanım sıklığını (yüzdelik oranını) bulan fonksiyon
def harf_oranlari(metin):
    harf_sayilari = {}
    toplam_harf_sayisi = 0

    for harf in metin:
        if harf_mi(harf):
            harf = kucuk_harf_yap(harf)
            harf_sayilari[harf] = harf_sayilari.get(harf, 0) + 1
            toplam_harf_sayisi += 1

    oranlar = {}

    for harf, sayi in harf_sayilari.items():
        oranlar[harf] = {"kullanım adedi": sayi, "kullanım oranı": (sayi / toplam_harf_sayisi) * 100}

    return oranlar

# Metindeki kelime sayısını bulan fonksiyon
def kelime_sayisi(metin):
    kelimeler = metin.split()
    return len(kelimeler)

# Metindeki cümle sayısını bulan fonksiyon
def cumle_sayisi(metin):
    cumleler = metin.split('.')
    return len(cumleler)

# Metindeki özel karakter sayısını bulan fonksiyon
def ozel_karakter_sayisi(metin):
    ozel_karakterler = "!@#$%^&*()-_=+[{]}\|;:'\",<.>/?`~"
    sayac = 0
    for karakter in metin:
        if karakter in ozel_karakterler:
            sayac += 1
    return sayac

def main():
    metin = input("Lütfen bir metin girin: ")
    oranlar = harf_oranlari(metin)
    kelime_say = kelime_sayisi(metin)
    cumle_say = cumle_sayisi(metin)
    ozel_karakter_say = ozel_karakter_sayisi(metin)

    print("\nMetindeki harflerin yüzde oranları:")
    for harf in sorted(oranlar.keys()):
        bilgi = oranlar[harf]
        kullanım_adedi = bilgi["kullanım adedi"]
        kullanım_oranı = bilgi["kullanım oranı"]
        print(f"'{harf}':\tKullanım adedi: {kullanım_adedi}\tKullanım oranı: %{kullanım_oranı:.2f}")

    print(f"\nMetindeki kelime sayısı: {kelime_say}")
    print(f"Metindeki cümle sayısı: {cumle_say}")
    print(f"Metindeki özel karakter sayısı: {ozel_karakter_say}")

if __name__ == "__main__":
    bilgi_ver()
    main()
