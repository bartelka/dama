import PIL
from PIL import Image, ImageDraw

sachovnica= []
for i in range(8):
    riadok = []
    for j in range(8):
        riadok.append(0)
    sachovnica.append(riadok)

def check(x:int,y:int) -> bool:
    for j in range(8):
        for i in range(8):
            if i == x or j == y or i + j == x + y or i - j == x - y:
                if sachovnica[j][i] == 1:
                    return False
    return True

pocet = 0
def drticka(dama:int):
    global sachovnica, pocet
    if dama == 8 :
        print(sachovnica)
        pocet += 1
        sachovnice(sachovnica,pocet)
    for i in range(8):
        if check(i,dama):
            sachovnica[dama][i] = 1
            drticka(dama+1)
            sachovnica[dama][i] = 0

def sachovnice(sach:list,pocet:int):
    velkost = 8
    sirka = 50
    img = Image.new("RGB", (velkost * sirka, velkost * sirka), "black")
    pixels = img.load()
    draw = ImageDraw.Draw(img)
    nazov_suboru = "kombinacia"+str(pocet)+".png"
    farby = ["white","black"]
    for y in range(velkost):
        for x in range(velkost):
            farba = farby[(x+y)%2]
            draw.rectangle([(x*sirka,y*sirka),((x+1)*sirka,(y+1)*sirka)],fill=farba)
            if sach[y][x] == 1:
                draw.ellipse([(x*sirka,y*sirka),((x+1)*sirka,(y+1)*sirka)],fill="green")
    img.save(nazov_suboru)

drticka(0)
