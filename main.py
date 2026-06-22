# KATEGORİ 1: Gerekli CBS ve analiz kütüphanelerinin yüklenmesi ve baraj resmi istatistik sözlüğünün tanımlanması
import os
import pandas as pd
import rasterio as rio
from meteostat import Point
import datetime
from ormanlik import Ormanlik
from baraj import Baraj

baraj_verileri = {
    "19.01.2025":{"aktii_doluluk":14.29, "hacim":60620000, "derinlik":43.66 },
    "19.07.2025":{"aktii_doluluk":10, "hacim":48020000, "derinlik":41}
}

# KATEGORİ 2: 12 aylık uydu verileri ve analiz sonuçları için hafızada boş global değişken havuzlarının ayrılması
ocak_orman1 = None
ocak_orman1_koordinat = None
ocak_orman1_crs = None
ocak_orman1_b4 = None
ocak_orman1_b8 = None
orman_1_ndvi = None
ocak_orman1_renkli = None
ocak_orman1_x = None
ocak_orman1_y = None

subat_orman2 = None
subat_orman2_koordinat = None
subat_orman2_crs = None
subat_orman2_b4 = None
subat_orman2_b8 = None
orman_2_ndvi = None
subat_orman2_renkli = None
subat_orman2_x = None
subat_orman2_y = None

mart_orman3 = None
mart_orman3_koordinat = None
mart_orman3_crs = None
mart_orman3_b4 = None
mart_orman3_b8 = None
orman_3_ndvi = None
mart_orman3_renkli = None
mart_orman3_x = None
mart_orman3_y = None

nisan_orman4 = None
nisan_orman4_koordinat = None
nisan_orman4_crs = None
nisan_orman4_b4 = None
nisan_orman4_b8 = None
orman_4_ndvi = None
nisan_orman4_renkli = None
nisan_orman4_x = None
nisan_orman4_y = None

mayis_orman5 = None
mayis_orman5_koordinat = None
mayis_orman5_crs = None
mayis_orman5_b4 = None
mayis_orman5_b8 = None
orman_5_ndvi = None
mayis_orman5_renkli = None
mayis_orman5_x = None
mayis_orman5_y = None

haziran_orman6 = None
haziran_orman6_koordinat = None
haziran_orman6_crs = None
haziran_orman6_b4 = None
haziran_orman6_b8 = None
orman_6_ndvi = None
haziran_orman6_renkli = None
haziran_orman6_x = None
haziran_orman6_y = None

temmuz_orman7 = None
temmuz_orman7_koordinat = None
temmuz_orman7_crs = None
temmuz_orman7_b4 = None
temmuz_orman7_b8 = None
orman_7_ndvi = None
temmuz_orman7_renkli = None
temmuz_orman7_x = None
temmuz_orman7_y = None

agustos_orman8 = None
agustos_orman8_koordinat = None
agustos_orman8_crs = None
agustos_orman8_b4 = None
agustos_orman8_b8 = None
orman_8_ndvi = None
agustos_orman8_renkli = None
agustos_orman8_x = None
agustos_orman8_y = None

eylul_orman9 = None
eylul_orman9_koordinat = None
eylul_orman9_crs = None
eylul_orman9_b4 = None
eylul_orman9_b8 = None
orman_9_ndvi = None
eylul_orman9_renkli = None
eylul_orman9_x = None
eylul_orman9_y = None

ekim_orman10 = None
ekim_orman10_koordinat = None
ekim_orman10_crs = None
ekim_orman10_b4 = None
ekim_orman10_b8 = None
orman_10_ndvi = None
ekim_orman10_renkli = None
ekim_orman10_x = None
ekim_orman10_y = None

kasim_orman11 = None
kasim_orman11_koordinat = None
kasim_orman11_crs = None
kasim_orman11_b4 = None
kasim_orman11_b8 = None
orman_11_ndvi = None
kasim_orman11_renkli = None
kasim_orman11_x = None
kasim_orman11_y = None

