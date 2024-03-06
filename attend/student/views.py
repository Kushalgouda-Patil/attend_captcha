from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import json
from .student_independent_files import student_main
from django.http import QueryDict
# Create your views here.
@csrf_exempt
def index(request):
    if request.method == 'POST':
        print(request.body)
        # data=json.loads(request.body);
        # usn=data['usn']
        # dd=int(data['dd'])
        # mm=data['mm']
        # yyyy=int(data['yyyy'])
        decoded_data = QueryDict(request.body.decode('utf-8'))
        usn = decoded_data.get('usn')
        dd = decoded_data.get('dd')
        mm = decoded_data.get('mm')
        yyyy = decoded_data.get('yyyy')
        print(usn,dd,mm,yyyy)
        return JsonResponse(student_main.main(usn,dd,mm,yyyy))
    else:
        return JsonResponse({'message': 'Invalid method'})
    