a=int(input('введіть суму: '))
b=input('виберіть валюту(USD,EUR,PLN,TRY):')
if(b=="USD"):
    print(f"{a*44.86}")
elif(b=="EUR"):
    print(f"{a * 50.15}")
elif (b == "PLN"):
    print(f"{a * 11.48}")
elif (b == "TRY"):
    print(f"{a * 0.91}")



