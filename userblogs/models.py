from django.db import models
from django.conf import settings
import uuid

class Blog(models.Model):
    blog_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    blogtime = models.CharField(max_length=50)
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Blog {self.blog_id} by {self.user}'

    class Meta:
        db_table = 'userblogs_blog' 
