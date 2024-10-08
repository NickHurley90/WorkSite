from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
  return render (request,'home.html')

def about(request):
  return render(request, 'about.html')


def jobs_index(request):
  return render(request, 'jobs/index.html', { 'jobs': jobs })


class Joblisting:  
  def __init__(self, title, description, requirements, trade_category, location):
    self.title = title
    self.description = description
    self.requirements = requirements
    self.trade_category = trade_category
    self.location = location

jobs = [
  Joblisting('Sunset Drive', 'Bathroom Renovations', 'Experience with instalation of jacuzzi', 'Plumbing', 'West Boca'),
  Joblisting('Lake Fort Worth', 'Bathroom Renovations', 'Experience with instalation of jacuzzi', 'Electical', 'West Boca'),
  Joblisting('Desert Rose', 'Bathroom Renovations', 'Experience with instalation of jacuzzi', 'Carpentry', 'West Boca'),
  Joblisting('Coconut Creek', 'Bathroom Renovations', 'Experience with instalation of jacuzzi', 'Plumbing', 'West Boca'),
]


