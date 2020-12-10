from collections import Counter
import sys

TURNOS = {'D', 'N'}
TRABAJO_MIN_APOYO = 15

# CONFIGURACIONES
CONF_ARREGLO = {
    'U1': 2,  # Nombre de Unidad / número trabajadores
    'U2': 2,
    'U3': 3,
    'DE': 2
}

TURNOS_UNIDAD = {
    'U1': [1, 1],  # dia / noche
    'U2': [1, 1],
    'U3': [1, 2]
}

TURNO_GENERAL = [3, 4]  # dia / noche


class Verificar:

    arreglo_original = []
    rol_serv = []

    def __init__(self, arreglo):
        self.arreglo_original = arreglo[:2]
        self.rol_serv = self.separar_unidades(arreglo)

    def separar_unidades(self, arreglo):
        rol_serv = []
        i = 2
        a = 0
        for n in CONF_ARREGLO.values():
            arr = arreglo[i:i + n]
            i += n
            unidad = {
                list(CONF_ARREGLO.keys())[a]: arr
            }
            a += 1
            rol_serv.append(unidad)
        return rol_serv

    def pasar_matriz(self):
        arr = []
        for u in self.rol_serv:
            for lis in u.values():
                for lis_sub in lis:
                    arr.append(lis_sub)
        return arr

    def notificar_error(self, pos_x, pos_y):
        dia = self.arreglo_original[1][pos_y]
        pos_x = pos_x + 2
        inicio = 2
        fin = 2
        for k, v in CONF_ARREGLO.items():
            fin = fin + v
            if pos_x in range(inicio, fin):
                nombre_unidad = k
                break
            inicio = inicio + v
        print('Error_3! Verificar Turno en la Unidad: {} / Dia: {}'.format(
            nombre_unidad, dia))



    def validacion_turno_trabajador(self):
        rol_serv = self.pasar_matriz()
        tam_x = len(rol_serv)
        tam_y = len(rol_serv[0])
        for x in range(tam_x):
            lis = [v.strip(' ') for v in rol_serv[x]]
            if '-' in lis:
                continue
            else:
                if lis.count('N') > TRABAJO_MIN_APOYO or lis.count('D') > TRABAJO_MIN_APOYO:
                    my_turn = Counter(lis).most_common()[0][0]
                    for y in range(tam_y):
                        if rol_serv[x][y].strip(' ') == 'x':
                            continue
                        elif rol_serv[x][y].strip(' ') != my_turn:
                            self.notificar_error(x, y)
                            sys.exit()
                else:
                    for y in range(tam_y):
                        if y == 0:
                            my_turn = rol_serv[x][y].strip(' ')
                            if my_turn == 'x':
                                my_turn = list(TURNOS - {rol_serv[x][y + 1].strip(' ')})[0]
                        if rol_serv[x][y].strip(' ') == 'x':
                            my_turn = list(TURNOS - set(my_turn))[0]
                        elif rol_serv[x][y].strip(' ') != my_turn:
                            self.notificar_error(x, y)
                            sys.exit()
                            break

    def validacion_turno_unidad(self):
        for u in self.rol_serv:
            i = 0
            nombre_uni = list(u.keys())[i]
            i += 1
            if nombre_uni != 'DE':
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
                            if cont_dia != TURNOS_UNIDAD[nombre_uni][0] or cont_noche != TURNOS_UNIDAD[nombre_uni][1]:
                                print('Error_2! Verificar Turno en la Unidad: {} / Dia: {}'.format(
                                    nombre_uni, self.arreglo_original[1][y]))
                                sys.exit()

    def validacion_total(self):
        rol_serv = self.pasar_matriz()
        tam_x = len(rol_serv)
        tam_y = len(rol_serv[0])
        for y in range(tam_y):
            lis_temp = []
            for x in range(tam_x):
                lis_temp.append(rol_serv[x][y].strip(' '))
            cont_dia = lis_temp.count('D')
            cont_noche = lis_temp.count('N')
            if cont_dia != TURNO_GENERAL[0] or cont_noche != TURNO_GENERAL[1]:
                print('Error_1! En la suma Total de turnos en el día: {} \n\t\tNOTA: Debe ser {} Dias / {} Noches'.format(
                    self.arreglo_original[1][y], TURNO_GENERAL[0], TURNO_GENERAL[1]))
                sys.exit()


