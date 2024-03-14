import random

def kirjuta_failisse(fail:str,järjend=[],järjend2=[]):
    """ Funktsion ümber kirjutab andmed failisse
    :param str fail: Faili nimi
    :param list järjend: esimene järjend
    :param list järjend2: teine järjend
    :rtype: any
    """
    f=open(fail,'w',encoding="utf-8")
    for i in range(len(järjend)):
        nimi=järjend[i]
        parool=järjend2[i]
        f.write(nimi+": "+parool+"\n")
    f.close
    return järjend

def loe_pas_ja_log(fail:str)->any:
    """ Loeb failist andmed, mis oli sisestatud formaadis "nimi:parool" igas reas eraldi
    :param str fail: Faili nimi
    :rtype: any
    """
    fail=open(fail,"r",encoding="utf-8")
    log=[]
    pas=[]
    for line in fail:
        n=line.find(":")
        log.append(line[0:n].strip())
        pas.append(line[n+1:len(line)].strip())
        fail.close
        return log,pas

def registreerimine(n:list,p:list)->any:
    """ 
    Funktsioon lisab uue kasutaja
    :param list n: Nimi järjend
    :param list p: Parool järjend
    :param list p: Salasõna järjend
    :rtype: any
    """
    while True:
        nimi=input("Nimi: ")
        if nimi=="":
            print("Nimi ei saa olla tühi.")
            print("")
        elif nimi in n:
            print("See nimi on juba registreeritud.")
            print("")
        else:
            break
    
    while True:
        valik=input("Kas soovite sisestada oma parooli või genereerida ühe? (Sisesta/Gener): ").capitalize()
        if valik=="Sisesta":
            parool=input("Parool: ")
        elif valik=="Gener":
            str0=".,:;!_*-+()/#¤%&"
            str1='0123456789'
            str2='qwertyuiopasdfghjklzxcvbnm'
            str3=str2.upper()
            str4=str0 + str1 + str2 + str3
            ls=list(str4)
            random.shuffle(ls)
            parool=''.join([random.choice(ls) for x in range(12)])
        else:
            print("Palun vali 'sisesta' või 'genereri'")
            print("")
            continue
        
        if parool=="":
            print("Parool ei saa olla tühi.")
            print("")
        else:
            print("Te olete edukalt registreerunud")
            kirjuta_failisse("Kasutaja_Parool.txt",nimi,parool)
            return nimi, parool

def autoriseerimine(n: list, p: list) -> bool:
    """
    Autoriseerib kasutaja süsteemi.

    :param list n: Nimi järjend
    :param list p: Parool järjend
    :rtype: bool
    """
    while True:
        nimi=input("Sisesta kasutajanimi: ").capitalize()
        parool=input("Sisesta parool: ")
        if nimi in n and parool==p[n.index(nimi)]:
            print("Autentimine õnnestus!")
            print("")
            return True
        else:
            print("Vigane kasutajanimi või parool!")
            print("")

def muuda_parool(n:list,p:list)->any:
    """
    Muudab kasutaja parooli.

    :param list n: Nimi järjend
    :param list n: Parool järjend
    :rtype: any
    """
    while True:
        nimi=input("Sisesta oma kasutajanimi: ").capitalize()
        if nimi not in n:
            print("Sellist kasutajanime ei ole.")
            print("")
            continue
        else:
            index=n.index(nimi)
            break

    while True:
        muutmine=input("Kas soovid muuta nime (N) või parooli (P)?: ").capitalize()
        if muutmine=="N":
            uus_nimi=input("Sisesta uus nimi: ")
            if uus_nimi=="":
                print("Nimi ei saa olla tühi.")
                print("")
                continue
            elif uus_nimi in n:
                print("See nimi on juba kasutusel.")
                print("")
                continue
            else:
                n[index]=uus_nimi
                print("Nimi edukalt muudetud.")
                print("")
                break
        elif muutmine=="P":
            uus_parool=input("Sisesta uus parool: ")
            if uus_parool=="":
                print("Parool ei saa olla tühi.")
                print("")
                continue
            else:
                p[index]=uus_parool
                print("Parool edukalt muudetud.")
                print("")
                break
        else:
            print("Vigane valik. Palun vali 'N' või 'P'.")
            print("")  



#fdgc ebmv xelp cunt 

import smtplib
import ssl
from email.message import EmailMessage
def unustatud_parool(n: list, p: list) -> None:
    """
    Saadab unustatud parooli e-kirja kasutajale.

    :param list n: Nimi järjend
    :param list p: Parool järjend
    :param list s: Salasõna järjend
    """
    while True:
        nimi = input("Sisesta oma kasutajanimi: ").capitalize()
        if nimi not in n:
            print("Sellist kasutajanime ei ole.")
            print("")
            continue
        else:
            index = n.index(nimi)
            break

    email = input("Sisesta oma e-posti aadress: ")
    if email == "":
        print("E-posti aadress ei saa olla tühi.")
        return

    port = 587
    smtp_server = "smtp.gmail.com"
    sender_email = "jelizaveta.ostapjuk.work@gmail.com"
    password = input("Sisestage oma e-posti parool: ")
    context = ssl.create_default_context()
    msg = EmailMessage()
    msg.set_content(f"Teie parool on: {p[index]}")
    msg['Subject'] = "Unustatud parool"
    msg['From'] = "jelizaveta.ostapjuk.work@gmail.com"
    msg['To'] = email

    try:
        server = smtplib.SMTP(smtp_server, port)
        server.ehlo()
        server.starttls(context=context)
        server.ehlo()
        server.login(sender_email, password)
        server.send_message(msg)
    except:
       print("Viga")