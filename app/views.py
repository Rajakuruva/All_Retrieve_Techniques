from django.shortcuts import render

from app.models import *
from django.db.models.functions import Length
from django.db.models import Q

# Create your views here.

def Data_Topic(request):
    lot=Topic.objects.all()
    lot=Topic.objects.all().order_by('Topic_name')
    lot=Topic.objects.all().order_by('-Topic_name')
    lot=Topic.objects.all().order_by(Length('Topic_name'))
    lot=Topic.objects.all().order_by(Length('Topic_name').desc())
    lot=Topic.objects.all()[::2]
    lot=Topic.objects.all()[1:3]
    lot=Topic.objects.all()[::3]
    lot=Topic.objects.filter(Topic_name='Chess')
    lot=Topic.objects.filter(Topic_name='Cricket')
    d={'topics':lot}
    return render(request,'Data_topic.html',d)

def Data_Webpage(request):
    tlo=Webpage.objects.all()
    tlo=Webpage.objects.filter(name__startswith='D')
    tlo=Webpage.objects.all()
    tlo=Webpage.objects.filter(name__startswith='R')
    tlo=Webpage.objects.all()
    tlo=Webpage.objects.filter(name__endswith='i')
    tlo=Webpage.objects.all()
    tlo=Webpage.objects.filter(State__startswith='T')
    tlo=Webpage.objects.all()
    tlo=Webpage.objects.filter(State__endswith='a')
    tlo=Webpage.objects.all()
    tlo=Webpage.objects.filter(name__in=('Rajasekhar','Dhoni'))
    tlo=Webpage.objects.all()
    tlo=Webpage.objects.filter(State__in=('Andhra pradesh','Chennai','Karnataka'))
    tlo=Webpage.objects.all()
    tlo=Webpage.objects.filter(name__contains='a')
    tlo=Webpage.objects.filter(State__contains='l')
    tlo=Webpage.objects.all()
    tlo=Webpage.objects.filter(name__regex='[A-Za-z]{7}')
    tlo=Webpage.objects.filter(name__regex='[A-Za-z]{10}')
    tlo=Webpage.objects.filter(State__regex='[A-Za-z]{4}')
    tlo=Webpage.objects.filter(Q(Topic_name='Cricket') & Q(name='Dhoni'))
    #LOW=Webpage.objects.filter(Q(topic_name='Cricket') & Q(name='dhoni'))
    tlo=Webpage.objects.filter(Q(State='Andhra pradesh') | Q(name='Rajasekhar'))
    tlo=Webpage.objects.filter(Q(State='Chennai')| Q(State='Andhra pradesh'))
    d={'Web':tlo}
    return render(request,'Data_Webpage.html',d)

def Data_AccessRecord(request):
    lo=AccessRecord.objects.all()
    lo=AccessRecord.objects.filter(Dates__month='02')
    lo=AccessRecord.objects.filter(Dates__month='06')
    lo=AccessRecord.objects.all()
    lo=AccessRecord.objects.filter(Dates__year='2022')
    lo=AccessRecord.objects.filter(Dates__year='2021')
    lo=AccessRecord.objects.all()
    lo=AccessRecord.objects.filter(Dates__day='07')
    lo=AccessRecord.objects.all()
    lo=AccessRecord.objects.filter(Dates__day='25')
    lo=AccessRecord.objects.all()
    d={'Access':lo}
    return render(request,'Data_AccessRecord.html',d)