aralik_orman12 = None
aralik_orman12_koordinat = None
aralik_orman12_crs = None
aralik_orman12_b4 = None
aralik_orman12_b8 = None
orman_12_ndvi = None
aralik_orman12_renkli = None
aralik_orman12_x = None
aralik_orman12_y = None

ocak_baraj1 = None
ocak_baraj1_koordinat = None
ocak_baraj1_crs = None
baraj_1_b3 = None
ocak_baraj1_b4 = None
ocak_baraj1_b8 = None
ocak_baraj1_ndwi = None
ocak_baraj1_renkli = None
ocak_baraj1_x = None
ocak_baraj1_y = None

subat_baraj2 = None
subat_baraj2_koordinat = None
subat_baraj2_crs = None
baraj_2_b3 = None
subat_baraj2_b4 = None
subat_baraj2_b8 = None
subat_baraj2_ndwi = None
subat_baraj2_renkli = None
subat_baraj2_x = None
subat_baraj2_y = None

mart_baraj3 = None
mart_baraj3_koordinat = None
mart_baraj3_crs = None
baraj_3_b3 = None
mart_baraj3_b4 = None
mart_baraj3_b8 = None
mart_baraj3_ndwi = None
mart_baraj3_renkli = None
mart_baraj3_x = None
mart_baraj3_y = None

nisan_baraj4 = None
nisan_baraj4_koordinat = None
nisan_baraj4_crs = None
baraj_4_b3 = None
nisan_baraj4_b4 = None
nisan_baraj4_b8 = None
nisan_baraj4_ndwi = None
nisan_baraj4_renkli = None
nisan_baraj4_x = None
nisan_baraj4_y = None

mayis_baraj5 = None
mayis_baraj5_koordinat = None
mayis_baraj5_crs = None
baraj_5_b3 = None
mayis_baraj5_b4 = None
mayis_baraj5_b8 = None
mayis_baraj5_ndwi = None
mayis_baraj5_renkli = None
mayis_baraj5_x = None
mayis_baraj5_y = None

haziran_baraj6 = None
haziran_baraj6_koordinat = None
haziran_baraj6_crs = None
baraj_6_b3 = None
haziran_baraj6_b4 = None
haziran_baraj6_b8 = None
haziran_baraj6_ndwi = None
haziran_baraj6_renkli = None
haziran_baraj6_x = None
haziran_baraj6_y = None

temmuz_baraj7 = None
temmuz_baraj7_koordinat = None
temmuz_baraj7_crs = None
baraj_7_b3 = None
temmuz_baraj7_b4 = None
temmuz_baraj7_b8 = None
temmuz_baraj7_ndwi = None
temmuz_baraj7_renkli = None
temmuz_baraj7_x = None
temmuz_baraj7_y = None

agustos_baraj8 = None
agustos_baraj8_koordinat = None
agustos_baraj8_crs = None
baraj_8_b3 = None
agustos_baraj8_b4 = None
agustos_baraj8_b8 = None
agustos_baraj8_ndwi = None
agustos_baraj8_renkli = None
agustos_baraj8_x = None
agustos_baraj8_y = None

eylul_baraj9 = None
eylul_baraj9_koordinat = None
eylul_baraj9_crs = None
baraj_9_b3 = None
eylul_baraj9_b4 = None
eylul_baraj9_b8 = None
eylul_baraj9_ndwi = None
eylul_baraj9_renkli = None
eylul_baraj9_x = None
eylul_baraj9_y = None

ekim_baraj10 = None
ekim_baraj10_koordinat = None
ekim_baraj10_crs = None
baraj_10_b3 = None
ekim_baraj10_b4 = None
ekim_baraj10_b8 = None
ekim_baraj10_ndwi = None
ekim_baraj10_renkli = None
ekim_baraj10_x = None
ekim_baraj10_y = None

