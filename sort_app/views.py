import json
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
import re


def sort(request):
    if not request.user.is_authenticated():
        return redirect('homepage')
    # res = ''
    if request.method == 'POST' and request.is_ajax():
        res = re.findall(r"[\w'.-]+", request.POST['input'])
        try:
            res = [float(x) for x in res]
        except:
            return HttpResponse(json.dumps({'error': 'Wrong input.'}), content_type="application/json")
    else:
        return render(request, 'sort.html')
    # res = ', '.join(str(x) for x in _bubble_(res))
    return HttpResponse(json.dumps({'result': _bubble_(res)}), content_type="application/json")


def _bubble_(l):
    for i in range(len(l)):
        for j in range(i+1, len(l)):
            if l[j] < l[i]:
                l[j], l[i] = l[i], l[j]
    return l
