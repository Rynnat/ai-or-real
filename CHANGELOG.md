# Sürüm geçmişi

## 0.2.1

- Ayarlardaki "Yedekle" bölümü tamamen kaldırıldı: dışa/içe aktarma butonları, gizli dosya seçici, durum satırı, ilgili CSS/JS ve 6 çeviri anahtarı (TR+EN) silindi. Ayarlar panelinde DİL satırının ardından doğrudan KREDİLER geliyor.
- Service worker önbellek anahtarı ve `lab.css` sürüm parametresi 0.2.1'e çekildi; eski önbelleğin güncellemeyi gizlemesi önlendi.

## 0.2.0 — Dev taslağı (henüz yayınlanmadı)

- **Kritik görsel düzeltme:** oyun sahnesi `aspect-ratio:1` (kare) ile sabitlenmişti, ama kütüphanedeki 297 görselin tamamı 1024×768 (4:3) — bu yüzden her turda, her temada görselin üstünde/altında boş bar kalıyordu. Sahne oranı `4/3`'e çekildi (masaüstü + mobil portrait); görseller artık çerçeveyi kırpılmadan tam dolduruyor.
- SFX motoruna ortak master bus + hafif kompresör eklendi (tüm sesler artık bunun üzerinden çıkıyor); tema seslerinin genel kazancı yükseltildi; kombo vuruşlarının güç eğrisi genişletildi; ARCADE'deki gibi katmanlı sub-bas her temaya eklendi; final vuruşları kalınlaştırıldı — kombolar artık ARCADE'e daha yakın şiddette.
- `sw.js` artık `images.json`'daki tüm oyun görsellerini de install sırasında önbelleğe alıyor; "offline çalışır" iddiası ilk açılıştan itibaren gerçekten geçerli.
- `manifest.json`: `display` "fullscreen"den "standalone"a çevrildi (bazı platformlarda daha tutarlı PWA kurulum davranışı).
- Ayarlara "Yedekle" bölümü eklendi: mevcut ayarlar + skor tablosu tek JSON dosyası olarak dışa aktarılabiliyor, aynı dosyadan içe aktarılıp geri yüklenebiliyor (cihaz değişince/tarayıcı verisi silinince veri kaybını önler).
- Arcade dışındaki bütün yanlış cevap sesleri telefon ve dizüstü hoparlörlerinde duyulacak frekanslara taşındı; her paketin temel oyun olaylarını kapsaması otomatik kontrole eklendi.
- Algı laboratuvarı teması: kırık beyaz zemin, turuncu vurgu, sade tipografi.
- Açılış, oyun, sonuç ve ayarlar yeni temaya uyarlandı.
- Neon seri efektleri sadeleştirildi; puanlama ve oyun akışı korundu.
- Sabit laboratuvar teması için eski meyve renk seçicisi kaldırıldı.
- Ekip sunumu için ayarlara Laboratuvar ve beş neon tema seçeneği eklendi; seçim anında uygulanıp cihazda saklanıyor.
- Tema seçimi renk paletinden tam arayüz geçişine çevrildi: LAB laboratuvar kompozisyonunu; neon seçenekleri arcade kompozisyonu, terminal tipografisi, eski metin ve efektleri kullanıyor.
- Renk varyantları tema menüsünden kaldırıldı. Menü artık iki bağımsız tasarım konsepti sunuyor: Deney ve Neon Arcade.
- Sunum ayarları beş katmana ayrıldı: Tasarım, Arka Plan, Yazı, VFX ve SFX. Hareket VFX seviyesine dahil edildi; tipografi, şekil, vurgu ve görsel sunumu Tasarım paketinde kaldı.
- Kontrast koruması eklendi: aynı açıklıktaki arka plan ve yazı seçildiğinde son seçim korunup karşı seçenek güvenli renge çevriliyor; Otomatik mod tasarıma göre okunabilir çifti çözüyor.
- Yerel geliştirme adreslerinde eski sürüm gösterilmemesi için service worker ve önbellek devre dışı bırakıldı.
- Açık/koyu seçenekleri gerçek renk paletleriyle değiştirildi. Yalnızca birebir aynı arka plan ve yazı rengi engelleniyor; farklı renk kombinasyonları sunum için serbest.
- Kâğıt, mürekkep ve kobalt seçenekleri arka plan ile yazı satırlarında aynı sütunlara hizalandı.
- Laboratuvar açılışındaki slogan sürüm numarasıyla değiştirildi; köşedeki tekrar eden sürüm etiketi kaldırıldı.
- Ayarlar paneli uygulama paletinden ayrıldı; mavi arka plan/siyah yazı gibi kombinasyonlarda başlıklar ve VFX kontrolleri sabit yüksek kontrastla gösteriliyor.
- Arcade açılışındaki “Yapay zekâ mı · Gerçek mi” satırı da sürüm numarasıyla değiştirildi.
- Tasarım düğmeleri hazır palet presetlerine dönüştürüldü: Deney kâğıt/mürekkep, Arcade mürekkep/kâğıt yükler. Sonrasında arka plan ve yazı ayrı ayrı özelleştirilebilir; temaya tekrar basmak orijinal paleti geri getirir.
- Laboratuvar tasarımının menü adı “Deney” yerine “EVIDENCE” olarak değiştirildi.
- Renk paletleri 2x5 düzene sıkıştırıldı: kâğıt, mürekkep, kobalt, sarı, mercan, menekşe, camgöbeği, gül, kum ve neon. Fazla orman tonu kaldırıldı.
- Tema seçenekleri 2x3 ızgaraya alınarak ayarlar panelinin yüksekliği azaltıldı.
- Spectrum başlığı aynı taban çizgisine hizalandı ve açılış kompozisyonu daha aşağı taşındı.
- Oyun sonu ekranındaki tekrar oynama düğmesine, skorun yanlışlıkla geçilmesini önleyen 3 saniyelik geri sayım kilidi eklendi.
- Genel SFX ve Genel VFX adları netleştirildi; Tema SFX alanı altı paketli ızgaraya dönüştürüldü. ARCADE korunurken EVIDENCE, SIGNAL, ARCHIVE, SPECTRUM ve ORBIT için tıklama, cevap, sayaç, bitiş ve bütün kombo seviyelerinde ayrı ritim/melodi sistemleri; farklı osilatör, harmonik, filtre, zarf ve yankı karakterleri oluşturuldu.
- Tema SFX düğmeleri görsel tema düğmeleriyle aynı sıraya ve renk kimliğine getirildi; paket seçimi kısa kombo önizlemesi çalıyor.
- Arcade'deki güç eğrisi tema paketlerine uyarlandı: çarpan büyüdükçe ses seviyesiyle birlikte nota sayısı, katman, bas, yoğunluk, süre ve final vuruşu kademeli olarak artıyor.
- Altıncı tasarım adayı ORBIT eklendi: koyu uzay konsolu, yörünge çizgileri, radar yüzeyleri ve camgöbeği preset paleti.
- Oyun içi görseller kare olacağı için tüm temalardaki sahne oranı ve dış çizgiler kareye uyarlandı; Signal ve Orbit'in dairesel kırpması kaldırıldı.
- Ayarlar başlığına oturumluk geliştirici modu açan böcek düğmesi eklendi. Tema, Tema SFX ve renk araçları yalnızca bu modda görünür; normal kullanıcıya Genel SFX, Genel VFX, Dil ve Krediler kalır.
- Geliştirici modunda klasik oyuna BİTİR ve ÇIKIŞ kontrolleri eklendi. BİTİR süreyi sıfırlayıp güvenli skor ekranını açar; ÇIKIŞ geri sayım dahil aktif turu iptal edip ana menüye döner.
- Klasik mod düğmesi Türkçede KLASİK, İngilizcede CLASSIC gösterilecek şekilde yerelleştirildi.
- Katlayıcı rozeti VFX kapalıyken de görünür tutuldu; Evidence, Signal, Archive, Spectrum ve Orbit için yüksek kontrastlı tema yüzeyleri eklendi.
- Ayar satırları sabit etiket/araç ızgarasına geçirildi; arka plan ve yazı renkleri aynı sütunlarda hizalanıyor.
- SFX ve VFX satırları birlikte Dil satırının hemen üstüne taşındı.
- VFX düğme grubu sola yaslandı.
- SFX kontrolü anahtar ve beş kademeli ses göstergesine dönüştürüldü; kademeler gerçek WebAudio çıkış seviyesini değiştirip cihazda saklıyor.
- Arka plan/yazı kontrolleri Renk 1/Renk 2 sistemine dönüştürüldü. Renk 1 ana yüzeyi, Renk 2 vurgu ve tema kimliğini yönetiyor; normal metin Renk 1’e göre otomatik siyah veya açık seçiliyor.
- Tema presetleri EVIDENCE için kâğıt/mercan, ARCADE için mürekkep/neon yeşil yükler; iki renk sonradan bağımsız değiştirilebilir.
- EVIDENCE açılışındaki “BİLGİ AI CLUB / Algı Laboratuvarı” şeridi ve “DENEY / 001” etiketi kaldırıldı.
- EVIDENCE Sonsuz Mod düğmesi ince çerçeve, hafif yüzey ve daha belirgin metinle görünür hale getirildi.
- Üç yeni tam tasarım teması eklendi: SIGNAL, ARCHIVE ve SPECTRUM. Her biri kendi yerleşim, tipografi, buton, oyun alanı, sonuç ekranı ve renk presetiyle çalışıyor.
- Yeni temaların açılış kompozisyonları ayrıştırıldı: SIGNAL skor solda/oyun sağda, ARCHIVE yatay dosya ve iki sütunlu skor şeridi, SPECTRUM üst üste binen afiş düzeni kullanıyor.
- Buton geometrileri temalara ayrıldı: SIGNAL kesik köşeli kontrol paneli ve kapsül ikincil eylem; ARCHIVE dosya sekmesi ve mühür; SPECTRUM büyük kapsül ve çıkartma formları kullanıyor.
- Buton ölçü hiyerarşisi temalara göre ayarlandı: ana eylemler büyütüldü, Sonsuz Mod kontrolleri küçültüldü; SPECTRUM masaüstünde dairesel ana eylem kullanıyor ve mobilde geniş kapsüle dönüşüyor.
- SPECTRUM Sonsuz Mod düğmesi skor kartının üzerinden alınarak CLASSIC’in altına taşındı; kompozisyon masaüstünde 28px aşağı kaydırıldı.
- Ana mod düğmesi iki dilde de START/BAŞLA yerine CLASSIC olarak adlandırıldı.
- Tema düğmeleri uygulama paletinden ayrıldı: Deney ve Arcade artık kendi sabit önizleme renklerini kullanıyor; seçili durum her kombinasyonda mavi halkayla gösteriliyor.
- Mobil skor geçişinin kaldırılması bu sürüme dahil.
- JavaScript/JSON ve yerel HTTP kontrolü yapıldı; görsel tarayıcı testi yapılmadı.
- Derin SFX denetimi: ORBIT temasının en yüksek kombo katmanındaki 27.5 Hz alt-bas notası, WebAudio ses motorunun 45 Hz alt sınırı yüzünden sabit tona düşüyordu (yükselen sweep hiç çalmıyordu) — 45→66 Hz'e çekilerek düzeltildi.
- Skor tablosu 5'ten 10 kayda çıkarıldıktan sonra unutulan "TOP 5" metinleri ("... TOP 5'E GİRDİN", "TOP 5 LEADERBOARD", "Top 5'e girince...") hem TR hem EN'de "TOP 10" ile güncellendi.
- add_images.py ve materialize.py'deki dosya adlandırma `{idx:02d}` yerine mevcut 3 haneli kütüphane adlandırmasıyla (001.jpg…318.jpg) eşleşecek şekilde `{idx:03d}` yapıldı.


