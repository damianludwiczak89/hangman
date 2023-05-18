from django.shortcuts import render
from pyfiglet import Figlet
from django.http import JsonResponse
from . import helpers

# Create your views here.
def index(request):
    figlet = Figlet()
    figlet.setFont(font="big")
    
    title = figlet.renderText("HANGMAN")

    # Categories
    figlet.setFont(font="big")
    choose = figlet.renderText("Choose:")
    animals = figlet.renderText("ANIMALS")
    countries = figlet.renderText("COUNTRIES")
    fruits = figlet.renderText("FRUITS")
    vegetables = figlet.renderText("VEGETABLES")


    return render(request, "hangman/index.html", {
        "title": title,
        "animals": animals,
        "countries": countries,
        "fruits": fruits,
        "vegetables": vegetables,
        "choose": choose,
    })

def generate_password(request, category):

    # Return random word from the category
    password = helpers.get_answer(category)
    return JsonResponse(password, safe=False, status=200)	

def check(request, answer, guess):

    guess = guess.upper()

    # If guess equals answer
    if guess == answer:
        return JsonResponse(1, safe=False, status=200)	

    # If answer contains a guess, assuming guess is only 1 character
    elif guess in answer and len(guess) == 1:
        return JsonResponse(2, safe=False, status=200)	

    # If there is no match
    else:
        return JsonResponse(3, safe=False, status=200)	

def hangman_ascii(request, status):
    # Return hangman in ascii accordingly to number of mistakes
    match status:
        case 0:
            drawing = f"\n  +---+\n      |\n      |\n      |\n      |\n      |\n      |\n=========\n"
        case 1:
            drawing = f"\n  +---+\n  |   |\n      |\n      |\n      |\n      |\n      |\n=========\n"
        case 2:
            drawing = f"\n  +---+\n  |   |\n  O   |\n      |\n      |\n      |\n      |\n=========\n"
        case 3:
            drawing = f"\n  +---+\n  |   |\n  O   |\n  |   |\n      |\n      |\n      |\n=========\n"
        case 4:
            drawing = f"\n  +---+\n  |   |\n  O   |\n /|   |\n      |\n      |\n      |\n=========\n"
        case 5:
            drawing = f"\n  +---+\n  |   |\n  O   |\n /|\  |\n      |\n      |\n      |\n=========\n"
        case 6:
            drawing = f"\n  +---+\n  |   |\n  O   |\n /|\  |\n /    |\n      |\n      |\n=========\n"
        case 7:
            drawing = f"\n  +---+\n  |   |\n  O   |\n /|\  |\n / \  |\n      |\n      |\n=========\n"

    return JsonResponse(drawing, safe=False, status=200)	

def blank(request, blanks, answer, guess):
        
        # If user guess full answer at once
        if answer == guess:
            return JsonResponse(" ".join(answer), safe=False, status=200)
        
        # Delete empty spaces between underscores temporarily for easier operations on strings
        blanks = blanks.replace(" ", "")

        # Convert to a list to make it mutable
        temp_list = list(blanks)

        for i in range(len(answer)):
            if answer[i] == guess.upper():
                temp_list[i] = guess.upper()
        # Convert back from list to a string and add empty spaces between underscores again for better readability
        blanks = " ".join(temp_list)

        return JsonResponse(blanks, safe=False, status=200)