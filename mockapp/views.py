from django.shortcuts import render

from django.http import JsonResponse

def handle_get_request(request):
    data = {'message': 'lorem'}
    return JsonResponse(data)

def search(request):
    if request.method == 'GET':
        keyword = request.GET.get('keyword', None)
        recipes = ["cake","carrot cake","ugly cake","pretty cake","chocolate cake"]
        if keyword is not None:
            response_data = {
                "recipes": recipes
            }
            return JsonResponse(response_data)
        else:
            error_data = {
                "error": "Invalid or missing keyword",
                "status_code": 400  # Bad Request
            }
            return JsonResponse(error_data, status=400)

def searchButton(request):
    if request.method == 'GET':
        keyword = request.GET.get('keyword', None)
        if keyword is not None:
            recipes = [{"id": 3, "Title": "Chocolate Cake", "Ingredients": ["dessert", "chocolate", "cake"]},
                       {"id": 2, "Title": "Ugly Cake", "Ingredients": ["ugly", "chocolate", "cake"]}]
            response_data = {
                "recipes": recipes
            }
            return JsonResponse(response_data)
        else:
            error_data = {
                "error": "Invalid or missing keyword",
                "status_code": 400
            }
            return JsonResponse(error_data, status=400)

    # If request method is neither GET nor POST
    error_data = {
        "error": "Unsupported request method",
        "status_code": 405  # Method Not Allowed
    }
    return JsonResponse(error_data, status=405)
