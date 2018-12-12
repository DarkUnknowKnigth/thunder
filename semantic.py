
import os
import shutil as sh
import subprocess
import json
import time
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
                    return [True,"Initializing..."]
                else:
                    os.system("dir")
                    return [True,"Can not find your config file"]
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
                _name=raw_input("Please enter your project name: ")
                if os.path.isfile(os.getcwd()+"/"+_name+"/light.json"):
                    current=os.getcwd()
                    os.chdir(os.getcwd()+"\\"+_name)
                    config = open("light.json")
                    _json=json.loads( str(config.read()))
                    os.system("START chrome.exe http://127.0.0.1:5000/")
                    os.system("index.py")                    
                    os.chdir(current)
                    return [True,"Server starter at: http://127.0.0.1:5000/"]
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
        elif stack[0]=="kdcn":
            if stack[1][1][2]=="add" or stack[1][1][2]=="a":
                xname = raw_input("please enter your project name: ")
                current = os.getcwd()
                path = current +"\\"+ xname
                name = stack[1][3][2]
                component = stack[1][2][2] #name of component 
                if(component == "route"):                
                    if os.path.isdir(path) and os.path.isfile(path+"\\route.py"):
                        #xd
                        newRoute = open(path + "\\route.py", "a")
                        addLines = ["\n\n@app.route( '/" + name + "', methods=['GET'] )", "\ndef " + name +"():", "\n\treturn '" + name +"'" ]
                        newRoute.writelines(addLines)
                        newRoute.close() 
                        print "we're inside the route bro"
                elif(component == "model"):
                    if os.path.isdir(path) and os.path.isfile(path+"\\model.py"):
                        newModel = open(path + "\\model.py", "a")
                        addLines = ["\n\nclass "+ name + ":", "\n\tname ='yourname' "]
                        newModel.writelines(addLines)
                        newModel.close()
                        print("new model was added")
                elif(component == 'controller' or component=='cn'):
                    if os.path.isdir(path) and os.path.isfile(path+"\\controller.py"):
                        newController = open(path + "\\controller.py", "a")
                        addLines = ["\n\tdef "+ name + "():", "\n\t\treturn 'data'"]
                        newController.writelines(addLines)
                        newController.close()
                        print("new controller was added")
                elif(component == 'view' or component=='vw'):
                    if os.path.isdir(path):
                        newVW = open(path+"\\templates\\" + name +".html", "w")
                        addLines = name
                        newVW.writelines(addLines)
                        newVW.close()
                        print("new view was added")
                return [True,"route is added..."]

            elif stack[1][1][2]=="make" or stack[1][1][2]=="m":
                None
            elif stack[1][1][2]=="delete" or stack[1][1][2]=="d":
                None
    def component(self,_component,_diective,_name):
        if stack[1][1][2]=="add" or stack[1][1][2]=="a":
        
            if _component=='route' or _component=='ro':
                None
            elif _component=='view' or _component=='vw':
                None
            elif _component=='controller' or _component=='cn':
                None
            elif _component=='model' or _component=='md':
                None
            elif _component=='all':
                None
                
        elif stack[1][1][2]=="make" or stack[1][1][2]=="m":
            if _component=='route' or _component=='ro':
                None
            elif _component=='view' or _component=='vw':
                None
            elif _component=='controller' or _component=='cn':
                None
            elif _component=='model' or _component=='md':
                None
            elif _component=='all':
                None
        
        elif stack[1][1][2]=="delete" or stack[1][1][2]=="d":
        
            if _component=='route' or _component=='ro':
                None
            elif _component=='view' or _component=='vw':
                None
            elif _component=='controller' or _component=='cn':
                None
            elif _component=='model' or _component=='md':
                None
            elif _component=='all':
                None
        else:
            None
        
            
            
                    




            