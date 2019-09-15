from django import forms
from sith_recruiting.models import Planet, Trial, Question
from random import randint

class RecruitForm(forms.Form):
    planets_set = Planet.objects.all()
    planets_choices = [
        (planet, planet.name) for planet in planets_set
    ]
    planet_choice = forms.CharField(label="Планета",
        widget=forms.Select(choices=planets_choices))
    name = forms.CharField(label="Имя", max_length=30)
    age = forms.IntegerField(label="Возраст")
    email = forms.EmailField(label="Email")

class TrialForm(forms.Form):
    def __init__(self, *args, **kwargs):
        super(TrialForm, self).__init__(*args, **kwargs)
        total_trials = Trial.objects.all().count()
        self.current_trial = Trial.objects.all()[randint(0, total_trials-1)]

        questions = Question.objects.filter(trial_id__exact=self.current_trial.id)

        for i in range(len(questions)):
            self.fields['question_%s' % questions[i].id] = \
            forms.BooleanField(label=questions[i].question_text, required=False)

