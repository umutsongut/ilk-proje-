import time
sinema = 15
tiyatro = 10

secim = input("Seçiminiz Tiyatro (0), Sinema(1)")
ogrenci = input("Ögrenciyim (0), Değilim(1)")


yiyecek ={

"Çikolata : 5 TL(0)",
"Mısır : 10 TL(1)"
}

icecek = {

"Kola : 10 TL(2)",
"Çay : 5 TL(3)"

}

if secim =="0":
    print("Seçiminiz Tiyatro")

    if ogrenci=="0":

                ortalama = int(input("Ortalamanız Nedir?: "))   
                if ortalama>80:
                    ortalama = 80
                print("Seçiminiz Tiyatro ve Öğrencisiniz, Ödeyeceğiniz Ücret" +" "+ str(tiyatro - tiyatro*ortalama/100)+ str("TL"))
        
                hizmet = input("Diğer Hizmetlerimize Göz Atmak İster Misiniz? : Evet(0), Hayır(1)")
            
                if hizmet=="0":
                    for i in yiyecek,icecek:
                        print(i) 
                        
                    hizmetSec =input("Seçim Yapmak İster Misiniz?E(0),H(1)")
                elif hizmet =="1":
                    print("Seçim Yapmadınız,Çıkış Yapılıyor...")
                    time.sleep(2)

            
                if hizmetSec=="0":
                        print("Seçiminiz Nelerdir?: ")
                   
                
                elif hizmetSec=="1":
                    print("Seçim Yapmadınız...")
                    
                time.sleep(0.5)
                    
                                                                         
                enter=int(input("Hizmet Kodu Girin:"))
                if enter==0:
                        print("Siparişiniz Çikolata, Toplam Ödenecek Tutar:" + str(tiyatro +5))
                elif enter==1:
                        print("Siparişiniz Mısır, Toplam Ödenecek Tutar:" + str(tiyatro + 10))
                elif enter==2:
                            print("Siparişiniz Kola, Toplam Ödenecek Tutar:"  + str(tiyatro +10) ) 
                elif enter==3:
                            print("Siparişiniz Çay, Toplam Ödenecek Tutar: " + str(tiyatro + 5) ) 
                else:
                        print("Çıkış Yapılıyor...")
                time.sleep(2)
                                                        
        
    if ogrenci=="1":
                print("Seçiminiz Tiyatro ve Öğrenci Değilsiniz, Ödeyeceğiniz Ücret:", str(tiyatro) + "TL")
        
                hizmet = input("Diğer Hizmetlerimize Göz Atmak İster Misiniz? : Evet(0), Hayır(1)")
               
                if hizmet=="0":
                        for i in yiyecek,icecek:
                            print(i)

                elif hizmet=="1":
                    print("Seçim Yapmadınız...")
                    print("Çıkış Yapılıyor.")
                    exit
                    time.sleep(1.5)
                
                
                    
                hizmetSec =input("Seçim Yapmak İster Misiniz?E(0),H(1)")
                if hizmetSec=="0":
                    for i in yiyecek,icecek:
                        print(i)

                               
                        
                print("Seçiminiz Nelerdir? ")
                time.sleep(0.2)
                
                enter=int(input("Hizmet Kodu Girin"))

                if enter == 0:
                        print("Seçiminiz Çikolata,ödenecek toplam tutar: " + str(sinema+5))
                        time.sleep(2)
                        print("İşlem Yönlendiriliyor,İyi Seyirler Dileriz...")

                if enter == 1:
                    print("Seçiminiz Mısır,ödenecek toplam tutar: " + str(sinema+10))       
                    time.sleep(2)
                    print("İşlem Yönlendiriliyor,İyi Seyirler Dileriz...")

                if enter == 2:
                    print("Seçiminiz Kola,ödenecek toplam tutar: " + str(sinema+10))                    
                    time.sleep(2)
                    print("İşlem Yönlendiriliyor,İyi Seyirler Dileriz...")

                if enter == 3 :
                    print("Seçiminiz Çay,ödenecek toplam tutar: " + str(sinema+5))                       
                    time.sleep(2)
                    print("İşlem Yönlendiriliyor,İyi Seyirler Dileriz...")
                    

