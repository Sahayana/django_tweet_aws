from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import TweetComment, TweetModel
from django.views.generic import ListView, TemplateView
# Create your views here.



@login_required
def home(request):
    tweets = TweetModel.objects.all().order_by('-created_at')
    context = {'tweets':tweets}    
    return render(request, 'tweet/home.html', context)


@login_required
def tweet(request):
    
    if request.method == 'POST':
        content = request.POST.get('my-content')
        tags = request.POST.get('tag', '').split(',')
        if content == '':
            msg = {'msg': '내용을 입력해주세요.'}
            return render(request, 'tweet/home.html', msg)

        tweet = TweetModel.objects.create(author=request.user, content=content)
        for tag in tags:
            tag = tag.strip()
            if tag != '':
                tweet.tags.add(tag)        
        tweet.save()
        return redirect('home')
    else:
        return redirect('home')

@login_required
def delete_tweet(request, id):
    tweet = get_object_or_404(TweetModel, id=id)
    tweet.delete()
    return redirect('home')



@login_required
def comment_create(request, tweet_id):

    tweet = get_object_or_404(TweetModel, id = tweet_id)    
    if request.method == 'POST':
        comment = TweetComment()
        comment.author = request.user
        comment.tweet = tweet
        comment.comment = request.POST.get('comment')
        comment.save()
        return redirect('home')
    else:
        return redirect('home')
        

@login_required
def comment_delete(request, id):
    comment = get_object_or_404(TweetComment, id=id)
    comment.delete()
    return redirect('home')


## Taggit

class TagCloudTV(TemplateView):
    template_name = 'taggit/tag_cloud_view.html'


class TaggedObjectLV(ListView):
    template_name = 'taggit/tag_with_post.html'
    model = TweetModel

    def get_queryset(self):
        return TweetModel.objects.filter(tags__name=self.kwargs.get('tag'))

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tagname'] = self.kwargs['tag']
        return context