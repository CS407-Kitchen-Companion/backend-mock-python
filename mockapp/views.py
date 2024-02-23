from django.shortcuts import render

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt


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


def list(request):
    if request.method == 'GET':
        keyword = request.GET.get('keyword', None)
        if keyword is not None:
            recipe = [{"id": keyword, "Title": "Chocolate Cake", "Ingredients": ["dessert", "chocolate", "cake"],"Body": "samplebody"}]
            response_data = {
                "recipe": recipe
            }
            return JsonResponse(response_data)
        else:
            recipe = [{"id": 1, "Title": "Chocolate Cake", "Ingredients": ["dessert", "chocolate", "cake"],
                       "Body": "samplebody"}]
            response_data = {
                "recipe": recipe
            }
            return JsonResponse(response_data)


def getFolders(request):
    if request.method == 'GET':
        recipe = [["folder1", "folder2", "folder3"]]
        response_data = {
            "folder": recipe
        }
        return JsonResponse(response_data)

def getRating(request,id):
    if request.method == 'GET':
        response_data = {
            "response": "See Data.",
            "status": 200,
            "error": False,
            "data": {
                "id": 1,
                "recipe": 1,
                "createdBy": 2,
                "rating": 5
            }
        }
        return JsonResponse(response_data)


def getSeveralRecipe(request):
    response_data = {
        "recipes": [
            1,
            2,
            3
        ]
    }
    return JsonResponse(response_data)

def getUser(request,id):
    response_data = {
        "response": "See Data.",
        "status": 200,
        "error": False,
        "data": {
            "id": 1,
            "username": "test_1",
            "email": "test@email",
            "createdAt": "2024-02-12T21:05:41.846385Z"
        }
    }
    return JsonResponse(response_data)

def getUserSavedRecipes(request):
    response_data = {
        "response": "See Data.",
        "status": 200,
        "error": False,
        "data": [
            2,
            3,
            4
        ]
    }
    return JsonResponse(response_data)


def getRecipe(request):
    response_data = {
        "response": "See Data.",
        "status": 200,
        "error": False,
        "data": {
            "id": 24,
            "title": "title 1",
            "content": [
                "direction1",
                "direction2"
            ],
            "createdBy": 2,
            "createdAt": "2024-02-20T23:43:38.226555Z",
            "comments": [],
            "ratings": [
                2
            ],
            "appliances": [
                "Knife",
                "Literal_Kitchen"
            ],
            "tags": [
                "abc",
                "def",
                "tag1"
            ],
            "ingredients": {
                "i1": "p1",
                "i2": "p2"
            },
            "ratingCount": 1,
            "calculatedRating": 5,
            "serves": 5,
            "time": 3600,
            "calories": 105,
            "updatedAt": "2024-02-20T23:44:21.954814Z",
            "edited": False
        }
    }
    return JsonResponse(response_data)


def getFoldersSpec(request,id):
    response_data = {
        "response": "See Data.",
        "status": 200,
        "error": False,
        "data": {
            "id": 1,
            "recipies": [
                3
            ],
            "title": "test folder 1",
            "createdBy": 4
        }
    }
    return JsonResponse(response_data)
