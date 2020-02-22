from django.contrib.auth import REDIRECT_FIELD_NAME, login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy, reverse
from django.views import generic
from django.views.generic import CreateView

from blog.forms import CommentForm
from blog.models import Article, Comment


class IndexView(generic.ListView):
    template_name = 'index.html'
    context_object_name = 'latest_articles_list'

    def get_queryset(self):
        """Return the last five published questions."""
        return Article.objects.order_by('-pub_date')[:5]


class ArticleView(generic.DetailView):
    model = Article
    template_name = 'article.html'


class NewComment(LoginRequiredMixin, CreateView):
    form_class = CommentForm
    template_name = 'new_comment_form.html'
    login_url = reverse_lazy('blog:login')
    redirect_field_name = REDIRECT_FIELD_NAME

    def form_valid(self, form):
        form.instance.article = get_object_or_404(Article, *self.args, **self.kwargs)
        return super(NewComment, self).form_valid(form)


class SignUp(CreateView):
    form_class = UserCreationForm
    template_name = 'registration/signup.html'
    success_url = reverse_lazy('blog:index')

    def form_valid(self, form):
        res = super(SignUp, self).form_valid(form)
        login(self.request, self.object)
        return res











