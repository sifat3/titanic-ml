from django.shortcuts import render
from . import ml_predict


def home(request):
    return render(request, 'base/index.html')


def result(request):

    pclass = request.POST.get('pclass')
    sex = request.POST.get('sex')
    age = int(request.POST.get('age'))
    sibsp = request.POST.get('sibsp')
    parch = request.POST.get('parch')
    fare = request.POST.get('fare')
    embarked = request.POST.get('embarked')
    title = request.POST.get('title')

    prediction = ml_predict.prediction_model(pclass, sex, age, sibsp, parch, fare, embarked, title)
    context = {
        'prediction': prediction
    }
    return render(request, 'base/result.html', context)

