import os 

caminho = os.path.dirname(os.path.abspath(__file__))

for file in os.listdir(caminho):

    if not file.endswith(".py"):

        caminhoAnt = os.path.join(caminho, file)
        pureName, extension = os.path.splitext(file)

        nameUpper = pureName.upper()
        newName = f"{nameUpper}{extension}"
        caminhoNovo = os.path.join(caminho, newName)
        os.rename(caminhoAnt, caminhoNovo)

input("\nDa pra dale:" )
    
    
    
    
    