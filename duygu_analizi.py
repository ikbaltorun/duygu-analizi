import cv2
from deepface import DeepFace

face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
cap = cv2.VideoCapture(0)

print("Kamera açılıyor... Çıkmak için 'q' tuşuna basabilirsin.")

# Dalgalanmaları önlemek için son ölçümleri tutacağımız bir liste oluşturuyoruz
son_skorlar = []

while True:
    ret, frame = cap.read()
    if not ret:
        print("Kameradan görüntü alınamadı!")
        break

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.3, minNeighbors=5)

    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
        face_roi = frame[y:y+h, x:x+w]
        
        try:
            result = DeepFace.analyze(face_roi, actions=['emotion'], enforce_detection=False)
            anlik_skor = result[0]['emotion']['happy']
            
            # YENİ EKLENEN KISIM: Pürüzsüzleştirme (Smoothing)
            # Anlık skoru listeye ekle
            son_skorlar.append(anlik_skor)
            
            # Eğer listede 10'dan fazla kayıt biriktiyse, en eskisini sil
            if len(son_skorlar) > 10:
                son_skorlar.pop(0)
            
            # Listedeki son 10 skoru toplayıp ortalamasını al
            ortalama_skor = sum(son_skorlar) / len(son_skorlar)
            
            # Artık anlık skora değil, ortalamaya göre karar veriyoruz
            if ortalama_skor > 75:
                durum = "Mutlu"
                renk = (0, 255, 0)
            elif ortalama_skor > 20:
                durum = "Tebessum Ediyor"
                renk = (255, 255, 0)
            else:
                durum = "Durgun"
                renk = (0, 0, 255)
            
            text = f"{durum} - Gulumseme: %{int(ortalama_skor)}"
            cv2.putText(frame, text, (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.7, renk, 2, cv2.LINE_AA)
            
        except Exception as e:
            pass 

    cv2.imshow('Gercek Zamanli Duygu Analizi', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
