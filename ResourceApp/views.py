from django.shortcuts import render
from django.http import HttpResponse


# Display HomePage
def HomePage(request):
    return render(request, 'ResourceApp/HomePage.html')


# Display SubjectPage
def SubjectPage(request):
    return render(request, 'ResourceApp/SubjectPage.html')


# Fetch resources from Google Sheet based on three selections and return them on ResultsPage
def result1(request):
    subject = request.GET['SubjectSelection']
    level = request.GET['LevelSelection']
    medium = request.GET['MediumSelection']
    return render(request, 'ResourceApp/ResultsPage.html', {'SubjectSelection': subject,
                                                            'LevelSelection': level, 'MediumSelection': medium})
