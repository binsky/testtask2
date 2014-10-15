from decimal import Decimal
import json
# import simplejson
from time import sleep
from django.core.serializers.json import DjangoJSONEncoder
from django.http import HttpResponse
from django.shortcuts import render, redirect
import re
# import simplejson


def sort_view(request):
    if not _logged_in_(request.user):
        return redirect('homepage')
    if request.method == 'GET' and request.is_ajax():
        data = request.GET.get('input')
        if data:
            sleep(2)
        key = 'result'
        try:
            val = _sort_(data)
        except:
            val = 'Wrong input.'
            key = 'error'
            if data is None:
                val = 'Nononon'
        return HttpResponse(json.dumps({key: val}, cls=DjangoJSONEncoder), content_type="application/json")
    return render(request, 'sort.html')


def _logged_in_(usr):
    if not usr.is_authenticated():
        return False
    return True


def _sort_(data):
    result = re.findall(r"[\w'.-]+", data)
    result = [Decimal(x) for x in result]
    # sleep(3)
    return _bubble_(result)


def _bubble_(data):
    for i in range(len(data)):
        for j in range(i+1, len(data)):
            if data[j] < data[i]:
                data[j], data[i] = data[i], data[j]
    return data


