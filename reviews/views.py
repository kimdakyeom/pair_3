from django.shortcuts import render
from .models import Review
from .forms import ReviewForm

# Create your views here.


def create(request):
    if request.method == "POST":
        form = ReviewForm(request.POST)
        if form.is_valid():
            form.save()
            context = {
                "form": form,
            }
            return render(request, "reviews/create.html", context)
    else:
        form = ReviewForm()
    context = {
        "form": form,
    }
    return render(request, "reviews/create.html", context)
