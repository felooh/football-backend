from rest_framework import serializers
from .models import Post


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        db_table = 'Post'
        managed = True
        verbose_name = 'Post'
        verbose_name_plural = 'Posts'
        model = Post
        fields =  "__all__"
    