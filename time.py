full_sec=86400
s=int(input('введіть секунди: '))
t=input('виберіть дію(sec,min,hr,): ')
if(t=="sec"):
    print(f"{full_sec-s}")
elif(t=="min"):
    print(f"{(full_sec-s)/60}")
elif (t== "hr"):
    print(f"{(full_sec-s)/3600}")
