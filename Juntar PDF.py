import os
from pypdf import PdfWriter
from time import sleep 

nameFinally = "Merged.pdf"
path = os.path.dirname(os.path.realpath(__file__))
merge = PdfWriter()
size = len([arq for arq in os.listdir(path) if arq.endswith(".pdf") and arq != nameFinally])

currentPdf = 0 

for pdf in os.listdir(path):
    if pdf.endswith(".pdf") and pdf != nameFinally:
        pathFull = os.path.join(path, pdf)
        merge.append(pathFull)
        currentPdf +=1 
        progress = (currentPdf * 100) // size
        print(f"Juntando {pdf}") 
        print("=" * progress, " " *(100-progress), "|")
        sleep(0.3)
        os.system("cls")
        nameFinally = "202" + path[-1] + ".pdf"
       

pathFinally = os.path.join(path, nameFinally)
merge.write(pathFinally)

merge.close()