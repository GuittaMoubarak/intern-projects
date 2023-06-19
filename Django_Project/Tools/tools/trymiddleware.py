from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.urls import reverse
# from django.utils.cache import add_never_cache_headers


# class NoCacheMiddleware:
#     def __init__(self, get_response):
#         self.get_response = get_response

#     def __call__(self, request):
#         response = self.get_response(request)

#         # Set the Cache-Control header to 'no-store'
#         patch_cache_control(response, no_store=True)

#         return response


class authMiddleware:

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        print("before response")
        print(request.path)
        if not request.user.is_authenticated and not (request.path == '/' or request.path == '/user_register'):
            return redirect("/")


        response = self.get_response(request)

        # patch_cache_control(response, no_store=True)
        # add_never_cache_headers(response)
        print("after response")
        return response
