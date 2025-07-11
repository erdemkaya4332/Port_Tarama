import nmap

def Port_Tarama(hedef_ip, taranacak_portlar):
    nm = nmap.PortScanner()
    try:
        print(f"'{hedef_ip}' adresi ve '{taranacak_portlar}' port aralığı üzerinde  tarama başlatılıyor...")
        nm.scan(hedef_ip, taranacak_portlar, arguments='-T4 -sV ')

        if hedef_ip in nm.all_hosts():
            if nm[hedef_ip].state() == 'up':
                if 'tcp' in nm[hedef_ip]:
                    for port in nm[hedef_ip]['tcp'].keys():
                        port_durum = nm[hedef_ip]['tcp'][port]['state']
                        servis = nm[hedef_ip]['tcp'][port]['name']
                        surum = nm[hedef_ip]['tcp'][port].get('version', 'Bilinmiyor')
                        print(f"Port {port} {port_durum} | Servis: {servis if servis else 'Bilinmiyor'} | Sürüm: {surum if surum else 'Bilinmiyor'} ", flush=True)
                else:
                    print(f"Uyarı: '{hedef_ip}' hostu Nmap tarafından 'down' olarak işaretlendi. Açık port bulunamayabilir.")
            else:
                print(f"Uyarı: '{hedef_ip}' hostu tarama sonuçlarında bulunamadı. Host mevcut olmayabilir veya ulaşılamaz olabilir.")

    except nmap.PortScannerError as e:
        print(f"Hata: Nmap taraması sırasinda bir 'PortScannerError' oluştu for '{hedef_ip}': {e}")
        print(
            "Lütfen Nmap'in doğru kurulduğundan ve yeterli yetkilere sahip olduğunuzdan emin olun.")
    except Exception as e:
        print(f"Hata: '{hedef_ip}' üzerinde tarama sırasında beklenmedik bir hata oluştu: {e}")





