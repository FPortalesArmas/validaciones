from collections import Counter
# Para arreglo_1
# conf_arreglo_1 = {
#     'u1': 2,  # Nombre de Unidad / número trabajadores
#     'u2': 2,
#     'u3': 3,
#     'd': 2
# }

conf_arreglo_1 = {
    'u1': 3,  # Nombre de Unidad / número trabajadores
    # 'u2': 2,
    'd': 1
}


#Turnos
turnos = {'D', 'N'}

# Turno Total Unidad
# TU = {
#     'u1': [1, 1],  # dia / noche
#     'u2': [1, 1],
#     'u3': [1, 2]
# }
TU = {
    'u1': [2, 1]  # dia / noche
    # 'u2': [1, 1]
}

# Turno Total Genral
TG = [2, 1]  # dia/noche

MIN_APOYO = 15

# ###############################################################

def main():
    def pasar_matriz(rol_serv):
        arr = []
        for u in rol_serv:
            for lis in u.values():
                for lis_sub in lis:
                    arr.append(lis_sub)
        return arr


    # validaciones

    #  Validación por fila
    def validacion_turno_trabajador(rol_serv):
        rol_serv = pasar_matriz(rol_serv)
        tam_x = len(rol_serv)
        tam_y = len(rol_serv[0])
        for x in range(tam_x):
            lis = [v.strip(' ') for v in rol_serv[x]]
            if '-' in lis:
                continue
            else:
                if lis.count('N') > MIN_APOYO or lis.count('D') > MIN_APOYO:
                    my_turn = Counter(lis).most_common()[0][0]
                    for y in range(tam_y):
                        if rol_serv[x][y].strip(' ') == 'x':
                            continue
                        elif rol_serv[x][y].strip(' ') != my_turn:
                            print('Corregir3!!!!')
                else:
                    for y in range(tam_y):
                        if y == 0:
                            my_turn = rol_serv[x][y].strip(' ')
                            if my_turn == 'x':
                                my_turn = list(turnos - {rol_serv[x][y+1].strip(' ')})[0]
                        if rol_serv[x][y].strip(' ') == 'x':
                            my_turn = list(turnos - set(my_turn))[0]
                        elif rol_serv[x][y].strip(' ') != my_turn:
                            print('Corregir4!!!')
                            break


    def validacion_turno_unidad(rol_serv):
        # print(rol_serv)
        for u in rol_serv:
            i = 0
            nombre_uni = list(u.keys())[i]
            i += 1
            if nombre_uni != 'd':
                for lis in u.values():
                    tam_x = len(lis)
                    tam_y = len(lis[0])
                    for y in range(tam_y):
                        lis_temp = []
                        for x in range(tam_x):
                            lis_temp.append(lis[x][y].strip(' '))
                        # Verif
                        if 'x' in lis_temp:
                            continue
                        else:
                            cont_dia = lis_temp.count('D')
                            cont_noche = lis_temp.count('N')
                            if cont_dia != TU[nombre_uni][0] or cont_noche != TU[nombre_uni][1]:
                                print('Verificar!!')


    def validacion_total(rol_serv):
        rol_serv = pasar_matriz(rol_serv)
        tam_x = len(rol_serv)
        tam_y = len(rol_serv[0])
        for y in range(tam_y):
            lis_temp = []
            for x in range(tam_x):
                lis_temp.append(rol_serv[x][y].strip(' '))
            cont_dia = lis_temp.count('D')
            cont_noche = lis_temp.count('N')
            if cont_dia != TG[0] or cont_noche != TG[1]:
                print('Verificar!!2')


    # ###############################################################


    # arreglo_1 = [
    # [' S ', ' D ', ' L ', ' M ', ' M ', ' J ', ' V ', ' S ', ' D ', ' L ', ' M ', ' M ', ' J ', ' V ', ' S ', ' D ', ' L ', ' M ', ' M ', ' J ', ' V ', ' S ', ' D ', ' L ', ' M ', ' M ', ' J ', ' V ', ' S ', ' D ', ' L '],
    # [' 1 ', ' 2 ', ' 3 ', ' 4 ', ' 5 ', ' 6 ', ' 7 ', ' 8 ', ' 9 ', ' 10', ' 11', ' 12', ' 13', ' 14', ' 15', ' 16', ' 17', ' 18', ' 19', ' 20', ' 21', ' 22', ' 23', ' 24', ' 25', ' 26', ' 27', ' 28', ' 29', ' 30', ' 31 '],
    # [' N ', ' N ', ' N ', ' N ', ' N ', ' N ', ' x ', ' D ', ' D ', ' D ', ' D ', ' D ', ' D ', ' x ', ' N ', ' N ', ' N ', ' N ', ' N ', ' N ', ' x ', ' D ', ' D ', ' D ', ' D ', ' D ', ' D ', ' x ', ' N ', ' N ', ' N '],
    # [' x ', ' D ', ' D ', ' D ', ' D ', ' D ', ' D ', ' x ', ' N ', ' N ', ' N ', ' N ', ' N ', ' N ', ' x ', ' D ', ' D ', ' D ', ' D ', ' D ', ' D ', ' x ', ' N ', ' N ', ' N ', ' N ', ' N ', ' N ', ' x ', ' D ', ' D '],
    # [' D ', ' x ', ' N ', ' N ', ' N ', ' N ', ' N ', ' N ', ' x ', ' D ', ' D ', ' D ', ' D ', ' D ', ' D ', ' x ', ' N ', ' N ', ' N ', ' N ', ' N ', ' N ', ' x ', ' D ', ' D ', ' D ', ' D ', ' D ', ' D ', ' x ', ' N '],
    # [' N ', ' N ', ' x ', ' D ', ' D ', ' D ', ' D ', ' D ', ' D ', ' x ', ' N ', ' N ', ' N ', ' N ', ' N ', ' N ', ' x ', ' D ', ' D ', ' D ', ' D ', ' D ', ' D ', ' x ', ' N ', ' N ', ' N ', ' N ', ' N ', ' N ', ' x '],
    # [' N ', ' N ', ' N ', ' x ', ' N ', ' N ', ' N ', ' N ', ' N ', ' N ', ' x ', ' N ', ' N ', ' N ', ' N ', ' N ', ' N ', ' x ', ' N ', ' N ', ' N ', ' N ', ' N ', ' N ', ' x ', ' N ', ' N ', ' N ', ' N ', ' N ', ' N '],
    # [' D ', ' D ', ' D ', ' D ', ' D ', ' x ', ' N ', ' N ', ' N ', ' N ', ' N ', ' N ', ' x ', ' D ', ' D ', ' D ', ' D ', ' D ', ' D ', ' x ', ' N ', ' N ', ' N ', ' N ', ' N ', ' N ', ' x ', ' D ', ' D ', ' D ', ' D '],
    # [' N ', ' N ', ' N ', ' N ', ' x ', ' D ', ' D ', ' D ', ' D ', ' D ', ' D ', ' x ', ' N ', ' N ', ' N ', ' N ', ' N ', ' N ', ' x ', ' D ', ' D ', ' D ', ' D ', ' D ', ' D ', ' x ', ' N ', ' N ', ' N ', ' N ', ' N '],
    # [' D ', ' D ', ' D ', ' x ', ' N ', ' N ', ' N ', ' N ', ' N ', ' N ', ' x ', ' D ', ' D ', ' D ', ' D ', ' D ', ' D ', ' x ', ' N ', ' N ', ' N ', ' N ', ' N ', ' N ', ' x ', ' D ', ' D ', ' D ', ' D ', ' D ', ' D '],
    # [' - ', ' - ', ' - ', ' N ', ' - ', ' - ', ' - ', ' - ', ' - ', ' - ', ' N ', ' - ', ' - ', ' - ', ' - ', ' - ', ' - ', ' N ', ' - ', ' - ', ' - ', ' - ', ' - ', ' - ', ' N ', ' - ', ' - ', ' - ', ' - ', ' - ', ' - ']
    # ]

    # arreglo_1 = [
    #     [' S ', ' D ', ' L ', ' M ', ' M ', ' J ', ' V ', ' S ', ' D ', ' L ', ' M ', ' M ', ' J ', ' V ', ' S ', ' D ', ' L ', ' M ', ' M ', ' J ', ' V ', ' S ', ' D ', ' L ', ' M ', ' M ', ' J ', ' V ', ' S ', ' D ', ' L '],
    #     [' 1 ', ' 2 ', ' 3 ', ' 4 ', ' 5 ', ' 6 ', ' 7 ', ' 8 ', ' 9 ', ' 10', ' 11', ' 12', ' 13', ' 14', ' 15', ' 16', ' 17', ' 18', ' 19', ' 20', ' 21', ' 22', ' 23', ' 24', ' 25', ' 26', ' 27', ' 28', ' 29', ' 30', ' 31'],
    #     [' N ', ' N ', ' x ', ' D ', ' D ', ' D ', ' D ', ' D ', ' D ', ' x ', ' N ', ' N ', ' N ', ' N ', ' N ', ' N ', ' x ', ' D ', ' D ', ' D ', ' D ', ' D ', ' D ', ' x ', ' N ', ' N ', ' N ', ' N ', ' N ', ' N ', ' x '],
    #     [' D ', ' D ', ' D ', ' x ', ' N ', ' N ', ' N ', ' N ', ' N ', ' N ', ' x ', ' D ', ' D ', ' D ', ' D ', ' D ', ' D ', ' x ', ' N ', ' N ', ' N ', ' N ', ' N ', ' N ', ' x ', ' D ', ' D ', ' D ', ' D ', ' D ', ' D '],
    #     [' N ', ' N ', ' N ', ' N ', ' x ', ' D ', ' D ', ' D ', ' D ', ' D ', ' D ', ' x ', ' N ', ' N ', ' N ', ' N ', ' N ', ' N ', ' x ', ' D ', ' D ', ' D ', ' D ', ' D ', ' D ', ' x ', ' N ', ' N ', ' N ', ' N ', ' N '],
    #     [' D ', ' D ', ' D ', ' D ', ' D ', ' x ', ' N ', ' N ', ' N ', ' N ', ' N ', ' N ', ' x ', ' D ', ' D ', ' D ', ' D ', ' D ', ' D ', ' x ', ' N ', ' N ', ' N ', ' N ', ' N ', ' N ', ' x ', ' D ', ' D ', ' D ', ' D '],
    #     [' D ', ' x ', ' N ', ' N ', ' N ', ' N ', ' N ', ' N ', ' x ', ' D ', ' D ', ' D ', ' D ', ' D ', ' D ', ' x ', ' N ', ' N ', ' N ', ' N ', ' N ', ' N ', ' x ', ' D ', ' D ', ' D ', ' D ', ' D ', ' D ', ' x ', ' N '],
    #     [' x ', ' D ', ' D ', ' D ', ' D ', ' D ', ' D ', ' x ', ' N ', ' N ', ' N ', ' N ', ' N ', ' N ', ' x ', ' D ', ' D ', ' D ', ' D ', ' D ', ' D ', ' x ', ' N ', ' N ', ' N ', ' N ', ' N ', ' N ', ' x ', ' D ', ' D '],
    #     [' N ', ' N ', ' N ', ' N ', ' N ', ' N ', ' x ', ' D ', ' D ', ' D ', ' D ', ' D ', ' D ', ' x ', ' N ', ' N ', ' N ', ' N ', ' N ', ' N ', ' x ', ' D ', ' D ', ' D ', ' D ', ' D ', ' D ', ' x ', ' N ', ' N ', ' N '],
    # ]

    arreglo_1 = [
        [' S ', ' D ', ' L ', ' M ', ' M ', ' J ', ' V ', ' S ', ' D ', ' L ', ' M ', ' M ', ' J ', ' V ', ' S ', ' D ', ' L ', ' M ', ' M ', ' J ', ' V ', ' S ', ' D ', ' L ', ' M ', ' M ', ' J ', ' V ', ' S ', ' D ', ' L '],
        [' 1 ', ' 2 ', ' 3 ', ' 4 ', ' 5 ', ' 6 ', ' 7 ', ' 8 ', ' 9 ', ' 10', ' 11', ' 12', ' 13', ' 14', ' 15', ' 16', ' 17', ' 18', ' 19', ' 20', ' 21', ' 22', ' 23', ' 24', ' 25', ' 26', ' 27', ' 28', ' 29', ' 30', ' 31'],
        [' N ', ' N ', ' x ', ' D ', ' D ', ' D ', ' D ', ' D ', ' D ', ' x ', ' N ', ' N ', ' N ', ' N ', ' N ', ' N ', ' x ', ' D ', ' D ', ' D ', ' D ', ' D ', ' D ', ' x ', ' N ', ' N ', ' N ', ' N ', ' N ', ' N ', ' x '],
        [' D ', ' D ', ' D ', ' x ', ' N ', ' N ', ' N ', ' N ', ' N ', ' N ', ' x ', ' D ', ' D ', ' D ', ' D ', ' D ', ' D ', ' x ', ' N ', ' N ', ' N ', ' N ', ' N ', ' N ', ' x ', ' D ', ' D ', ' D ', ' D ', ' D ', ' D '],
        [' D ', ' D ', ' D ', ' D ', ' D ', ' x ', ' D ', ' D ', ' D ', ' D ', ' D ', ' D ', ' x ', ' D ', ' D ', ' D ', ' D ', ' D ', ' D ', ' x ', ' D ', ' D ', ' D ', ' D ', ' D ', ' D ', ' x ', ' D ', ' D ', ' D ', ' D '],
        [' - ', ' - ', ' N ', ' N ', ' - ', ' D ', ' - ', ' - ', ' - ', ' D ', ' D ', ' - ', ' D ', ' - ', ' - ', ' - ', ' N ', ' N ', ' - ', ' D ', ' - ', ' - ', ' - ', ' D ', ' D ', ' - ', ' D ', ' - ', ' - ', ' - ', ' N '],
    ]

    rol_serv = []
    tam = len(arreglo_1)
    i = 2
    a = 0

    for n in conf_arreglo_1.values():
        arr = arreglo_1[i:i+n]
        i += n
        unidad = {
            list(conf_arreglo_1.keys())[a]: arr
        }
        a += 1
        rol_serv.append(unidad)

    # for v in rol_serv:
    #     print(v)

    validacion_turno_unidad(rol_serv)
    validacion_total(rol_serv)
    validacion_turno_trabajador(rol_serv)


if __name__ == '__main__':
    main()
