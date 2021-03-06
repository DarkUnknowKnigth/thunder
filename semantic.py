
import os
import shutil as sh
import subprocess
import json
import time
from colorama import init, Fore, Back, Style
init(autoreset=True)
 
class semantic:
    def semanticize(self,stack):
        if stack[0]=='kgnp':
            if os.path.isdir(stack[1][3][2]):
                os.chdir(stack[1][3][2])
                if not os.path.isdir(stack[1][3][2]+"/"+stack[1][2][2]):
                    os.mkdir(stack[1][2][2])
                    return [True,Fore.CYAN+"Creating project in: "+stack[1][3][2]]
                else:
                    return [True,Fore.RED+"This project already exist: "+stack[1][3][2]] 
        elif stack[0]=='kc':
            if stack[1][1][2]=="exit" or stack[1][1][2]=="e":
                return [False,"Exit..."]
            if stack[1][1][2]=="init" or stack[1][1][2]=="i":
                _name=raw_input("Please enter your project name: ")
                directory = os.getcwd() +"\\"+ _name


                if os.path.isfile(os.getcwd()+"/"+_name+"/light.json"):
                    current=os.getcwd()
                    os.chdir(os.getcwd()+"\\"+_name)
                    config = open("light.json")
                    _json=json.loads( str(config.read()))
                    #route
                    f=open("route.py","w+")
                    h=open("__init__.py","w+")
                    h.close()
                    g=open(current+'/temp/route.py')
                    def_rot=g.read()
                    g.close()
                    f.write(def_rot)
                    f.close()
                    #TEMPLATEs
                    try:               
                        dirToStatic = current + "\\temp\\static"
                        dirToCopy = current + "\\temp\\templates"         
                        sh.copytree(dirToStatic, directory + "\\static")
                        sh.copytree(dirToCopy, directory + "\\templates")
                        _current=os.getcwd()
                        os.chdir(os.getcwd()+"\\templates")
                        f=open("view.html","w+")
                        g=open(current+'/temp/view.html')
                        def_rot=g.read()
                        g.close()
                        f.write(def_rot)
                        f.close()
                        os.chdir(_current)
                    except:
                        print current
                        print directory  
                        #os.system("xcopy "+ current +"\\temp\\templates " + directory + "\\templates")
                        print("Your template had already initializate")
                        _current=os.getcwd()
                        os.chdir(os.getcwd()+"\\templates")
                        f=open("view.html","w+")
                        g=open(current+'/temp/view.html')
                        def_rot=g.read()
                        g.close()
                        f.write(def_rot)
                        f.close()
                        os.chdir(_current)
                    #CONTROLLER
                    f=open("controller.py","w+")
                    g=open(current+'/temp/controller.py')
                    def_rot=g.read()
                    g.close()
                    f.write(def_rot)
                    f.close()
                   
                    #MODEL  
                    f=open("model.py","w+")
                    g=open(current+'/temp/model.py')
                    def_rot=g.read()
                    g.close()
                    f.write(def_rot)
                    f.close()
                    
                    #INDEX
                    f = open("index.py","w+")
                    g = open (current+'/temp/index.py','r')
                    default_index = g.read()
                    g.close()
                    f.write(default_index)
                    f.close()
                    os.chdir(current)
                    return [True,Fore.YELLOW+"Initializing..."]
                else:
                    os.system("dir")
                    return [True,Fore.RED+"Can not find your config file"]
        elif stack[0]=='kgn':
            if not os.path.isdir(stack[1][2][2]):
                os.mkdir(stack[1][2][2])
                current=os.getcwd()
                os.chdir(current+"/"+stack[1][2][2])
                f= open("light.json","w+")
                config='{ "project":"'+stack[1][2][2]+'",\n"path":"'+str(os.getcwd()).replace("\\","\\\\")+'",\n"start":"index.py",\n"version":"1.0.0"\n }'
                f.write(str(config))
                f.close()
                g=open(".env","w+")
                var="PORT=5000\nHOST=127.0.0.1\n"
                g.write(str(var))
                g.close()
                os.chdir(current)
                return [True,Fore.GREEN+"(+_+) Creating project in current directory"]
            else:
                return [True,Fore.YELLOW+"(X_X) This project already exist: "+stack[1][2][2]]
        elif stack[0]=='kp':
            if stack[1][1][2]=="--version":
                #print subprocess.Popen("Flask --version", shell=False, stdout=subprocess.PIPE).stdout.read()
                print( Back.BLUE +  Fore.BLACK +"Flask 1.0")
                #print("Thunder 0.0.1")
                return [True, Fore.YELLOW + "Thunder 1.0.1"]
            elif stack[1][1][2]=="--v":
                print( Back.BLUE +  Fore.BLACK +"Flask 1.0")
                #print("Thunder 0.0.1")
                return [True, Fore.YELLOW + "Thunder 1.0.1"]
            elif stack[1][1][2]=="--help":
                print("INSTRUCTIONS...")
                helper = os.getcwd() + "\\temp\\help\\instruccion.md"
                file = open(helper, "r")
                for line in file:
                    print Fore.BLUE + line
                return [True,"..."]
            elif stack[1][1][2]=="--h":
                print("INSTRUCTIONS...")
                helper = os.getcwd() + "\\temp\\help\\instruccion.md"
                file = open(helper, "r")
                for line in file:
                    print Fore.BLUE + line
                return [True,"..."]
            else:
                return [True, Fore.RED + "Unknow parameter"]
        elif stack[0]=='kdp':
            if stack[1][2][2]=="--help" or stack[1][2][2]=="--h":
                    if(stack[1][1][2] == "add"):
                        print("INSTRUCTIONS...")
                        helper = os.getcwd() + "\\temp\\help\\add.md"
                        file = open(helper, "r")
                        for line in file:
                            print Fore.BLUE + line
                        return [True,"..."]
                    elif(stack[1][1][2] == "make"):
                        print("INSTRUCTIONS...")
                        helper = os.getcwd() + "\\temp\\help\\make.md"
                        file = open(helper, "r")
                        for line in file:
                            print Fore.BLUE + line
                        return [True,"."]
                    elif(stack[1][1][2] == "delete"):
                        print("INSTRUCTIONS...")
                        helper = os.getcwd() + "\\temp\\help\\delete.md"
                        file = open(helper, "r")
                        for line in file:
                            print Fore.BLUE + line
                        return [True,"..."]
            else:
                return [True,"Unknow parameter"]
        elif stack[0]=='kap':
            if  (stack[1][1][2]=="serve" or stack[1][1][2]=="s") and (stack[1][2][2]=="--browser" or stack[1][2][2]=="--b"):
                print("open app in browser")#Crear un archivo de configuracion
                _name=raw_input("Please enter your project name: ")
                if os.path.isfile(os.getcwd()+"/"+_name+"/light.json"):
                    current=os.getcwd()
                    os.chdir(os.getcwd()+"\\"+_name)
                    config = open("light.json")
                    _json=json.loads( str(config.read()))
                    os.system("START chrome.exe http://127.0.0.1:5000/")
                    os.system("index.py")                    
                    os.chdir(current)
                    return [True,Fore.BLACK+Back.YELLOW+"Server starter at: http://127.0.0.1:5000/"]
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
            if stack[1][1][2]=="serve" or stack[1][1][2]=="s":
                _name=raw_input("Please enter your project name: ")
                if os.path.isfile(os.getcwd()+"/"+_name+"/light.json"):
                    current=os.getcwd()
                    os.chdir(os.getcwd()+"\\"+_name)
                    config = open("light.json")
                    _json=json.loads( str(config.read()))
                    os.system("index.py")                    
                    os.chdir(current)
                    return [True,Fore.BLACK+Back.YELLOW+"Server starter at: http://127.0.0.1:5000/"]
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
        elif stack[0]=="kdcn":
            if stack[1][1][2]=="add" or stack[1][1][2]=="a":
                xname = raw_input("please enter your project name: ")
                current = os.getcwd()
                path = current +"\\"+ xname
                name = stack[1][3][2]
                component = stack[1][2][2] #name of component 
                if(component == "route" or component == "ro"):                
                    if os.path.isdir(path) and os.path.isfile(path+"\\route.py"):
                        #xd
                        newRoute = open(path + "\\route.py", "a")
                        addLines = ["\n\n@app.route( '/" + name + "', methods=['GET'] )", "\ndef " + name +"():", "\n\treturn render_template('" + name +"')" ]
                        newRoute.writelines(addLines)
                        newRoute.close() 
                        
                        return [True,  Fore.GREEN + Style.DIM + "*** new "+ component + " - " + name + " is added"]
                    else:
                        
                        return [True, Fore.RED +"(x_X) your project with the name: " + Back.YELLOW + xname  + Back.RESET + Fore.RED + " doest'n exist"]
                elif(component == "model" or component == "md"):
                    if os.path.isdir(path) and os.path.isfile(path+"\\model.py"):
                        newModel = open(path + "\\model.py", "a")
                        addLines = ["\n\nclass "+ name + ":", "\n\tname ='yourname' "]
                        newModel.writelines(addLines)
                        newModel.close()
                        return [True, "*** new "+ component + " - " + name + " is added"]
                    else:
                        return [True, Fore.RED +"(x_X) your project with the name: " + Back.YELLOW + xname  + Back.RESET + Fore.RED + " doest'n exist"]
                elif(component == 'controller' or component=='cn'):
                    if os.path.isdir(path) and os.path.isfile(path+"\\controller.py"):
                        newController = open(path + "\\controller.py", "a")
                        addLines = ["\n\tdef "+ name + "():", "\n\t\treturn 'data'"]
                        newController.writelines(addLines)
                        newController.close()
                        return [True, "*** new "+ component + " - " + name + " is added"]
                    else:
                        return [True, Fore.RED +"(x_X) your project with the name: " + Back.YELLOW + xname  + Back.RESET + Fore.RED + " doest'n exist"]
                elif(component == 'view' or component=='vw'):
                    #if os.path.isdir(path):
                        #newVW = open(path+"\\templates\\" + name +".html", "w")
                        #addLines = ["{% extends 'base.html'%}", "\n{% block text %}", "\n"+name, " is working \n{% endblock %}"]
                        #newVW.writelines(addLines)
                        #newVW.close()
                    return [True, Fore.LIGHTCYAN_EX + "(o.0) you can't add views, just make views"]
                    #else:
                    #    return [True, Fore.RED +"(x_X) your project with the name: " + Back.YELLOW + xname  + Back.RESET + Fore.RED + " doest'n exist"]
                return [True,"."]

            elif stack[1][1][2]=="make" or stack[1][1][2]=="m":
                xname = raw_input("please enter your project name: ")
                current = os.getcwd()
                path = current +"\\"+ xname
                component = stack[1][2][2]
                directive = stack[1][1][2]
                name  = stack[1][3][2]
                if component=='route' or component=='ro':
                    #if os.path.isdir(path) and os.path.isfile(path+"\\route.py"):
                        #newRoute = open(path + "\\"+ name +".route.py", "w")
                        #addLines = ["\n\n@app.route( '/" + name + "', methods=['GET'] )", "\ndef " + name +"():", "\n\treturn '" + name +"'" ]
                        #newRoute.writelines(addLines)
                        #newRoute.close() 
                        #print "we're inside the route bro"
                    return [True, Fore.RED + "(x_X) This fuction can't do it with Thunder. "]
                elif component=='view' or component=='vw':

                    if os.path.isdir(path):
                        newVW = open(path+"\\templates\\" + name +".html", "w")
                        addLines = ["{% extends 'base.html'%}", "\n{% block text %}", "\n"+name, " is working \n{% endblock %}"]
                        newVW.writelines(addLines)
                        newVW.close()
                        return [True, "new view - " + name + " is maked"]
                    else:
                        return [True, Fore.RED +"(x_X) your project with the name: " + Back.YELLOW + xname  + Back.RESET + Fore.RED + " doest'n exist"]
                elif component=='controller' or component=='cn':
                    if os.path.isdir(path):
                        newController = open(path + "\\controller_" + name, "w")
                        addLines = ["class controller_" + name, "\n\tdef get():", "\n\treturn 'data'"]
                        newController.writelines(addLines)
                        newController.close()
                        return [True, "new controller - " + name + " is maked"]
                    else:
                        return [True, Fore.RED +"(x_X) your project with the name: " + Back.YELLOW + xname  + Back.RESET + Fore.RED + " doest'n exist"]
                elif component=='model' or component=='md':
                    if os.path.isdir(path):
                        newModel = open(path + "\\model_" + name + ".py", "w")
                        addLines = ["class " + name, "\n\tid=0", "\n\tname=''"]
                        newModel.writelines(addLines)
                        newModel.close()
                        return [True, "new model - " + name + " is maked"]
                    else:
                        return [True, Fore.RED +"(x_X) your project with the name: " + Back.YELLOW + xname  + Back.RESET + Fore.RED + " doest'n exist"]
                elif component=='all':
                    if os.path.isdir(path):
                        newVW = open(path+"\\templates\\" + name +".html", "w")
                        newController = open(path + "\\controller_" + name+".py", "w")
                        newModel = open(path + "\\model_" + name + ".py", "w")
                        #newRoute = open(path + "\\route_" + name +".py", "w")
                        #addLines = ["\n\n@app.route( '/" + name + "', methods=['GET'] )", "\ndef " + name +"():", "\n\treturn render_template('" + name +".html" +"')" ]
                        #newRoute.writelines(addLines)
                        addLines = ["{% extends 'base.html'%}", "\n{% block text %}", "\n"+name, " is working \n{% endblock %}"]
                        newVW.writelines(addLines)
                        newVW.close()
                        addLines = ["class controller_" + name, "\n\tdef get():", "\n\treturn 'data'"]
                        newController.writelines(addLines)
                        newController.close()
                        addLines = ["class " + name, "\n\tid=0", "\n\tname=''"]
                        newModel.writelines(addLines)
                        newModel.close()
                        return [True, "new " + name + " is added"]
                    else:
                        return [True, Fore.RED +"(x_X) your project with the name: " + Back.YELLOW + xname  + Back.RESET + Fore.RED + " doest'n exist"]

                return [True, "is running make"]

            elif stack[1][1][2]=="delete" or stack[1][1][2]=="d":
                xname = raw_input("please enter your project name: ")
                current = os.getcwd()
                path = current +"\\"+ xname
                directive = stack[1][2][2]
                name  = stack[1][3][2]
                filename = path +  "\\"+name
                print filename
                if(os.path.isdir(path)):
                    if(directive == "view" or directive == "vw"):
                        if(os.path.isfile(path+"\\templates\\"+name+".html")):
                            os.remove(path+"\\templates\\"+name+".html")
                            return [True, Fore.RED +  " [-] "+ Fore.RESET + Fore.GREEN + name +" was be removed"]
                        else:
                            return [True, Fore.RED + "(x.X) Your file " + name + " does't exist"]
                    elif(directive == "model" or directive == "ro"):
                            if(os.path.isfile(path+"\\"+name+".py")):
                                os.remove(path + "\\model_"+ "\\"+name+".py")
                                return [True, Fore.RED +  " [-] "+ Fore.RESET + Fore.GREEN + name +" was be removed"]
                            else:
                             return [True, Fore.RED + "(x.X) Your file " + name + " does't exist"]
                    elif(directive == "controller" or directive == "cn"):
                        if(os.path.isfile(path+"\\"+name+".py")):
                            os.remove(path + "\\controller_"+ "\\"+name+".py")
                            return [True, Fore.RED +  " [-] "+ Fore.RESET + Fore.GREEN + name +" was be removed"]
                        else:
                            return [True, Fore.RED + "(x.X) Your file " + name + " does't exist"]
                    elif(directive == "all"):
                        temp = path+"\\templates\\"+name+".html"
                        mod = path+"\\model_"+name+".py"
                        cont = path+"\\controller_"+name+".py"
                        print temp+"\n"+mod+"\n"+cont
                        
                        if(os.path.isfile(temp) and os.path.isfile(mod) and os.path.isfile(cont)):
                            os.remove(temp)
                            os.remove(mod)
                            os.remove(cont)
                            return [True, Fore.RED +  " [-] "+ Fore.RESET + Fore.GREEN + name +" was be removed"]
                        else:
                            return [True, Fore.RED + "(x.X) Your file " + name + " does't exist"]
                else:
                    return [True, Fore.RED + "(x.X) Your Dir " + name + " does't exist"]

        
            
            
                    




            