kasim_baraj11 = None
kasim_baraj11_koordinat = None
kasim_baraj11_crs = None
baraj_11_b3 = None
kasim_baraj11_b4 = None
kasim_baraj11_b8 = None
kasim_baraj11_ndwi = None
kasim_baraj11_renkli = None
kasim_baraj11_x = None
kasim_baraj11_y = None

aralik_baraj12 = None
aralik_baraj12_koordinat = None
aralik_baraj12_crs = None
baraj_12_b3 = None
aralik_baraj12_b4 = None
aralik_baraj12_b8 = None
aralik_baraj12_ndwi = None
aralik_baraj12_renkli = None
aralik_baraj12_x = None
aralik_baraj12_y = None

ocak_baraj_nesnesi = None
ocak_ndwi = None
ocak_orman_nesnesi = None
orman_ocak_ndwi = None
temmuz_baraj_nesnesi = None
temmuz_ndwi = None
temmuz_orman_nesnesi = None
orman_temmuz_ndwi = None
ocak_ayi_sicaklik = None
temmuz_ayi_sicaklik = None

ndvi_farki = None
sicaklik_farki = None
doluluk_farki = None
kayip_orani = None
bitki_kayip_orani = None

doluluk_ocak = None
doluluk_temmuz = None
sicaklik_ocak = None
sicaklik_temmuz = None

_initialized = False

# KATEGORİ 3: Uydu görüntülerinin (Raster) piksel matrislerini ve koordinat sistemlerini okuyan güvenli yükleme fonksiyonları
def load_raster(path):
    with rio.open(path) as src:
        return src.read(1), src.transform, src.crs

def try_load_raster(path):
    if not os.path.exists(path):
        print(f"UYARI: Dosya bulunamadı: {path}")
        return None, None, None
    try:
        return load_raster(path)
    except Exception as e:
        print(f"UYARI: Raster okunamadı: {path} -> {e}")
        return None, None, None
