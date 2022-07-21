from random import choices
from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.contrib import messages
from posts.models import Post, Author
from posts.forms import PostForm, AuthorForm


""" def posts_list(request):
    posts = Post.objects.all()
    return render(
        request=request,
        template_name="posts/list.html",
        context={"posts": posts}
    ) """

def posts_details(request, id):
    post = Post.objects.get(id=id)
    author = Author.objects.get(id=post.author_id_id)
    return render(
        request=request,
        template_name="posts/details.html",
        context={"post": post, "author": author}
    )

def posts_list(request):
    if request.method == "POST":
        form = PostForm(data=request.POST)
        print(f'*******{form}')
        if form.is_valid():
            Post.objects.get_or_create(**form.cleaned_data)
            messages.add_message(
                request,
                messages.SUCCESS,
                "New post created!!"
           )
        else:
            messages.add_message(
                request,
                messages.ERROR,
                form.errors['__all__']
            )

    form = PostForm()
    posts = Post.objects.all()
    return render(
        request=request,
        template_name="posts/list.html",
        context={
            "posts": posts,
            "form": form
        }    
        )


def author_details(request, id):
    author = Author.objects.get(id=id)
    return render(
        request=request,
        template_name="posts/author_details.html",
        context={"author": author}
    )

def authors_list(request):
    if request.method == "POST":
        form = AuthorForm(data=request.POST)
        print(f'*******{form}')
        if form.is_valid():
            Author.objects.get_or_create(**form.cleaned_data)
            messages.add_message(
                request,
                messages.SUCCESS,
                "New Author created!!"
           )
        else:
            messages.add_message(
                request,
                messages.ERROR,
                form.errors['__all__']
            )

    form = AuthorForm()
    authors = Author.objects.all()
    return render(
        request=request,
        template_name="posts/authors_list.html",
        context={
            "authors": authors,
            "form": form
        }    
        )