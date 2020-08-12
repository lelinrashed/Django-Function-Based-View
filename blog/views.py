from blog.forms import PostModelForm
from blog.models import PostModel
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.http import Http404, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404


# @login_required
def post_model_create_view(request):
    # if request.method == "POST":
    #     # print(request.POST)
    #     form = PostModelForm(request.POST)
    #     if form.is_valid():
    #         form.save(commit=False)
    #         print(form.cleaned_data)

    form_a = PostModelForm(request.POST or None)
    context = {
        "form": form_a
    }
    if form_a.is_valid():
        obj = form_a.save(commit=False)
        obj.save()
        messages.success(request, "Created a new blog post!")
        context = {
            "form": PostModelForm()
        }
        # return HttpResponseRedirect("/blog/")
        # return HttpResponseRedirect("/blog/{id}".format(id=obj.id))

    template = "blog/create-view.html"
    return render(request, template, context)


# @login_required
def post_model_update_view(request, id=None):
    obj = get_object_or_404(PostModel, id=id)
    form_a = PostModelForm(request.POST or None, instance=obj)
    context = {
        "form": form_a,
    }
    if form_a.is_valid():
        obj = form_a.save(commit=False)
        obj.save()
        messages.success(request, "Updated blog post!")
        # return HttpResponseRedirect("/blog/")
        return HttpResponseRedirect("/blog/{id}".format(id=obj.id))

    template = "blog/update-view.html"
    return render(request, template, context)


def post_model_detail_view(request, id):
    obj = get_object_or_404(PostModel, id=id)
    context = {
        "object": obj
    }
    template = "blog/detail-view.html"
    return render(request, template, context)


def post_model_delete_view(request, id):
    obj = get_object_or_404(PostModel, id=id)
    if request.method == "POST":
        obj.delete()
        messages.success(request, "Blog post deleted successfully!")
        return HttpResponseRedirect("/blog/")
    context = {
        "object": obj
    }
    template = "blog/delete-view.html"
    return render(request, template, context)


def post_model_list_view(request):
    query = request.GET.get("q", None)
    qs = PostModel.objects.all()
    if query is not None:
        qs = qs.filter(
            Q(title__icontains=query) |
            Q(content__icontains=query) |
            Q(slug__icontains=query)
        )
    context = {
        "object_list": qs
    }
    template = "blog/list-view.html"
    return render(request, template, context)


@login_required
def login_required_view(request):
    print(request.user)
    qs = PostModel.objects.all()
    context = {
        "object_list": qs
    }
    if request.user.is_authenticated:
        template = "blog/list-view.html"
    else:
        template = "blog/list-view-public.html"
        # raise Http404
        return HttpResponseRedirect("/login/")

    return render(request, template, context)
