import os

from tkinter.filedialog import askdirectory

caminho = askdirectory(title="Selecione uma pasta")
lista_arquivos = os.listdir(caminho)


codigos = {
    
    "python":[".py"],
    "arduino":[".ino"],
    "javaScript":[".js"],
    "C":[".c"],
    "web":[".html",".css"],   
}

locais = {
    "imagens": [".png", ".jpg", ".ico"],
    "planilhas": [".xlsx",".xlsm",".ods"],
    "apresentações": [".pptx"],
    "textos": [".pdf",".txt",".docx"],
    "audio": [".mp3",".wav",".m4a"],  
    "dados":[".csv",".sql",".accdb","mdb"],
}
locais.update(codigos)

for arquivo in lista_arquivos:
        nome, extensao = os.path.splitext(f"{caminho}/{arquivo}")
        
        for pasta in locais:
            if extensao in locais[pasta]:
                try:
                    if extensao in codigos[pasta]:
                        if not os.path.exists(f"{caminho}/codigos/"):
                            os.mkdir(f"{caminho}/codigos")  
                            
                        if not os.path.exists(f"{caminho}/codigos/{pasta}"):
                            os.mkdir(f"{caminho}/codigos/{pasta}")
                            
                        os.rename(f"{caminho}/{arquivo}",f"{caminho}/codigos/{pasta}/{arquivo}")
                        
                except KeyError:
                                                                                          
                        if not os.path.exists(f"{caminho}/{pasta}"):
                            os.mkdir(f"{caminho}/{pasta}")
                        
                        os.rename(f"{caminho}/{arquivo}",f"{caminho}/{pasta}/{arquivo}")
                        
for arquivo in lista_arquivos:
    if os.path.isfile(f"{caminho}/{arquivo}"):
        nome, extensao = os.path.splitext(f"{caminho}/{arquivo}")
        if not os.path.exists(f"{caminho}/outros/"):
            os.mkdir(f"{caminho}/outros")  
                    
        os.rename(f"{caminho}/{arquivo}",f"{caminho}/outros/{arquivo}")
        

print("arquivos organizados!!")


