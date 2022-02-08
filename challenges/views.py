from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse


# Create your views here.
monthly_challenges = {
    "january": "eat no meat for the entire month",
    "febuary":  "eat no meat for the entire month",
    "march":  "eat no meat for the entire month",
    "april":  "eat no meat for the entire month",
    "may":  "eat no meat for the entire month",
    "june":  "eat no meat for the entire month",
    "july":  "eat no meat for the entire month",
    'august': "eat no meat for the entire month",
    "september": "eat no meat for the entire month",
    "october": "eat no meat for the entire month",
    "november": "eat no meat for the entire month",
    "december": "eat no meat for the entire month",
}
    
def index(request):
    list_items = ""
    months = list(monthly_challenges.keys())
    
    for month in months:
        capitalized_month = month.capitalize()
        month_path = reverse("month-challenge", args=[month])
        list_items += f"<li><a href=\"{month_path}\">{capitalized_month}</a></li>"
    response_data = f"<ul>{list_items}</ul>"
    return HttpResponse(response_data)

def monthly_challenge_by_number(request,month):
    months = list(monthly_challenges.keys())
    if month > len(months):
        return HttpResponseNotFound('invalid month')
    redirect_month = months[month - 1]
    redirect_path = reverse("month-challenge", args=[redirect_month])
    return HttpResponseRedirect(redirect_path) 

def monthly_challenge(request, month):
    try:
        challenge_text = monthly_challenges[month]
        return render(request,'challenges/challenge.html', {
            "text": challenge_text
        })
    except:
        return HttpResponseNotFound("this month is not supported")