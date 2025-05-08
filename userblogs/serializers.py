from rest_framework import serializers
from .models import Blog

class BlogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Blog
        fields = ['blog_id', 'username', 'blogtime', 'content', 'timestamp']
        read_only_fields = ['blog_id', 'username', 'timestamp']