## 0.1.1 — Hazırlanıyor (henüz yayınlanmadı)

- Telefonda skor tablosuna sağ/sol okla geçiş kaldırıldı.
- Mobil başlangıç ekranı tek sütuna indirildi; gizli ikinci sayfa kaldırıldı.
- Geniş ekran skor tablosu ve oyun sonu skorları korundu.
- JavaScript sözdizimi kontrol edildi; tarayıcı testi henüz yapılmadı.


## 0.1.0 — 2026-08-31

İlk temel sürüm. Mevcut arcade görünümü korunmuştur; yeni tasarım henüz uygulanmamıştır.

- AI or Real adıyla bağımsız proje başlatıldı.
- Orijinal görseller ve oyun akışı korundu.
- Eski çevrimiçi skor tablosu bağlantısı kaldırıldı; skorlar cihazda tutuluyor.
- Tarayıcı depolama ve önbellek adları ayrıldı.
- Hazır rekor kaldırıldı ve ekran yön kilidi açıldı.

### Doğrulama

JavaScript ve JSON sözdizimi kontrol edildi. Tarayıcı ve cihaz testleri henüz yapılmadı.

## Sürüm kuralları

- VERSION, oyundaki BUILD ve bu dosya birlikte güncellenir.
- Her sürüm Git etiketiyle işaretlenir: v0.1.0, v0.1.1 vb.
- Küçük görünüm düzeltmeleri: 0.1.x; kapsamlı arayüz yenilemesi: 0.2.0.
- İlk GitHub pushundan sonraki değişiklikler, kullanıcı internet önizlemesini görüp onaylamadan GitHub'a gönderilmez.
- Bir commit veya etiket oluşturulması, internette yayın yapıldığı anlamına gelmez.
