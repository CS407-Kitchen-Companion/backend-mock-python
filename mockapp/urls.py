from django.urls import path
from .views import handle_get_request,search,searchButton,list,getFolders,getSeveralRecipe,getUser,getUserSavedRecipes,getRecipe,getRating,getFoldersSpec

urlpatterns = [
    path('get/', handle_get_request, name='handle_get_request'),
    path('search/', search, name='search'),
    path('list/', list, name='list'),
    path('submitsearch/', searchButton, name='submitsearch'),
    path('getFolders/', getFolders, name="getFolders"),
    path('getRating/<int:id>/', getRating, name="getRating"),
    path('getSeveralRecipe/',getSeveralRecipe, name='getSeveralRecipe'),
    path('users/<int:id>/',getUser, name="getUser"),
    path('users/recipes/',getUserSavedRecipes, name='getUserSavedRecipes'),
    path('getRecipe/', getRecipe, name='getRecipe'),
    path('getFolder/<int:id>/', getFoldersSpec, name="getFoldersSpec"),
]
