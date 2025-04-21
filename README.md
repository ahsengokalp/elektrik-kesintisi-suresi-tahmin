⚡ Elektrik Kesintisi Süre Tahmin Modeli
Bu proje, geçmiş kesinti verilerine ve hava durumuna dayanarak elektrik kesintisi süresini tahmin etmek amacıyla geliştirilmiş bir sınıflandırma modeli içerir. Proje kapsamında, kullanıcı dostu bir Streamlit arayüzü geliştirilerek hem tahminlerin hem de verilerin görsel olarak sunulması sağlanmıştır.

📌 Proje Özeti
📊 Veri Görselleştirme: Kullanıcı, belirli bir tarihi seçerek o gün yaşanan elektrik kesintilerini tablo halinde görüntüleyebilir.

📈 Model Tahmin Sonuçları: Eğitim aşamasında elde edilen precision, recall ve F1-score gibi metrikler sınıflara göre sunulur.

⏳ Kesinti Süresi Tahmini: Kullanıcıdan alınan il ve hava durumu bilgisine göre model, kesintinin tahmini süresini ve bitiş zamanını verir.

🧠 Kullanılan Teknolojiler
Python 3.x

Pandas, NumPy

Scikit-learn

Streamlit (arayüz için)

Matplotlib / Seaborn (grafikler için)

Jupyter Notebook (model eğitimi)

📊 Model Performansı

Sınıf	Precision	Recall	F1-Score	Support
Kısa	0.77	0.95	0.85	982
Orta	0.42	0.27	0.33	272
Uzun	0.44	0.07	0.12	179
Çok Uzun	0.60	0.66	0.63	168
📌 Notlar
Uygulama görsel olarak sade ve kullanıcı dostu bir tasarıma sahiptir.

Tahmin sınıfları, hava durumu ve il bilgisine göre sınıflandırılmaktadır.

Kesinti süresi tahminleri yaklaşık dakikalar bazında hesaplanır.
