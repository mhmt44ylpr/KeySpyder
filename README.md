
# 🕷️ KeySpyder

KeySpyder, Python ile yazılmış, kullanıcıların klavye tuş kayıtlarını izleyen (keylogger) ve bu kayıtları e-posta yoluyla ileten bir araçtır. Eğitim ve güvenlik testleri amacıyla geliştirilmiştir.
![Ekran görüntüsü 2025-05-24 210733](https://github.com/user-attachments/assets/31fca2d3-2862-4fe2-b962-4fe0cdc55ca2)

---

## 🚨 Uyarı

**Bu araç yalnızca eğitim, test ve etik hackleme amaçlı kullanılmalıdır. İzinsiz kullanım, kişisel gizliliği ihlal eder ve yasalara aykırıdır. Geliştirici hiçbir yasa dışı kullanımda sorumluluk kabul etmez.**

---

## 🛠️ Özellikler

- Klavye tuşlarını izler.
- Tüm kayıtları `.txt` olarak kaydeder.
- `ESC` tuşuna basıldığında logları e-posta olarak gönderir.
- Dinamik olarak Python dosyasından `.exe` üretimi sağlar.
- `Rich`, `Figlet`, `Colorama` ile zengin terminal çıktısı.
- `--onefile` ile tek dosya EXE oluşturma desteği.
- CapsLock aktifse büyük harf kaydı yapar.

---

## 📦 Gereksinimler

> Python 3.8+ önerilir.

Aşağıdaki modüllerin kurulu olması gerekir:

```bash
pip install -r requirements.txt
```

### `requirements.txt` içeriği:
```txt
pynput
rich
colorama
pyfiglet
```

Ek olarak PyInstaller gereklidir:
```bash
pip install pyinstaller
```

---

## 🔧 Kullanım

Komutu terminalden şu şekilde çalıştırın:

```bash
python keyspyder.py -m example@gmail.com -p sifren123
```

| Parametre | Açıklama                       |
|----------|-------------------------------|
| `-m`     | Gönderici ve alıcı mail adresi |
| `-p`     | Mail hesabının şifresi         |

> `smtp.gmail.com` kullanıldığı için Gmail hesabınızda **"Daha az güvenli uygulama erişimini"** açmanız veya **uygulama şifresi** oluşturmanız gerekebilir.

---

## 🧪 Örnek Terminal Çıktısı

```text
    __ __           _____                 __
   / //_/__  __  __/ ___/____  __  ______/ /__  _____
  / ,< / _ \/ / / /\__ \/ __ \/ / / / __  / _ \/ ___/
 / /| /  __/ /_/ /___/ / /_/ / /_/ / /_/ /  __/ /
/_/ |_\___/\__, //____/ .___/\__, /\__,_/\___/_/
          /____/     /_/    /____/

[+] Mail doğrulandı
[+] Keyspader.py dosyası oluşturuldu
[+] EXE dosyası dist/Keyspader.exe olarak oluşturuldu
```

---

## 📁 Dosya Yapısı

```
KeySpyder/
├── keyspyder.py       # Ana uygulama
├── Keyspader.py       # Otomatik oluşturulan keylogger kodu
├── dist/              # EXE dosyasının çıktısı
├── build/             # PyInstaller build klasörü
├── README.md
└── requirements.txt
```

---

## ⚙️ EXE Oluşturma

Kod, `Keyspader.py` adında yeni bir keylogger dosyası oluşturur ve ardından `pyinstaller` ile `.exe` formatına dönüştürür.

Komut örneği:

```bash
python keyspyder.py -m example@gmail.com -p sifren123
```

Ardından `dist/Keyspader.exe` içinde EXE dosyanız hazır olacaktır.

---

## 📬 Logların Gönderimi

- Tuş logları `log.txt` olarak kaydedilir.
- `ESC` tuşuna basıldığında bu dosya e-posta ile iletilir.
- Hatalar `Rich` kullanılarak loglanır.

---

## 🧑‍💻 Geliştirici

**KeySpyder** by CHARON 
 
📌 GitHub: [github.com/mhmt44ylpr](https://github.com/mhmt44ylpr)

---

## 🛡️ Lisans

Bu proje MIT Lisansı ile lisanslanmıştır. Detaylar için [LICENSE](LICENSE) dosyasına göz atın.
