#Kütüphanelerin import edilmesi
import streamlit as st
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
import pandas as pd
import main
main.initialize()
import sunum
import main
import seaborn as sns
import plotly.graph_objects as go


#Panel başlığı ve Genel değişken atama
st.title("GÖK SUSA Analiz Paneli")
st.write("Sentinel 2 uydu verileri ve meteostat hava durumu verileri kullanarak izmir barajıındaki değişimi anlık olarak takip etmektedir")
st.write("--------------------------------------------")
ocak_doluluk = sunum.doluluk_ocak
temmuz_doluluk = sunum.doluluk_temmuz
sicaklik_degisim = int(sunum.sicaklik_temmuz - sunum.sicaklik_ocak)



# sol menü  Kontrol elemanları
st.sidebar.title(" Sistem Hakkında")
st.sidebar.write("Proje  uydu görüntleri ile su orman bitki örtüsü kuraklık analizi yapan otonom bir sistemdir")
st.sidebar.write("Proje Durumu :")
st.sidebar.progress(15)
sol_kolon, sag_kolon = st.sidebar.columns(2)
secilen_enlem = sol_kolon.number_input(label = "Enlem", value = 38.1409)
secilen_boylam = sag_kolon.number_input(label = "Boylam", value = 27.0998)
secilen_tarih = st.sidebar.date_input(label = "Analiz Tarihi Seçiniz")



#otonom CBS Analizleri ve Görselleştirme Motoru
tus = st.button("Kapsamlı Analizi Başlat")
if tus :
    ndwi_farki = main.orman_temmuz_ndwi - main.orman_ocak_ndwi
    lat_enlem, lon_boylam = 38.1409, 27.0998
    harita_verisi = pd.DataFrame({'lat': [secilen_enlem], 'lon': [secilen_boylam]})
    yagis_trend_listesi = [120, 95, 75 ,50 , 25, 10, 5, 15, 30, 65, 90, 115]
    sol_sutun_harita,sag_sutun_harita = st.columns(2)



    if -90 < secilen_enlem < 90:
        sol_sutun, orta_sutun, sag_sutun, sutun = st.columns(4)
        sol_sutun.metric(label = "Ocak Ayı Doluluk", value = ocak_doluluk)
        orta_sutun.metric( label = "Temmuz Ayı Doluluk", value = temmuz_doluluk)
        sag_sutun.metric(label = "Yıllık Değişim", value = sicaklik_degisim)
        sutun.metric(label = "Orman Sağlık İndeksi", value = int(main.bitki_kayip_orani.mean()))
        st.map(harita_verisi, zoom = 10.5)
        sunum.grafik_olustur(None, None, None)
        fig = go.Figure(data = go.Indicator(
                    mode = "gauge+number",
                    title = {'text':"Güncel Baraj Durumu(%)"},
                    value = temmuz_doluluk,
                    gauge = {
                        'axis': {'range': [0,100]},
                        'bar': {'color': "black"},
                        'steps': [
                            {'range': [0,25], 'color': "red"},
                            {'range': [25,50], 'color': "orange"},
                            {'range': [50,75], 'color': "yellow"},
                            {'range': [75,100], 'color': "green"},

                        ]
                    }
))
        with sol_sutun_harita:
            fig, ax = plt.subplots(figsize=(8,6), dpi= 300)
            plt.title("Bitki Kaybı Oranı Isı Haritası")
            sns.heatmap(ndwi_farki, cmap="gist_earth_r", ax=ax, xticklabels=False, yticklabels=False)
            st.pyplot(fig)
        with sag_sutun_harita:
            fig, ax = plt.subplots(figsize=(8,6), dpi= 300)
            plt.title("Aylık Orman ve Baraj Verileri Trendi")
        orman_verisi = []
        baraj_verisi = []
        aylar = []
        for ay in range(1, 13):
            aylik_orman_ndvi = getattr(main, f"orman_{ay}_ndvi", None)
            aylik_baraj_b3 = getattr(main, f"baraj_{ay}_b3", None) if ay != 1 else getattr(main, "ocak_baraj1_b3", None)
            
            if aylik_orman_ndvi is not None:
                orman_ort = aylik_orman_ndvi.mean()
                orman_verisi.append(orman_ort)
                aylar.append(ay)
            
            if aylik_baraj_b3 is not None:
                baraj_ort = aylik_baraj_b3.mean()
                baraj_verisi.append(baraj_ort)
        if orman_verisi:
            sns.lineplot(x=aylar, y=orman_verisi, label="Orman NDVI Ortalaması", ax=ax, marker='o')
        if baraj_verisi:
            sns.lineplot(x=aylar, y=baraj_verisi, label="Baraj B3 Ortalaması", ax=ax, marker='s')
        
        ax.set_xlabel("Aylar")
        ax.set_ylabel("Değer")
        st.pyplot(fig)
        
        

        #Karar Destek Sistemi ve Yapay Zeka Tahminleri        
        yillik_orman_trend = None
        yillik_baraj_trend = None
        orman_trend_listesi = []
        baraj_trend_listesi = []

        for ay in range(1, 13):
            if ay == 1:
                yillik_orman_trend = main.orman_1_ndvi / main.orman_2_ndvi / main.orman_3_ndvi / main.orman_4_ndvi / main.orman_5_ndvi / main.orman_6_ndvi / main.orman_7_ndvi / main.orman_8_ndvi / main.orman_9_ndvi / main.orman_10_ndvi / main.orman_11_ndvi / main.orman_12_ndvi 
                yillik_baraj_trend = main.baraj_1_b3.mean() / main.baraj_2_b3.mean() / main.baraj_3_b3.mean() / main.baraj_4_b3.mean() / main.baraj_5_b3.mean() / main.baraj_6_b3.mean() / main.baraj_7_b3.mean() / main.baraj_8_b3.mean() / main.baraj_9_b3.mean() / main.baraj_10_b3.mean() / main.baraj_11_b3.mean() / main.baraj_12_b3.mean()
            aylik_orman_ndvi = getattr(main, f"orman_{ay}_ndvi", None)
            aylik_baraj_b3 = getattr(main, f"baraj_{ay}_b3", None) if ay != 1 else getattr(main, "baraj_1_b3", None)
            if aylik_orman_ndvi is not None:
                orman_ort = aylik_orman_ndvi.mean()
                orman_trend_listesi.append(orman_ort)
            if aylik_baraj_b3 is not None:
                baraj_ort = aylik_baraj_b3.mean()
                baraj_trend_listesi.append(baraj_ort)

        yapay_zeka_modeli = LinearRegression().fit([[deger] for deger in yagis_trend_listesi], baraj_trend_listesi)
        gelecek_yagis = (baraj_trend_listesi [-1] + baraj_trend_listesi[-2] - baraj_trend_listesi[-3]) /3
        tahmini_baraj_seviyesi = yapay_zeka_modeli.predict([[gelecek_yagis]]) [0]

        st.info(f"GÖK SUSA Yapay Zeka Tahmini: Önümüzdeki 3 ay yağış trendi bu şekilde devam ederse, baraj doluluk oranının {tahmini_baraj_seviyesi:.2f}% olması beklenmektedir")


        ax.axis('off')
        st.plotly_chart(fig, use_container_width= True )
        st.pyplot(plt)

        st.success("Analiz Başarıyla tamamlandı, rapor güncellendi!")
    else:
        print("Hatalı aralık girişi yapıldı, lütfen  -90 ile 90 arasında bir değer giriniz.")
        st.stop()