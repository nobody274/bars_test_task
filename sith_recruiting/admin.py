from django.contrib import admin

from .models import Sith, Planet, Trial, Question

class QuestionInLine(admin.StackedInline):
    model = Question
    extra = 1

class TrialAdmin(admin.ModelAdmin):
    #fieldsets = [
    #    ('Order code', {'fields': ['order_code']}),
    #]
    fields = ['order_code']
    inlines = [QuestionInLine]


admin.site.register(Sith)
admin.site.register(Planet)
admin.site.register(Trial, TrialAdmin)
