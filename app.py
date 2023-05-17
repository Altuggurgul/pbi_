import pickle
from pathlib import Path


import streamlit as st
import streamlit.components.v1 as components
import pandas as pd
import base64

import streamlit_authenticator as stauth

st.set_page_config(page_title="My Webpage", page_icon=": tada :", layout="wide", initial_sidebar_state="expanded")

names = ["Altug Gurgul", "Mehmet Ergan", "Yusuf Yavuzcan"]
usernames = ["agurgul", "mergan", "yyavuzcan"]

file_path = Path(__file__).parent / "hashed_pw.pkl"
with file_path.open("rb") as file:
    hashed_passwords = pickle.load(file)

authenticator = stauth.Authenticate(names, usernames, hashed_passwords, "report_page","abcdef",
                                    cookie_expiry_days=30)

name, authentication_status, username = authenticator.login("Login", "main")

if authentication_status == False:
    st.error("Kullanıcı adı/parola yanlış")

if authentication_status:



    def show_pdf(file_path):
        with open(file_path, "rb") as f:
            base64_pdf = base64.b64encode(f.read()).decode('utf-8')
        pdf_display = f'<embed src="data:application/pdf;base64,{base64_pdf}" width="1280" height="720" type="application/pdf"></embed>'
        st.markdown(pdf_display, unsafe_allow_html=True)


    st.title("RAPOR SAYFASI")

    authenticator.logout("Logout", "sidebar")
    st.sidebar.image("datavadisi.png",width=200)
    st.sidebar.title(f"Hoşgeldin {name}")



    select_1= st.sidebar.selectbox("Rapor Tipleri:", ["Tüm Raporlar","Satış Raporları", "Stok Raporları", "Müşteri Analitiği",
                                                      "Pazarlama","CRM", "HR","Sosyal Medya", "Web Site"])

    ## DATAFRAME
    df = pd.DataFrame({'Rapor Adı': ["Satıs Raporu - 1", "Satıs Raporu - 2", "Satıs Raporu - 3", "Stok Raporu-1", "Finans Dashboard(Satıs)",
                                     "CEO Dashboard(Satıs)", "Satıs Raporu - 4","Pazarlama Dashboard",
                                     "Satış Dashboard (CRM) ", "Web Site Analitiği", "Müşteri Analitigi 1", "Müşteri Analitigi 2",
                                     "Müşteri Değerlendirme", "HR Dashboard 1", "HR Dashboard 2", "HR Dashboard 3",
                                     "Sosyal Medya Dashboard","HR_Dashboard 4","Satıs Raporu - 5","Satıs Raporu - 6","Satıs Raporu - 7",
                                     "Satıs Raporu - 8"]},
                      index=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22])

    # ÜST BÖLÜM

    with st.container():

        col1, col2,col3 = st.columns(3)

        if select_1 == "Tüm Raporlar":
            with col1:
                st.subheader("Tüm Rapor Listesi")
                st.table(df)
                st.write("*Son Güncelleme Tarihi: 17.05.2023*")

            with st.container():

                st.write("**Satış Raporu - 1**")
                show_pdf("POWERBICANLI_PDF/Satıs_Dhasboard_DEV.pdf")

                st.write("---")
                st.write("**Satış Raporu - 2**")
                show_pdf("POWERBICANLI_PDF/Satıs_Dashboard_DEV_v2.3_FINAL.pdf")

                st.write("---")
                st.write("**Satış Raporu - 3**")
                show_pdf("POWERBICANLI_PDF/Satıs_Dashboard_v3.pdf")

                st.write("---")
                st.write("**Stok Raporu-1**")
                show_pdf("POWERBICANLI_PDF/Stok_Raporu_1.pdf")

                st.write("---")
                st.write("**Finans Dashboard(Satıs)**")
                show_pdf("POWERBICANLI_PDF/1_Finans Dashboard.pdf")

                st.write("---")
                st.write("**CEO Dashboard(Satıs)**")
                show_pdf("POWERBICANLI_PDF/1_Yonetici Dashboard.pdf")

                st.write("---")
                st.write("**Satış Raporu - 4**")
                show_pdf("POWERBICANLI_PDF/Satıs_Dhasboard_DEV_WHITE.pdf")

                st.write("---")
                st.write("**Pazarlama Dashboard**")
                show_pdf("POWERBICANLI_PDF/1_Pazarlama Dashboard.pdf")

                st.write("---")
                st.write("**Satış Dashboard(CRM)**")
                show_pdf("POWERBICANLI_PDF/1_Satıs_Dashboard_CRM.pdf")

                st.write("---")
                st.write("**Web Site Analitiği**")
                show_pdf("POWERBICANLI_PDF/1_WebSiteAnalitigi.pdf")

                st.write("---")
                st.write("**Müşteri Analitiği 1**")
                show_pdf("POWERBICANLI_PDF/Musteri Analizi.pdf")

                st.write("---")
                st.write("**Müşteri Analitiği 2**")
                show_pdf("POWERBICANLI_PDF/2_Musteri Analizi.pdf")

                st.write("---")
                st.write("**Müşteri Değerlendirme**")
                show_pdf("POWERBICANLI_PDF/3_Musteri Degerlendirme.pdf")

                st.write("---")
                st.write("**HR Dashboard 1**")
                show_pdf("POWERBICANLI_PDF/HR_Dashboard_1.pdf")

                st.write("---")
                st.write("**HR Dashboard 2**")
                show_pdf("POWERBICANLI_PDF/HR_Dashboard_2.pdf")

                st.write("---")
                st.write("**HR Dashboard 3**")
                show_pdf("POWERBICANLI_PDF/HR_Dashboard_3.pdf")

                st.write("---")
                st.write("**Sosyal Medya Analitiği**")
                show_pdf("POWERBICANLI_PDF/Sosyal Medya Dashboard.pdf")

                st.write("---")
                st.write("**HR Dashboard 4**")
                show_pdf("POWERBICANLI_PDF/HR_Dashboard_4.pdf")

                st.write("---")
                st.write("**Satış Raporu - 5**")
                show_pdf("POWERBICANLI_PDF/5_Bolge Performans.pdf")

                st.write("---")
                st.write("**Satış Raporu - 6**")
                show_pdf("POWERBICANLI_PDF/6_DonanımSatıs.pdf")

                st.write("---")
                st.write("**Satış Raporu - 7**")
                show_pdf("POWERBICANLI_PDF/1_Urun Satıs Icgoruleri.pdf")

                st.write("---")
                st.write("**Satış Raporu - 8**")
                show_pdf("POWERBICANLI_PDF/7_Satıs_Dashboard.pdf")


        if select_1 == 'Satış Raporları':
            st.balloons()
            with col2:
                st.write("**Rapor Listesi**")
                df_2 = df.loc[df["Rapor Adı"].str.contains("Satıs"), :]
                st.dataframe(df_2)

            with col1:
                st.subheader(":blue[Satıs Raporları]")
                # st.dataframe(pd.DataFrame({"Rapor Adı": ["Satış Raporu - 1","Satış Raporu 2","Satış Raporu 3"], "Kullanıcı Sayısı": ["20","10","15"]}))
                st.image("sales.jpeg",width=400)

            with col3:
                st.write("**Rapor Seçimi**")
                select_2 = st.selectbox('Seçim Yapınız', ['Seçim Yapınız', 'Satıs Raporu 1', 'Satıs Raporu 2', 'Satıs Raporu 3',"Finans Dashboard(Satıs)",
                                                          "CEO Dashboard(Satıs)", "Satıs Raporu 4","Satıs Raporu 5",
                                                          "Satıs Raporu 6","Satıs Raporu 7","Satıs Raporu 8"])


    #RAPOR GÖRÜNÜMLERİ
            with st.container():

                if select_2 == "Satıs Raporu 1":
                    with st.container():
                        st.write("---")
                        st.markdown("**SATIS RAPORU 1**")
                        components.iframe("https://app.powerbi.com/view?r=eyJrIjoiZDE0NThhZTctMTIyNi00N2MzLTg2YmUtOTVkZjg2ZjQ1MDFlIiwidCI6IjlmZTNjZTM5LTIwOWQtNGM5NS1hMWQxLWViZjA0NjY3NDkyYyIsImMiOjl9",
                                height=600, width=1000)

                        st.write("---")
                        st.markdown("**Rapor Bilgiler**")
                        with st.expander("Raporun Hedef Kitlesi Kimdir?"):
                            st.write("""
            
                            Satış kontrol paneli, bir kuruluşun finansal ve satış içgörülerini sergilemek için yönetici düzeyinde bir rapor olarak oluşturulmuştur. Hedeflenen kullanıcılar yönetici seviyesindeki çalışanlar olduğu için gösterge tablosu, kullanıcıların raporu kolayca taramasına olanak tanıyan üst düzey içgörüler sunar. Kullanıcılar daha sonra, panel üzerindeki yer alan rakamların keşfetmeye değer bir içgörüyü tetiklemesi durumunda, ayrıntılı metriklere dalmak için ek seçeneğe sahip olur.
            
                            """)
                        with st.expander("Raporun Amacı Nedir?"):
                            st.write("""
                            Panonun amacı, işletmenin zaman içindeki mali performansına ilişkin üst düzey bir genel bakış sağlamaktır. Ek olarak, kullanıcıların konuma ve ürün kategorisine göre finansal performansa dalmasına olanak tanır. Bu odak alanlarının her ikisi de, kullanıcıların finansal eğilimleri ve aşırı/düşük performans alanlarını belirlemesine olanak tanır. Kullanıcılar daha sonra çabalarını nereye odaklayacaklarını belirlemek için bu ilk içgörüleri kullanabilirler.
            
            
            
            
                            """)
                        with st.expander("Raporun temel içgörüleri nelerdir?"):
                            st.write("""
            
            
                            **KPI'lar -** Gelir, Kar, Siparişler, Müşteriler, Miktar:\n
                            _‍İşletmenin mali durumunun anlık görüntüsünü sağlar_
            
                            **Alan Grafiği -** Gelir, Kar, Siparişler, Müşteriler, Miktar (12 ay):\n
                            _Kullanıcıların mevsimsel iş akışını belirlemesine yardımcı olur_
            
                            **Çubuk Grafik -** Bölge, mağaza ve ürüne göre gelir:\n
                            _Kullanıcıların coğrafyaya ve kategoriye göre mali performanslarını anlamalarına yardımcı olur_
            
                            **Çizgi Grafik -** Büyüme performansı:\n
                            _İşletmenin mali büyüme durumunun anlık görüntüsünü sağlar_
            
                            **Halka Grafik -** Kategoriler Göre Satın alma Yüzdesi:\n
                            _Ürün kategorisine göre satılan ürün adet bilgisi dağılımını sağlar._
            
            
                            """
                                     )
                        with st.expander("Rapor İçeriği:"):
                            st.write("""
            
                        Raporun amacı, bir perakende mağazasının son 12 ayda ürün satışlarını analiz etmektir. Rapor, farklı ürün kategorilerindeki satışlarını görselleştirir ve her bir kategori için bir dizi farklı gösterim içerir.
            
                        Raporun ana bileşenleri şunlardır:
            
                        **Satış Performansı:** Bu bileşen, seçilen tarih aralığındaki farklı kategorilerdeki ürünlerin satışlarını, gelirlerini, giderlerini ve satılan ürün adetlerini gösteren bir grafik sunar. Bu grafikte, farklı kategorilerin toplam satış, kar, maliyetin yanı sıra, her bir kategorideki en çok satılan ürünlerin de gösterilir.
            
                        **BÖLGE:** Bu bileşen, satışların coğrafi dağılımını harita üzerinde gösterir. Harita, farklı bölgelerdeki toplam satışları renkli bir şekilde gösterir ve kullanıcılara, farklı bölgelerdeki satışlar arasındaki farklılıkları analiz etme imkanı verir.
            
                        **Kategori Bazında Satışlar:** Bu bileşen, her bir kategori için toplam satışları ve gelirleri gösterir. Kullanıcılar, her bir kategori için satış trendlerini analiz etmek ve hangi kategorilerin en çok satıldığını görmek için bu bileşeni kullanabilirler.
            
                        **En Çok Satan Ürünler:** Bu bileşen, her bir kategori için en çok satan ürünleri gösterir. Bu bileşen, hangi ürünlerin en popüler olduğunu ve hangi ürünlerin daha fazla reklam yapılması gerektiğini belirlemek için kullanılabilir.
            
                        **Satış Trendleri:** Bu bileşen, son 12 ayda farklı kategorilerdeki ürünlerin satış trendlerini gösterir. Kullanıcılar, hangi kategorilerin daha popüler hale geldiğini veya hangi kategorilerin daha az popüler hale geldiğini belirlemek için bu bileşeni kullanabilirler.
            
                        """)
                        with st.expander("Versiyon Bilgileri"):
                            st.write(
                            """
            
                            **Rapor Adı:** Satış Raporu 1\n
                            **Geliştirme Tarihi:** 10.04.2022\n
                            **Versiyon:** 1.0\n
                            **Son Güncelleme Tarihi:** 16.04.2022
                            """)

                    with st.container():

                        st.write("**Rapor Sayfaları PDF Görünümü**")

                        col1, col2, col3 = st.columns(3)
                        with col1:
                            if st.button('PDF Görünümünü Aç', key='1'):
                                with col2:
                                    st.subheader("Rapor Sayfaları")
                                    show_pdf('POWERBICANLI_PDF/Satıs_Dhasboard_DEV.pdf')

                            st.button('PDF Görünümünü Kapat', key='2')

                            with open("POWERBICANLI_PDF/Satıs_Dhasboard_DEV.pdf",
                                      "rb") as pdf_file:
                                PDFbyte = pdf_file.read()
                            st.download_button(label="PDF Görünümü İndir", key='3',
                                               data=PDFbyte,
                                               file_name="Rapor Görünümü.pdf",
                                               mime='application/octet-stream')

                if select_2 == "Satıs Raporu 2":
                    with st.container():
                        st.write("---")
                        st.markdown("**SATIS RAPORU 2**")
                        components.iframe(
                            "https://app.powerbi.com/view?r=eyJrIjoiNWVjNWEyYTYtNmRhNC00MTZjLTllMzYtNWI4YjI3OTQ0YWM1IiwidCI6IjlmZTNjZTM5LTIwOWQtNGM5NS1hMWQxLWViZjA0NjY3NDkyYyIsImMiOjl9",
                            height=600, width=1000)
                        st.write("---")
                        st.markdown("**Rapor Bilgiler**")
                        with st.expander("Raporun Hedef Kitlesi Kimdir?"):
                            st.write("""
    
                            Satış kontrol paneli, bir kuruluşun finansal ve satış içgörülerini sergilemek için yönetici düzeyinde bir rapor olarak oluşturulmuştur. Hedeflenen kullanıcılar yönetici seviyesindeki çalışanlar olduğu için gösterge tablosu, kullanıcıların raporu kolayca taramasına olanak tanıyan üst düzey içgörüler sunar. Kullanıcılar daha sonra, panel üzerindeki yer alan rakamların keşfetmeye değer bir içgörüyü tetiklemesi durumunda, ayrıntılı metriklere dalmak için ek seçeneğe sahip olur.
    
                            """)
                        with st.expander("Raporun Amacı Nedir?"):
                            st.write("""
                            Panonun amacı, işletmenin zaman içindeki mali performansına ilişkin üst düzey bir genel bakış sağlamaktır. Ek olarak, kullanıcıların konuma ve ürün kategorisine göre finansal performansa dalmasına olanak tanır. Bu odak alanlarının her ikisi de, kullanıcıların finansal eğilimleri ve aşırı/düşük performans alanlarını belirlemesine olanak tanır. Kullanıcılar daha sonra çabalarını nereye odaklayacaklarını belirlemek için bu ilk içgörüleri kullanabilirler.
    
    
    
    
                            """)
                        with st.expander("Raporun temel içgörüleri nelerdir?"):
                            st.write("""
    
    
                            **KPI'lar -** Gelir, Kar, Siparişler, Müşteriler, Miktar:\n
                            _‍İşletmenin mali durumunun anlık görüntüsünü sağlar_
    
                            **Alan Grafiği -** Gelir, Kar, Siparişler, Müşteriler, Miktar (12 ay):\n
                            _Kullanıcıların mevsimsel iş akışını belirlemesine yardımcı olur_
    
                            **Çubuk Grafik -** Bölge, mağaza ve ürüne göre gelir:\n
                            _Kullanıcıların coğrafyaya ve kategoriye göre mali performanslarını anlamalarına yardımcı olur_
    
                            **Çizgi Grafik -** Büyüme performansı:\n
                            _İşletmenin mali büyüme durumunun anlık görüntüsünü sağlar_
    
                            **Halka Grafik -** Kategoriler Göre Satın alma Yüzdesi:\n
                            _Ürün kategorisine göre satılan ürün adet bilgisi dağılımını sağlar._
    
    
                            """
                                     )
                        with st.expander("Rapor İçeriği:"):
                            st.write("""
    
                        Raporun amacı, bir perakende mağazasının son 12 ayda ürün satışlarını analiz etmektir. Rapor, farklı ürün kategorilerindeki satışlarını görselleştirir ve her bir kategori için bir dizi farklı gösterim içerir.
    
                        Raporun ana bileşenleri şunlardır:
    
                        **Satış Performansı:** Bu bileşen, seçilen tarih aralığındaki farklı kategorilerdeki ürünlerin satışlarını, gelirlerini, giderlerini ve satılan ürün adetlerini gösteren bir grafik sunar. Bu grafikte, farklı kategorilerin toplam satış, kar, maliyetin yanı sıra, her bir kategorideki en çok satılan ürünlerin de gösterilir.
    
                        **BÖLGE:** Bu bileşen, satışların coğrafi dağılımını harita üzerinde gösterir. Harita, farklı bölgelerdeki toplam satışları renkli bir şekilde gösterir ve kullanıcılara, farklı bölgelerdeki satışlar arasındaki farklılıkları analiz etme imkanı verir.
    
                        **Kategori Bazında Satışlar:** Bu bileşen, her bir kategori için toplam satışları ve gelirleri gösterir. Kullanıcılar, her bir kategori için satış trendlerini analiz etmek ve hangi kategorilerin en çok satıldığını görmek için bu bileşeni kullanabilirler.
    
                        **En Çok Satan Ürünler:** Bu bileşen, her bir kategori için en çok satan ürünleri gösterir. Bu bileşen, hangi ürünlerin en popüler olduğunu ve hangi ürünlerin daha fazla reklam yapılması gerektiğini belirlemek için kullanılabilir.
    
                        **Satış Trendleri:** Bu bileşen, son 12 ayda farklı kategorilerdeki ürünlerin satış trendlerini gösterir. Kullanıcılar, hangi kategorilerin daha popüler hale geldiğini veya hangi kategorilerin daha az popüler hale geldiğini belirlemek için bu bileşeni kullanabilirler.
    
                        """)
                        with st.expander("Versiyon Bilgileri"):
                            st.write(
                                """
        
                                **Rapor Adı:** Satış Raporu 1\n
                                **Geliştirme Tarihi:** 10.04.2022\n
                                **Versiyon:** 1.0\n
                                **Son Güncelleme Tarihi:** 16.04.2022
                                """)
                        with st.container():

                                st.write("**Rapor Sayfaları PDF Görünümü**")

                                col1, col2, col3 = st.columns(3)
                                with col1:
                                    if st.button('PDF Görünümünü Aç', key='1'):
                                        with col2:
                                            st.subheader("Rapor Sayfaları")
                                            show_pdf('POWERBICANLI_PDF/Satıs_Dashboard_DEV_v2.3_FINAL.pdf')

                                    st.button('PDF Görünümünü Kapat', key='2')

                                    with open("POWERBICANLI_PDF/Satıs_Dashboard_DEV_v2.3_FINAL.pdf",
                                              "rb") as pdf_file:
                                        PDFbyte = pdf_file.read()
                                    st.download_button(label="PDF Görünümü İndir", key='3',
                                                       data=PDFbyte,
                                                       file_name="Rapor Görünümü.pdf",
                                                       mime='application/octet-stream')

                if select_2 == "Satıs Raporu 3":
                    with st.container():
                        st.write("---")
                        st.markdown("**SATIS RAPORU 3**")
                        components.iframe(
                            "https://app.powerbi.com/view?r=eyJrIjoiM2QwMzM1YzUtY2VlNi00ODM5LWI2ODAtM2ZiNDEyNzkwNjQ3IiwidCI6IjlmZTNjZTM5LTIwOWQtNGM5NS1hMWQxLWViZjA0NjY3NDkyYyIsImMiOjl9",
                            height=600, width=1000)
                        st.write("---")
                        st.markdown("**Rapor Bilgiler**")
                        with st.expander("Raporun Hedef Kitlesi Kimdir?"):
                            st.write("""
    
                            Satış kontrol paneli, bir kuruluşun finansal ve satış içgörülerini sergilemek için yönetici düzeyinde bir rapor olarak oluşturulmuştur. Hedeflenen kullanıcılar yönetici seviyesindeki çalışanlar olduğu için gösterge tablosu, kullanıcıların raporu kolayca taramasına olanak tanıyan üst düzey içgörüler sunar. Kullanıcılar daha sonra, panel üzerindeki yer alan rakamların keşfetmeye değer bir içgörüyü tetiklemesi durumunda, ayrıntılı metriklere dalmak için ek seçeneğe sahip olur.
    
                            """)
                        with st.expander("Raporun Amacı Nedir?"):
                            st.write("""
                            Panonun amacı, işletmenin zaman içindeki mali performansına ilişkin üst düzey bir genel bakış sağlamaktır. Ek olarak, kullanıcıların konuma ve ürün kategorisine göre finansal performansa dalmasına olanak tanır. Bu odak alanlarının her ikisi de, kullanıcıların finansal eğilimleri ve aşırı/düşük performans alanlarını belirlemesine olanak tanır. Kullanıcılar daha sonra çabalarını nereye odaklayacaklarını belirlemek için bu ilk içgörüleri kullanabilirler.
    
    
    
    
                            """)
                        with st.expander("Raporun temel içgörüleri nelerdir?"):
                            st.write("""
    
    
                            **KPI'lar -** Gelir, Kar, Siparişler, Müşteriler, Miktar:\n
                            _‍İşletmenin mali durumunun anlık görüntüsünü sağlar_
    
                            **Alan Grafiği -** Gelir, Kar, Siparişler, Müşteriler, Miktar (12 ay):\n
                            _Kullanıcıların mevsimsel iş akışını belirlemesine yardımcı olur_
    
                            **Çubuk Grafik -** Bölge, mağaza ve ürüne göre gelir:\n
                            _Kullanıcıların coğrafyaya ve kategoriye göre mali performanslarını anlamalarına yardımcı olur_
    
                            **Çizgi Grafik -** Büyüme performansı:\n
                            _İşletmenin mali büyüme durumunun anlık görüntüsünü sağlar_
    
                            **Halka Grafik -** Kategoriler Göre Satın alma Yüzdesi:\n
                            _Ürün kategorisine göre satılan ürün adet bilgisi dağılımını sağlar._
    
    
                            """
                                     )
                        with st.expander("Rapor İçeriği:"):
                            st.write("""
    
                        Raporun amacı, bir perakende mağazasının son 12 ayda ürün satışlarını analiz etmektir. Rapor, farklı ürün kategorilerindeki satışlarını görselleştirir ve her bir kategori için bir dizi farklı gösterim içerir.
    
                        Raporun ana bileşenleri şunlardır:
    
                        **Satış Performansı:** Bu bileşen, seçilen tarih aralığındaki farklı kategorilerdeki ürünlerin satışlarını, gelirlerini, giderlerini ve satılan ürün adetlerini gösteren bir grafik sunar. Bu grafikte, farklı kategorilerin toplam satış, kar, maliyetin yanı sıra, her bir kategorideki en çok satılan ürünlerin de gösterilir.
    
                        **BÖLGE:** Bu bileşen, satışların coğrafi dağılımını harita üzerinde gösterir. Harita, farklı bölgelerdeki toplam satışları renkli bir şekilde gösterir ve kullanıcılara, farklı bölgelerdeki satışlar arasındaki farklılıkları analiz etme imkanı verir.
    
                        **Kategori Bazında Satışlar:** Bu bileşen, her bir kategori için toplam satışları ve gelirleri gösterir. Kullanıcılar, her bir kategori için satış trendlerini analiz etmek ve hangi kategorilerin en çok satıldığını görmek için bu bileşeni kullanabilirler.
    
                        **En Çok Satan Ürünler:** Bu bileşen, her bir kategori için en çok satan ürünleri gösterir. Bu bileşen, hangi ürünlerin en popüler olduğunu ve hangi ürünlerin daha fazla reklam yapılması gerektiğini belirlemek için kullanılabilir.
    
                        **Satış Trendleri:** Bu bileşen, son 12 ayda farklı kategorilerdeki ürünlerin satış trendlerini gösterir. Kullanıcılar, hangi kategorilerin daha popüler hale geldiğini veya hangi kategorilerin daha az popüler hale geldiğini belirlemek için bu bileşeni kullanabilirler.
    
                        """)
                        with st.expander("Versiyon Bilgileri"):
                            st.write(
                                """
    
                                **Rapor Adı:** Satış Raporu 1\n
                                **Geliştirme Tarihi:** 10.04.2022\n
                                **Versiyon:** 1.0\n
                                **Son Güncelleme Tarihi:** 16.04.2022
                                """)
                        with st.container():
                            st.write("**Rapor Sayfaları PDF Görünümü**")

                            col1, col2, col3 = st.columns(3)
                            with col1:
                                if st.button('PDF Görünümünü Aç', key='1'):
                                    with col2:
                                        st.subheader("Rapor Sayfaları")
                                        show_pdf('POWERBICANLI_PDF/Satıs_Dashboard_v3.pdf')

                                st.button('PDF Görünümünü Kapat', key='2')

                                with open("POWERBICANLI_PDF/Satıs_Dashboard_v3.pdf",
                                          "rb") as pdf_file:
                                    PDFbyte = pdf_file.read()
                                st.download_button(label="PDF Görünümü İndir", key='3',
                                                   data=PDFbyte,
                                                   file_name="Rapor Görünümü.pdf",
                                                   mime='application/octet-stream') ## RAPOR GÖRÜBÜRA #

                if select_2 == "Satıs Raporu 4":
                    with st.container():
                        st.write("---")
                        st.markdown("**SATIS RAPORU 4**")
                        components.iframe(
                            "https://app.powerbi.com/view?r=eyJrIjoiZTc5NzJhYzItYjU4Ny00MzkwLWJmMjMtODU1Y2M0ZTFmOGI3IiwidCI6IjlmZTNjZTM5LTIwOWQtNGM5NS1hMWQxLWViZjA0NjY3NDkyYyIsImMiOjl9",
                            height=600, width=1000)
                        st.write("---")
                        st.markdown("**Rapor Bilgiler**")
                        with st.expander("Raporun Hedef Kitlesi Kimdir?"):
                            st.write("""
    
                            Satış kontrol paneli, bir kuruluşun finansal ve satış içgörülerini sergilemek için yönetici düzeyinde bir rapor olarak oluşturulmuştur. Hedeflenen kullanıcılar yönetici seviyesindeki çalışanlar olduğu için gösterge tablosu, kullanıcıların raporu kolayca taramasına olanak tanıyan üst düzey içgörüler sunar. Kullanıcılar daha sonra, panel üzerindeki yer alan rakamların keşfetmeye değer bir içgörüyü tetiklemesi durumunda, ayrıntılı metriklere dalmak için ek seçeneğe sahip olur.
    
                            """)
                        with st.expander("Raporun Amacı Nedir?"):
                            st.write("""
                            Panonun amacı, işletmenin zaman içindeki mali performansına ilişkin üst düzey bir genel bakış sağlamaktır. Ek olarak, kullanıcıların konuma ve ürün kategorisine göre finansal performansa dalmasına olanak tanır. Bu odak alanlarının her ikisi de, kullanıcıların finansal eğilimleri ve aşırı/düşük performans alanlarını belirlemesine olanak tanır. Kullanıcılar daha sonra çabalarını nereye odaklayacaklarını belirlemek için bu ilk içgörüleri kullanabilirler.
    
    
    
    
                            """)
                        with st.expander("Raporun temel içgörüleri nelerdir?"):
                            st.write("""
    
    
                            **KPI'lar -** Gelir, Kar, Siparişler, Müşteriler, Miktar:\n
                            _‍İşletmenin mali durumunun anlık görüntüsünü sağlar_
    
                            **Alan Grafiği -** Gelir, Kar, Siparişler, Müşteriler, Miktar (12 ay):\n
                            _Kullanıcıların mevsimsel iş akışını belirlemesine yardımcı olur_
    
                            **Çubuk Grafik -** Bölge, mağaza ve ürüne göre gelir:\n
                            _Kullanıcıların coğrafyaya ve kategoriye göre mali performanslarını anlamalarına yardımcı olur_
    
                            **Çizgi Grafik -** Büyüme performansı:\n
                            _İşletmenin mali büyüme durumunun anlık görüntüsünü sağlar_
    
                            **Halka Grafik -** Kategoriler Göre Satın alma Yüzdesi:\n
                            _Ürün kategorisine göre satılan ürün adet bilgisi dağılımını sağlar._
    
    
                            """
                                     )
                        with st.expander("Rapor İçeriği:"):
                            st.write("""
    
                        Raporun amacı, bir perakende mağazasının son 12 ayda ürün satışlarını analiz etmektir. Rapor, farklı ürün kategorilerindeki satışlarını görselleştirir ve her bir kategori için bir dizi farklı gösterim içerir.
    
                        Raporun ana bileşenleri şunlardır:
    
                        **Satış Performansı:** Bu bileşen, seçilen tarih aralığındaki farklı kategorilerdeki ürünlerin satışlarını, gelirlerini, giderlerini ve satılan ürün adetlerini gösteren bir grafik sunar. Bu grafikte, farklı kategorilerin toplam satış, kar, maliyetin yanı sıra, her bir kategorideki en çok satılan ürünlerin de gösterilir.
    
                        **BÖLGE:** Bu bileşen, satışların coğrafi dağılımını harita üzerinde gösterir. Harita, farklı bölgelerdeki toplam satışları renkli bir şekilde gösterir ve kullanıcılara, farklı bölgelerdeki satışlar arasındaki farklılıkları analiz etme imkanı verir.
    
                        **Kategori Bazında Satışlar:** Bu bileşen, her bir kategori için toplam satışları ve gelirleri gösterir. Kullanıcılar, her bir kategori için satış trendlerini analiz etmek ve hangi kategorilerin en çok satıldığını görmek için bu bileşeni kullanabilirler.
    
                        **En Çok Satan Ürünler:** Bu bileşen, her bir kategori için en çok satan ürünleri gösterir. Bu bileşen, hangi ürünlerin en popüler olduğunu ve hangi ürünlerin daha fazla reklam yapılması gerektiğini belirlemek için kullanılabilir.
    
                        **Satış Trendleri:** Bu bileşen, son 12 ayda farklı kategorilerdeki ürünlerin satış trendlerini gösterir. Kullanıcılar, hangi kategorilerin daha popüler hale geldiğini veya hangi kategorilerin daha az popüler hale geldiğini belirlemek için bu bileşeni kullanabilirler.
    
                        """)
                        with st.expander("Versiyon Bilgileri"):
                            st.write(
                                """
    
                                **Rapor Adı:** Satış Raporu 1\n
                                **Geliştirme Tarihi:** 10.04.2022\n
                                **Versiyon:** 1.0\n
                                **Son Güncelleme Tarihi:** 16.04.2022
                                """)
                        with st.container():
                            st.write("**Rapor Sayfaları PDF Görünümü**")

                            col1, col2, col3 = st.columns(3)
                            with col1:
                                if st.button('PDF Görünümünü Aç', key='1'):
                                    with col2:
                                        st.subheader("Rapor Sayfaları")
                                        show_pdf('POWERBICANLI_PDF/Satıs_Dhasboard_DEV_WHITE.pdf')

                                st.button('PDF Görünümünü Kapat', key='2')

                                with open("POWERBICANLI_PDF/Satıs_Dhasboard_DEV_WHITE.pdf",
                                          "rb") as pdf_file:
                                    PDFbyte = pdf_file.read()
                                st.download_button(label="PDF Görünümü İndir", key='3',
                                                   data=PDFbyte,
                                                   file_name="Rapor Görünümü.pdf",
                                                   mime='application/octet-stream') ## RAPOR GÖRÜBÜRA #

                if select_2 == "Finans Dashboard(Satıs)":
                    with st.container():
                        st.write("---")
                        st.markdown("**Finans Dashboard(Satıs)**")
                        components.iframe(
                            "https://app.powerbi.com/view?r=eyJrIjoiNjc3MTNhMGUtYTE5OS00ZDE2LWE1MmYtMmJhNDY5M2Q4MDJjIiwidCI6IjlmZTNjZTM5LTIwOWQtNGM5NS1hMWQxLWViZjA0NjY3NDkyYyIsImMiOjl9",
                            height=600, width=1000)
                        st.write("---")
                        st.markdown("**Rapor Bilgiler**")
                        with st.expander("Raporun Hedef Kitlesi Kimdir?"):
                            st.write("""
    
                            Satış kontrol paneli, bir kuruluşun finansal ve satış içgörülerini sergilemek için yönetici düzeyinde bir rapor olarak oluşturulmuştur. Hedeflenen kullanıcılar yönetici seviyesindeki çalışanlar olduğu için gösterge tablosu, kullanıcıların raporu kolayca taramasına olanak tanıyan üst düzey içgörüler sunar. Kullanıcılar daha sonra, panel üzerindeki yer alan rakamların keşfetmeye değer bir içgörüyü tetiklemesi durumunda, ayrıntılı metriklere dalmak için ek seçeneğe sahip olur.
    
                            """)
                        with st.expander("Raporun Amacı Nedir?"):
                            st.write("""
                            Panonun amacı, işletmenin zaman içindeki mali performansına ilişkin üst düzey bir genel bakış sağlamaktır. Ek olarak, kullanıcıların konuma ve ürün kategorisine göre finansal performansa dalmasına olanak tanır. Bu odak alanlarının her ikisi de, kullanıcıların finansal eğilimleri ve aşırı/düşük performans alanlarını belirlemesine olanak tanır. Kullanıcılar daha sonra çabalarını nereye odaklayacaklarını belirlemek için bu ilk içgörüleri kullanabilirler.
    
    
    
    
                            """)
                        with st.expander("Raporun temel içgörüleri nelerdir?"):
                            st.write("""
    
    
                            **KPI'lar -** Gelir, Kar, Siparişler, Müşteriler, Miktar:\n
                            _‍İşletmenin mali durumunun anlık görüntüsünü sağlar_
    
                            **Alan Grafiği -** Gelir, Kar, Siparişler, Müşteriler, Miktar (12 ay):\n
                            _Kullanıcıların mevsimsel iş akışını belirlemesine yardımcı olur_
    
                            **Çubuk Grafik -** Bölge, mağaza ve ürüne göre gelir:\n
                            _Kullanıcıların coğrafyaya ve kategoriye göre mali performanslarını anlamalarına yardımcı olur_
    
                            **Çizgi Grafik -** Büyüme performansı:\n
                            _İşletmenin mali büyüme durumunun anlık görüntüsünü sağlar_
    
                            **Halka Grafik -** Kategoriler Göre Satın alma Yüzdesi:\n
                            _Ürün kategorisine göre satılan ürün adet bilgisi dağılımını sağlar._
    
    
                            """
                                     )
                        with st.expander("Rapor İçeriği:"):
                            st.write("""
    
                        Raporun amacı, bir perakende mağazasının son 12 ayda ürün satışlarını analiz etmektir. Rapor, farklı ürün kategorilerindeki satışlarını görselleştirir ve her bir kategori için bir dizi farklı gösterim içerir.
    
                        Raporun ana bileşenleri şunlardır:
    
                        **Satış Performansı:** Bu bileşen, seçilen tarih aralığındaki farklı kategorilerdeki ürünlerin satışlarını, gelirlerini, giderlerini ve satılan ürün adetlerini gösteren bir grafik sunar. Bu grafikte, farklı kategorilerin toplam satış, kar, maliyetin yanı sıra, her bir kategorideki en çok satılan ürünlerin de gösterilir.
    
                        **BÖLGE:** Bu bileşen, satışların coğrafi dağılımını harita üzerinde gösterir. Harita, farklı bölgelerdeki toplam satışları renkli bir şekilde gösterir ve kullanıcılara, farklı bölgelerdeki satışlar arasındaki farklılıkları analiz etme imkanı verir.
    
                        **Kategori Bazında Satışlar:** Bu bileşen, her bir kategori için toplam satışları ve gelirleri gösterir. Kullanıcılar, her bir kategori için satış trendlerini analiz etmek ve hangi kategorilerin en çok satıldığını görmek için bu bileşeni kullanabilirler.
    
                        **En Çok Satan Ürünler:** Bu bileşen, her bir kategori için en çok satan ürünleri gösterir. Bu bileşen, hangi ürünlerin en popüler olduğunu ve hangi ürünlerin daha fazla reklam yapılması gerektiğini belirlemek için kullanılabilir.
    
                        **Satış Trendleri:** Bu bileşen, son 12 ayda farklı kategorilerdeki ürünlerin satış trendlerini gösterir. Kullanıcılar, hangi kategorilerin daha popüler hale geldiğini veya hangi kategorilerin daha az popüler hale geldiğini belirlemek için bu bileşeni kullanabilirler.
    
                        """)
                        with st.expander("Versiyon Bilgileri"):
                            st.write(
                                """
    
                                **Rapor Adı:** Satış Raporu 1\n
                                **Geliştirme Tarihi:** 10.04.2022\n
                                **Versiyon:** 1.0\n
                                **Son Güncelleme Tarihi:** 16.04.2022
                                """)
                        with st.container():
                            st.write("**Rapor Sayfaları PDF Görünümü**")

                            col1, col2, col3 = st.columns(3)
                            with col1:
                                if st.button('PDF Görünümünü Aç', key='1'):
                                    with col2:
                                        st.subheader("Rapor Sayfaları")
                                        show_pdf('POWERBICANLI_PDF/1_Finans Dashboard.pdf')

                                st.button('PDF Görünümünü Kapat', key='2')

                                with open("POWERBICANLI_PDF/1_Finans Dashboard.pdf",
                                          "rb") as pdf_file:
                                    PDFbyte = pdf_file.read()
                                st.download_button(label="PDF Görünümü İndir", key='3',
                                                   data=PDFbyte,
                                                   file_name="Rapor Görünümü.pdf",
                                                   mime='application/octet-stream') ## RAPOR GÖRÜBÜRA #

                if select_2 == "CEO Dashboard(Satıs)":
                    with st.container():
                        st.write("---")
                        st.markdown("**CEO Dashboard(Satıs)**")
                        components.iframe(
                            "https://app.powerbi.com/view?r=eyJrIjoiZDc5NzFlMGYtODliMy00M2E0LTg3NWQtNDU4MDI2Y2NlMjU4IiwidCI6IjlmZTNjZTM5LTIwOWQtNGM5NS1hMWQxLWViZjA0NjY3NDkyYyIsImMiOjl9",
                            height=600, width=1000)
                        st.write("---")
                        st.markdown("**Rapor Bilgiler**")
                        with st.expander("Raporun Hedef Kitlesi Kimdir?"):
                            st.write("""
    
                            Satış kontrol paneli, bir kuruluşun finansal ve satış içgörülerini sergilemek için yönetici düzeyinde bir rapor olarak oluşturulmuştur. Hedeflenen kullanıcılar yönetici seviyesindeki çalışanlar olduğu için gösterge tablosu, kullanıcıların raporu kolayca taramasına olanak tanıyan üst düzey içgörüler sunar. Kullanıcılar daha sonra, panel üzerindeki yer alan rakamların keşfetmeye değer bir içgörüyü tetiklemesi durumunda, ayrıntılı metriklere dalmak için ek seçeneğe sahip olur.
    
                            """)
                        with st.expander("Raporun Amacı Nedir?"):
                            st.write("""
                            Panonun amacı, işletmenin zaman içindeki mali performansına ilişkin üst düzey bir genel bakış sağlamaktır. Ek olarak, kullanıcıların konuma ve ürün kategorisine göre finansal performansa dalmasına olanak tanır. Bu odak alanlarının her ikisi de, kullanıcıların finansal eğilimleri ve aşırı/düşük performans alanlarını belirlemesine olanak tanır. Kullanıcılar daha sonra çabalarını nereye odaklayacaklarını belirlemek için bu ilk içgörüleri kullanabilirler.
    
    
    
    
                            """)
                        with st.expander("Raporun temel içgörüleri nelerdir?"):
                            st.write("""
    
    
                            **KPI'lar -** Gelir, Kar, Siparişler, Müşteriler, Miktar:\n
                            _‍İşletmenin mali durumunun anlık görüntüsünü sağlar_
    
                            **Alan Grafiği -** Gelir, Kar, Siparişler, Müşteriler, Miktar (12 ay):\n
                            _Kullanıcıların mevsimsel iş akışını belirlemesine yardımcı olur_
    
                            **Çubuk Grafik -** Bölge, mağaza ve ürüne göre gelir:\n
                            _Kullanıcıların coğrafyaya ve kategoriye göre mali performanslarını anlamalarına yardımcı olur_
    
                            **Çizgi Grafik -** Büyüme performansı:\n
                            _İşletmenin mali büyüme durumunun anlık görüntüsünü sağlar_
    
                            **Halka Grafik -** Kategoriler Göre Satın alma Yüzdesi:\n
                            _Ürün kategorisine göre satılan ürün adet bilgisi dağılımını sağlar._
    
    
                            """
                                     )
                        with st.expander("Rapor İçeriği:"):
                            st.write("""
    
                        Raporun amacı, bir perakende mağazasının son 12 ayda ürün satışlarını analiz etmektir. Rapor, farklı ürün kategorilerindeki satışlarını görselleştirir ve her bir kategori için bir dizi farklı gösterim içerir.
    
                        Raporun ana bileşenleri şunlardır:
    
                        **Satış Performansı:** Bu bileşen, seçilen tarih aralığındaki farklı kategorilerdeki ürünlerin satışlarını, gelirlerini, giderlerini ve satılan ürün adetlerini gösteren bir grafik sunar. Bu grafikte, farklı kategorilerin toplam satış, kar, maliyetin yanı sıra, her bir kategorideki en çok satılan ürünlerin de gösterilir.
    
                        **BÖLGE:** Bu bileşen, satışların coğrafi dağılımını harita üzerinde gösterir. Harita, farklı bölgelerdeki toplam satışları renkli bir şekilde gösterir ve kullanıcılara, farklı bölgelerdeki satışlar arasındaki farklılıkları analiz etme imkanı verir.
    
                        **Kategori Bazında Satışlar:** Bu bileşen, her bir kategori için toplam satışları ve gelirleri gösterir. Kullanıcılar, her bir kategori için satış trendlerini analiz etmek ve hangi kategorilerin en çok satıldığını görmek için bu bileşeni kullanabilirler.
    
                        **En Çok Satan Ürünler:** Bu bileşen, her bir kategori için en çok satan ürünleri gösterir. Bu bileşen, hangi ürünlerin en popüler olduğunu ve hangi ürünlerin daha fazla reklam yapılması gerektiğini belirlemek için kullanılabilir.
    
                        **Satış Trendleri:** Bu bileşen, son 12 ayda farklı kategorilerdeki ürünlerin satış trendlerini gösterir. Kullanıcılar, hangi kategorilerin daha popüler hale geldiğini veya hangi kategorilerin daha az popüler hale geldiğini belirlemek için bu bileşeni kullanabilirler.
    
                        """)
                        with st.expander("Versiyon Bilgileri"):
                            st.write(
                                """
    
                                **Rapor Adı:** Satış Raporu 1\n
                                **Geliştirme Tarihi:** 10.04.2022\n
                                **Versiyon:** 1.0\n
                                **Son Güncelleme Tarihi:** 16.04.2022
                                """)
                        with st.container():
                            st.write("**Rapor Sayfaları PDF Görünümü**")

                            col1, col2, col3 = st.columns(3)
                            with col1:
                                if st.button('PDF Görünümünü Aç', key='1'):
                                    with col2:
                                        st.subheader("Rapor Sayfaları")
                                        show_pdf('POWERBICANLI_PDF/1_Yonetici Dashboard.pdf')

                                st.button('PDF Görünümünü Kapat', key='2')

                                with open("POWERBICANLI_PDF/1_Yonetici Dashboard.pdf",
                                          "rb") as pdf_file:
                                    PDFbyte = pdf_file.read()
                                st.download_button(label="PDF Görünümü İndir", key='3',
                                                   data=PDFbyte,
                                                   file_name="Rapor Görünümü.pdf",
                                                   mime='application/octet-stream') ## RAPOR GÖRÜBÜRA #

                if select_2 == "Satıs Raporu 5":
                    with st.container():
                        st.write("---")
                        st.markdown("**SATIS RAPORU 5**")
                        components.iframe(
                            "https://app.powerbi.com/view?r=eyJrIjoiMDgzOTIzNTMtYjFiMy00NGMyLWI0NzUtYTNiMzYxMTQ5OTljIiwidCI6IjlmZTNjZTM5LTIwOWQtNGM5NS1hMWQxLWViZjA0NjY3NDkyYyIsImMiOjl9",
                            height=600, width=1000)
                        st.write("---")
                        st.markdown("**Rapor Bilgiler**")
                        with st.expander("Raporun Hedef Kitlesi Kimdir?"):
                            st.write("""

                            Satış kontrol paneli, bir kuruluşun finansal ve satış içgörülerini sergilemek için yönetici düzeyinde bir rapor olarak oluşturulmuştur. Hedeflenen kullanıcılar yönetici seviyesindeki çalışanlar olduğu için gösterge tablosu, kullanıcıların raporu kolayca taramasına olanak tanıyan üst düzey içgörüler sunar. Kullanıcılar daha sonra, panel üzerindeki yer alan rakamların keşfetmeye değer bir içgörüyü tetiklemesi durumunda, ayrıntılı metriklere dalmak için ek seçeneğe sahip olur.

                            """)
                        with st.expander("Raporun Amacı Nedir?"):
                            st.write("""
                            Panonun amacı, işletmenin zaman içindeki mali performansına ilişkin üst düzey bir genel bakış sağlamaktır. Ek olarak, kullanıcıların konuma ve ürün kategorisine göre finansal performansa dalmasına olanak tanır. Bu odak alanlarının her ikisi de, kullanıcıların finansal eğilimleri ve aşırı/düşük performans alanlarını belirlemesine olanak tanır. Kullanıcılar daha sonra çabalarını nereye odaklayacaklarını belirlemek için bu ilk içgörüleri kullanabilirler.




                            """)
                        with st.expander("Raporun temel içgörüleri nelerdir?"):
                            st.write("""


                            **KPI'lar -** Gelir, Kar, Siparişler, Müşteriler, Miktar:\n
                            _‍İşletmenin mali durumunun anlık görüntüsünü sağlar_

                            **Alan Grafiği -** Gelir, Kar, Siparişler, Müşteriler, Miktar (12 ay):\n
                            _Kullanıcıların mevsimsel iş akışını belirlemesine yardımcı olur_

                            **Çubuk Grafik -** Bölge, mağaza ve ürüne göre gelir:\n
                            _Kullanıcıların coğrafyaya ve kategoriye göre mali performanslarını anlamalarına yardımcı olur_

                            **Çizgi Grafik -** Büyüme performansı:\n
                            _İşletmenin mali büyüme durumunun anlık görüntüsünü sağlar_

                            **Halka Grafik -** Kategoriler Göre Satın alma Yüzdesi:\n
                            _Ürün kategorisine göre satılan ürün adet bilgisi dağılımını sağlar._


                            """
                                     )
                        with st.expander("Rapor İçeriği:"):
                            st.write("""

                        Raporun amacı, bir perakende mağazasının son 12 ayda ürün satışlarını analiz etmektir. Rapor, farklı ürün kategorilerindeki satışlarını görselleştirir ve her bir kategori için bir dizi farklı gösterim içerir.

                        Raporun ana bileşenleri şunlardır:

                        **Satış Performansı:** Bu bileşen, seçilen tarih aralığındaki farklı kategorilerdeki ürünlerin satışlarını, gelirlerini, giderlerini ve satılan ürün adetlerini gösteren bir grafik sunar. Bu grafikte, farklı kategorilerin toplam satış, kar, maliyetin yanı sıra, her bir kategorideki en çok satılan ürünlerin de gösterilir.

                        **BÖLGE:** Bu bileşen, satışların coğrafi dağılımını harita üzerinde gösterir. Harita, farklı bölgelerdeki toplam satışları renkli bir şekilde gösterir ve kullanıcılara, farklı bölgelerdeki satışlar arasındaki farklılıkları analiz etme imkanı verir.

                        **Kategori Bazında Satışlar:** Bu bileşen, her bir kategori için toplam satışları ve gelirleri gösterir. Kullanıcılar, her bir kategori için satış trendlerini analiz etmek ve hangi kategorilerin en çok satıldığını görmek için bu bileşeni kullanabilirler.

                        **En Çok Satan Ürünler:** Bu bileşen, her bir kategori için en çok satan ürünleri gösterir. Bu bileşen, hangi ürünlerin en popüler olduğunu ve hangi ürünlerin daha fazla reklam yapılması gerektiğini belirlemek için kullanılabilir.

                        **Satış Trendleri:** Bu bileşen, son 12 ayda farklı kategorilerdeki ürünlerin satış trendlerini gösterir. Kullanıcılar, hangi kategorilerin daha popüler hale geldiğini veya hangi kategorilerin daha az popüler hale geldiğini belirlemek için bu bileşeni kullanabilirler.

                        """)
                        with st.expander("Versiyon Bilgileri"):
                            st.write(
                                """

                                **Rapor Adı:** Satış Raporu 1\n
                                **Geliştirme Tarihi:** 10.04.2022\n
                                **Versiyon:** 1.0\n
                                **Son Güncelleme Tarihi:** 16.04.2022
                                """)
                        with st.container():
                            st.write("**Rapor Sayfaları PDF Görünümü**")

                            col1, col2, col3 = st.columns(3)
                            with col1:
                                if st.button('PDF Görünümünü Aç', key='1'):
                                    with col2:
                                        st.subheader("Rapor Sayfaları")
                                        show_pdf('POWERBICANLI_PDF/5_Bolge Performans.pdf')

                                st.button('PDF Görünümünü Kapat', key='2')

                                with open("POWERBICANLI_PDF/5_Bolge Performans.pdf",
                                          "rb") as pdf_file:
                                    PDFbyte = pdf_file.read()
                                st.download_button(label="PDF Görünümü İndir", key='3',
                                                   data=PDFbyte,
                                                   file_name="Rapor Görünümü.pdf",
                                                   mime='application/octet-stream')  ## RAPOR GÖRÜBÜRA #

                if select_2 == "Satıs Raporu 6":
                    with st.container():
                        st.write("---")
                        st.markdown("**SATIS RAPORU 6**")
                        components.iframe(
                            "https://app.powerbi.com/view?r=eyJrIjoiMzE2Mjg4NzctNWNjNS00MjgwLWJmOGEtNDQ5MmFiNzViZjYxIiwidCI6IjlmZTNjZTM5LTIwOWQtNGM5NS1hMWQxLWViZjA0NjY3NDkyYyIsImMiOjl9",
                            height=600, width=1000)
                        st.write("---")
                        st.markdown("**Rapor Bilgiler**")
                        with st.expander("Raporun Hedef Kitlesi Kimdir?"):
                            st.write("""

                            Satış kontrol paneli, bir kuruluşun finansal ve satış içgörülerini sergilemek için yönetici düzeyinde bir rapor olarak oluşturulmuştur. Hedeflenen kullanıcılar yönetici seviyesindeki çalışanlar olduğu için gösterge tablosu, kullanıcıların raporu kolayca taramasına olanak tanıyan üst düzey içgörüler sunar. Kullanıcılar daha sonra, panel üzerindeki yer alan rakamların keşfetmeye değer bir içgörüyü tetiklemesi durumunda, ayrıntılı metriklere dalmak için ek seçeneğe sahip olur.

                            """)
                        with st.expander("Raporun Amacı Nedir?"):
                            st.write("""
                            Panonun amacı, işletmenin zaman içindeki mali performansına ilişkin üst düzey bir genel bakış sağlamaktır. Ek olarak, kullanıcıların konuma ve ürün kategorisine göre finansal performansa dalmasına olanak tanır. Bu odak alanlarının her ikisi de, kullanıcıların finansal eğilimleri ve aşırı/düşük performans alanlarını belirlemesine olanak tanır. Kullanıcılar daha sonra çabalarını nereye odaklayacaklarını belirlemek için bu ilk içgörüleri kullanabilirler.




                            """)
                        with st.expander("Raporun temel içgörüleri nelerdir?"):
                            st.write("""


                            **KPI'lar -** Gelir, Kar, Siparişler, Müşteriler, Miktar:\n
                            _‍İşletmenin mali durumunun anlık görüntüsünü sağlar_

                            **Alan Grafiği -** Gelir, Kar, Siparişler, Müşteriler, Miktar (12 ay):\n
                            _Kullanıcıların mevsimsel iş akışını belirlemesine yardımcı olur_

                            **Çubuk Grafik -** Bölge, mağaza ve ürüne göre gelir:\n
                            _Kullanıcıların coğrafyaya ve kategoriye göre mali performanslarını anlamalarına yardımcı olur_

                            **Çizgi Grafik -** Büyüme performansı:\n
                            _İşletmenin mali büyüme durumunun anlık görüntüsünü sağlar_

                            **Halka Grafik -** Kategoriler Göre Satın alma Yüzdesi:\n
                            _Ürün kategorisine göre satılan ürün adet bilgisi dağılımını sağlar._


                            """
                                     )
                        with st.expander("Rapor İçeriği:"):
                            st.write("""

                        Raporun amacı, bir perakende mağazasının son 12 ayda ürün satışlarını analiz etmektir. Rapor, farklı ürün kategorilerindeki satışlarını görselleştirir ve her bir kategori için bir dizi farklı gösterim içerir.

                        Raporun ana bileşenleri şunlardır:

                        **Satış Performansı:** Bu bileşen, seçilen tarih aralığındaki farklı kategorilerdeki ürünlerin satışlarını, gelirlerini, giderlerini ve satılan ürün adetlerini gösteren bir grafik sunar. Bu grafikte, farklı kategorilerin toplam satış, kar, maliyetin yanı sıra, her bir kategorideki en çok satılan ürünlerin de gösterilir.

                        **BÖLGE:** Bu bileşen, satışların coğrafi dağılımını harita üzerinde gösterir. Harita, farklı bölgelerdeki toplam satışları renkli bir şekilde gösterir ve kullanıcılara, farklı bölgelerdeki satışlar arasındaki farklılıkları analiz etme imkanı verir.

                        **Kategori Bazında Satışlar:** Bu bileşen, her bir kategori için toplam satışları ve gelirleri gösterir. Kullanıcılar, her bir kategori için satış trendlerini analiz etmek ve hangi kategorilerin en çok satıldığını görmek için bu bileşeni kullanabilirler.

                        **En Çok Satan Ürünler:** Bu bileşen, her bir kategori için en çok satan ürünleri gösterir. Bu bileşen, hangi ürünlerin en popüler olduğunu ve hangi ürünlerin daha fazla reklam yapılması gerektiğini belirlemek için kullanılabilir.

                        **Satış Trendleri:** Bu bileşen, son 12 ayda farklı kategorilerdeki ürünlerin satış trendlerini gösterir. Kullanıcılar, hangi kategorilerin daha popüler hale geldiğini veya hangi kategorilerin daha az popüler hale geldiğini belirlemek için bu bileşeni kullanabilirler.

                        """)
                        with st.expander("Versiyon Bilgileri"):
                            st.write(
                                """

                                **Rapor Adı:** Satış Raporu 1\n
                                **Geliştirme Tarihi:** 10.04.2022\n
                                **Versiyon:** 1.0\n
                                **Son Güncelleme Tarihi:** 16.04.2022
                                """)
                        with st.container():
                            st.write("**Rapor Sayfaları PDF Görünümü**")

                            col1, col2, col3 = st.columns(3)
                            with col1:
                                if st.button('PDF Görünümünü Aç', key='1'):
                                    with col2:
                                        st.subheader("Rapor Sayfaları")
                                        show_pdf('POWERBICANLI_PDF/6_DonanımSatıs.pdf')

                                st.button('PDF Görünümünü Kapat', key='2')

                                with open("POWERBICANLI_PDF/6_DonanımSatıs.pdf",
                                          "rb") as pdf_file:
                                    PDFbyte = pdf_file.read()
                                st.download_button(label="PDF Görünümü İndir", key='3',
                                                   data=PDFbyte,
                                                   file_name="Rapor Görünümü.pdf",
                                                   mime='application/octet-stream')  ## RAPOR GÖRÜBÜRA #

                if select_2 == "Satıs Raporu 7":
                    with st.container():
                        st.write("---")
                        st.markdown("**SATIS RAPORU 7**")
                        components.iframe(
                            "https://app.powerbi.com/view?r=eyJrIjoiZjlmMjRhY2EtYjg2OS00ZWY3LWE1ZTUtN2ZiMTQ0MzhmMWI5IiwidCI6IjlmZTNjZTM5LTIwOWQtNGM5NS1hMWQxLWViZjA0NjY3NDkyYyIsImMiOjl9",
                            height=600, width=1000)
                        st.write("---")
                        st.markdown("**Rapor Bilgiler**")
                        with st.expander("Raporun Hedef Kitlesi Kimdir?"):
                            st.write("""

                            Satış kontrol paneli, bir kuruluşun finansal ve satış içgörülerini sergilemek için yönetici düzeyinde bir rapor olarak oluşturulmuştur. Hedeflenen kullanıcılar yönetici seviyesindeki çalışanlar olduğu için gösterge tablosu, kullanıcıların raporu kolayca taramasına olanak tanıyan üst düzey içgörüler sunar. Kullanıcılar daha sonra, panel üzerindeki yer alan rakamların keşfetmeye değer bir içgörüyü tetiklemesi durumunda, ayrıntılı metriklere dalmak için ek seçeneğe sahip olur.

                            """)
                        with st.expander("Raporun Amacı Nedir?"):
                            st.write("""
                            Panonun amacı, işletmenin zaman içindeki mali performansına ilişkin üst düzey bir genel bakış sağlamaktır. Ek olarak, kullanıcıların konuma ve ürün kategorisine göre finansal performansa dalmasına olanak tanır. Bu odak alanlarının her ikisi de, kullanıcıların finansal eğilimleri ve aşırı/düşük performans alanlarını belirlemesine olanak tanır. Kullanıcılar daha sonra çabalarını nereye odaklayacaklarını belirlemek için bu ilk içgörüleri kullanabilirler.




                            """)
                        with st.expander("Raporun temel içgörüleri nelerdir?"):
                            st.write("""


                            **KPI'lar -** Gelir, Kar, Siparişler, Müşteriler, Miktar:\n
                            _‍İşletmenin mali durumunun anlık görüntüsünü sağlar_

                            **Alan Grafiği -** Gelir, Kar, Siparişler, Müşteriler, Miktar (12 ay):\n
                            _Kullanıcıların mevsimsel iş akışını belirlemesine yardımcı olur_

                            **Çubuk Grafik -** Bölge, mağaza ve ürüne göre gelir:\n
                            _Kullanıcıların coğrafyaya ve kategoriye göre mali performanslarını anlamalarına yardımcı olur_

                            **Çizgi Grafik -** Büyüme performansı:\n
                            _İşletmenin mali büyüme durumunun anlık görüntüsünü sağlar_

                            **Halka Grafik -** Kategoriler Göre Satın alma Yüzdesi:\n
                            _Ürün kategorisine göre satılan ürün adet bilgisi dağılımını sağlar._


                            """
                                     )
                        with st.expander("Rapor İçeriği:"):
                            st.write("""

                        Raporun amacı, bir perakende mağazasının son 12 ayda ürün satışlarını analiz etmektir. Rapor, farklı ürün kategorilerindeki satışlarını görselleştirir ve her bir kategori için bir dizi farklı gösterim içerir.

                        Raporun ana bileşenleri şunlardır:

                        **Satış Performansı:** Bu bileşen, seçilen tarih aralığındaki farklı kategorilerdeki ürünlerin satışlarını, gelirlerini, giderlerini ve satılan ürün adetlerini gösteren bir grafik sunar. Bu grafikte, farklı kategorilerin toplam satış, kar, maliyetin yanı sıra, her bir kategorideki en çok satılan ürünlerin de gösterilir.

                        **BÖLGE:** Bu bileşen, satışların coğrafi dağılımını harita üzerinde gösterir. Harita, farklı bölgelerdeki toplam satışları renkli bir şekilde gösterir ve kullanıcılara, farklı bölgelerdeki satışlar arasındaki farklılıkları analiz etme imkanı verir.

                        **Kategori Bazında Satışlar:** Bu bileşen, her bir kategori için toplam satışları ve gelirleri gösterir. Kullanıcılar, her bir kategori için satış trendlerini analiz etmek ve hangi kategorilerin en çok satıldığını görmek için bu bileşeni kullanabilirler.

                        **En Çok Satan Ürünler:** Bu bileşen, her bir kategori için en çok satan ürünleri gösterir. Bu bileşen, hangi ürünlerin en popüler olduğunu ve hangi ürünlerin daha fazla reklam yapılması gerektiğini belirlemek için kullanılabilir.

                        **Satış Trendleri:** Bu bileşen, son 12 ayda farklı kategorilerdeki ürünlerin satış trendlerini gösterir. Kullanıcılar, hangi kategorilerin daha popüler hale geldiğini veya hangi kategorilerin daha az popüler hale geldiğini belirlemek için bu bileşeni kullanabilirler.

                        """)
                        with st.expander("Versiyon Bilgileri"):
                            st.write(
                                """

                                **Rapor Adı:** Satış Raporu 1\n
                                **Geliştirme Tarihi:** 10.04.2022\n
                                **Versiyon:** 1.0\n
                                **Son Güncelleme Tarihi:** 16.04.2022
                                """)
                        with st.container():
                            st.write("**Rapor Sayfaları PDF Görünümü**")

                            col1, col2, col3 = st.columns(3)
                            with col1:
                                if st.button('PDF Görünümünü Aç', key='1'):
                                    with col2:
                                        st.subheader("Rapor Sayfaları")
                                        show_pdf('POWERBICANLI_PDF/1_Urun Satıs Icgoruleri.pdf')

                                st.button('PDF Görünümünü Kapat', key='2')

                                with open("POWERBICANLI_PDF/1_Urun Satıs Icgoruleri.pdf",
                                          "rb") as pdf_file:
                                    PDFbyte = pdf_file.read()
                                st.download_button(label="PDF Görünümü İndir", key='3',
                                                   data=PDFbyte,
                                                   file_name="Rapor Görünümü.pdf",
                                                   mime='application/octet-stream')  ## RAPOR GÖRÜBÜRA #

                if select_2 == "Satıs Raporu 8":
                    with st.container():
                        st.write("---")
                        st.markdown("**SATIS RAPORU 8**")
                        components.iframe(
                            "https://app.powerbi.com/view?r=eyJrIjoiY2FiZGI5OTUtZDU3MC00Yzg0LTg3ZTItNGE4NmVhOGIzNTlkIiwidCI6IjlmZTNjZTM5LTIwOWQtNGM5NS1hMWQxLWViZjA0NjY3NDkyYyIsImMiOjl9",
                            height=600, width=1000)
                        st.write("---")
                        st.markdown("**Rapor Bilgiler**")
                        with st.expander("Raporun Hedef Kitlesi Kimdir?"):
                            st.write("""

                            Satış kontrol paneli, bir kuruluşun finansal ve satış içgörülerini sergilemek için yönetici düzeyinde bir rapor olarak oluşturulmuştur. Hedeflenen kullanıcılar yönetici seviyesindeki çalışanlar olduğu için gösterge tablosu, kullanıcıların raporu kolayca taramasına olanak tanıyan üst düzey içgörüler sunar. Kullanıcılar daha sonra, panel üzerindeki yer alan rakamların keşfetmeye değer bir içgörüyü tetiklemesi durumunda, ayrıntılı metriklere dalmak için ek seçeneğe sahip olur.

                            """)
                        with st.expander("Raporun Amacı Nedir?"):
                            st.write("""
                            Panonun amacı, işletmenin zaman içindeki mali performansına ilişkin üst düzey bir genel bakış sağlamaktır. Ek olarak, kullanıcıların konuma ve ürün kategorisine göre finansal performansa dalmasına olanak tanır. Bu odak alanlarının her ikisi de, kullanıcıların finansal eğilimleri ve aşırı/düşük performans alanlarını belirlemesine olanak tanır. Kullanıcılar daha sonra çabalarını nereye odaklayacaklarını belirlemek için bu ilk içgörüleri kullanabilirler.




                            """)
                        with st.expander("Raporun temel içgörüleri nelerdir?"):
                            st.write("""


                            **KPI'lar -** Gelir, Kar, Siparişler, Müşteriler, Miktar:\n
                            _‍İşletmenin mali durumunun anlık görüntüsünü sağlar_

                            **Alan Grafiği -** Gelir, Kar, Siparişler, Müşteriler, Miktar (12 ay):\n
                            _Kullanıcıların mevsimsel iş akışını belirlemesine yardımcı olur_

                            **Çubuk Grafik -** Bölge, mağaza ve ürüne göre gelir:\n
                            _Kullanıcıların coğrafyaya ve kategoriye göre mali performanslarını anlamalarına yardımcı olur_

                            **Çizgi Grafik -** Büyüme performansı:\n
                            _İşletmenin mali büyüme durumunun anlık görüntüsünü sağlar_

                            **Halka Grafik -** Kategoriler Göre Satın alma Yüzdesi:\n
                            _Ürün kategorisine göre satılan ürün adet bilgisi dağılımını sağlar._


                            """
                                     )
                        with st.expander("Rapor İçeriği:"):
                            st.write("""

                        Raporun amacı, bir perakende mağazasının son 12 ayda ürün satışlarını analiz etmektir. Rapor, farklı ürün kategorilerindeki satışlarını görselleştirir ve her bir kategori için bir dizi farklı gösterim içerir.

                        Raporun ana bileşenleri şunlardır:

                        **Satış Performansı:** Bu bileşen, seçilen tarih aralığındaki farklı kategorilerdeki ürünlerin satışlarını, gelirlerini, giderlerini ve satılan ürün adetlerini gösteren bir grafik sunar. Bu grafikte, farklı kategorilerin toplam satış, kar, maliyetin yanı sıra, her bir kategorideki en çok satılan ürünlerin de gösterilir.

                        **BÖLGE:** Bu bileşen, satışların coğrafi dağılımını harita üzerinde gösterir. Harita, farklı bölgelerdeki toplam satışları renkli bir şekilde gösterir ve kullanıcılara, farklı bölgelerdeki satışlar arasındaki farklılıkları analiz etme imkanı verir.

                        **Kategori Bazında Satışlar:** Bu bileşen, her bir kategori için toplam satışları ve gelirleri gösterir. Kullanıcılar, her bir kategori için satış trendlerini analiz etmek ve hangi kategorilerin en çok satıldığını görmek için bu bileşeni kullanabilirler.

                        **En Çok Satan Ürünler:** Bu bileşen, her bir kategori için en çok satan ürünleri gösterir. Bu bileşen, hangi ürünlerin en popüler olduğunu ve hangi ürünlerin daha fazla reklam yapılması gerektiğini belirlemek için kullanılabilir.

                        **Satış Trendleri:** Bu bileşen, son 12 ayda farklı kategorilerdeki ürünlerin satış trendlerini gösterir. Kullanıcılar, hangi kategorilerin daha popüler hale geldiğini veya hangi kategorilerin daha az popüler hale geldiğini belirlemek için bu bileşeni kullanabilirler.

                        """)
                        with st.expander("Versiyon Bilgileri"):
                            st.write(
                                """

                                **Rapor Adı:** Satış Raporu 1\n
                                **Geliştirme Tarihi:** 10.04.2022\n
                                **Versiyon:** 1.0\n
                                **Son Güncelleme Tarihi:** 16.04.2022
                                """)
                        with st.container():
                            st.write("**Rapor Sayfaları PDF Görünümü**")

                            col1, col2, col3 = st.columns(3)
                            with col1:
                                if st.button('PDF Görünümünü Aç', key='1'):
                                    with col2:
                                        st.subheader("Rapor Sayfaları")
                                        show_pdf('POWERBICANLI_PDF/7_Satıs_Dashboard.pdf')

                                st.button('PDF Görünümünü Kapat', key='2')

                                with open("POWERBICANLI_PDF/7_Satıs_Dashboard.pdf",
                                          "rb") as pdf_file:
                                    PDFbyte = pdf_file.read()
                                st.download_button(label="PDF Görünümü İndir", key='3',
                                                   data=PDFbyte,
                                                   file_name="Rapor Görünümü.pdf",
                                                   mime='application/octet-stream')  ## RAPOR GÖRÜBÜRA #



        if select_1 == 'Stok Raporları':
            # st.snow()

            with col2:
                st.write("**Rapor Listesi**")
                df_3 = df.loc[df["Rapor Adı"].str.contains("Stok"), :]
                st.dataframe(df_3)

            with col1:
                # st.subheader("Kullanım Bilgileri")
                # st.dataframe(pd.DataFrame({"Rapor Adı": ["Stok Raporu - 1"], "Kullanıcı Sayısı": ["20"]}))
                st.subheader(":red[Stok Raporları]")
                st.image("warehouse-management-software.png",width=300)

            with col3:
                st.write("**Rapor Seçimi**")
                select_2 = st.selectbox('Lütfen Görmek İstediğiniz Raporu Seçiniz', ['Seçim Yapınız', 'Stok Raporu-1'])

            with st.container():

                if select_2 == "Stok Raporu-1":
                    with st.container():
                        st.write("---")
                        st.markdown("**STOK RAPORU 1**")
                        components.iframe(
                            "https://app.powerbi.com/view?r=eyJrIjoiNDQ1YmEzZjYtOGZhNC00OGVlLTg0MTgtYjQ3OTI0YWE2MDg4IiwidCI6IjlmZTNjZTM5LTIwOWQtNGM5NS1hMWQxLWViZjA0NjY3NDkyYyIsImMiOjl9",
                            height=600, width=1000)
                        st.write("---")
                        st.markdown("**Rapor Bilgiler**")
                        with st.expander("Raporun Hedef Kitlesi Kimdir?"):
                            st.write("""
    
                            Satış kontrol paneli, bir kuruluşun finansal ve satış içgörülerini sergilemek için yönetici düzeyinde bir rapor olarak oluşturulmuştur. Hedeflenen kullanıcılar yönetici seviyesindeki çalışanlar olduğu için gösterge tablosu, kullanıcıların raporu kolayca taramasına olanak tanıyan üst düzey içgörüler sunar. Kullanıcılar daha sonra, panel üzerindeki yer alan rakamların keşfetmeye değer bir içgörüyü tetiklemesi durumunda, ayrıntılı metriklere dalmak için ek seçeneğe sahip olur.
    
                            """)

                        with st.container():
                            st.write("**Rapor Sayfaları PDF Görünümü**")

                            col1, col2, col3 = st.columns(3)
                            with col1:
                                if st.button('PDF Görünümünü Aç', key='1'):
                                    with col2:
                                        st.subheader("Rapor Sayfaları")
                                        show_pdf('POWERBICANLI_PDF/Stok_Raporu_1.pdf')

                                st.button('PDF Görünümünü Kapat', key='2')

                                with open("POWERBICANLI_PDF/Stok_Raporu_1.pdf",
                                          "rb") as pdf_file:
                                    PDFbyte = pdf_file.read()
                                st.download_button(label="PDF Görünümü İndir", key='3',
                                                   data=PDFbyte,
                                                   file_name="Rapor Görünümü.pdf",
                                                   mime='/application/octet-stream')

        if select_1 == 'HR':
            # st.snow()

            with col2:
                st.write("**Rapor Listesi**")
                df_hr = df.loc[df["Rapor Adı"].str.contains("HR"), :]
                st.dataframe(df_hr)

            with col1:
                # st.subheader("Kullanım Bilgileri")
                # st.dataframe(pd.DataFrame({"Rapor Adı": ["Stok Raporu - 1"], "Kullanıcı Sayısı": ["20"]}))
                st.subheader(":red[HR Raporları]")
                st.image("warehouse-management-software.png",width=300)

            with col3:
                st.write("**Rapor Seçimi**")
                select_2 = st.selectbox('Lütfen Görmek İstediğiniz Raporu Seçiniz', ['Seçim Yapınız', 'HR Dashboard 1','HR Dashboard 2','HR Dashboard 3',
                                                                                     'HR Dashboard 4'])

            with st.container():

                if select_2 == "HR Dashboard 1":
                    with st.container():
                        st.write("---")
                        st.markdown("**HR Dashboard 1**")
                        components.iframe(
                            "https://app.powerbi.com/view?r=eyJrIjoiZDNmZmNmMWQtNWM1Yy00ZmIwLTgwYTYtYWViYTZkMmE1ZWMxIiwidCI6IjlmZTNjZTM5LTIwOWQtNGM5NS1hMWQxLWViZjA0NjY3NDkyYyIsImMiOjl9",
                            height=600, width=1000)
                        st.write("---")
                        st.markdown("**İK ANALİTİĞİ**")
                        # with st.expander("Raporun Hedef Kitlesi Kimdir?"):
                        st.write("""
    
    
    
    İK analitiği, insan kaynakları (İK) verilerinin toplanması, analizi ve yorumlanması yoluyla işletmelerin İK stratejilerini optimize etmelerine yardımcı olan bir disiplindir. İK analitiği, İK kararlarının verimliliğini artırmak için niceliksel ve niteliksel verileri kullanır. Bu veriler, işe alım, işe yerleştirme, performans yönetimi, eğitim ve geliştirme, çalışan bağlılığı, maaş ve yan haklar gibi İK işlevlerindeki kararları desteklemek için kullanılabilir.
    
    İK analitiği ayrıca işletmelerin İK verilerini anlamalarına, trendleri ve örüntüleri belirlemelerine, çalışanların performansını ve tatmin düzeyini ölçmelerine ve gelecekteki ihtiyaçlar için planlama yapmalarına yardımcı olur. Bu sayede işletmeler, İK kararlarını verirken daha doğru ve verimli kararlar alabilirler.
    
    Son zamanlarda, İK analitiği daha da önemli hale gelmiştir çünkü işletmeler, çalışanların ihtiyaçlarını ve beklentilerini karşılamak için daha stratejik bir yaklaşım benimsemektedir. İK analitiği, işletmelerin İK stratejilerini optimize etmelerine yardımcı olarak, çalışanların performansını artırmalarına, işletme hedeflerine ulaşmalarına ve rekabet avantajı elde etmelerine yardımcı olur.
                            """)

                        with st.container():
                            st.write("---")
                            st.write("**Rapor Sayfaları PDF Görünümü**")

                            col1, col2, col3 = st.columns(3)
                            with col1:
                                if st.button('PDF Görünümünü Aç', key='1'):
                                    with col2:
                                        st.subheader("Rapor Sayfaları")
                                        show_pdf('POWERBICANLI_PDF/HR_Dashboard_1.pdf')

                                st.button('PDF Görünümünü Kapat', key='2')

                                with open("POWERBICANLI_PDF/HR_Dashboard_1.pdf",
                                          "rb") as pdf_file:
                                    PDFbyte = pdf_file.read()
                                st.download_button(label="PDF Görünümü İndir", key='3',
                                                   data=PDFbyte,
                                                   file_name="Rapor Görünümü.pdf",
                                                   mime='application/octet-stream')

                if select_2 == "HR Dashboard 2":
                    with st.container():
                        st.write("---")
                        st.markdown("**HR Dashboard 2**")
                        components.iframe(
                            "https://app.powerbi.com/view?r=eyJrIjoiYjc0ZTA5MmEtZWY3OC00Y2RlLWE2N2ItZDk1OTc1ZGQ5NDkyIiwidCI6IjlmZTNjZTM5LTIwOWQtNGM5NS1hMWQxLWViZjA0NjY3NDkyYyIsImMiOjl9",
                            height=600, width=1000)
                        st.write("---")
                        st.markdown("**İK ANALİTİĞİ**")
                        # with st.expander("Raporun Hedef Kitlesi Kimdir?"):
                        st.write("""
    
    
    
    İK analitiği, insan kaynakları (İK) verilerinin toplanması, analizi ve yorumlanması yoluyla işletmelerin İK stratejilerini optimize etmelerine yardımcı olan bir disiplindir. İK analitiği, İK kararlarının verimliliğini artırmak için niceliksel ve niteliksel verileri kullanır. Bu veriler, işe alım, işe yerleştirme, performans yönetimi, eğitim ve geliştirme, çalışan bağlılığı, maaş ve yan haklar gibi İK işlevlerindeki kararları desteklemek için kullanılabilir.
    
    İK analitiği ayrıca işletmelerin İK verilerini anlamalarına, trendleri ve örüntüleri belirlemelerine, çalışanların performansını ve tatmin düzeyini ölçmelerine ve gelecekteki ihtiyaçlar için planlama yapmalarına yardımcı olur. Bu sayede işletmeler, İK kararlarını verirken daha doğru ve verimli kararlar alabilirler.
    
    Son zamanlarda, İK analitiği daha da önemli hale gelmiştir çünkü işletmeler, çalışanların ihtiyaçlarını ve beklentilerini karşılamak için daha stratejik bir yaklaşım benimsemektedir. İK analitiği, işletmelerin İK stratejilerini optimize etmelerine yardımcı olarak, çalışanların performansını artırmalarına, işletme hedeflerine ulaşmalarına ve rekabet avantajı elde etmelerine yardımcı olur.
                            """)
                        with st.container():
                            st.write("---")
                            st.write("**Rapor Sayfaları PDF Görünümü**")

                            col1, col2, col3 = st.columns(3)
                            with col1:
                                if st.button('PDF Görünümünü Aç', key='1'):
                                    with col2:
                                        st.subheader("Rapor Sayfaları")
                                        show_pdf('POWERBICANLI_PDF/HR_Dashboard_2.pdf')

                                st.button('PDF Görünümünü Kapat', key='2')

                                with open("POWERBICANLI_PDF/HR_Dashboard_2.pdf",
                                          "rb") as pdf_file:
                                    PDFbyte = pdf_file.read()
                                st.download_button(label="PDF Görünümü İndir", key='3',
                                                   data=PDFbyte,
                                                   file_name="Rapor Görünümü.pdf",
                                                   mime='application/octet-stream')

                if select_2 == "HR Dashboard 3":
                    with st.container():
                        st.write("---")
                        st.markdown("**HR Dashboard 3**")
                        components.iframe(
                            "https://app.powerbi.com/view?r=eyJrIjoiNDgzYzIxYWItMjE4Mi00MTFhLTllMDktNTNhYzIwZjU4MzA1IiwidCI6IjlmZTNjZTM5LTIwOWQtNGM5NS1hMWQxLWViZjA0NjY3NDkyYyIsImMiOjl9",
                            height=600, width=1000)
                        st.write("---")
                        st.markdown("**İK ANALİTİĞİ**")
                        # with st.expander("Raporun Hedef Kitlesi Kimdir?"):
                        st.write("""
    
    
    
    İK analitiği, insan kaynakları (İK) verilerinin toplanması, analizi ve yorumlanması yoluyla işletmelerin İK stratejilerini optimize etmelerine yardımcı olan bir disiplindir. İK analitiği, İK kararlarının verimliliğini artırmak için niceliksel ve niteliksel verileri kullanır. Bu veriler, işe alım, işe yerleştirme, performans yönetimi, eğitim ve geliştirme, çalışan bağlılığı, maaş ve yan haklar gibi İK işlevlerindeki kararları desteklemek için kullanılabilir.
    
    İK analitiği ayrıca işletmelerin İK verilerini anlamalarına, trendleri ve örüntüleri belirlemelerine, çalışanların performansını ve tatmin düzeyini ölçmelerine ve gelecekteki ihtiyaçlar için planlama yapmalarına yardımcı olur. Bu sayede işletmeler, İK kararlarını verirken daha doğru ve verimli kararlar alabilirler.
    
    Son zamanlarda, İK analitiği daha da önemli hale gelmiştir çünkü işletmeler, çalışanların ihtiyaçlarını ve beklentilerini karşılamak için daha stratejik bir yaklaşım benimsemektedir. İK analitiği, işletmelerin İK stratejilerini optimize etmelerine yardımcı olarak, çalışanların performansını artırmalarına, işletme hedeflerine ulaşmalarına ve rekabet avantajı elde etmelerine yardımcı olur.
                            """)

                        with st.container():
                            st.write("---")
                            st.write("**Rapor Sayfaları PDF Görünümü**")

                            col1, col2, col3 = st.columns(3)
                            with col1:
                                if st.button('PDF Görünümünü Aç', key='1'):
                                    with col2:
                                        st.subheader("Rapor Sayfaları")
                                        show_pdf('POWERBICANLI_PDF/HR_Dashboard_3.pdf')

                                st.button('PDF Görünümünü Kapat', key='2')

                                with open("POWERBICANLI_PDF/HR_Dashboard_3.pdf",
                                          "rb") as pdf_file:
                                    PDFbyte = pdf_file.read()
                                st.download_button(label="PDF Görünümü İndir", key='3',
                                                   data=PDFbyte,
                                                   file_name="Rapor Görünümü.pdf",
                                                   mime='application/octet-stream')

                if select_2 == "HR Dashboard 4":
                    with st.container():
                        st.write("---")
                        st.markdown("**HR Dashboard 4**")
                        components.iframe(
                            'https://app.powerbi.com/view?r=eyJrIjoiYWVmYWE4MzgtMWRjOS00ODYxLWIwNzktOThjMmU1MDNhYWE3IiwidCI6IjlmZTNjZTM5LTIwOWQtNGM5NS1hMWQxLWViZjA0NjY3NDkyYyIsImMiOjl9',
                            height=600, width=1000)
                        st.write("---")
                        st.markdown("**İK ANALİTİĞİ**")
                        # with st.expander("Raporun Hedef Kitlesi Kimdir?"):
                        st.write("""



    İK analitiği, insan kaynakları (İK) verilerinin toplanması, analizi ve yorumlanması yoluyla işletmelerin İK stratejilerini optimize etmelerine yardımcı olan bir disiplindir. İK analitiği, İK kararlarının verimliliğini artırmak için niceliksel ve niteliksel verileri kullanır. Bu veriler, işe alım, işe yerleştirme, performans yönetimi, eğitim ve geliştirme, çalışan bağlılığı, maaş ve yan haklar gibi İK işlevlerindeki kararları desteklemek için kullanılabilir.

    İK analitiği ayrıca işletmelerin İK verilerini anlamalarına, trendleri ve örüntüleri belirlemelerine, çalışanların performansını ve tatmin düzeyini ölçmelerine ve gelecekteki ihtiyaçlar için planlama yapmalarına yardımcı olur. Bu sayede işletmeler, İK kararlarını verirken daha doğru ve verimli kararlar alabilirler.

    Son zamanlarda, İK analitiği daha da önemli hale gelmiştir çünkü işletmeler, çalışanların ihtiyaçlarını ve beklentilerini karşılamak için daha stratejik bir yaklaşım benimsemektedir. İK analitiği, işletmelerin İK stratejilerini optimize etmelerine yardımcı olarak, çalışanların performansını artırmalarına, işletme hedeflerine ulaşmalarına ve rekabet avantajı elde etmelerine yardımcı olur.
                            """)

                        with st.container():
                            st.write("---")
                            st.write("**Rapor Sayfaları PDF Görünümü**")

                            col1, col2, col3 = st.columns(3)
                            with col1:
                                if st.button('PDF Görünümünü Aç', key='1'):
                                    with col2:
                                        st.subheader("Rapor Sayfaları")
                                        show_pdf('POWERBICANLI_PDF/HR_Dashboard_4.pdf')

                                st.button('PDF Görünümünü Kapat', key='2')

                                with open("POWERBICANLI_PDF/HR_Dashboard_4.pdf",
                                          "rb") as pdf_file:
                                    PDFbyte = pdf_file.read()
                                st.download_button(label="PDF Görünümü İndir", key='3',
                                                   data=PDFbyte,
                                                   file_name="Rapor Görünümü.pdf",
                                                   mime='application/octet-stream')





        if select_1 == 'Pazarlama':
            # st.snow()

            with col2:
                st.write("**Rapor Listesi**")
                df_pazarlama = df.loc[df["Rapor Adı"].str.contains("Pazarla"), :]
                st.dataframe(df_pazarlama)

            with col1:
                # st.subheader("Kullanım Bilgileri")
                # st.dataframe(pd.DataFrame({"Rapor Adı": ["Stok Raporu - 1"], "Kullanıcı Sayısı": ["20"]}))
                st.subheader(":red[Pazarlama Raporları]")
                st.image("warehouse-management-software.png",width=300)

            with col3:
                st.write("**Rapor Seçimi**")
                select_2 = st.selectbox('Lütfen Görmek İstediğiniz Raporu Seçiniz', ['Seçim Yapınız', 'Pazarlama Dashboard'])

            with st.container():

                if select_2 == "Pazarlama Dashboard":
                    with st.container():
                        st.write("---")
                        st.markdown("**PAZARLAMA RAPORU 1**")
                        components.iframe(
                            "https://app.powerbi.com/view?r=eyJrIjoiYTdjN2NlOTktZjhjZi00ZWM3LTlkN2QtYmUxMmU2YmU2Y2E1IiwidCI6IjlmZTNjZTM5LTIwOWQtNGM5NS1hMWQxLWViZjA0NjY3NDkyYyIsImMiOjl9",
                            height=600, width=1000)
                        st.write("---")
                        st.markdown("**PAZARLAMA ANALİTİĞİ**")
                        # with st.expander("Raporun Hedef Kitlesi Kimdir?"):
                        st.write("""
    
    Pazarlama analitiği, pazarlama faaliyetlerinde kullanılan verilerin toplanması, analizi ve yorumlanmasıyla pazarlama stratejilerini optimize etmeyi amaçlayan bir disiplindir. Pazarlama analitiği, pazarlama performansını izlemek, müşteri davranışlarını anlamak, pazar trendlerini belirlemek ve pazarlama kararlarını vermek için veri odaklı içgörüler sağlar.
    
    Pazarlama analitiği, çeşitli veri kaynaklarından elde edilen verileri kullanarak pazarlama faaliyetlerini daha etkili hale getirmek için analiz yapar. Bu veriler arasında tüketici davranışı verileri, satış verileri, pazarlama kampanyası verileri, web analitiği verileri, sosyal medya verileri ve müşteri geri bildirimleri gibi çeşitli veri kaynakları bulunur.
    
    Pazarlama analitiği, işletmelere pazarlama stratejilerini belirlemek ve optimize etmek için derinlemesine anlayışlar sunar. Bu analizler, müşteri segmentasyonunu anlamayı, müşteri yolculuğunu izlemeyi, pazar trendlerini belirlemeyi, rekabet analizi yapmayı ve pazarlama kampanyalarının etkinliğini değerlendirmeyi içerir.
    
    Pazarlama analitiği aynı zamanda gerçek zamanlı analiz imkanı sağlar. İşletmeler, kampanyaları izlerken ve etkinliklerini değerlendirirken anlık verilere dayalı kararlar alabilir. Bu da hızlı tepki verme, hedef kitleye daha kişiselleştirilmiş mesajlar gönderme ve pazarlama stratejilerini anında ayarlama imkanı sağlar.
    
    Pazarlama analitiği için kullanılan yöntemler arasında veri madenciliği, istatistiksel analiz, tahmine dayalı analiz, sosyal ağ analizi ve makine öğrenimi gibi yöntemler bulunur. Bu yöntemler, verilerden anlamlı içgörüler elde etmeyi, pazarlama stratejilerini optimize etmeyi ve müşteri ilişkilerini geliştirmeyi sağlar.
    
    Pazarlama analitiği, işletmelere daha iyi pazarlama kararları alabilme, müşterilerle daha etkili iletişim kurabilme ve rekabet avantajı elde etme imkanı sunar. Verilere dayalı pazarlama stratejileri sayesinde işletmeler, hedef kitleye daha etkili şekilde ulaşabilir, müşteri memnuniyetini artırabilir ve satış performansını iyileştirebilir.
                            """)

                        with st.container():
                            st.write("---")
                            st.write("**Rapor Sayfaları PDF Görünümü**")

                            col1, col2, col3 = st.columns(3)
                            with col1:
                                if st.button('PDF Görünümünü Aç', key='1'):
                                    with col2:
                                        st.subheader("Rapor Sayfaları")
                                        show_pdf('POWERBICANLI_PDF/1_Pazarlama Dashboard.pdf')

                                st.button('PDF Görünümünü Kapat', key='2')

                                with open("POWERBICANLI_PDF/1_Pazarlama Dashboard.pdf",
                                          "rb") as pdf_file:
                                    PDFbyte = pdf_file.read()
                                st.download_button(label="PDF Görünümü İndir", key='3',
                                                   data=PDFbyte,
                                                   file_name="Rapor Görünümü.pdf",
                                                   mime='application/octet-stream')

        if select_1 == 'Müşteri Analitiği':
            # st.snow()

            with col2:
                st.write("**Rapor Listesi**")
                df_musteri = df.loc[df["Rapor Adı"].str.contains("Müşteri"), :]
                st.dataframe(df_musteri)

            with col1:
                # st.subheader("Kullanım Bilgileri")
                # st.dataframe(pd.DataFrame({"Rapor Adı": ["Stok Raporu - 1"], "Kullanıcı Sayısı": ["20"]}))
                st.subheader(":red[Müşteri Analitiği]")
                st.image("warehouse-management-software.png",width=300)

            with col3:
                st.write("**Rapor Seçimi**")
                select_2 = st.selectbox('Lütfen Görmek İstediğiniz Raporu Seçiniz', ['Seçim Yapınız', "Müşteri Analitigi 1", "Müşteri Analitigi 2","Müşteri Değerlendirme"])

            with st.container():

                if select_2 == "Müşteri Analitigi 1":
                    with st.container():
                        st.write("---")
                        st.markdown("**Müşteri Analitigi RAPORU 1**")
                        components.iframe(
                            "https://app.powerbi.com/view?r=eyJrIjoiMzhlODAxYzctNTBmYS00NGU3LTg1ZWItYzI4ZjM3NzZlZTQ4IiwidCI6IjlmZTNjZTM5LTIwOWQtNGM5NS1hMWQxLWViZjA0NjY3NDkyYyIsImMiOjl9",
                            height=600, width=1000)
                        st.write("---")
                        st.markdown("**MÜŞTERİ ANALİTİĞİ**")
                        # with st.expander("Raporun Hedef Kitlesi Kimdir?"):
                        st.write("""
    
    Müşteri analitiği, müşteri verilerinin toplanması, analizi ve yorumlanmasıyla müşteri davranışlarını anlama ve pazarlama stratejilerini optimize etmeyi amaçlayan bir disiplindir. Müşteri analitiği, müşteriyle ilgili verileri kullanarak müşteri segmentasyonu, müşteri değeri analizi, müşteri sadakati ve churn analizi gibi önemli içgörüler elde etmeyi hedefler.
    
    Müşteri analitiği, işletmelere müşterileri daha iyi anlama ve onlara daha kişiselleştirilmiş hizmetler sunma imkanı sağlar. İşletmeler, müşteri analitiği sayesinde müşterilerin satın alma alışkanlıklarını, tercihlerini, demografik özelliklerini, etkileşim geçmişlerini ve diğer davranış verilerini analiz eder. Bu analizler sonucunda işletmeler, farklı müşteri segmentlerini belirleyebilir, pazarlama stratejilerini kişiselleştirebilir ve müşterilerle daha etkili iletişim kurabilir.
    
    Müşteri analitiği aynı zamanda müşteri değeri analizi yapma imkanı sunar. Müşteri değeri analizi, müşterilerin işletmeye olan katkılarını ölçmeyi ve değerli müşterileri belirlemeyi amaçlar. Değerli müşterilerin tespit edilmesiyle işletmeler, bu müşterilere özel teklifler sunabilir, sadakat programları geliştirebilir ve uzun vadeli müşteri ilişkilerini güçlendirebilir.
    
    Müşteri analitiği ayrıca müşteri sadakati ve churn analizine de odaklanır. Müşteri sadakati analizi, müşterilerin işletmeyle olan bağlılığını değerlendirirken churn analizi ise müşteri kaybını (churn) önlemeye yönelik çalışmaları içerir. İşletmeler, müşteri analitiği kullanarak müşteri sadakatini artırmak için stratejiler geliştirebilir ve müşteri kaybını öngörmek ve önlemek için müşteri davranışlarını izleyebilir.
    
    Müşteri analitiği, veri madenciliği, istatistiksel analiz, makine öğrenimi ve tahmine dayalı analiz gibi yöntemleri kullanır. Bu yöntemler, müşteri verilerinden anlamlı içgörüler çıkararak işletmelere müşteri odaklı kararlar alabilmeleri için temel sağlar ve pazarlama stratejilerini optimize etmelerine yardımcı olur.
                            """)

                        with st.container():
                            st.write("---")
                            st.write("**Rapor Sayfaları PDF Görünümü**")

                            col1, col2, col3 = st.columns(3)
                            with col1:
                                if st.button('PDF Görünümünü Aç', key='1'):
                                    with col2:
                                        st.subheader("Rapor Sayfaları")
                                        show_pdf('POWERBICANLI_PDF/Musteri Analizi.pdf')

                                st.button('PDF Görünümünü Kapat', key='2')

                                with open("POWERBICANLI_PDF/Musteri Analizi.pdf",
                                          "rb") as pdf_file:
                                    PDFbyte = pdf_file.read()
                                st.download_button(label="PDF Görünümü İndir", key='3',
                                                   data=PDFbyte,
                                                   file_name="Rapor Görünümü.pdf",
                                                   mime='application/octet-stream')

                if select_2 == "Müşteri Analitigi 2":
                    with st.container():
                        st.write("---")
                        st.markdown("**Müşteri Analitigi RAPORU 2**")
                        components.iframe(
                            "https://app.powerbi.com/view?r=eyJrIjoiZmM4NjdjYzItNWRmZC00OTA4LWJiZmItZWNlMDUxNmJmOTFkIiwidCI6IjlmZTNjZTM5LTIwOWQtNGM5NS1hMWQxLWViZjA0NjY3NDkyYyIsImMiOjl9",
                            height=600, width=1000)
                        st.write("---")
                        st.markdown("**MÜŞTERİ ANALİTİĞİ**")
                        # with st.expander("Raporun Hedef Kitlesi Kimdir?"):
                        st.write("""
    
    Müşteri analitiği, müşteri verilerinin toplanması, analizi ve yorumlanmasıyla müşteri davranışlarını anlama ve pazarlama stratejilerini optimize etmeyi amaçlayan bir disiplindir. Müşteri analitiği, müşteriyle ilgili verileri kullanarak müşteri segmentasyonu, müşteri değeri analizi, müşteri sadakati ve churn analizi gibi önemli içgörüler elde etmeyi hedefler.
    
    Müşteri analitiği, işletmelere müşterileri daha iyi anlama ve onlara daha kişiselleştirilmiş hizmetler sunma imkanı sağlar. İşletmeler, müşteri analitiği sayesinde müşterilerin satın alma alışkanlıklarını, tercihlerini, demografik özelliklerini, etkileşim geçmişlerini ve diğer davranış verilerini analiz eder. Bu analizler sonucunda işletmeler, farklı müşteri segmentlerini belirleyebilir, pazarlama stratejilerini kişiselleştirebilir ve müşterilerle daha etkili iletişim kurabilir.
    
    Müşteri analitiği aynı zamanda müşteri değeri analizi yapma imkanı sunar. Müşteri değeri analizi, müşterilerin işletmeye olan katkılarını ölçmeyi ve değerli müşterileri belirlemeyi amaçlar. Değerli müşterilerin tespit edilmesiyle işletmeler, bu müşterilere özel teklifler sunabilir, sadakat programları geliştirebilir ve uzun vadeli müşteri ilişkilerini güçlendirebilir.
    
    Müşteri analitiği ayrıca müşteri sadakati ve churn analizine de odaklanır. Müşteri sadakati analizi, müşterilerin işletmeyle olan bağlılığını değerlendirirken churn analizi ise müşteri kaybını (churn) önlemeye yönelik çalışmaları içerir. İşletmeler, müşteri analitiği kullanarak müşteri sadakatini artırmak için stratejiler geliştirebilir ve müşteri kaybını öngörmek ve önlemek için müşteri davranışlarını izleyebilir.
    
    Müşteri analitiği, veri madenciliği, istatistiksel analiz, makine öğrenimi ve tahmine dayalı analiz gibi yöntemleri kullanır. Bu yöntemler, müşteri verilerinden anlamlı içgörüler çıkararak işletmelere müşteri odaklı kararlar alabilmeleri için temel sağlar ve pazarlama stratejilerini optimize etmelerine yardımcı olur.
                            """)

                        with st.container():
                            st.write("---")
                            st.write("**Rapor Sayfaları PDF Görünümü**")

                            col1, col2, col3 = st.columns(3)
                            with col1:
                                if st.button('PDF Görünümünü Aç', key='1'):
                                    with col2:
                                        st.subheader("Rapor Sayfaları")
                                        show_pdf('POWERBICANLI_PDF/2_Musteri Analizi.pdf')

                                st.button('PDF Görünümünü Kapat', key='2')

                                with open("POWERBICANLI_PDF/2_Musteri Analizi.pdf",
                                          "rb") as pdf_file:
                                    PDFbyte = pdf_file.read()
                                st.download_button(label="PDF Görünümü İndir", key='3',
                                                   data=PDFbyte,
                                                   file_name="Rapor Görünümü.pdf",
                                                   mime='application/octet-stream')

                if select_2 == "Müşteri Değerlendirme":
                    with st.container():
                        st.write("---")
                        st.markdown("**Müşteri Değerlendirme RAPORU 1**")
                        components.iframe(
                            "https://app.powerbi.com/view?r=eyJrIjoiMjc1YWUyYTgtOTZjMS00MmZiLWFmZjQtYzU1YTg4Mjk1ODYxIiwidCI6IjlmZTNjZTM5LTIwOWQtNGM5NS1hMWQxLWViZjA0NjY3NDkyYyIsImMiOjl9",
                            height=600, width=1000)
                        st.write("---")
                        st.markdown("**MÜŞTERİ ANALİTİĞİ**")
                        # with st.expander("Raporun Hedef Kitlesi Kimdir?"):
                        st.write("""
    
    Müşteri analitiği, müşteri verilerinin toplanması, analizi ve yorumlanmasıyla müşteri davranışlarını anlama ve pazarlama stratejilerini optimize etmeyi amaçlayan bir disiplindir. Müşteri analitiği, müşteriyle ilgili verileri kullanarak müşteri segmentasyonu, müşteri değeri analizi, müşteri sadakati ve churn analizi gibi önemli içgörüler elde etmeyi hedefler.
    
    Müşteri analitiği, işletmelere müşterileri daha iyi anlama ve onlara daha kişiselleştirilmiş hizmetler sunma imkanı sağlar. İşletmeler, müşteri analitiği sayesinde müşterilerin satın alma alışkanlıklarını, tercihlerini, demografik özelliklerini, etkileşim geçmişlerini ve diğer davranış verilerini analiz eder. Bu analizler sonucunda işletmeler, farklı müşteri segmentlerini belirleyebilir, pazarlama stratejilerini kişiselleştirebilir ve müşterilerle daha etkili iletişim kurabilir.
    
    Müşteri analitiği aynı zamanda müşteri değeri analizi yapma imkanı sunar. Müşteri değeri analizi, müşterilerin işletmeye olan katkılarını ölçmeyi ve değerli müşterileri belirlemeyi amaçlar. Değerli müşterilerin tespit edilmesiyle işletmeler, bu müşterilere özel teklifler sunabilir, sadakat programları geliştirebilir ve uzun vadeli müşteri ilişkilerini güçlendirebilir.
    
    Müşteri analitiği ayrıca müşteri sadakati ve churn analizine de odaklanır. Müşteri sadakati analizi, müşterilerin işletmeyle olan bağlılığını değerlendirirken churn analizi ise müşteri kaybını (churn) önlemeye yönelik çalışmaları içerir. İşletmeler, müşteri analitiği kullanarak müşteri sadakatini artırmak için stratejiler geliştirebilir ve müşteri kaybını öngörmek ve önlemek için müşteri davranışlarını izleyebilir.
    
    Müşteri analitiği, veri madenciliği, istatistiksel analiz, makine öğrenimi ve tahmine dayalı analiz gibi yöntemleri kullanır. Bu yöntemler, müşteri verilerinden anlamlı içgörüler çıkararak işletmelere müşteri odaklı kararlar alabilmeleri için temel sağlar ve pazarlama stratejilerini optimize etmelerine yardımcı olur.
                            """)

                        with st.container():
                            st.write("---")
                            st.write("**Rapor Sayfaları PDF Görünümü**")

                            col1, col2, col3 = st.columns(3)
                            with col1:
                                if st.button('PDF Görünümünü Aç', key='1'):
                                    with col2:
                                        st.subheader("Rapor Sayfaları")
                                        show_pdf('POWERBICANLI_PDF/3_Musteri Degerlendirme.pdf')

                                st.button('PDF Görünümünü Kapat', key='2')

                                with open("POWERBICANLI_PDF/3_Musteri Degerlendirme.pdf",
                                          "rb") as pdf_file:
                                    PDFbyte = pdf_file.read()
                                st.download_button(label="PDF Görünümü İndir", key='3',
                                                   data=PDFbyte,
                                                   file_name="Rapor Görünümü.pdf",
                                                   mime='application/octet-stream')

        if select_1 == 'CRM':
            # st.snow()

            with col2:
                st.write("**Rapor Listesi**")
                df_crm = df.loc[df["Rapor Adı"].str.contains("CRM"), :]
                st.dataframe(df_crm)

            with col1:
                # st.subheader("Kullanım Bilgileri")
                # st.dataframe(pd.DataFrame({"Rapor Adı": ["Stok Raporu - 1"], "Kullanıcı Sayısı": ["20"]}))
                st.subheader(":red[CRM Raporları]")
                st.image("warehouse-management-software.png",width=300)

            with col3:
                st.write("**Rapor Seçimi**")
                select_2 = st.selectbox('Lütfen Görmek İstediğiniz Raporu Seçiniz', ['Seçim Yapınız', 'Satış Dashboard (CRM)'])

            with st.container():

                if select_2 == "Satış Dashboard (CRM)":
                    with st.container():
                        st.write("---")
                        st.markdown("**CRM RAPORU 1**")
                        components.iframe(
                            "https://app.powerbi.com/view?r=eyJrIjoiNjBiYjhjMTAtMjg5OS00YWQxLWEyODQtNmYyMWFlYzM5NzU4IiwidCI6IjlmZTNjZTM5LTIwOWQtNGM5NS1hMWQxLWViZjA0NjY3NDkyYyIsImMiOjl9",
                            height=600, width=1000)
                        st.write("---")
                        st.markdown("**CRM ANALİTİĞİ**")
                        # with st.expander("Raporun Hedef Kitlesi Kimdir?"):
                        st.write("""
    
    CRM analitiği, Müşteri İlişkileri Yönetimi (CRM) verilerinin toplanması, analizi ve yorumlanmasıyla müşteri ilişkileri stratejilerini optimize etmeyi amaçlayan bir disiplindir. CRM analitiği, müşteri verilerini kullanarak müşteri davranışlarını anlama, trendleri belirleme ve müşteri ilişkileri yönetimine yönelik stratejik kararlar almayı sağlar.
    
    CRM analitiği, işletmelerin müşteri verilerini analiz ederek daha iyi müşteri anlayışı elde etmelerini ve müşteri hizmetlerini iyileştirmelerini sağlar. Bu analizler, müşteri satın alma alışkanlıklarını, tercihlerini, demografik özelliklerini, geri bildirimlerini ve diğer etkileşim verilerini içerebilir. Bu bilgiler işletmelere müşteri segmentasyonu, kişiselleştirilmiş pazarlama stratejileri, müşteri sadakati programları ve müşteri deneyimini geliştirmek için odaklanılması gereken alanlar hakkında değerli içgörüler sağlar.
    
    CRM analitiği aynı zamanda işletmelere müşteri yaşam döngüsü analizi yapma imkanı verir. Bu analiz, müşterilerin işletmeyle ilk etkileşiminden başlayarak satın alma, hizmet kullanımı ve sadakat aşamalarını kapsar. Bu sayede işletmeler, müşteri yolculuğunu daha iyi anlayabilir, müşteri ilişkilerini güçlendirebilir ve müşteri kazanımı ve tutma stratejilerini optimize edebilir.
    
    CRM analitiği, veri madenciliği, istatistiksel analiz, makine öğrenimi ve tahmine dayalı analiz gibi yöntemleri kullanır. Bu yöntemler, müşteri verilerinden anlamlı içgörüler çıkararak işletmelere rekabet avantajı sağlar ve müşteri ilişkilerini güçlendirmeye yardımcı olur.
                            """)

                        with st.container():
                            st.write("---")
                            st.write("**Rapor Sayfaları PDF Görünümü**")

                            col1, col2, col3 = st.columns(3)
                            with col1:
                                if st.button('PDF Görünümünü Aç', key='1'):
                                    with col2:
                                        st.subheader("Rapor Sayfaları")
                                        show_pdf('POWERBICANLI_PDF/1_Satıs_Dashboard_CRM.pdf')

                                st.button('PDF Görünümünü Kapat', key='2')

                                with open("POWERBICANLI_PDF/1_Satıs_Dashboard_CRM.pdf",
                                          "rb") as pdf_file:
                                    PDFbyte = pdf_file.read()
                                st.download_button(label="PDF Görünümü İndir", key='3',
                                                   data=PDFbyte,
                                                   file_name="Rapor Görünümü.pdf",
                                                   mime='application/octet-stream')

        if select_1 == 'Sosyal Medya':
            # st.snow()

            with col2:
                st.write("**Rapor Listesi**")
                df_crm = df.loc[df["Rapor Adı"].str.contains("Sosyal"), :]
                st.dataframe(df_crm)

            with col1:
                # st.subheader("Kullanım Bilgileri")
                # st.dataframe(pd.DataFrame({"Rapor Adı": ["Stok Raporu - 1"], "Kullanıcı Sayısı": ["20"]}))
                st.subheader(":red[Sosyal Medya Raporları]")
                st.image("warehouse-management-software.png",width=300)

            with col3:
                st.write("**Rapor Seçimi**")
                select_2 = st.selectbox('Lütfen Görmek İstediğiniz Raporu Seçiniz', ['Seçim Yapınız', 'Sosyal Medya Dashboard'])

            with st.container():

                if select_2 == "Sosyal Medya Dashboard":
                    with st.container():
                        st.write("---")
                        st.markdown("**Sosyal Medya Dashboard**")
                        components.iframe(
                            "https://app.powerbi.com/view?r=eyJrIjoiNjBiYjhjMTAtMjg5OS00YWQxLWEyODQtNmYyMWFlYzM5NzU4IiwidCI6IjlmZTNjZTM5LTIwOWQtNGM5NS1hMWQxLWViZjA0NjY3NDkyYyIsImMiOjl9",
                            height=600, width=1000)
                        st.write("---")
                        st.markdown("**SOSYAL MEDYA ANALİTİĞİ**")
                        # with st.expander("Raporun Hedef Kitlesi Kimdir?"):
                        st.write("""
    
    Pazarlama analitiği, pazarlama faaliyetlerinde kullanılan verilerin toplanması, analizi ve yorumlanmasıyla pazarlama stratejilerini optimize etmeyi amaçlayan bir disiplindir. Pazarlama analitiği, pazarlama performansını izlemek, müşteri davranışlarını anlamak, pazar trendlerini belirlemek ve pazarlama kararlarını vermek için veri odaklı içgörüler sağlar.
    
    Pazarlama analitiği, çeşitli veri kaynaklarından elde edilen verileri kullanarak pazarlama faaliyetlerini daha etkili hale getirmek için analiz yapar. Bu veriler arasında tüketici davranışı verileri, satış verileri, pazarlama kampanyası verileri, web analitiği verileri, sosyal medya verileri ve müşteri geri bildirimleri gibi çeşitli veri kaynakları bulunur.
    
    Pazarlama analitiği, işletmelere pazarlama stratejilerini belirlemek ve optimize etmek için derinlemesine anlayışlar sunar. Bu analizler, müşteri segmentasyonunu anlamayı, müşteri yolculuğunu izlemeyi, pazar trendlerini belirlemeyi, rekabet analizi yapmayı ve pazarlama kampanyalarının etkinliğini değerlendirmeyi içerir.
    
    Pazarlama analitiği aynı zamanda gerçek zamanlı analiz imkanı sağlar. İşletmeler, kampanyaları izlerken ve etkinliklerini değerlendirirken anlık verilere dayalı kararlar alabilir. Bu da hızlı tepki verme, hedef kitleye daha kişiselleştirilmiş mesajlar gönderme ve pazarlama stratejilerini anında ayarlama imkanı sağlar.
    
    Pazarlama analitiği için kullanılan yöntemler arasında veri madenciliği, istatistiksel analiz, tahmine dayalı analiz, sosyal ağ analizi ve makine öğrenimi gibi yöntemler bulunur. Bu yöntemler, verilerden anlamlı içgörüler elde etmeyi, pazarlama stratejilerini optimize etmeyi ve müşteri ilişkilerini geliştirmeyi sağlar.
    
    Pazarlama analitiği, işletmelere daha iyi pazarlama kararları alabilme, müşterilerle daha etkili iletişim kurabilme ve rekabet avantajı elde etme imkanı sunar. Verilere dayalı pazarlama stratejileri sayesinde işletmeler, hedef kitleye daha etkili şekilde ulaşabilir, müşteri memnuniyetini artırabilir ve satış performansını iyileştirebilir. """)

                        with st.container():
                            st.write("---")
                            st.write("**Rapor Sayfaları PDF Görünümü**")

                            col1, col2, col3 = st.columns(3)
                            with col1:
                                if st.button('PDF Görünümünü Aç', key='1'):
                                    with col2:
                                        st.subheader("Rapor Sayfaları")
                                        show_pdf('POWERBICANLI_PDF/Sosyal Medya Dashboard.pdf')

                                st.button('PDF Görünümünü Kapat', key='2')

                                with open("POWERBICANLI_PDF/Sosyal Medya Dashboard.pdf",
                                          "rb") as pdf_file:
                                    PDFbyte = pdf_file.read()
                                st.download_button(label="PDF Görünümü İndir", key='3',
                                                   data=PDFbyte,
                                                   file_name="Rapor Görünümü.pdf",
                                                   mime='application/octet-stream')

        if select_1 == 'Web Site':
            # st.snow()

            with col2:
                st.write("**Rapor Listesi**")
                df_crm = df.loc[df["Rapor Adı"].str.contains("Web"), :]
                st.dataframe(df_crm)

            with col1:
                # st.subheader("Kullanım Bilgileri")
                # st.dataframe(pd.DataFrame({"Rapor Adı": ["Stok Raporu - 1"], "Kullanıcı Sayısı": ["20"]}))
                st.subheader(":red[Sosyal Medya Raporları]")
                st.image("warehouse-management-software.png",width=300)

            with col3:
                st.write("**Rapor Seçimi**")
                select_2 = st.selectbox('Lütfen Görmek İstediğiniz Raporu Seçiniz', ['Seçim Yapınız', 'Web Site Analitiği'])

            with st.container():

                if select_2 == "Web Site Analitiği":
                    with st.container():
                        st.write("---")
                        st.markdown("**Web Site Raporu**")
                        components.iframe(
                            "https://app.powerbi.com/view?r=eyJrIjoiNjBiYjhjMTAtMjg5OS00YWQxLWEyODQtNmYyMWFlYzM5NzU4IiwidCI6IjlmZTNjZTM5LTIwOWQtNGM5NS1hMWQxLWViZjA0NjY3NDkyYyIsImMiOjl9",
                            height=600, width=1000)
                        st.write("---")
                        st.markdown("**WEB SİTE ANALİTİĞİ**")
                        # with st.expander("Raporun Hedef Kitlesi Kimdir?"):
                        st.write("""
    
    Web sitesi analitiği, bir web sitesinin performansını izlemek, ziyaretçi davranışlarını anlamak ve web sitesi stratejilerini optimize etmek için kullanılan veri analizi sürecidir. Web sitesi analitiği, web sitesine ilişkin verilerin toplanması, analizi ve yorumlanmasıyla gerçekleştirilir.
    
    Web sitesi analitiği için genellikle web analitik araçları kullanılır. Bu araçlar, web sitesine gelen ziyaretçiler hakkında çeşitli verileri toplar ve bunları analiz etme imkanı sağlar. Bu veriler arasında ziyaretçi sayısı, sayfa görüntüleme sayısı, oturum süresi, dönüşüm oranları, kaynak trafik kaynakları, demografik bilgiler ve kullanıcı davranışı gibi bilgiler bulunur.
    
    Web sitesi analitiği, işletmelere web sitesinin performansını ölçme ve değerlendirme imkanı sağlar. İşletmeler, web sitesi analitiği verilerini kullanarak ziyaretçi trafiğini ve etkileşimlerini izleyebilir, hangi sayfaların en çok ilgi gördüğünü belirleyebilir ve kullanıcıların web sitesindeki dönüşüm yolculuğunu analiz edebilir. Bu bilgiler, web sitesinin kullanıcı deneyimini iyileştirmek, dönüşüm oranlarını artırmak ve işletmenin hedeflerine ulaşmasına yardımcı olmak için kullanılabilir.
    
    Web sitesi analitiği aynı zamanda pazarlama stratejilerini optimize etme konusunda da önemli bir rol oynar. İşletmeler, web sitesi analitiği verilerini kullanarak hangi pazarlama kampanyalarının en etkili olduğunu belirleyebilir, trafik kaynaklarını analiz edebilir ve kullanıcıların web sitesindeki etkileşimlerini takip edebilir. Bu bilgiler, pazarlama bütçesinin daha etkili kullanılmasına yardımcı olur ve pazarlama stratejilerinin iyileştirilmesine katkı sağlar.
    
    Web sitesi analitiği için kullanılan yöntemler arasında sayfa izleme, hedefleme, dönüşüm izleme, A/B testleri ve trafiğin kaynaklarını analiz etme gibi teknikler bulunur. Bu yöntemler, işletmelere web sitesi performansını izlemek, kullanıcı davranışlarını anlamak ve web sitesi stratejilerini optimize etmek için kapsamlı bir içgörü sağlar.
    
    Sonuç olarak, web sitesi analitiği, işletmelere web sitesinin performansını ve etkisini ölçme ve değerlendirme imkanı sunar. Verilere dayalı kararlar alarak web sitesini geliştirmek, kullanıcı deneyimini iyileştirmek ve işletmenin hedeflerini gerçekleşt """)

                        with st.container():
                            st.write("---")
                            st.write("**Rapor Sayfaları PDF Görünümü**")

                            col1, col2, col3 = st.columns(3)
                            with col1:
                                if st.button('PDF Görünümünü Aç', key='1'):
                                    with col2:
                                        st.subheader("Rapor Sayfaları")
                                        show_pdf('POWERBICANLI_PDF/1_WebSiteAnalitigi.pdf')

                                st.button('PDF Görünümünü Kapat', key='2')

                                with open("POWERBICANLI_PDF/1_WebSiteAnalitigi.pdf",
                                          "rb") as pdf_file:
                                    PDFbyte = pdf_file.read()
                                st.download_button(label="PDF Görünümü İndir", key='3',
                                                   data=PDFbyte,
                                                   file_name="Rapor Görünümü.pdf",
                                                   mime='application/octet-stream')





