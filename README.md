# DUYGU ANALİZ PROGRAMI 🧠

Python, OpenCV ve Keras/TensorFlow kullanarak geliştirilmiş, gerçek zamanlı yüz ifadelerinden duygu tahmini yapan bir Derin Öğrenme projesidir.

## 🛠️ Teknolojiler & Kütüphaneler
* **Dil:** Python
* **Derin Öğrenme:** TensorFlow, Keras
* **Görüntü İşleme:** OpenCV (Yüz tespiti için Haar Cascade)
* **Veri İşleme:** NumPy, Pandas
* **Arayüz:** Streamlit (Web tabanlı demo)

## 🏗️ Mimari Yapı
Proje, Convolutional Neural Network (CNN) mimarisi üzerine kuruludur:
1. **Veri Ön İşleme:** Görüntülerin gri tonlamaya çevrilmesi ve boyutlandırılması.
2. **Model Eğitimi:** CNN katmanları ile yüz ifadelerindeki örüntülerin (mutlu, üzgün, kızgın vb.) çıkarılması.
3. **Gerçek Zamanlı Tahmin:** OpenCV ile kamera üzerinden alınan verinin eğitilen model ile anlık analizi.



## 🎯 Proje Özellikleri
* **Yüksek Doğruluk:** CNN modeli ile farklı yüz ifadelerinin sınıflandırılması.
* **Canlı Analiz:** Web kamerası üzerinden anlık duygu tespiti.
* **Kolay Kullanım:** Streamlit ile şık ve interaktif bir arayüz.

## 🚀 Kurulum ve Çalıştırma
Projeyi kendi bilgisayarınızda denemek için aşağıdaki adımları sırasıyla uygulayın:

**1. Repoyu klonlayın:** Terminalinizi açın ve kodları bilgisayarınıza çekmek için şu komutu çalıştırın
   ```bash
   git clone https://github.com/ikbaltorun/duygu-analizi
   ```
**2. Gerekli Kütüphaneleri Kurun:** Projenin çalışması için ihtiyaç duyulan Derin Öğrenme ve Görüntü İşleme modüllerini yüklemek için şu komutu çalıştırın
   ```bash
   pip install opencv-python tensorflow keras numpy pandas streamlit
   ```
**3. Uygulamayı Başlatın:** Web tabanlı Streamlit arayüzünü çalıştırmak ve kamerayı aktif hale getirmek için şu komutu kullanın
   ```bash
   streamlit run app.py
   ```
(Not: Eğer çalıştırılacak ana Python dosyanızın adı farklıysa, komuttaki app.py kısmını kendi dosya adınızla değiştirin.)

---
*İkbal Torun|2026*