if __name__ == '__main__':

    arreglo_1 = [
        [' S ', ' D ', ' L ', ' M ', ' M ', ' J ', ' V ', ' S ', ' D ', ' L ', ' M ', ' M ', ' J ', ' V ', ' S ', ' D ', ' L ', ' M ', ' M ', ' J ', ' V ', ' S ', ' D ', ' L ', ' M ', ' M ', ' J ', ' V ', ' S ', ' D ', ' L '],
        [' 1 ', ' 2 ', ' 3 ', ' 4 ', ' 5 ', ' 6 ', ' 7 ', ' 8 ', ' 9 ', ' 10', ' 11', ' 12', ' 13', ' 14', ' 15', ' 16', ' 17', ' 18', ' 19', ' 20', ' 21', ' 22', ' 23', ' 24', ' 25', ' 26', ' 27', ' 28', ' 29', ' 30', ' 31 '],
        [' N ', ' N ', ' N ', ' N ', ' N ', ' N ', ' x ', ' D ', ' D ', ' D ', ' D ', ' D ', ' D ', ' x ', ' N ', ' N ', ' N ', ' N ', ' N ', ' N ', ' x ', ' D ', ' D ', ' D ', ' D ', ' D ', ' D ', ' x ', ' N ', ' N ', ' N '],
        [' x ', ' D ', ' D ', ' D ', ' D ', ' D ', ' D ', ' x ', ' N ', ' N ', ' N ', ' N ', ' N ', ' N ', ' x ', ' D ', ' D ', ' D ', ' D ', ' D ', ' D ', ' x ', ' N ', ' N ', ' N ', ' N ', ' N ', ' N ', ' x ', ' D ', ' D '],
        [' D ', ' x ', ' N ', ' N ', ' N ', ' N ', ' N ', ' N ', ' x ', ' D ', ' D ', ' D ', ' D ', ' D ', ' D ', ' x ', ' N ', ' N ', ' N ', ' N ', ' N ', ' N ', ' x ', ' D ', ' D ', ' D ', ' D ', ' D ', ' D ', ' x ', ' N '],
        [' N ', ' N ', ' x ', ' D ', ' D ', ' D ', ' D ', ' D ', ' D ', ' x ', ' N ', ' N ', ' N ', ' N ', ' N ', ' N ', ' x ', ' D ', ' D ', ' D ', ' D ', ' D ', ' D ', ' x ', ' N ', ' N ', ' N ', ' N ', ' N ', ' N ', ' x '],
        [' N ', ' N ', ' N ', ' x ', ' N ', ' N ', ' N ', ' N ', ' N ', ' N ', ' x ', ' N ', ' N ', ' N ', ' N ', ' N ', ' N ', ' x ', ' N ', ' N ', ' N ', ' N ', ' N ', ' N ', ' x ', ' N ', ' N ', ' N ', ' N ', ' N ', ' N '],
        [' D ', ' D ', ' D ', ' D ', ' D ', ' x ', ' N ', ' N ', ' N ', ' N ', ' N ', ' N ', ' x ', ' D ', ' D ', ' D ', ' D ', ' D ', ' D ', ' x ', ' N ', ' N ', ' N ', ' N ', ' N ', ' N ', ' x ', ' D ', ' D ', ' D ', ' D '],
        [' N ', ' N ', ' N ', ' N ', ' x ', ' D ', ' D ', ' D ', ' D ', ' D ', ' D ', ' x ', ' N ', ' N ', ' N ', ' N ', ' N ', ' N ', ' x ', ' D ', ' D ', ' D ', ' D ', ' D ', ' D ', ' x ', ' N ', ' N ', ' N ', ' N ', ' N '],
        [' D ', ' D ', ' D ', ' x ', ' N ', ' N ', ' N ', ' N ', ' N ', ' N ', ' x ', ' D ', ' D ', ' D ', ' D ', ' D ', ' D ', ' x ', ' N ', ' N ', ' N ', ' N ', ' N ', ' N ', ' x ', ' D ', ' D ', ' D ', ' D ', ' D ', ' D '],
        [' - ', ' - ', ' - ', ' N ', ' - ', ' - ', ' - ', ' - ', ' - ', ' - ', ' N ', ' - ', ' - ', ' - ', ' - ', ' - ', ' - ', ' N ', ' - ', ' - ', ' - ', ' - ', ' - ', ' - ', ' N ', ' - ', ' - ', ' - ', ' - ', ' - ', ' - ']
    ]
    Verificar(arreglo_1).validacion_turno_unidad()
    Verificar(arreglo_1).validacion_total()
    Verificar(arreglo_1).validacion_turno_trabajador()
