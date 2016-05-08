# posts/api.py
from django.contrib.auth.models import User

from restless.dj import DjangoResource
from restless.preparers import FieldsPreparer

from posts.models import Post


class PostResource(DjangoResource):
    # Controls what data is included in the serialized output.
    preparer = FieldsPreparer(fields={
        'id': 'id',
        'title': 'title',
        'author': 'user.username',
        'body': 'content',
        'posted_on': 'posted_on',
    })

    # GET /
    def list(self):
        return Post.objects.all()

    # GET /pk/
    def detail(self, pk):
        return Post.objects.get(id=pk)

    # POST /
    def create(self):
        return Post.objects.create(
            title=self.data['title'],
            user=User.objects.get(username=self.data['author']),
            content=self.data['body']
        )

    # PUT /pk/
    def update(self, pk):
        try:
            post = Post.objects.get(id=pk)
        except Post.DoesNotExist:
            post = Post()

        post.title = self.data['title']
        post.user = User.objects.get(username=self.data['author'])
        post.content = self.data['body']
        post.save()
        return post

    # DELETE /pk/
    def delete(self, pk):
        Post.objects.get(id=pk).delete()