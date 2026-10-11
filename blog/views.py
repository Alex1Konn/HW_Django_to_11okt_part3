
#задание 7
# from django.shortcuts import render
#
# def index(request):
#     steps = ['Старт', 'Разгон', 'Взлёт']
#     steps_reversed = list(reversed(steps))
#     return render(request, 'blog/index.html', {
#         'steps': steps,
#         'steps_reversed': steps_reversed
#     })

#задание 8
# from django.shortcuts import render
#
# def index(request):
#     news = ['Старт', 'Разгон', 'Взлёт']
#     return render(request, 'blog/index.html', {'news': news})

# задание 9
# from django.shortcuts import render
#
# def index(request):
#     grades = {'Иванов': [5, 4, 5], 'Петров': [3, 4, 2]}
#     context = {
#         'grades': grades,
#         'title': 'Журнал оценок'
#     }
#     return render(request, 'blog/index.html', context)
