# AI or Real

AI ile üretilmiş görselleri gerçek fotoğraflardan ayırt etme oyunu.
Başlangıç kodu: https://github.com/rynnat/ai-or-not

## Bu başlangıç sürümü

- Orijinal oyundan bağımsız Git deposu; henüz uzak depo veya yayın yok.
- AI or Real adı ve bağımsız tarayıcı depolama anahtarları.
- Eski çevrimiçi skor tablosuyla bağlantı kapalı; skorlar yalnızca bu cihazda saklanır.
- Hazır örnek rekor kaldırıldı; tablo gerçek oyun sonuçlarıyla dolar.
- PWA yön kilidi kaldırıldı. Tam telefon/tablet/masaüstü tasarımı henüz yapılmadı.

## Geliştirme öncelikleri

1. Hesapsız, açıklama gerektirmeyen hızlı başlangıcı koru.
2. Telefon, tablet ve masaüstünde kırpılmayan görseller ve rahat cevap butonları.
3. Yeni görsel kimlik ve erişilebilir klavye/dokunma etkileşimi.
4. Yayından önce sunucu tarafında güvenli ortak skor tablosu.

## Yerel çalıştırma

Bu klasörü statik bir HTTP sunucusuyla sunun; örneğin Python kuruluysa:

```sh
python -m http.server 4173 --bind 127.0.0.1
```

Ardından http://127.0.0.1:4173 adresini açın.
