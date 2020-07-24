from django.shortcuts import render, redirect
from django.urls import reverse
from . import models


def post_list(request):
    all_posts = models.Post.objects.all()
    return render(request, "home.html", {"posts": all_posts})


def post_detail(request, pk):
    post = models.Post.objects.get(pk=pk)
    return render(request, "post_detail.html", {"post": post})


def post_create(request):
    if request.method == "POST":
        title = request.POST.get("title", None)
        content = request.POST.get("content", None)
        author = request.POST.get("author", None)
        if title and content:
            post = models.Post.objects.create(
                title=title, content=content, author=author
            )
            return redirect(reverse("board:post_detail", kwargs={"pk": post.pk}))

    elif request.method == "GET":
        return render(request, "post_create.html")


def post_update(request, pk):
    post = models.Post.objects.get(pk=pk)
    if request.method == "POST":
        post.title = request.POST.get("title")
        post.author = request.POST.get("author")
        post.content = request.POST.get("content")

        post.save()
        return redirect(reverse("board:post_detail", kwargs={"pk": pk}))

    else:
        return render(request, "post_update.html", {"post": post})


def post_delete(request, pk):
    if request.method == "POST":
        post = models.Post.objects.get(pk=pk)
        post.delete()

    return redirect(reverse("board:post_list"))
