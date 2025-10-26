from django.shortcuts import render , HttpResponse , get_list_or_404 , get_object_or_404
from portfolio.models import Project, Post  # <-- Naya import

# Create your views here.
def index(request):
    # Database se data fetch karna
    projects = Project.objects.all()  # Saare projects le aao
    posts = Post.objects.all()        # Saare posts le aao
    
    # Data ko template me bhejna
    context = {
        'projects': projects,
        'posts': posts,
    }
    return render(request, 'index.html', context) # <-- 'context' ko yahaan pass karo





# --- Blog ---

def blog_list(request):
    posts = Post.objects.all().order_by('-created_at') # Saare posts
    context = {
        'posts': posts,
    }
    return render(request, 'blog_list.html', context)

def blog_detail(request, post_id):
    post = get_object_or_404(Post, id=post_id) 
    context = {
        'post': post,
    }
    return render(request, 'blog_detail.html', context)

# --- Project ---

def project_list(request):
    projects = Project.objects.all().order_by('-created_at') # Saare projects
    context = {
        'projects': projects,
    }
    return render(request, 'project_list.html', context)

def project_detail(request, project_id):
    project = get_object_or_404(Project, id=project_id)
    context = {
        'project': project,
    }
    return render(request, 'project_detail.html', context)





#Both of these are stattic page
# ... baaki saare views ...

# Naya function (About Page)
def about(request):
    return render(request, 'about.html')

# ... baaki saare views ...

# Naya function (Contact Page)
def contact(request):
    return render(request, 'contact.html')


#Thank you page

# ... baaki saare views ...

# Naya function (Thank You Page)
def thank_you(request):
    return render(request, 'thank_you.html')