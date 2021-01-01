import requests 

print("""
           |  _|                                 
  __|  _ \ | | \ \  \   / _ \  _ \_  /  _ \  __| 
\__ \  __/ | __|\ \  \ /  __/  __/  /   __/ |    
____/\___|_|_|   \_/\_/ \___|\___|___|\___|_|    
                                                 
""")

while True:
    numara= input("Hedef Telefon Numarasını Giriniz (ülke kodu ile ama '+' sız):")
    mesaj = input('Mesajınızı Girin:')
    print(f'Alıcı:{numara}\nSenin Mesajın:{mesaj}')
    print("Devam etmek istiyorsan(1)\nlf bilgileri değiştirmek istiyorsan (2)")
    edit=int(input())
    if edit==1:
        resp=requests.post('https://textbelt.com/text',{'phone':numara,
                                                         'message':mesaj,
                                                         'key':'textbelt',
                                                         })

        response=resp.json()
        if response['success']==False:
        	print('ERROR : ',response['error'])
        elif response['success']==True:
            print('TAMAM, MESAJIN KODU:',response['textId'])
            break
        elif edit==2:
            continue
        else: 
            print("Yanlış Gomut!! \nGüvenliğin için mesaj bilgilerini kontrol ettiğinden emin ol")
            continue



