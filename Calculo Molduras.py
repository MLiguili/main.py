l = 30
a = 21
num_quadros = 188
barra = 270
l_barra = 2
desconto = (l_barra*2) + 1
if l > a:
    perna_gnd = l + desconto
    perna_peq = a + desconto
else:
    perna_gnd = a + desconto
    perna_peq = l + desconto

num_per_gnd = int(barra / perna_gnd)
sobra = barra - (num_per_gnd * perna_gnd)

if sobra >= (perna_peq - desconto):
    num_per_peq_sobra = int(sobra / (perna_peq - desconto))
    nova_sobra = sobra - (num_per_peq_sobra * (perna_peq - desconto))
    print(f"pra esse projeto, terá {num_per_gnd} perna(s) grandes e {num_per_peq_sobra} perna(s) pequena por barra e {nova_sobra} cm de sobra".upper())

else:
    print(f"pra esse projeto, terá {num_per_gnd} perna(s) grandes e {sobra} cm de sobra".upper())
