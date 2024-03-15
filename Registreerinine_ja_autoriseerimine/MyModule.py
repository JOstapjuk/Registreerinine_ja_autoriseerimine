import random

def kirjuta_failisse(fail:str, järjend=[], järjend2=[]):
    """ Funktsion ümber kirjutab andmed failisse
    :param str fail: Faili nimi
    :param list järjend: esimene järjend
    :param list järjend2: teine järjend
    :rtype: any
    """
    existing_data = []
    try:
        with open(fail, 'r', encoding="utf-8") as v:
            for line in v:
                existing_data.append(line.strip())
    except FileNotFoundError:
        pass

    with open(fail, 'a', encoding="utf-8") as f:
        for i in range(len(järjend)):
            nimi = str(järjend[i])
            parool = str(järjend2[i])
            entry = nimi + ": " + parool + "\n"
            if not any(nimi in line for line in existing_data):
                f.write(entry)
    return järjend

# def kirjuta_failisse(fail:str,järjend=[],järjend2=[]):
#     """ Funktsion ümber kirjutab andmed failisse
#     :param str fail: Faili nimi
#     :param list järjend: esimene järjend
#     :param list järjend2: teine järjend
#     :rtype: any
#     """                                                      с этим кодом он записывал первого пользователя 2 раза при попытке записать второго пользователя
#     f=open(fail,'a',encoding="utf-8")
#     for i in range(len(järjend)):
#         nimi=str(järjend[i])
#         parool=str(järjend2[i])
#         f.write(nimi + ": " + parool + "\n")
#     f.close()
#     return järjend

def loe_pas_ja_log(fail:str)->any:
    """ Loeb failist andmed, mis oli sisestatud formaadis "nimi:parool" igas reas eraldi
    :param str fail: Faili nimi
    :rtype: any
    """
    log = []
    pas = []
    with open(fail, "r", encoding="utf-8") as f:  #https://www.freecodecamp.org/news/with-open-in-python-with-statement-syntax-example/ - обьяснение функции with open ... as ...
        for line in f:
            n = line.find(":")
            log.append(line[0:n].strip())
            pas.append(line[n+1:].strip())
    return log, pas

    # f=open(fail,"r",encoding="utf-8")
    # log=[]
    # pas=[]
    # for line in f:
    #     n=line.find(":")
    #     log.append(line[0:n].strip())                           у меня не получилось сделать с этим кодом, писало что файл закрывается слишком рано
    #     pas.append(line[n+1:len(line)].strip())
    #     f.close
    #     return log,pas

def registreerimine(n: list, p: list) -> any:
    """ 
    Funktsioon lisab uue kasutaja
    :param list n: Nimede nimekiri
    :param list p: Paroolide nimekiri
    :rtype: any
    """
    while True:
        result = loe_pas_ja_log("Kasutaja_Parool.txt")
        if result is None:
            log, pas = [], []
        else:
            log, pas = result
        nimi = input("Nimi: ")
        if nimi == "":
            print("Nimi ei saa olla tühi.")
            print("")
        elif nimi in log:
            print("See nimi on juba registreeritud.")
            print("")
        else:
            break 

    while True:
        valik = input("Kas soovite sisestada oma parooli või genereerida ühe? (Sisesta/Gener): ").capitalize()
        if valik == "Sisesta":
            parool = input("Parool: ")
        elif valik == "Gener":
            str0 = ".,:;!_*-+()/#¤%&"
            str1 = '0123456789'
            str2 = 'qwertyuiopasdfghjklzxcvbnm'
            str3 = str2.upper()
            str4 = str0 + str1 + str2 + str3
            ls = list(str4)
            random.shuffle(ls)
            parool = ''.join([random.choice(ls) for x in range(12)])
        else:
            print("Palun vali 'sisesta' või 'gener'")
            print("")
            continue
        
        if parool == "":
            print("Parool ei saa olla tühi.")
            print("")
        else:
            print("Te olete edukalt registreerunud")
            n.append(nimi)
            p.append(parool)
            kirjuta_failisse("Kasutaja_Parool.txt", n, p)
            return n, p
    
def autoriseerimine(fail: str) -> bool:
    """
    Autoriseerib kasutaja süsteemis.

    :param str fail: Faili nimi kasutajate ja paroolidega
    :rtype: bool
    """
    log, pas = loe_pas_ja_log(fail)
    print("Leitud kasutajad:", log)

    while True:
        nimi = input("Sisesta kasutajanimi: ").strip()
        parool = input("Sisesta parool: ")

        if nimi in log:
            if parool == pas[log.index(nimi)]:
                print("Autoriseerimine õnnestus!")
                print("")
                return True
            else:
                print("Vigane parool!")
                print("")
        else:
            print("Sellist kasutajanime ei eksisteeri!")
            print("")
        
def muuda_parool(n: list, p: list) -> None:
    """
    Muudab kasutaja parooli või nime.

    :param list n: Nimi järjend
    :param list p: Parool järjend
    """
    log, pas = loe_pas_ja_log("Kasutaja_Parool.txt")

    while True:
        nimi = input("Sisesta oma kasutajanimi: ")
        if nimi not in log:
            print("Sellist kasutajanime ei ole.")
            print("")
            continue
        else:
            index = log.index(nimi)
            break

    while True:
        muutmine = input("Kas soovid muuta nime (N) või parooli (P)?: ").capitalize()
        if muutmine == "N":
            uus_nimi = input("Sisesta uus nimi: ")
            if uus_nimi == "":
                print("Nimi ei saa olla tühi.")
                print("")
                continue
            elif uus_nimi in log:
                print("See nimi on juba kasutusel.")
                print("")
                continue
            else:
                n.pop(index)
                p.pop(index)
                n.append(uus_nimi)
                p.append(pas[index])
                print("Nimi edukalt muudetud.")
                print("")
                break
        elif muutmine == "P":
            uus_parool = input("Sisesta uus parool: ")
            if uus_parool == "":
                print("Parool ei saa olla tühi.")
                print("")
                continue
            else:
                p.pop(index)
                p.append(uus_parool)
                print("Parool edukalt muudetud.")
                print("")
                break
        else:
            print("Vigane valik. Palun vali 'N' või 'P'.")
            print("")
        kirjuta_failisse("Kasutaja_Parool.txt", n, p)
            
#fdgc ebmv xelp cunt 
            
import smtplib
import ssl
from email.message import EmailMessage

def unustatud_parool() -> None:
    """
    Saadab unustatud parooli kasutaja e-postile.
    """
    log, pas = loe_pas_ja_log("Kasutaja_Parool.txt")

    while True:
        nimi = input("Sisesta oma kasutajanimi: ").capitalize()
        if nimi not in log:
            print("Sellist kasutajanime ei ole.")
            print("")
            continue
        else:
            index = log.index(nimi)
            break

    email = input("Sisesta oma e-posti aadress: ")
    if email == "":
        print("E-posti aadress ei saa olla tühi.")
        return

    port = 587
    smtp_server = "smtp.gmail.com"
    sender_email = "jelizaveta.ostapjuk.work@gmail.com"
    password = "fdgc ebmv xelp cunt"
    context = ssl.create_default_context()
    msg = EmailMessage()
    msg.set_content(f"Teie parool on: {pas[index]}")
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
        print("E-kiri parooliga saadetud.")
    except:
        print("Viga")