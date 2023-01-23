l = 30
a = 21
num_quadros = 188
barra = 275
l_barra = 2
desconto = (l_barra*2) + 1
if l > a:
    perna_gnd = l + desconto
    perna_peq = a + desconto
else:
    perna_gnd = a + desconto
    perna_peq = l + desconto

num_per_gnd_por_barra = int(barra / perna_gnd)
sobra = barra - (num_per_gnd_por_barra * perna_gnd)

total_perna_gnd_por_porjeto = num_quadros * 2
total_perna_peq_por_porjeto = num_quadros * 2



if sobra >= (perna_peq - desconto):
    num_per_peq_sobra = int(sobra / (perna_peq - desconto))
    nova_sobra = sobra - (num_per_peq_sobra * (perna_peq - desconto))
    print(f"por barra terá {num_per_gnd_por_barra} perna(s) grandes e {num_per_peq_sobra} perna(s) pequena por barra e {nova_sobra} cm de sobra".upper())
    print(f" Total de pernas grandes: {total_perna_gnd_por_porjeto}".upper())
    print(f" Total de pernas pequenas: {total_perna_gnd_por_porjeto}".upper())

else:
    print(f"por barra terá {num_per_gnd_por_barra} perna(s) grandes e {sobra} cm de sobra".upper())
    print(f" Total de pernas grandes: {total_perna_gnd_por_porjeto}".upper())
    print(f" Total de pernas pequenas: {total_perna_gnd_por_porjeto}".upper())

#num_barras_para_per_gnd = total_perna_gnd_por_porjeto/num_per_gnd_por_barra
#num_barras_para_per_peq = total_perna_peq_por_porjeto/num_per_peq_sobra

#if num_quadros != 1:
    #print(f'precisa de {num_barras_para_per_gnd} barras para as pernas grandes'.upper())
    #print(f'precisa de {num_barras_para_per_peq} barras para as pernas pequenas'.upper())

