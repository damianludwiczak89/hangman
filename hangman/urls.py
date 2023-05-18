from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),

    # API routes
    path("generate_password/<str:category>", views.generate_password, name="generate_password"),
    path("check/<str:answer>/<str:guess>", views.check, name="check"),
    path("hangman_ascii/<int:status>", views.hangman_ascii, name="hangman_ascii"),
    path("blank/<str:blanks>/<str:answer>/<str:guess>", views.blank, name="blank")
 ]