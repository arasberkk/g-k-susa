import matplotlib.pyplot as plt
# Circular import sorunu çözmek için
import main as main
main.initialize()
from main import doluluk_ocak, doluluk_temmuz, sicaklik_ocak, sicaklik_temmuz, ndvi_farki, orman_ocak_ndwi, orman_temmuz_ndwi


x_ekseni = ["Ocak", "Temmuz"]
tarih = ["19.01.2025", "19.07.2025", "19.01.2024", "19.07.2024"]




#Dosya açma ve yazma izinleri kontrolü
su_kaybi = doluluk_ocak - doluluk_temmuz
sicaklik_farki = sicaklik_temmuz - sicaklik_ocak
with open("rapor.txt","w", encoding="utf-8") as dosya:
    print("GÖK SUSA ANALİZ RAPORU\n")
    print("----------------------------------------------\n")
    print(f"Ocak ve Temmuz Aylarında Baraj Doluluk Oranı ve Ortalama Sıcaklık  %{su_kaybi:.2f}\n")
    if su_kaybi > 5:
        dosya.write("DİKKAT: Kritik seviyede su azalması tespit edildi! Acil önlemler alınmalıdır.\n")
    else:
        dosya.write("Durum: Su seviyesi mevsimsler normaller dahilinde görünüyor.\n")

    print("Veri Kaynağı: Meteostat ve ESA Sentinel-2\n")
        
    dosya.write(f"Ocak Ayı Baraj Doluluk Oranı: {doluluk_ocak:.2f}%\n\n")
    dosya.write(f"Temmuz Ayı Baraj Doluluk Oranı: {doluluk_temmuz:.2f}%\n\n")
    dosya.write(f"Ocak Ayı Ortalama Sıcaklık: {sicaklik_ocak:.2f}°C\n\n")
    dosya.write(f"Temmuz Ayı Ortalama Sıcaklık: {sicaklik_temmuz:.2f}°C\n\n")
    dosya.write(f"Ocak Ayı Orman Sağlık İndeksi: {orman_ocak_ndwi}\n\n")
    dosya.write(f"Temmuz Ayı Orman Sağlık İndeksi: {orman_temmuz_ndwi}\n\n")



def grafik_olustur (enlem, boylam, tarih):
    fig,ax1 = plt.subplots()
    ax1.plot(x_ekseni,[doluluk_ocak, doluluk_temmuz], marker='o', label='Baraj Doluluk Oranı (%)')
    ax1.plot(x_ekseni, [sicaklik_ocak, sicaklik_temmuz], marker='o', label='Ortalama Sıcaklık (°C)')
    ax2 = ax1.twinx()
    ax2.plot(x_ekseni, [orman_ocak_ndwi.mean(), orman_temmuz_ndwi.mean()], marker= 'o', label = 'Orman Sağlık İndeksi', color = 'green')
    ax1.legend()
    ax2.legend()
    plt.title("Ocak ve Temmuz Aylarında Baraj Doluluk Oranı, Ortalama Sıcaklık ve Orman Sağlık İndeksi")
    plt.xlabel("Aylar")
    plt.ylabel("Değerler")
    plt.legend()

    plt.grid(True) 



plt.show()

print(" Analiz başarıyla kaydedildi ve görselleştirildi. Rapor dosyasını kontrol edin.")