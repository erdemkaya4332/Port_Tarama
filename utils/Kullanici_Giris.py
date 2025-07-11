import ipaddress
import sys


def IP_Girisi():
    while True:
        hedef_girdi = input("Taranacak IP adresini giriniz: ").strip()
        try:
            try:
                ip = ipaddress.ip_address(hedef_girdi)
                print(f"'{hedef_girdi}' tek bir IP adresi olarak algılandı.")
                return [str(ip)]
            except ValueError:
                pass

            girdi = ipaddress.ip_network(hedef_girdi, strict=False)
            if isinstance(girdi, ipaddress.IPv4Network) and girdi.prefixlen == 24:
                print(f"'{hedef_girdi}' bir /24 ağ olarak algılandı. Hostlar taranacak.")
                return [str(ip) for ip in girdi.hosts()]
            else:
                print("Hata: Sadece tek bir IP adresi veya /24'lük ağ aralığı desteklenmektedir.")
                continue
        except ValueError:
            print("Hata: Geçersiz IP adresi veya ağ formatı. Lütfen 'X.X.X.X' veya 'X.X.X.0/24' formatında girin.")
        except Exception as e:
            print(f"Beklenmedik bir hata oluştu: {e}")
            sys.exit(1)

def Port_Girisi():
    while True:
        port_girdi = input("1-65535 arasında bir port aralığı giriniz: ").strip()
        try:
            parcalar = port_girdi.split('-')
            if len(parcalar) != 2:
                raise ValueError("Hatalı format. Lütfen başlangıç-bitiş formatında girin.")
            baslangic_portu = int(parcalar[0])
            bitis_portu = int(parcalar[1])

            if not (1 <= baslangic_portu <= 65535 and 1 <= bitis_portu <= 65535):
                print("Hata: Port numaraları 1 ile 65535 arasında olmalıdır.")
                continue

            if baslangic_portu > bitis_portu:
                print("Hata: Başlangıç portu bitiş portundan büyük olamaz.")
                continue
            return f"{baslangic_portu}-{bitis_portu}"

        except ValueError as ve:
            print(f"Hata: Gecersiz port araligi formati. {ve}")
        except Exception as e:
            print(f"Beklenmedik bir hata olustu: {e}")
            sys.exit(1)
