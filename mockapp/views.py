from django.shortcuts import render

from django.http import JsonResponse

def handle_get_request(request):
    data = {'message': 'lorem'}
    return JsonResponse(data)