elif secim=="1":
    print("Seçiminiz Sinema")
    if  ogrenci=="0":
        ortalama = int(input("Ortalamanız Nedir?: "))
        if ortalama>=80:
            ortalama = 80
        print("Seçiminiz Sinema ve Öğrencisiniz "+ str(sinema - sinema*ortalama/100)+ " " + "TL")
        hizmet = input("Diğer Hizmetlerimize Göz Atmak İster Misiniz? Evet(0), Hayır(1)")
        if hizmet=="0":
            for i in yiyecek,icecek:
                print(i)
        elif hizmet=="1":
            print("Seçim Yapmadınız,İşlem Yönlendiriliyor,İyi Seyirler Dileriz...")

    
        
        hizmetSec =input("Seçim Yapmak İster Misiniz?E(0),H(1)")
        if hizmetSec=="0":
                print("Seçiminiz Nelerdir? ")
                    
                enter=int(input("Hizmet Kodu Girin"))
               
                if enter == 0:
                    print("Seçiminiz Çikolata,ödenecek toplam tutar: " + str(sinema+5))
                    time.sleep(2)
                    print("İşlem Yönlendiriliyor,İyi Seyirler Dileriz...")
                
                elif enter == 1:
                    print("Seçiminiz Mısır,ödenecek toplam tutar: " + str(sinema+10))       
                    time.sleep(2)
                    print("İşlem Yönlendiriliyor,İyi Seyirler Dileriz...")
                
                elif enter == 2:
                    print("Seçiminiz Kola,ödenecek toplam tutar: " + str(sinema+10))                    
                    time.sleep(2)
                    print("İşlem Yönlendiriliyor,İyi Seyirler Dileriz...")
                
                elif enter == 3 :
                        print("Seçiminiz Çay,ödenecek toplam tutar: " + str(sinema+5))                       
                        time.sleep(2)
                        print("İşlem Yönlendiriliyor,İyi Seyirler Dileriz...")
    
                elif ogrenci =="0":
                    print("Seçiminiz Sinema Öğrenci Değilsiniz " + str(sinema))            
            
        else:
            print("Seçim Yapılmadı,İşlem Yönlendiriliyor,İyi Seyirler Dileriz...")
            

    elif ogrenci =="1":
        print("Seçiminiz Sinema ve Öğrenci Değilsiniz, Ödeyeceğiniz Ücret " + str(sinema) )
        hizmet = input("Diğer Hizmetlerimize Göz Atmak İster Misiniz? Evet(0), Hayır(1)")
        if hizmet=="0":
            for i in yiyecek,icecek:
                print(i)
            hizmetSec =input("Seçim Yapmak İster Misiniz?E(0),H(1)")
            if hizmetSec=="0":
                enter=int(input("Hizmet Kodu Girin"))
                if enter == (0):
                    print("Seçiminiz Çikolata,ödenecek toplam tutar: " + str(sinema+5))
                    print("İşlem Yönlendiriliyor...")
                    time.sleep(0.5)
                elif enter == (1):
                    print("Seçiminiz Mısır,ödenecek toplam tutar: " + str(sinema+10))
                    print("İşlem Yönlendiriliyor...")
                    time.sleep(0.5)
                elif enter == (2):
                    print("Seçiminiz Kola,ödenecek toplam tutar: " + str(sinema+10))
                    print("İşlem Yönlendiriliyor...")
                    time.sleep(0.5)
                elif enter == (3):
                    print("Seçiminiz Çay,ödenecek toplam tutar: " + str(sinema+5))
                    print("İşlem Yönlendiriliyor...")
                    time.sleep(0.5)
            elif hizmetSec=="1":
                print("Seçim Yapılmadı")
else:
    print("Hatalı Tuşlama")