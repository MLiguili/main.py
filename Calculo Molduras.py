l = 30
a = 21
num_quadros = 188
area_vidro = l * a
l_vidro = 240
a_vidro = 160
barra = 270
l_barra = 2
desconto = (l_barra*2) + 1
if l > a:
    perna_gnd = l
    perna_peq = a
else:
    perna_gnd = a
    perna_peq = l

quant_perna_gnd = (barra/ (perna_gnd + desconto)).__int__() * num_quadros
print(quant_perna_gnd)
