import os 
import tkinter as tk 

#Path to the folder where the files will be stored 
path = r"C:\Users\Recrutamento-05\Desktop\python"

window = tk.Tk()
window.geometry("300x200")


for file in os.listdir(path):

    #Choose the file format 
    if file.endswith('.pdf'): 	
        oldPath = os.path.join(path, file)
        pureName, extension = os.path.splitext(file)
	
        #Choose the conditions and increment for the repeated files 
        split = pureName.rsplit('(', 1)
        pureName = split[0].rstrip()
        try:
            num = int(split[1][:1]) + 1 
        except:
            num = 1
  
        newName = f"{pureName} ({num}){extension}"
        newPath = os.path.join(path, newName)  
        
        #Finally, try renaming and creating a window with a message for the each file
        try:
            os.rename(oldPath, newPath)
            tk.Label(window, text="Sucess").pack()
        except:
            tk.Label(window, text=f"erro").pack()

window.mainloop()

        
