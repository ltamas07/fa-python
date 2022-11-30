import random

fafile = open('fa.txt','w')

fa = []

for i in range(31):
    fa.append(random.randint(50,100))


maxFa = 0
minFa = 0
for szam in fa:
    if szam > maxFa:
        maxFa = szam
    if szam < minFa:
        minFa = szam

print(f'Ennyi volt a legkisebb fakitermelés: {minFa}')
print(f'Ennyi volt a legnagyobb fakitermelés: {maxFa}')
fafile.write(f'Ennyi volt a legkisebb fakitermelés: {minFa}\n')
fafile.write(f'Ennyi volt a legnagyobb fakitermelés: {maxFa}\n')



alkalom = 0
if fa > 82:
    alkalom = alkalom + 1
print(f'Ennyiszer volt nagyobb 82m3-nál : {alkalom}')
fafile.write(f'Ennyiszer volt nagyobb 82 m3-nál: {alkalom}\n')

print(f'Ennyi volt a fakitermelés 20.-án: {fa[20]}')
fafile.write(f'Ennyi volt a fakitermelés 20. -án : {fa[20]}\n')


for szamok in fa:
    ossz = ossz + szamok
atlag = ossz / szamok
print(f'A hőmérséklet átlaga: {atlag:0.2f}')
fafile.write(f'A fakitermelés átlaga: {atlag:0.2f}\n')

fafile.close()