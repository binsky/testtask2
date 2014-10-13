from django.contrib.auth.decorators import login_required
from django.shortcuts import render


@login_required
def sort(request):
    import re
    res = ''
    if request.method == 'POST':
        res = re.findall(r"[\w'.-]+", request.POST['input'])
    try:
        res = [float(x) for x in res]
    except:
        return render(request, 'sort.html', {'result': 'Wrong input.'})
    res = ', '.join(str(x) for x in _bubble_(res))
    return render(request, 'sort.html', {'result': res})


def _bubble_(list):
    for i in range(len(list)):
        for j in range(i+1, len(list)):
            if list[j] < list[i]:
                list[j], list[i] = list[i], list[j]
    return list
