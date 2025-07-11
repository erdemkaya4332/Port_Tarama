import sys
from utils import Kullanici_Giris
from utils import Port_Tarama

def main():
    print("--- Python ile Nmap Port Tarayıcı ---")
    try:
        hedef_ipler = Kullanici_Giris.IP_Girisi()
        port_araligi = Kullanici_Giris.Port_Girisi()
        print(f"\nToplam {len(hedef_ipler)} IP adresi taranacak.")
        print(f"Port araligi: {port_araligi}")

        print("\n--- Tarama Sonuclari ---")

        for ip in hedef_ipler:
            Port_Tarama.Port_Tarama(ip, port_araligi)

        print("\nTarama tamamlandi.")

    except Exception as e:
        print(f"\nBeklenmedik bir hata oluştu ve program sonlanıyor: {e}")
        sys.exit(1)



if __name__ == "__main__":
    main()