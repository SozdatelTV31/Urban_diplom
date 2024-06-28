from django.shortcuts import render, get_object_or_404, redirect

from django.contrib.auth.decorators import login_required
from .models import ImageFeed
from .mechanics import process_image
from .forms import ImageFeedForm


def gates(request):
    return render(request, 'gates.html')


def home(request):
    return render(request, 'home.html')


@login_required
def naro_pic(request):
    image_feeds = ImageFeed.objects.filter(user=request.user)
    return render(request, 'naro_pic.html', {'image_feeds': image_feeds})


@login_required
def process(request, feed_id):
    image_feed = get_object_or_404(ImageFeed, id=feed_id, user=request.user)
    process_image(feed_id)
    return redirect('naro_pic')


@login_required
def add(request):
    if request.method == 'POST':
        form = ImageFeedForm(request.POST, request.FILES)
        if form.is_valid():
            image_feed = form.save(commit=False)
            image_feed.user = request.user
            image_feed.save()
            return redirect('naro_pic')
    else:
        form = ImageFeedForm()
    return render(request, 'add_image_feed.html', {'form': form})


@login_required
def delete(request, image_id):
    image = get_object_or_404(ImageFeed, id=image_id, user=request.user)
    image.delete()
    return redirect('naro_pic')


def about(request, *args, **kwargs):
    return render(request, 'about.html', {})
