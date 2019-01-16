from django.shortcuts import render
from blog.models import BlogPost

def blog_post_search(request):
	posts = BlogPost.objects.all()
	query = request.GET.get('q')
	if query:
		quesryset_list = posts.filter(title__icontain=query)
		return render(request, 'blog/index.html')



