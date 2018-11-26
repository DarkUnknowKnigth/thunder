import token as t
import table as tab
import syntaxis as s
class translator:
    INSTRUCTION=""
    tokenify=t.token()
    tablify=tab.table()
    syntaxify=s.syntaxis()
    stackify=tab.table()
    IS_INTERPRETING=True
    def start(self):
        print(
            "    ___(                     )\n"+
            "   (      THUNDER-flask      _)\n"+
            "  (_                       __)\n"+
            "    ((                _____)\n"+
            "      (_________)----'\n"+
            "         _/  /\n"+
            "        /  _/\n"+
            "      _/  /\n"+
            "     / __/\n"+
            "   _/ /\n"+
            "  /__/\n"+
            " //\n"+
            "/'\n")
    def listen(self):
        while self.IS_INTERPRETING:
            self.INSTRUCTION=raw_input('thunder>')
            self.INSTRUCTION=self.INSTRUCTION.strip()
            # Sacar los tokens
            tokens=self.tokenify.tokenize(self.INSTRUCTION)
            # Agregar tokens a la tabla
            ok=True #variable validadora de errores
            for token in tokens:
                if(token[1]=="error"):
                    print("(X_X)Invalid Token: "+token[2]+" in index "+str(token[0]))
                    ok=False #informar de error
                else:
                    self.tablify.add(token)
            #no hay error continuar a syntaxis
            if ok:
                #sacar el top de instrucciones
                tab=self.tablify.top()
                #verificar validez sintactica del comando
                if self.syntaxify.syntaxize(tab) != None:
                    self.stackify.data=self.syntaxify.syntaxize(tab)
                    #analizar por clave la semantica
                    print(self.stackify.data)
                else:
                    print("(X_X) invalid comand: "+' '.join(str(x[2]) for x in tab )+'\n(X_X) unknown syntaxis: '+' '.join(str(x[1]) for x in tab ))
            

                    




c=translator()
c.start()
c.listen()