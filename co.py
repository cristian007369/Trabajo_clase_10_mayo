if i<16:
    print("Criterio ingreso en hospital, IMC="+str(i))
else:
    if i<=17:
        print("Infrapeso, IMC="+str(i))
    else:
        if i<=18:

            print("Bajo de peso, IMC="+str(i))

        else:
            if i<=25:
    
                print("Peso normal (Saludable), IMC="+str(i))
    
            else:
                if i<=30:
        
                    print("Sobrepeso (Obesidad grado I), IMC="+str(i))
        
                else:
                    if i<=35:
            
                        print("Obesidad crónica (Obesidad grado II), IMC="+str(i))
            
                    else:
                        if i<=40:
                
                            print("Obesida premórbida (Obesidad grado III), IMC="+str(i))
                
                        else:
                
                            print("Obesida mórbida (Obesida grado IV), IMC="+str(i))