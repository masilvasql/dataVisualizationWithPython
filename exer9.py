entrada = open('18s_humano.fasta').read()   
saida = open("out.html","w")

cont2 = {}

for i in ['A','T','C','G']:
    for j in ['A' , 'T', 'C', 'G']:
        cont2[i+j] = 0

try:
    for k in range(len(entrada)):
        cont2[entrada[k]+entrada[k+1]] +=1
except:
    warning = 1

i = 1
for k in cont2:
    saida.write("<div style = 'width:65px; border:1px solid #111; color:red; height: 65px; float:left; background-color:rgba(0,0,0,"+str(cont2[k]/max(cont2.values()))+")'>"+k+"</div>\n")
    if i%4 == 0:
        saida.write("<div style = 'clear:both'></div>")
    i +=1
