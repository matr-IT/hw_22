from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Blogs
from .forms import BlogForm


class BlogsCreateView(CreateView):
    model = Blogs
    form_class = BlogForm
    template_name = 'blogs/blog_form.html'
    success_url = reverse_lazy('blogs:blogs_list')

class BlogsUpdateView(UpdateView):
    model = Blogs
    form_class = BlogForm
    template_name = 'blogs/blog_form.html'
    success_url = reverse_lazy('blogs:blogs_list')

class BlogsListView(ListView):
    model = Blogs
    template_name = 'blogs/blogs_list.html'
    context_object_name = 'blogs'

    def get_queryset(self):
        return Blogs.objects.filter(is_published=Blogs.PUBLISHED)


class BlogsDetailView(DetailView):
    model = Blogs
    template_name = 'blogs/blogs_detail.html'
    context_object_name = 'blog'

    def get(self, request, *args, **kwargs):
        self.object = self.get_object()

        self.object.views_count += 1
        self.object.save()

        context = self.get_context_data(object=self.object)
        return self.render_to_response(context)

class BlogsDeleteView(DeleteView):
    model = Blogs
    template_name = 'blogs/blog_confirm_delete.html'
    success_url = reverse_lazy('blogs:blogs_list')
    context_object_name = 'blog'


