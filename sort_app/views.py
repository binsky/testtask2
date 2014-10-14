import json
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render, redirect


# @login_required
def sort(request):
    if not request.user.is_authenticated():
        return redirect('homepage')
    import re
    res = ''
    if request.method == 'POST' and request.is_ajax():
        res = re.findall(r"[\w'.-]+", request.POST['input'])
        try:
            res = [float(x) for x in res]
        except:
            return HttpResponse(json.dumps({'result': 'Wrong input'}), content_type="application/json")
    else:
        return render(request, 'sort.html')
    res = ', '.join(str(x) for x in _bubble_(res))
    return HttpResponse(json.dumps({'result': res}), content_type="application/json")


def _bubble_(list):
    for i in range(len(list)):
        for j in range(i+1, len(list)):
            if list[j] < list[i]:
                list[j], list[i] = list[i], list[j]
    return list
