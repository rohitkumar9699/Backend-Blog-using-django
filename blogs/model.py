# from django.db import models
# import uuid

# class Blog(models.Model):
#     blog_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
#     blogtime = models.DateTimeField()
#     content = models.TextField()
#     timestamp = models.DateTimeField(auto_now_add=True)

#     def __str__(self):
#         return f"Blog {self.blog_id} at {self.blogtime}"
