from random import randint

score=0
while True:
  secenekler=["tas","kagıt","makas"]
  bilgisayar=secenekler[randint(0,2)] 
  kullanici=input("tas, kağıt, makas?")

  if kullanici==bilgisayar:
    print("Berabere, tekrar deneyin")
  elif kullanici==secenekler[0]:
    if bilgisayar==secenekler[1]:
        score=score-1 
        print("kaybettiniz",bilgisayar,kullanici)
    else:
        score=score+1 
        print("kazandınız",bilgisayar,kullanici)
  elif kullanici==secenekler[1]:
    if bilgisayar==secenekler[2]:
        score=score-1
        print("puan kaybettiniz",bilgisayar,kullanici)
    else:
        score=score+1
        print("+1 puan kazandınız",bilgisayar,kullanici)
  elif kullanici==secenekler[2]:
    if bilgisayar==secenekler[0]:
        score=score-1
        print("puan kaybettiniz",bilgisayar,kullanici)
    else:
        score=score+1
        print("+1 puan kazandınız",bilgisayar,kullanici)
  else:
     print("final puanınız:",score)
     break   
                                    