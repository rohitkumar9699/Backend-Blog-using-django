
from django.http import JsonResponse
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from userblogs.models import Blog
from rest_framework.exceptions import AuthenticationFailed

class AddBlogView(APIView):
    permission_classes = [IsAuthenticated]  # Ensures that the user must be authenticated

    def post(self, request):
        # Extract username from the request's access token
        user = request.user  # This is the user associated with the JWT token

        if not user:
            raise AuthenticationFailed('Invalid token')

        blogtime = request.data.get('blogtime')
        content = request.data.get('content')

        if not blogtime or not content:
            return Response({"error": "blogtime and content are required"}, status=400)

        # Create and save the new blog post
        blog = Blog.objects.create(user=user, blogtime=blogtime, content=content)

        return Response({
            "message": "Blog created successfully",
            "blog_id": str(blog.blog_id),
            "username": user.username
        }, status=201)



class ViewBlogView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        user = request.user

        if user.is_superuser:
            blogs = Blog.objects.all()
        else:
            blogs = Blog.objects.filter(user=user)

        blog_list = [{
            'blog_id': str(blog.blog_id),
            'username': blog.user.username,
            'blogtime': blog.blogtime,
            'content': blog.content,
            'timestamp': blog.timestamp
        } for blog in blogs]

        return Response(blog_list)
