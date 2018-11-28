import os
import subprocess
class semantic:
    def semanticize(self,stack):
        if stack[0]=='kgnp':
            if os.path.isdir(stack[1][3][2]):
                os.chdir(stack[1][3][2])
                if not os.path.isdir(stack[1][3][2]+"/"+stack[1][2][2]):
                    os.mkdir(stack[1][2][2])
                    return [True,"Creating project in: "+stack[1][3][2]]
                else:
                    return [True,"This project already exist: "+stack[1][3][2]]
        elif stack[0]=='kc':
            if stack[1][1][2]=="exit" or stack[1][1][2]=="e":
                return [False,"Exit..."]
        elif stack[0]=='kgn':
            if not os.path.isdir(stack[1][2][2]):
                os.mkdir(stack[1][2][2])
                current=os.getcwd()
                os.chdir(current+"/"+stack[1][2][2])
                f= open("light.json","w+")
                config='{ "project":"'+stack[1][2][2]+'",\n"path":"'+str(os.getcwd()).replace("\\","\\\\")+'",\n"start":"index.py",\n"version":"1.0.0"\n }'
                f.write(str(config))
                os.chdir(current)
                return [True,"Creating project in current directory"]
            else:
                return [True,"This project already exist: "+stack[1][2][2]]
        elif stack[0]=='kp':
            if stack[1][1][2]=="--version":
                #print subprocess.Popen("Flask --version", shell=False, stdout=subprocess.PIPE).stdout.read()
                print("Flask 1.0")
                print("Thunder 0.0.1")
                return [True,"x-x-x-x-x-x-x-x-x-x"]
            elif stack[1][1][2]=="--v":
                print("Flask 1.0")
                print("Thunder 0.0.1")
                return [True,"x-x-x-x-x-x-x-x-x-x"]
            elif stack[1][1][2]=="--help":
                print("INSTRUCTIONS...")
                return [True,"x-x-x-x-x-x-x-x-x-x"]
            elif stack[1][1][2]=="--h":
                print("INSTRUCTIONS...")
                return [True,"x-x-x-x-x-x-x-x-x-x"]
            else:
                return [True,"Unknow parameter"]
        elif stack[0]=='kdp':
            if stack[1][2][2]=="--help":
                print("INSTRUCTIONS...")
                return [True,"x-x-x-x-x-x-x-x-x-x"]
            elif stack[1][2][2]=="--h":
                print("INSTRUCTIONS...")
                return [True,"x-x-x-x-x-x-x-x-x-x"]
            else:
                return [True,"Unknow parameter"]
        elif stack[0]=='kap':
            if  (stack[1][1][2]=="serve" or stack[1][1][2]=="s") and (stack[1][2][2]=="--browser" or stack[1][2][2]=="--b"):
                print("open app in browser")#Crear un archivo de configuracion
                if os.path.isfile(os.getcwd()+"index.py"):
                    os.system("Python index.py")
                    os.system("START chrome.exe 127.0.0.0:4100")
                    return [True,"Server starter at: 127.0.0.0:4100"]
                else:
                    return [True,"The file index.py not exist"]              

            elif (stack[1][1][2]=="reset" or stack[1][1][2]=="rs") and (stack[1][2][2]=="--help" or stack[1][2][2]=="--h"):
                print("mostrar ayuda")
                return [True,"OPTIONS"]

            elif (stack[1][1][2]=="stop" or stack[1][1][2]=="st" ) and (stack[1][2][2]=="--help" or stack[1][2][2]=="--h"):
                print("mostrar ayuda")
                return [True,"OPTIONS"]
            else:
                return [True,"Unknow action parameter sintax"]

        elif stack[0]=="ka":
            if (stack[1][1][2]=="serve" or stack[1][1][2]=="s" ):
                if os.path.isfile(os.getcwd()+"index.py"):
                    os.system("Python index.py")
                    return [True,"Server starter at: 127.0.0.0:4100"]
                else:
                    return [True,"The file index.py not exist"]
            elif stack[1][1][2]=="reset" or stack[1][1][2]=="rs":
                print("buscar proceso, matar e iniciar de nuevo")
                return [True,"Resetting"]
            elif stack[1][1][2]=="stop" or stack[1][1][2]=="st":
                print("buscar proceso, matar")
                return [True,"Stopping"]
            else:
                return [True,"Unknow action sintaxis"]




            