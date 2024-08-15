# python-telnet-server
Python telnet server

Kurulum:
1) Dosyaları linux sisteme kopyalayın
2) Kopyalanan dizinde root yetkisinde terminal açın
3) "chmod 777 telnetStart.py && chmod 777 telnet.py" komutunu çalıştırıp dosyalara tam yetki verin
4) "python startTelnet.py&" komutuyla yazılımı arka planda çalıştırın
5) Client tarafında (örn: Teraterm) ile Service: Other TCP Port 23 olacak şekilde cihaz ipsi üzerinden bağlantı kurun
6) Teraterm Setup -> Terminal sekmesinden Local Echo kısmını aktif edin
7) Kurulum sonrasında sadece 4.adım kullanılarak daha sonraki kullanımlarda uygulama başlatılabilir

Uygulamayı sonlandırmak için
1) Root yetkisine sahip terminal de jobs yazın ve çalışan işleri listeleyin
2) Listeden "./telnetStart.py &" yazılımının id numarasını öğrenin (örn:1)
3) terminal ekranında "kill %1" şeklinde uygulamayı sonlandırın (1 yazan kısıma öğrendiğiniz id numarasını yazacaksınız)
4) Uygulama bu yöntemle kapatıldığında port hemen kapanmayabilir , uygulamayı tekrar açmak istediğinizde port kullanımda hatası alabilirsiniz , bir süre bekleyip tekrar uygulamayı başlatabilirsiniz

Not: python 3.5 üzeri kullanılması tavsiye edilir.
