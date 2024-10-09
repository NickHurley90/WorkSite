from django.shortcuts import render, get_object_or_404, redirect
from .models import StaffRegister, JobListing, JobRegistration
from .forms import EmployerForm, StaffRegisterForm, SignUpForm
from django.contrib.auth import login

# Home Page
def home(request):
    return render(request, 'home.html')

# About Page
def about(request):
    return render(request, 'about.html')

# Job listings
def job_listings(request):
    listings = JobListing.objects.all()
    return render(request, 'job_listing.html', {'listings': listings})

# Job Detail View
def job_detail(request, listing_id):
    listing = get_object_or_404(JobListing, id=listing_id)
    return render(request, 'job_detail.html', {'listing': listing})

# Staff - Register for a Job Listing
def register_for_job(request, listing_id):
    listing = get_object_or_404(JobListing, id=listing_id)
    if request.method == 'POST':
        # Assuming staff details are passed in the form (no login system yet)
        staff_id = request.POST['staff_id']
        staff = get_object_or_404(StaffRegister, id=staff_id)
        JobRegistration.objects.create(listing=listing, staff=staff)
        return redirect('job_listings')
    return render(request, 'register_for_job.html', {'listing': listing})

# Create a job listing (for employers)
def create_job_listing(request):
    if request.method == 'POST':
        title = request.POST['title']
        description = request.POST['description']
        requirements = request.POST['requirements']
        trade_category = request.POST['trade_category']
        location = request.POST['location']
        listing_id = request.POST['listing_id']  # You can auto-generate this as needed
        JobListing.objects.create(
            title=title,
            description=description,
            requirements=requirements,
            trade_category=trade_category,
            location=location,
            listing_id=listing_id
        )
        return redirect('job_listings')
    return render(request, 'create_job_listing.html')

# Employer registration view
def employer_register(request):
    if request.method == 'POST':
        form = EmployerForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('employer_login')  # Redirect to login or success page
    else:
        form = EmployerForm()
    return render(request, 'registration/employer_register.html', {'form': form})

# Staff registration view
def staff_register(request):
    if request.method == 'POST':
        form = StaffRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('staff_login')  # Redirect to login or success page
    else:
        form = StaffRegisterForm()
    return render(request, 'registration/staff_register.html', {'form': form})

def job_register(request, job_id):
    job = JobListing.objects.get(id=job_id)
    if request.method == 'POST':
        form = JobRegistration(request.POST)
        if form.is_valid():
            job_registration = form.save(commit=False)
            job_registration.listing = job
            job_registration.staff = StaffRegister.objects.get(username=request.POST['username'])  # Example
            job_registration.save()
            return redirect('job_list')
    else:
        form = JobRegistration()
    return render(request, 'jobs/job_register.html', {'form': form, 'job': job})

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Log in the user after signing up
            return redirect('home')  # Redirect to the home page or another page
    else:
        form = SignUpForm()
    return render(request, 'registration/signup.html', {'form': form})