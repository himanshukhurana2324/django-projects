from django.shortcuts import render
from .models import Destination
# Create your views here.
def home(request):
    desc1 = Destination()
    desc1.img= 'destination_1.jpg'
    desc1.name="Chandigarh"
    desc1.price=200
    desc1.desc="Welcome to Chandigarh"

    desc2 = Destination()
    desc2.img= 'destination_2.jpg'
    desc2.name="Kerela"
    desc2.price=300
    desc2.desc="Welcome to Kerela"

    desc3 = Destination()
    desc3.img= 'destination_3.jpg'
    desc3.name="Kolkata"
    desc3.price=400
    desc3.desc="Welcome to Kolkata"

    data=[desc1, desc2, desc3]
    return render(request,'index.html', {'dest':data},)