import os 

path = os.path.dirname(os.path.abspath(__file__))

for file in os.listdir(path):

    if not file.endswith(".py"):

        oldPath = os.path.join(path, file)
        pureName, extension = os.path.splitext(file)

        nameUpper = pureName.upper()
        newName = f"{nameUpper}{extension}"
        nePath = os.path.join(path, newName)
        os.rename(oldPath, newPath)

input("\nDa pra dale:" )
    
    
    
    
    
