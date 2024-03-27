class Personel:
    def __init__(self, adi, departman, calisma_yili, maas):
        self.adi = adi
        self.departman = departman
        self.calisma_yili = calisma_yili
        self.maas = maas

class Firma:
    def __init__(self):
        self.personel_listesi = []

    def personel_ekle(self, personel):
        self.personel_listesi.append(personel)

    def personel_listele(self):
        for personel in self.personel_listesi:
            print(f"Adı: {personel.adi}, Departmanı: {personel.departman}, Çalışma Yılı: {personel.calisma_yili}, Maaşı: {personel.maas}")

    def maas_zammi(self, personel, zam_orani):
        for p in self.personel_listesi:
            if p == personel:
                p.maas *= (1 + zam_orani / 100)

    def personel_cikart(self, personel):
        if personel in self.personel_listesi:
            self.personel_listesi.remove(personel)
        else:
            print("Personel listede bulunamadı.")

# Personel nesneleri oluşturulması
personel1 = Personel("Ipek", "Muhasebe", 3, 5000)
personel2 = Personel("Beyza", "Pazarlama", 5, 6000)

# Firma nesnesi oluşturulması
firma = Firma()

# Kullanıcıdan personel bilgilerini alma
adi = input("Personel adını giriniz: ")
departman = input("Personelin çalıştığı departmanı giriniz: ")
calisma_yili = int(input("Personelin çalışma yılını giriniz: "))
maas = float(input("Personelin maaşını giriniz: "))

# Personel nesnesi oluşturma
yeni_personel = Personel(adi, departman, calisma_yili, maas)

# Oluşturulan personeli firmaya ekleme
firma.personel_ekle(yeni_personel)


# Personel ekleme
firma.personel_ekle(personel1)
firma.personel_ekle(personel2)

# Personel listeleme
print("Firma Çalışanları:")
firma.personel_listele()

# Maaş zammı
firma.maas_zammi(personel1, 10)

# Personel çıkartma
firma.personel_cikart(personel2)

# Maaş zammı
zam_orani = float(input("\nMaaş zam oranını giriniz (% cinsinden): "))
firma.maas_zammi(yeni_personel, zam_orani)

# Personel çıkartma
cikar = input("\nPersoneli çıkarmak istiyor musunuz? (Evet/Hayır): ").lower()
if cikar == "evet":
    firma.personel_cikart(yeni_personel)

# Güncellenmiş personel listesi
print("\nGüncellenmiş Firma Çalışanları:")
firma.personel_listele()
