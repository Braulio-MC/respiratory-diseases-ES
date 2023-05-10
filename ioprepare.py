import os
import unicodedata
from enum import Enum
from random import choice
from typing import Literal
from diseases import diseases
from tabulate import tabulate


class _ResponseOptions(Enum):
    YES = 'si'
    N0 = 'no'


class _PickOneUtil:
    selected = None
    selected_questions = None
    locked = False


def _strip_accents(s: str):
    return ''.join(c for c in unicodedata.normalize('NFD', s)
                   if unicodedata.category(c) != 'Mn')


def _pick_one_and_lock():
    if not _PickOneUtil.locked:
        _PickOneUtil.selected = choice([*diseases.keys()])
        _PickOneUtil.selected_questions = diseases[_PickOneUtil.selected]['questions']
        _PickOneUtil.locked = True


def get_response(prompt: str, manner: Literal['random', 'pickone', 'stepbystep'] = 'stepbystep'):
    # _clear_screen()
    if manner == 'random':
        response = choice((_ResponseOptions.YES.value, _ResponseOptions.N0.value))
        print(prompt, response)
    elif manner == 'pickone':
        _pick_one_and_lock()
        if prompt.removesuffix(' (si/no): ') in _PickOneUtil.selected_questions:
            response = _ResponseOptions.YES.value
        else:
            response = _ResponseOptions.N0.value
    else:
        response = input(prompt)
        if response.isalpha():
            response = _strip_accents(response.lower())
        while response not in (_ResponseOptions.YES.value, _ResponseOptions.N0.value):
            response = input(prompt)
            if response.isalpha():
                response = _strip_accents(response.lower())
    return response


def _clear_screen():
    if os.name == 'posix':
        os.system('clear')
    elif os.name == 'ce' or os.name == 'nt' or os.name == 'dos':
        os.system('cls')


def init_render():
    # _clear_screen()
    print('A continuacion, conteste las siguientes preguntas para determinar una inferencia a su caso.')


def disease_matched_render(disease: str):
    # _clear_screen()
    print('<================================|  Conclusion  |=====================================>')
    print('''El motor de inferencia determino que la enfermedad presentada es {}, 
ya que el 100% de las preguntas para inferir la enfermedad fueron contestadas con un si.
Las preguntas contestadas con si fueron:'''.format(disease))
    questions = map(lambda q: '\t* ' + q, diseases[disease]['questions'])
    print(*questions, sep='\n')
    print('\n<===============================|  Recomendacion  |===================================>')
    print(diseases[disease]['treatment'])
    print('<=====================================================================================>')


def disease_not_matched_render(percentages: dict):
    # _clear_screen()
    print('<================================|  Conclusion  |=====================================>')
    print('''El motor de inferencia no pudo determinar una enfermedad especifica, pero se realizo un 
reporte con el porcentaje de probabilidad para cada enfermedad conocida por el motor.''')
    print('\n<=============================|  Reporte general  |===================================>')
    data = {'Enfermedad': percentages.keys(), 'Porcentaje': percentages.values()}
    print(tabulate(data, headers='keys', tablefmt='double_grid', showindex=True,
                   missingval='N/A', colalign=('center',), stralign='center', numalign='center'))
    print('\n<===========================|  Mayor probabilidad (3)  |==============================>')
    percentages = dict(sorted(percentages.items(), key=lambda item: item[1], reverse=True)[:3])
    data = {'Enfermedad': percentages.keys(), 'Porcentaje': percentages.values()}
    print(tabulate(data, headers='keys', tablefmt='double_grid', showindex=True,
                   missingval='N/A', colalign=('center',), stralign='center', numalign='center'))
    print('\n<======================|  Recomendacion por enfermedad (3)  |=========================>')
    disease_name_treatment = map(lambda d: d + ': ' + diseases[d]['treatment'] + '\n' + '-' * 45, percentages.keys())
    print(*disease_name_treatment, sep='\n')
    print('<=====================================================================================>')
