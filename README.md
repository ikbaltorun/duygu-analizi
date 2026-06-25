# Emotion Recognition System 🧠

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

## 🚀 Nasıl Çalıştırılır?
1. Repoyu klonlayın:
   ```bash
   git clone (https://github.com/ikbaltorun/duygu-analizi)
