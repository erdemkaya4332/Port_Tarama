# Python Nmap Port Tarayıcı

Bu proje, Python programlama dili ve `python-nmap` kütüphanesini kullanarak geliştirilmiş basit ve etkili bir port tarayıcı uygulamasıdır. Belirtilen IP adresleri veya /24 ağ aralıkları üzerinde port taraması yaparak açık portları, üzerlerinde çalışan servisleri ve versiyon bilgilerini keşfeder.

## Özellikler

* **Esnek IP Girişi**: Tek bir IP adresi (örn. `192.168.1.1`) veya bir /24 ağ aralığı (örn. `192.168.1.0/24`) taraması yapabilme.
* **Özelleştirilebilir Port Aralığı**: Kullanıcının belirlediği port aralığında (örn. `1-1024`, `80-443`) tarama yapabilme.
* **Servis ve Versiyon Tespiti**: Açık portlar üzerinde çalışan servisleri ve bunların versiyon bilgilerini görüntüleme.
* **Kapsamlı Hata Yönetimi**: Geçersiz IP/port girişleri ve Nmap taraması sırasında oluşabilecek hatalar için kullanıcı dostu geri bildirimler.
* **Temiz ve Modüler Kod Yapısı**: Her bir ana işlevselliğin (kullanıcı girişi, port taraması) ayrı modüllere ayrılması.

## Klasör Yapısı

* `main.py`: Uygulamanın ana yürütülebilir dosyasıdır. Kullanıcı etkileşimini ve tarama sürecini koordine eder.
* `utils/`: Yardımcı fonksiyonları içeren modüllerin bulunduğu dizin.
    * `Kullanici_Giris.py`: Kullanıcıdan IP ve port bilgilerini almak için girdi doğrulama fonksiyonları.
    * `Port_Tarama.py`: Nmap kütüphanesini kullanarak gerçek port tarama mantığını içerir.

## 🚀 Nasıl Çalıştırılır?

### Ön Koşullar

Bu projeyi çalıştırabilmek için sisteminizde aşağıdaki yazılımların kurulu olması gerekmektedir:

1.  **Python 3.13: Proje Python 3 üzerinde geliştirilmiştir.
    * [Python İndirme Sayfası](https://www.python.org/downloads/)
2.  **Nmap**: Port taraması için temel araçtır.
    * [Nmap İndirme Sayfası](https://nmap.org/download.html)
3.  **Gerekli Python Kütüphaneleri**:
    * `python-nmap`: Nmap'i Python üzerinden kullanmak için gerekli kütüphane.
    * `ipaddress`: IP adresleri ve ağlar üzerinde işlem yapmak için Python'ın yerleşik kütüphanesi

### Uygulama Kullanımı
1.IP Adresi veya Ağ Aralığı Girişi
Program sizden taranacak IP adresini veya ağ aralığını isteyecektir:

Tek IP Adresi Örneği: 
<img width="413" height="69" alt="image" src="https://github.com/user-attachments/assets/302950eb-8b4b-4921-9aeb-876597cb0d7d" />

Ağ Aralığı Örneği (/24):
<img width="540" height="69" alt="image" src="https://github.com/user-attachments/assets/603f655f-eec6-4ac6-9fae-81083806111d" />

2. Port Aralığı Girişi
Ardından taranacak port aralığını girmeniz istenecektir:

Port Aralığı Örneği:
<img width="403" height="76" alt="port_giris" src="https://github.com/user-attachments/assets/18167acc-7662-4b00-9ea0-7e1ec5d18379" />

3. Tarama Çıktısı
Program, girilen IP(ler) üzerinde belirtilen port aralığını taramaya başlayacak ve her bir portun durumunu anlık olarak ekrana yazdıracaktır. Açık portlar için servis ve sürüm bilgisi de gösterilecektir.

<img width="669" height="221" alt="image" src="https://github.com/user-attachments/assets/5e3162ca-fe77-4002-89f1-abaa363c42f4" />


