

# Create my views
from django.shortcuts import render
from django.http import HttpResponse
from .models import Destination

def index(request):
  # des1= Destination()
  # des1.name="Chandigarh"
  # des1.price="300"
  # des1.desc="Lets visit the Rose Garden"
  # des1.offer=True
  # des1.img="chandigarh.jpg"

  # des2= Destination()
  # des2.name="Kerela"
  # des2.price="400"
  # des2.desc="Time to feel the monsoon"
  # des2.offer=False
  # des2.img="destination_2.jpg"
  
  # des3= Destination()
  # des3.name="Bangalore"
  # des3.price="500"
  # des3.desc="The IT hub"
  # des3.offer=False
  # des3.img="destination_3.jpg"
 
  # data=[des1, des2, des3]



  # here we are fetching all the objects from the database and sending it to the html file
  data = Destination.objects.all()
 
  return render(request,'index.html', {'dest':data})
