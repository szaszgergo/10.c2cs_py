class Magassag:
    def __init__(self, egysor):
        darabok=egysor.strip('\n').split('\t')
        self.orszag = darabok[0]
        self.foldrajzi_hely = darabok[1]
        self.magassag = int(darabok[2])


f = open("tengerszint.txt","r")
beolvas = f.readlines()
f.close()
adatok = []
for item in beolvas:
   