# KATEGORİ 4: Ana Başlatıcı Motor; 12 aylık verilerin otomatik yüklenmesi, CBS nesnelerinin üretilmesi ve kuraklık indekslerinin hesaplanması
def initialize():
    """Tüm veri yükleme ve analiz kodunu başlat"""
    global _initialized
    if _initialized:
        return
    
    global ocak_orman1, ocak_orman1_koordinat, ocak_orman1_crs, ocak_orman1_b4, ocak_orman1_b8, orman_1_ndvi, ocak_orman1_renkli
    global subat_orman2, subat_orman2_koordinat, subat_orman2_crs, subat_orman2_b4, subat_orman2_b8, orman_2_ndvi, subat_orman2_renkli
    global mart_orman3, mart_orman3_koordinat, mart_orman3_crs, mart_orman3_b4, mart_orman3_b8, orman_3_ndvi, mart_orman3_renkli
    global nisan_orman4, nisan_orman4_koordinat, nisan_orman4_crs, nisan_orman4_b4, nisan_orman4_b8, orman_4_ndvi, nisan_orman4_renkli
    global mayis_orman5, mayis_orman5_koordinat, mayis_orman5_crs, mayis_orman5_b4, mayis_orman5_b8, orman_5_ndvi, mayis_orman5_renkli
    global haziran_orman6, haziran_orman6_koordinat, haziran_orman6_crs, haziran_orman6_b4, haziran_orman6_b8, orman_6_ndvi, haziran_orman6_renkli
    global temmuz_orman7, temmuz_orman7_koordinat, temmuz_orman7_crs, temmuz_orman7_b4, temmuz_orman7_b8, orman_7_ndvi, temmuz_orman7_renkli
    global agustos_orman8, agustos_orman8_koordinat, agustos_orman8_crs, agustos_orman8_b4, agustos_orman8_b8, orman_8_ndvi, agustos_orman8_renkli
    global eylul_orman9, eylul_orman9_koordinat, eylul_orman9_crs, eylul_orman9_b4, eylul_orman9_b8, orman_9_ndvi, eylul_orman9_renkli
    global ekim_orman10, ekim_orman10_koordinat, ekim_orman10_crs, ekim_orman10_b4, ekim_orman10_b8, orman_10_ndvi, ekim_orman10_renkli
    global kasim_orman11, kasim_orman11_koordinat, kasim_orman11_crs, kasim_orman11_b4, kasim_orman11_b8, orman_11_ndvi, kasim_orman11_renkli
    global aralik_orman12, aralik_orman12_koordinat, aralik_orman12_crs, aralik_orman12_b4, aralik_orman12_b8, orman_12_ndvi, aralik_orman12_renkli
    global ocak_baraj1, ocak_baraj1_koordinat, ocak_baraj1_crs, ocak_baraj1_b3, ocak_baraj1_b4, ocak_baraj1_b8, ocak_baraj1_ndwi, ocak_baraj1_renkli
    global subat_baraj2, subat_baraj2_koordinat, subat_baraj2_crs, baraj_2_b3, subat_baraj2_b4, subat_baraj2_b8, subat_baraj2_ndwi, subat_baraj2_renkli
    global mart_baraj3, mart_baraj3_koordinat, mart_baraj3_crs, baraj_3_b3, mart_baraj3_b4, mart_baraj3_b8, mart_baraj3_ndwi, mart_baraj3_renkli
    global nisan_baraj4, nisan_baraj4_koordinat, nisan_baraj4_crs, baraj_4_b3, nisan_baraj4_b4, nisan_baraj4_b8, nisan_baraj4_ndwi, nisan_baraj4_renkli
    global mayis_baraj5, mayis_baraj5_koordinat, mayis_baraj5_crs, baraj_5_b3, mayis_baraj5_b4, mayis_baraj5_b8, mayis_baraj5_ndwi, mayis_baraj5_renkli
    global haziran_baraj6, haziran_baraj6_koordinat, haziran_baraj6_crs, baraj_6_b3, haziran_baraj6_b4, haziran_baraj6_b8, haziran_baraj6_ndwi, haziran_baraj6_renkli
    global temmuz_baraj7, temmuz_baraj7_koordinat, temmuz_baraj7_crs, baraj_7_b3, temmuz_baraj7_b4, temmuz_baraj7_b8, temmuz_baraj7_ndwi, temmuz_baraj7_renkli
    global agustos_baraj8, agustos_baraj8_koordinat, agustos_baraj8_crs, baraj_8_b3, agustos_baraj8_b4, agustos_baraj8_b8, agustos_baraj8_ndwi, agustos_baraj8_renkli
    global eylul_baraj9, eylul_baraj9_koordinat, eylul_baraj9_crs, baraj_9_b3, eylul_baraj9_b4, eylul_baraj9_b8, eylul_baraj9_ndwi, eylul_baraj9_renkli
    global ekim_baraj10, ekim_baraj10_koordinat, ekim_baraj10_crs, baraj_10_b3, ekim_baraj10_b4, ekim_baraj10_b8, ekim_baraj10_ndwi, ekim_baraj10_renkli
    global kasim_baraj11, kasim_baraj11_koordinat, kasim_baraj11_crs, baraj_11_b3, kasim_baraj11_b4, kasim_baraj11_b8, kasim_baraj11_ndwi, kasim_baraj11_renkli
    global aralik_baraj12, aralik_baraj12_koordinat, aralik_baraj12_crs, baraj_12_b3, aralik_baraj12_b4, aralik_baraj12_b8, aralik_baraj12_ndwi, aralik_baraj12_renkli
    global ocak_baraj_nesnesi, ocak_ndwi, ocak_orman_nesnesi, orman_ocak_ndwi
    global temmuz_baraj_nesnesi, temmuz_ndwi, temmuz_orman_nesnesi, orman_temmuz_ndwi
    global ocak_ayi_sicaklik, temmuz_ayi_sicaklik
    global ndvi_farki, sicaklik_farki, doluluk_farki, kayip_orani, bitki_kayip_orani
    global doluluk_ocak, doluluk_temmuz, sicaklik_ocak, sicaklik_temmuz
    
    # Exec the old main.py code via exec to load all data
    import subprocess
    import sys
    
    # Try to load all data
    try:
        month_names = [
            "ocak", "subat", "mart", "nisan", "mayis", "haziran",
            "temmuz", "agustos", "eylul", "ekim", "kasim", "aralik"
        ]

        for ay_index, ay_ad in enumerate(month_names, start=1):
            orman_dir = f"uydu_goruntuleri/orman_{ay_ad}.tif"
            orman_b4 = f"{orman_dir}/orman_{ay_ad}_b4.tiff"
            orman_b8 = f"{orman_dir}/orman_{ay_ad}_b8.tiff"
            orman_ndvi = f"{orman_dir}/orman_{ay_ad}_ndvi.tiff"
            orman_renkli = f"{orman_dir}/orman_{ay_ad}_renkli.tiff"

            orman_data, orman_coord, orman_crs = try_load_raster(orman_b4)
            if orman_data is None:
                print(f"UYARI: Orman B4 verisi yüklenemedi: {orman_b4}")
                continue

            globals()[f"{ay_ad}_orman{ay_index}"] = orman_data
            globals()[f"{ay_ad}_orman{ay_index}_koordinat"] = orman_coord
            globals()[f"{ay_ad}_orman{ay_index}_crs"] = orman_crs
            globals()[f"{ay_ad}_orman{ay_index}_b4"] = orman_data

            orman_b8_data, _, _ = try_load_raster(orman_b8)
            globals()[f"{ay_ad}_orman{ay_index}_b8"] = orman_b8_data

            orman_ndvi_data, _, _ = try_load_raster(orman_ndvi)
            globals()[f"orman_{ay_index}_ndvi"] = orman_ndvi_data

            orman_renkli_data, _, _ = try_load_raster(orman_renkli)
            globals()[f"{ay_ad}_orman{ay_index}_renkli"] = orman_renkli_data

            if orman_coord is not None and orman_data is not None:
                globals()[f"{ay_ad}_orman{ay_index}_x"] = rio.transform.xy(orman_coord, int(orman_data.shape[0] / 2), int(orman_data.shape[1] / 2))
                globals()[f"{ay_ad}_orman{ay_index}_y"] = rio.transform.xy(orman_coord, int(orman_data.shape[0] / 2), int(orman_data.shape[1] / 2))
            else:
                globals()[f"{ay_ad}_orman{ay_index}_x"] = None
                globals()[f"{ay_ad}_orman{ay_index}_y"] = None

            baraj_dir = f"uydu_goruntuleri/baraj_{ay_ad}.tif"
            baraj_b3 = f"{baraj_dir}/baraj_{ay_ad}_b3.tiff"
            baraj_b4 = f"{baraj_dir}/baraj_{ay_ad}_b4.tiff"
            baraj_b8 = f"{baraj_dir}/baraj_{ay_ad}_b8.tiff"
            baraj_ndwi = f"{baraj_dir}/baraj_{ay_ad}_ndwi.tiff"
            baraj_renkli = f"{baraj_dir}/baraj_{ay_ad}_renkli.tiff"

            baraj_data, baraj_coord, baraj_crs = try_load_raster(baraj_b4)
            if baraj_data is None:
                print(f"UYARI: Baraj B4 verisi yüklenemedi: {baraj_b4}")
                continue

            globals()[f"{ay_ad}_baraj{ay_index}"] = baraj_data
            globals()[f"{ay_ad}_baraj{ay_index}_koordinat"] = baraj_coord
            globals()[f"{ay_ad}_baraj{ay_index}_crs"] = baraj_crs
            globals()[f"{ay_ad}_baraj{ay_index}_b4"] = baraj_data

            if ay_index == 1:
                baraj_b3_data, _, _ = try_load_raster(baraj_b3)
                globals()["ocak_baraj1_b3"] = baraj_b3_data
                globals()["baraj_1_b3"] = baraj_b3_data
            else:
                baraj_b3_data, _, _ = try_load_raster(baraj_b3)
                globals()[f"baraj_{ay_index}_b3"] = baraj_b3_data

            baraj_b8_data, _, _ = try_load_raster(baraj_b8)
            globals()[f"{ay_ad}_baraj{ay_index}_b8"] = baraj_b8_data

            baraj_ndwi_data, _, _ = try_load_raster(baraj_ndwi)
            globals()[f"{ay_ad}_baraj{ay_index}_ndwi"] = baraj_ndwi_data

            baraj_renkli_data, _, _ = try_load_raster(baraj_renkli)
            globals()[f"{ay_ad}_baraj{ay_index}_renkli"] = baraj_renkli_data

            if baraj_coord is not None and baraj_data is not None:
                globals()[f"{ay_ad}_baraj{ay_index}_x"] = rio.transform.xy(baraj_coord, int(baraj_data.shape[0] / 2), int(baraj_data.shape[1] / 2))
                globals()[f"{ay_ad}_baraj{ay_index}_y"] = rio.transform.xy(baraj_coord, int(baraj_data.shape[0] / 2), int(baraj_data.shape[1] / 2))
            else:
                globals()[f"{ay_ad}_baraj{ay_index}_x"] = None
                globals()[f"{ay_ad}_baraj{ay_index}_y"] = None

        # Analiz
        ocak_baraj_nesnesi = Baraj(ocak_baraj1_b3, ocak_baraj1_b8)
        ocak_ndwi = ocak_baraj_nesnesi.ndwi_hesapla()
        ocak_orman_nesnesi = Ormanlik(ocak_orman1_b4, ocak_orman1_b8)
        orman_ocak_ndwi = orman_1_ndvi / 10000
        
        temmuz_baraj_nesnesi = Baraj(baraj_7_b3, temmuz_baraj7_b8)
        temmuz_ndwi = temmuz_baraj_nesnesi.ndwi_hesapla()
        temmuz_orman_nesnesi = Ormanlik(temmuz_orman7_b4, temmuz_orman7_b8)
        orman_temmuz_ndwi = orman_7_ndvi / 10000
        
        ocak_ayi_sicaklik = pd.read_csv(r"veriler\menderes_sicaklik_ocak.csv")
        temmuz_ayi_sicaklik = pd.read_csv(r"veriler\menderes_sicaklik_temmuz.csv")
        
        # Verili filtrele
        ocak_ayi_sicaklik = ocak_ayi_sicaklik[["temp" , "rhum"]]
        temmuz_ayi_sicaklik = temmuz_ayi_sicaklik[["temp", "rhum"]]
        
        doluluk_ocak = baraj_verileri["19.01.2025"]["aktii_doluluk"]
        doluluk_temmuz = baraj_verileri["19.07.2025"]["aktii_doluluk"]
        sicaklik_ocak = ocak_ayi_sicaklik["temp"].mean()
        sicaklik_temmuz = temmuz_ayi_sicaklik["temp"].mean()
        
        # Fark hesapla
        ndvi_farki = orman_1_ndvi - orman_7_ndvi
        sicaklik_farki = sicaklik_temmuz - sicaklik_ocak
        doluluk_farki = doluluk_ocak - doluluk_temmuz
        kayip_orani = (doluluk_farki / sicaklik_farki) 
        bitki_kayip_orani = (ndvi_farki / sicaklik_farki)
        
        _initialized = True
        print("Tüm veriler başarıyla yüklendi!")
    except Exception as e:
        print(f"Veri yükleme hatası: {e}")
        raise
