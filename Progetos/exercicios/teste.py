soma=0
for i in range (1,5):
    print ('Digite o peso do paciente', i )  
    peso= float (input())
    print ('Digite a altura do paciente', i )  
    altura= float (input())
    imc = peso/(altura*altura) 
    print ("O IMC do paciente é:",imc) 