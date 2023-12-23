from django.shortcuts import render
from asvs_app.models import NgoLogo
from carousel.models import CarouselImage
from about_asvs.models import Vision,Mission,AboutNgo
from what_we_can.models import Health,Education,Environment,SocialCare
from event.models import Event
from meet_our_team.models import Team
from blog.models import Blog


def homepage(request):
    ngologo = NgoLogo.objects.first()
    carousel = CarouselImage.objects.all()
    about = AboutNgo.objects.all().first()
    mission = Mission.objects.all().first()
    vision = Vision.objects.all().first()
    what_we_can_health = Health.objects.all().first()
    what_we_can_education = Education.objects.all().first()
    what_we_can_environment = Environment.objects.all().first()
    what_we_can_socialcare = SocialCare.objects.all().first()
    event = Event.objects.filter(is_active=True)
    team = Team.objects.filter(is_active = True)
    blog = Blog.objects.all()
    data = {
        "ngologo":ngologo,
        "carousel":carousel,
        "mission":mission,
        "about":about,
        "vision":vision,
        "what_we_can_health":what_we_can_health,
        "what_we_can_education":what_we_can_education,
        "what_we_can_environment":what_we_can_environment,
        "what_we_can_socialcare":what_we_can_socialcare,
        "event":event,
        "team":team,
        "blog":blog
    }
    r = render(request,"asvs_app/index.html",data)
    return r