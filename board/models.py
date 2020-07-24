from django.db import models


class Author(models.Model):

    """ Author Model Definition """

    # CharField는 반드시 max_length를 설정해줘야 한다.
    name = models.CharField(max_length=20)
    age = models.IntegerField(null=True, blank=True)
    gender = models.CharField(max_length=10, null=True, blank=True)

    def __str__(self):
        return self.name


class Post(models.Model):

    """ Post Model Definition """

    title = models.CharField(max_length=50)
    # author와 Post를 일대다 관계로 설정
    author = models.CharField(max_length=20)
    content = models.TextField(null=True)
    # 게시글을 만든 시간을 자동으로 찍어서 저장
    created_at = models.DateTimeField(auto_now_add=True)
    # 게시글이 업데이트 되는 시간을 자동으로 찍어서 저장
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
