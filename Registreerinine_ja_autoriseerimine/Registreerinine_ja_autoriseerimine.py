from MyModule import * 
nimed=[]
paroolid=[]
while True:
    operatsioon=print("Registreerimine(R)\nAutoriseerimine(A)\nNime või parooli muutmine(M)\nUnustanud parooli taastamine(U)\nLõpetamine(L)")
    vastus=str(input()).capitalize()
    if vastus=="R":
        registreerimine(nimed,paroolid)
        print("")
    elif vastus=="A":
        autoriseerimine(nimed,paroolid)
    elif vastus=="M":
        muuda_parool(nimed,paroolid)
        print(nimed,paroolid)
    elif vastus=="U":
        unustatud_parool(nimed,paroolid)
    elif vastus=="L":
        break
    else:
        print("Palun vali toiming siit nimekirjast")
