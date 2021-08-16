from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from .forms import CustomRegister
from django.contrib import messages
from .models import job, reviews, transactions
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import ListView, DetailView, CreateView, DeleteView, UpdateView
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.db.models import Count
# Create your views here.




class JobListView(ListView):
    model = job
    template_name = 'freelance/home.html'
    context_object_name = 'jobs'
    ordering = ['-date_posted']
    paginate_by = 2
    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(finished = False)


def JobListViewFiltered(request):
    if request.method == "POST":
        searched = request.POST['searched']
        if not searched.isnumeric():
            return redirect('Main-Page')   
        return render(request, 'freelance/home_search.html', {'jobs': job.objects.filter(price__gte=0, price__lte=int(searched)).order_by('-date_posted')})
    else:
        return redirect('Main-Page')


def ChartTransaction(request):
    stats = transactions.objects.values('workerID__username').annotate(total=Count('workerID')).order_by()
    #print(stats)
    store = {}
    for sub in stats.iterator():
        store[sub['workerID__username']] = sub['total']
    return render(request, 'freelance/transaction_chart.html', {'dict': store})



class ReviewListView(ListView):
    model = reviews
    template_name = 'freelance/review_home.html'
    ordering = ['-date_posted']
    context_object_name = 'reviews'
    paginate_by = 2


def register(request):
    if request.method == "POST":
        form = CustomRegister(request.POST)
        if form.is_valid():
            form.save()
            return redirect('Main-Page')
    else:
        form = CustomRegister()
    return render(request,'freelance/register.html', {'form': form} )
@login_required(login_url='login')
def BuyJob(request, pk):
    getJob = job.objects.get(pk=pk)
    getJob.finished = True
    getJob.save()
    newTransaction = transactions(jobID=getJob,workerID=request.user)
    newTransaction.save()
    messages.success(request, "Successfully hired for job")
    return render(request, 'freelance/buyjob.html')


class JobDetailView(DetailView):
    model = job
    template_name = 'freelance/job_detail.html'


class JobDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    login_url = 'login'
    template_name = 'freelance/job_delete.html'
    model = job
    success_url = '/'
    def test_func(self):
        return self.get_object().userID == self.request.user

class ReviewDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    login_url = 'login'
    template_name = 'freelance/review_delete.html'
    model = reviews
    success_url = '/'
    def test_func(self):
        return self.get_object().userID == self.request.user


class JobUpdateView(LoginRequiredMixin, UserPassesTestMixin,UpdateView):
    login_url = 'login'
    model = job
    fields = ['title','price','finished', 'description', 'language', 'categories']
    template_name = 'freelance/job_edit.html'
    success_url = '/'
    def test_func(self):
        return self.get_object().userID == self.request.user


class ReviewDetailView(DetailView):
    model = reviews
    template_name = 'freelance/review_detail.html'

def ReviewSearchBar(request):
    if request.method == "POST":
        searched = request.POST['searched']
        return render(request, 'freelance/search_reviews.html', {'reviews': reviews.objects.filter(reviewee__username=searched)})
    else:
        return redirect('Main-Page')




class ReviewUpdate(LoginRequiredMixin, UserPassesTestMixin,UpdateView):
    login_url = 'login'
    model = reviews
    fields = ['description']
    template_name = 'freelance/review_update.html'
    success_url = '/'
    def test_func(self):
        return self.get_object().userID == self.request.user

class WriteReview(LoginRequiredMixin, CreateView):
    login_url = 'login'
    model = reviews
    template_name = 'freelance/review.html'
    fields = ['description', 'reviewee']
    def form_valid(self, form):
            form.instance.userID = self.request.user
            return super().form_valid(form)
    def get_success_url(self):
        return reverse('review-detail', kwargs={'pk': self.object.pk})

class JobCreateView(LoginRequiredMixin, CreateView):
    login_url = 'login'
    model = job
    template_name = 'freelance/jobpost.html'
    fields = ['title','price', 'description', 'language', 'categories']
    def form_valid(self, form):
            form.instance.userID = self.request.user
            return super().form_valid(form)

    def get_success_url(self):
        return reverse('job-detail', kwargs={'pk': self.object.pk})

