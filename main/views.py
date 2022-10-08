from django.shortcuts import render, HttpResponse, get_object_or_404, HttpResponseRedirect
from .models import Story
 
# relative import of forms
from .models import Blog
from .templates.blogs.forms import BlogForm
 

def homeView(request):
    stories = Story.objects.all()
    return render(request, 'index.html', {'stories': stories})


    # data = {
    #     "title": "Sherdooni",
    #     "users": [
    #         {
    #             "id": 1,
    #             "name": "Safa",
    #             "email": "safa@gmail.com",
    #         },
    #         {
    #             "id": 2,
    #             "name": "Vafa",
    #             "email": "vafa@gmail.com",
    #         },
    #         {
    #             "id": 3,
    #             "name": "Sahba",
    #             "email": "sahba@gmail.com",
    #         }
    #     ]
    # }

    # return render(request, 'main/index.html', data)


def indexView(request):
    return render(request, 'main/index.html')
    return HttpResponse('<center>..:: Main Page ::..</center>')

    
def blogListView(request):
    # lists = Blog.objects.all()
    # return render(request, 'blogs/list.html', {'lists': lists})
    context ={}
    context["dataset"] = Blog.objects.all()
    return render(request, "blogs/list.html", context)



def blogCreate(request):
    # dictionary for initial data with
    # field names as keys
    context ={}
 
    # add the dictionary during initialization
    form = BlogForm(request.POST or None)
    if form.is_valid():
        form.save()
         
    context['form']= form
    return render(request, "blogs/create.html", context)

def blogDetail(request, id):
    # dictionary for initial data with
    # field names as keys
    context ={}
 
    # add the dictionary during initialization
    context["data"] = Blog.objects.get(id = id)
         
    return render(request, "blogs/single.html", context)

# update view for details
def blogUpdate(request, id):
    # dictionary for initial data with
    # field names as keys
    context ={}
 
    # fetch the object related to passed id
    obj = get_object_or_404(Blog, id = id)
 
    # pass the object as instance in form
    form = BlogForm(request.POST or None, instance = obj)
 
    # save the data from the form and
    # redirect to detail_view
    if form.is_valid():
        form.save()
        return HttpResponseRedirect("/blog/"+id)
 
    # add form dictionary to context
    context["form"] = form
 
    return render(request, "blogs/update.html", context)


# delete view for details
def blogDelete(request, id):
    # dictionary for initial data with
    # field names as keys
    context ={}
 
    # fetch the object related to passed id
    obj = get_object_or_404(Blog, id = id)
 
 
    if request.method =="POST":
        # delete object
        obj.delete()
        # after deleting redirect to
        # home page
        return HttpResponseRedirect("/blog/")
 
    return render(request, "blogs/delete.html", context)
