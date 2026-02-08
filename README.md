## 🔧 Teknik Detaylar
* **Veri Kaynağı:** OpenWeatherMap 5 günlük / 3 saatlik tahmin verisi kullanılmıştır.
* **Veri İşleme:** Kullanıcının istediği gün sayısına göre `8 * n` formülü ile veri setinden ilgili aralık filtrelenmiştir.
* **Modüler Yapı:** Backend mantığı `get_data` fonksiyonu ile izole edilmiştir, böylece farklı arayüzlere (Streamlit, Flask vb.) kolayca entegre edilebilir.
