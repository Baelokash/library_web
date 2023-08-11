from django.shortcuts import render

def index(reguest):
    return render(reguest, "style/homePage.html")

