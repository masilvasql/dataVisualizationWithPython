entrada = open('bacteria.fasta').read()
saida = open('bacteria.html','w')

cont = {}

for i in ['A','T','C','G']:
    for j in ['A' , 'T', 'C', 'G']:
        cont[i+j] = 0

entrada = entrada.replace('\n',"")

try:
    for k in range(len(entrada)):
        cont[entrada[k]+entrada[k+1]] +=1
except:
    warning = 1


i = 1
for k in cont:
    saida.write("<div style = 'width:65px; border:1px solid #111; color:red;height: 65px; float:left; background-color:rgba(0,0,0,"+str(cont[k]/max(cont.values()))+")'>"+k+"</div>\n")
    if i%4 == 0:
        saida.write("<div style = 'clear:both'></div>")
    i +=1