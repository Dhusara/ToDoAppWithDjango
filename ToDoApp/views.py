from django.shortcuts import render, redirect
from .models import Post
from .forms import PostForm
from django.contrib import messages

def index(request):
    if request.method == 'POST':
        form = PostForm(request.POST or None)

        if form.is_valid():
            form.save()
            all_items = Post.objects.all
            messages.success(request, (""))
            return render(request, 'index.html', {'all_items': all_items})

    else:
        all_items = Post.objects.all
        return render(request, 'index.html', {'all_items': all_items})

def delete(request, list_id):
    item = Post.objects.get(pk=list_id)
    item.delete()
    messages.success(request, (''))
    return redirect('index')
