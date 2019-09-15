from django.db import models

class Planet(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name

class Recruit(models.Model):
    name = models.CharField(max_length=30)
    planet = models.ForeignKey(Planet, on_delete=models.CASCADE)
    age = models.SmallIntegerField()
    email = models.EmailField()
    is_shadow_hand = models.BooleanField(default=False)

    def __str__(self):
        return self.name

class Sith(models.Model):
    name = models.CharField(max_length=30)
    planet = models.ForeignKey(Planet, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Trial(models.Model):
    order_code = models.IntegerField()

    def __str__(self):
        return str(self.order_code)

class Question(models.Model):
    question_text = models.CharField(max_length=200)
    trial = models.ForeignKey(Trial, on_delete=models.CASCADE)

    def __str__(self):
        return self.question_text

class Answer(models.Model):
    recruit = models.ForeignKey(Recruit, on_delete=models.CASCADE)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    value = models.BooleanField(default=False)