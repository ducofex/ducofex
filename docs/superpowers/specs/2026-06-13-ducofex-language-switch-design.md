# Ducofex dil seçimi ve YouTube entegrasyonu tasarımı

## Özet

`products/cnc/web/website_v1/Option1` içindeki canlı sayfalara iki dilli bir arayüz eklenecek. Varsayılan dil `TR` olacak, üst kısımda küçük `TR | EN` seçicisi bulunacak, kullanıcı seçimi tarayıcıda saklanacak ve sayfalar arasında korunacak. Ayrıca Ducofex YouTube hesabı `https://www.youtube.com/@Ducofex` header veya footer sosyal alanına entegre edilecek.

Bu çalışma yalnızca aktif kullanılan canlı sayfaları kapsar:

- `index.html`
- `machines.html`
- `gen-1.html`
- `gen-2.html`
- `about-us.html`
- `contact-us.html`
- `partners.html`
- `printing-3d.html`
- `printable-models.html`
- `lokumai.html`

Eski template sayfalar bu kapsamın dışındadır.

## Hedefler

- Siteye Türkçe ve İngilizce arasında hızlı geçiş eklemek
- Varsayılan dili Türkçe yapmak
- Seçilen dili sayfa yenilense veya kullanıcı başka canlı sayfaya geçse bile korumak
- Mevcut statik site yapısını bozmamak
- YouTube hesabını görünür ve profesyonel bir şekilde eklemek

## Yaklaşım

Statik site yapısı korunacak. Ayrı `tr` ve `en` sayfaları üretmek yerine tek HTML dosya seti üzerinde istemci taraflı bir dil sistemi kurulacak.

### Önerilen teknik çözüm

- Her canlı sayfada çevrilebilir metin alanları işaretlenecek
- Ortak bir JavaScript dosyası üzerinden dil sözlüğü uygulanacak
- Dil seçimi `localStorage` içine yazılacak
- Sayfa açıldığında varsayılan olarak `TR`, kayıt varsa seçilmiş dil yüklenecek

Bu çözüm mevcut yapıya en az müdahale eden ve bakım maliyeti en düşük olan çözümdür.

## Arayüz davranışı

### Dil seçici

- Header üst şeritte küçük `TR | EN` seçici olacak
- Aktif dil daha belirgin görünecek
- Varsayılan seçim `TR` olacak
- Kullanıcı seçince aynı anda metinler değişecek

### YouTube entegrasyonu

- Ducofex YouTube bağlantısı sosyal alana eklenecek
- En az footer’da görünür olacak
- Uygun görünürse header üst şeritte e-posta yanında da gösterilecek

## İçerik kapsamı

Çeviri şu alanları kapsayacak:

- header üst şerit metinleri
- menü başlıkları
- hero başlıkları ve açıklamaları
- CTA butonları
- kart başlıkları ve açıklamaları
- footer kısa marka metni
- aktif canlı sayfalardaki gövde metinleri

Çevrilmeyecek veya şimdilik sabit kalabilecek alanlar:

- dosya adları
- URL yapısı
- marka adı `Ducofex`
- e-posta adresi ve sosyal linkler

## Mimari notlar

### JavaScript

Mevcut `js/functions.js` dosyasına gereğinden fazla gömülmek yerine dil sistemi için net ve izole bir bölüm eklenecek ya da ayrı bir dosya oluşturulacak. Amaç, mevcut legacy script’leri bozmeden dil davranışını sade tutmaktır.

### HTML işaretleme

Çevrilecek metinler ya:

- `data-i18n` benzeri attribute ile işaretlenecek

veya

- ortak bir sözlük anahtarına bağlanacak

Yaklaşım uygulama sırasında mevcut HTML yapısına en güvenli uyacak formda seçilecek.

## Hata önleme kuralları

- Eğer bir anahtarın İngilizce veya Türkçe karşılığı eksikse bu açıkça tespit edilmeli
- Hiçbir canlı sayfada yarım Türkçe yarım İngilizce görünüm bırakılmamalı
- Mobil menü de ana menü ile aynı dil mantığını kullanmalı
- Dil seçimi bozulursa güvenli geri dönüş dili `TR` olmalı

## Test beklentileri

Uygulama sonrası şu kontroller yapılacak:

- tüm canlı sayfalarda `TR | EN` seçici görünüyor mu
- ilk açılışta dil `TR` mi
- `EN` seçilince aynı sayfadaki metinler değişiyor mu
- başka bir canlı sayfaya geçince seçilen dil korunuyor mu
- mobil menüde de çeviri çalışıyor mu
- YouTube linki doğru hesaba gidiyor mu
- validator mevcut canlı site için bozulmuyor mu

## Kabul kriterleri

Çalışma başarılı sayılırsa:

- canlı sayfalarda iki dilli geçiş çalışır
- varsayılan dil Türkçedir
- dil seçimi kalıcıdır
- butonlar ve menü etiketleri iki dilde de profesyonel görünür
- YouTube hesabı siteye eklenmiştir
- deploy için yine yalnızca `Option1` klasörü yeterlidir
