from MyModule import * 
nimed=[]
paroolid=[]
while True:
    operatsioon=print("Registreerimine(R)\nAutoriseerimine(A)\nNime või parooli muutmine(M)\nUnustanud parooli taastamine(U)\nLõpetamine(L)")
    vastus=str(input()).capitalize()
    if vastus == "R":
        nimed, paroolid = registreerimine(nimed, paroolid)
        for i in range(len(nimed)):
            print(f"Kasutajanimi: {nimed[i]}, Parool: {paroolid[i]}")
        print("")
    elif vastus=="A":
        autoriseerimine("Kasutaja_Parool.txt")
    elif vastus=="M":
        muuda_parool(nimed,paroolid)
        print(nimed,paroolid)
    elif vastus=="U":
        unustatud_parool()
    elif vastus=="L":
        break
    else:
        print("Palun vali toiming siit nimekirjast")
