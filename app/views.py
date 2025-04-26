from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from app.models import BlogPost

from app.forms import BlogPostForm


# Create your views here.


def blog_list(request):
    posts = BlogPost.objects.filter(status="published").all().order_by("-created_at")
    return render(request, "app/blog_list.html", {"posts": posts})


def blog_detail(request, post_id):
    post = BlogPost.objects.filter(status="published").get(id=post_id)
    return render(request, "app/blog_detail.html", {"post": post})


@login_required  # restrict access to authenticated users only
def create_blog(request):
    if request.method == "POST":
        form = BlogPostForm(request.POST)
        if form.is_valid():
            title = form.cleaned_data["title"]
            content = form.cleaned_data["content"]
            status = form.cleaned_data["status"]

            print(title, content, status)

            # newblog = {"title": title, "content": content, "status": status}

            newpost = BlogPost(title=title, content=content, status=status, author=request.user)
            newpost.save()  # this actually saves the new post to DB

            # redirect to blog list page
            return redirect("blog_list")
    else:
        form = BlogPostForm()

    return render(request, "app/create_blog.html", {"form": form})


@login_required  # restrict access to authenticated users only
def update_blog(request, post_id):
    post = BlogPost.objects.get(id=post_id)

    if request.method == "POST":
        form = BlogPostForm(request.POST, initial={"title": post.title, "content": post.content, "status": post.status})
        if form.has_changed():
            print("Form has changed")
            print(form.changed_data)
            if form.is_valid():
                post.title = form.cleaned_data["title"]
                post.content = form.cleaned_data["content"]
                post.status = form.cleaned_data["status"]
                post.save()

                return redirect("blog_list")
        else:
            print("Form has not changed")
    else:
        form = BlogPostForm(initial={"title": post.title, "content": post.content, "status": post.status})

    return render(request, "app/update_blog.html", {"form": form, "post": post})


@login_required  # restrict access to authenticated users only
def delete_blog(request, post_id):
    post = BlogPost.objects.get(id=post_id)

    if request.method == "POST":
        post.delete()

        return redirect("blog_list")

    return render(request, "app/delete_blog.html", {"post": post})


def dashboard(request):
    posts = BlogPost.objects.filter(author=request.user).order_by("-created_at")
    return render(request, "account/dashboard.html", {"posts": posts})
