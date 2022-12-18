from django.shortcuts import render
from django.http import HttpResponse
import numpy as np

# Create your views here.

def vector(request):
    a = int(request.GET.get('a', None))
    size = request.GET.get('size', None)
    old = 0

    if size is None:
        return HttpResponse('Размер не указан')

    try:
        size = int(size)
    except:
        return HttpResponse('Размер не число')

    if size <= 0:
        return HttpResponse('Размер меньше или равен 0')

    matrix = request.GET.get('matrix', None)

    if matrix is None:
        return HttpResponse('Матрица не указана')

    matrix = matrix.split('*')

    new_matrix = []

    if len(matrix) != size:
        return HttpResponse('Матрица неверного размера')

    for row in matrix:
        try:
            row = list(map(float, row.split('_')))
        except:
            return HttpResponse('В матрице содержатся недопустимые значения')

        if len(row) != size:
            return HttpResponse('Неверный размер строки в матрице')

        new_matrix.append(row)


    new_matrix = np.array(new_matrix)
    old = new_matrix
    new_matrix = a*new_matrix
    '''new_matrix = [[value * a for value in num] for num in new_matrix]'''

    '''new_matrix = '<br/><br/>'.join([',&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;'.join(map(str,row)) for row in vector_matrix])
    new_matrix = '<p style=\"font-size:20pt;\">'+vector_matrix_str+'</p>'''

    return HttpResponse(f"<br><center>Старая матрица равна: {old}<center\><br\>"
                        f"<br><center>Новая матрица умноденная на {a} равна: {new_matrix}<center\><br\>")
