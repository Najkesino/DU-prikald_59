import tkinter 
canvas = tkinter.Canvas (width=500, height=400, bg='white')
canvas.pack() #importujem kniznicu s platnom na kreslenie a dalsimi vlastnostami

zoznam = [None]
nastupujuci = [0]*8
vystupujuci = [0]*8
miesta = [None]*8 #vytvorim si 4 zoznamy do ktorych si ulozim informacie z textoveho suboru
i = 0 #pocitadlo 
x = 100 #suradnica x na vypisanie miest v plastne
y = 30 #suradnica y na vypisanie miest v plastne
x1 = 170 #suradnica x na vykreslenie obdlznikov v plastne
y1 = 15 #suradnica y na vykreslenie obdlznikov v plastne
farba = 'green' #premenna na vypln obdlznika
pocitadlo = 0 #premenna na vypocet aktualnych cestujucich
pocet = 0

subor = open('vytazenost_autobusovej_linky.D', 'r') #otvorim si subor
for riadok in subor: #for cyklus na citanie riadkov zo suboru
    riadok = riadok.strip() #odstranim z riadku neviditelne znaky
    riadok = riadok.split(' ') #riadok rozdelim po kazdej medzere
    zoznam = riadok #riadok ulozim do zoznamu
    zoznam.append(' ') #pridam do zoznamu nakoniec medzeru aby mi fungovala podmienka if kvôli miestam ktore su rozdelene na dve casti aby som ich spojil pomocou if-u
    if zoznam[3]!='': #podmienka if kde zistim ci je tam nieco
        zoznam[2] = zoznam[2]+' '+zoznam[3] #do zoznamu na tretie miesto ulozim informaciu z tretieho a stvrteho miesta dokopi lebo niektore nazvy miest su dvojmiestne tak ich ulozim ako jednu informaciu
        zoznam.pop(3) #ak mi na stvrtom mieste v zozname ostala medzera alebo prebytocna informacia odstranim ju
    nastupujuci[i] = zoznam[0] #do zoznamu nastupujuci pridam informaciu z pomocneho zoznamu
    vystupujuci[i] = zoznam[1] #do zoznamu vystupujuci pridam informaciu z pomocneho zoznamu
    miesta[i] = zoznam[2] #do zoznamu miesta pridam informaciu z pomocneho zoznamu
    i += 1 #pocitadlo zvysujem aby som ho mohol pouzit v zoznamoch
subor.close() #zatvorim citany subor

for neviem in range(i): #for cyklom vypisem vsetky miesta
        canvas.create_text(x, y, text=miesta[neviem], font='Arial 10 bold') #vypise nazov miesta zastavky
        y += 50 #zvacsi y suradnicu aby neboli vsetky miesta vykreslene na jednom mieste
        
def vypis(event): #definujem funkciu vypis na vykreslenie do grafickeho platna
    global y1, pocet, pocitadlo, farba #zaidentifikovanie premennych ako gglobalne aby som ich mohol upravovat
    canvas.create_rectangle(x1, y1, x1+200, y1+30) #vykresli vonkajsi prazdny obdlznik
    pocitadlo = pocitadlo+int(nastupujuci[pocet])-int(vystupujuci[pocet]) #v premennej pocitadlo pridavam hodnoty zo zoznamov nastupujuci a vystupujuci na zistenie aktualneho poctu cestujucich
    if pocitadlo>50: #podmienka if na zistenie ci je prekroceny poceet cestujucich, ak ano zmeni farbu vyplne na cervenu
        farba = 'red'
    elif pocitadlo<=50:
        farba = 'green'
    canvas.create_rectangle(x1, y1, x1+(pocitadlo*4), y1+30, fill=farba) #vykresli ako je autobus na tom s kapacitou
    y1 += 50 #zvacsi y1 suradnicu aby neboli vsetky obdlzniky vykreslene na jednom mieste
    pocet += 1 #zvacsi premennu pocet
    
canvas.bind_all('<Key>', vypis) #nabindujem si lubovolnu klavesu a po jej stlaceni mi zavola funkciu vypis
