from django.shortcuts import render, redirect
from .models import Articles
from .forms import ArticlesForm
from django.views.generic import DetailView, UpdateView, DeleteView


def news(request, *args, **kwargs):
    db_news = Articles.objects.order_by('-date')
    return render(request, 'news.html', {'db_news': db_news})


def create(request, *args, **kwargs):
    error = ''
    if request.method == 'POST':
        form_post = ArticlesForm(request.POST)
        if form_post.is_valid():
            form_post.save()
            return redirect('/news')
        else:
            error = 'Не тот формат поста'

    form = ArticlesForm()
    data = {
        'form': form,
        'error': error
    }
    return render(request, 'create_news.html', data)


class ViewingPost(DetailView):
    model = Articles
    template_name = 'viewing_post_pattern.html'
    context_object_name = 'post_next'


class UpdatePost(UpdateView):
    model = Articles
    template_name = 'update_news.html'
    form_class = ArticlesForm


class DeletePost(DeleteView):
    model = Articles
    success_url = '/news'
    template_name = 'news_delete.html'
