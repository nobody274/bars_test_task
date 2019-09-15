from django.shortcuts import render
from django.urls import reverse
from django.http import HttpResponseRedirect
from django.core.mail import send_mail

from .forms import RecruitForm, TrialForm
from .models import Recruit, Planet, Answer, Question, Sith

def index(request):
    return render(request, 'sith_recruiting/index.html', {})

def recruit(request):
    form = RecruitForm()
    try:
        new_recruit = Recruit()
        new_recruit.name = request.POST['name']
        new_recruit.email = request.POST['email']
        new_recruit.age = request.POST['age']
        new_recruit.planet = Planet.objects.filter(name=request.POST['planet_choice'])[0]
        new_recruit.is_shadow_hand = False
    except Exception as e:
        return render(request, 'sith_recruiting/recruit.html', {
            'form': form,
            'error_message': str(e)
                })
    else:
        new_recruit.save()
        return HttpResponseRedirect(reverse('sith_recruiting:trial', args=(new_recruit.id,)))

def sith(request):
    if request.method == "POST":
        new_shadow_hand = Recruit.objects.get(pk=int(request.POST['recruit_select']))
        new_shadow_hand.is_shadow_hand = True
        new_shadow_hand.save()

        send_mail(
            "Поздравляем",
            "Вас выбрали рукой тени",
            "sith_recruiting@deathstar.com",
            (new_shadow_hand.email,),
        )
        return HttpResponseRedirect(reverse('sith_recruiting:index'))
        #recruit = Recruit.objects.get(pk=request.POST[''])
    else:
        siths_set = Sith.objects.all()
        recruits_set = Recruit.objects.filter(is_shadow_hand__exact=False)
        answers = Answer.objects.all()
        questions = Question.objects.all()
        return render(request, 'sith_recruiting/sith.html', {
            'siths_set': siths_set,
            'recruits_set': recruits_set,
            'answers': answers,
            'questions': questions,
            }
    )

def recruit_trial(request, new_recruit_id):
    form = TrialForm()
    if request.method == "POST":
        for i in form.fields:
            new_answer = Answer()
            new_answer.recruit = Recruit.objects.get(pk=new_recruit_id)
            current_id = i.split('_')[1]
            new_answer.question = Question.objects.filter(
                id__exact=current_id
            )[0]
            if i in request.POST: new_answer.value = True
            else: new_answer.value = False
            new_answer.save()
        return HttpResponseRedirect(reverse('sith_recruiting:index'))
    else:
        return render(request, 'sith_recruiting/recruit.html', {'form': form})