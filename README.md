# python-telnet-server
Python telnet server

Kurulum:
1) "sudo su" komutuyla root yetkisinde terminal açın 
2) "cd /x" ile usb bellek dizinini açın
3) "mount -o remount,rw /usr" komutuyla dizine yazma yetkisi verelim
4) "mkdir /usr/telnet" komutuyla telnet için dizin oluşturalım
5) "cp startTelnet.py /usr/telnet/ && cp telnet.py /usr/telnet/" komutu ile telnet dosyalarını linux sisteme kopyalayın
6) "chmod 777 /usr/telnet/telnetStart.py && chmod 777 /usr/telnet/telnet.py" komutunu çalıştırıp dosyalara tam yetki verin
7) "cp telnet.service /etc/systemd/system/" ile service dosyasını kopyalayın
8) "systemctl daemon-reload" komutu ile servis dosyalarını güncelleyelim
9) "systemctl start telnetserver.service" komutu ile telnet servisini başlatalım
10) "systemctl enable telnetserver.service" komutu ile telnet servisini aktif edelim
11) "systemctl status telnetserver.service" komutu ile telnet servisinin durumu kontrol edelim (Active Running gözükmeli)
12) Client tarafında (örn: Teraterm) ile Service: Other TCP Port 23 olacak şekilde cihaz ipsi üzerinden bağlantı kurun


Uygulamayı sonlandırmak için
1) "sudo su" komutuyla root yetkisinde terminal açın 
2) "systemctl stop telnetserver.service" komutuyla oluşturduğumuz telnet servisini durdurun
3) "systemctl disable telnetserver.service" komutu ile telnet servisini pasif edelim
4) Uygulama bu yöntemle kapatıldığında port hemen kapanmayabilir , uygulamayı tekrar açmak istediğinizde port kullanımda hatası alabilirsiniz , bir süre bekleyip tekrar uygulamayı başlatabilirsiniz

Not: python 3.5 üzeri kullanılmalıdır
