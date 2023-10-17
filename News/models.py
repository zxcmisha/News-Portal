from django.db import models
from django.contrib.auth.models import User
from django.db.models import Sum

# Create your models here.


class Author(models.Model):
    authorUser = models.OneToOneField(User, on_delete=models.CASCADE)
    rat_author = models.FloatField(default=0.0)

    def update_rating(self):
        postRat = self.post_set.aggregate(postRating=Sum('rat_post'))
        pRat = 0
        pRat += postRat.get('postRating')

        commentRat = self.authorUser.comment_set.aggregate(commentRating=Sum('rat_com'))
        cRat = 0
        cRat += commentRat.get('commentRating')

        self.rat_author = pRat * 3 + cRat
        self.save()


class Category(models.Model):
    name = models.CharField(max_length=255, unique = True)


class Post(models.Model):
    author = models.ForeignKey(Author, on_delete=models.CASCADE)

    NEWS = 'NW'
    ARTICLE = 'AR'
    CATEGORY_CHOICES = (
        (NEWS, 'Новость'),
        (ARTICLE, 'Статья')
    )

    choice = models.CharField(max_length=2, choices=CATEGORY_CHOICES, default=ARTICLE)
    create_post = models.DateTimeField(auto_now_add=True)
    postCategory = models.ManyToManyField(Category, through='PostCategory')
    head = models.CharField(max_length=128)
    text_post = models.TextField()
    rat_post = models.FloatField(default=0.0)

    def like(self):
        self.rat_post += 1
        self.save()

    def dislike(self):
        self.rat_post -= 1
        self.save()

    def preview(self):
        return self.text_post[0:123] + '...'


class PostCategory(models.Model):
    postThrough = models.ForeignKey(Post, on_delete=models.CASCADE)
    categoryThrough = models.ForeignKey(Category, on_delete=models.CASCADE)


class Comment(models.Model):
    com_post = models.ForeignKey(Post, on_delete=models.CASCADE)
    user_com = models.ForeignKey(User, on_delete=models.CASCADE)
    text_com = models.CharField(max_length=255)
    create_com = models.DateTimeField(auto_now_add=True)
    rat_com = models.FloatField(default=0.0)

    def like(self):
        self.rat_com += 1
        self.save()

    def dislike(self):
        self.rat_com -= 1
        self.save()
