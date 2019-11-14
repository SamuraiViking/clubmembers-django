from rest_framework import viewsets
from .serializers import PostSerializer, ClubMemberSerializer
from .models import Post, ClubMember

class PostView(viewsets.ModelViewSet):
    serializer_class = PostSerializer
    queryset = Post.objects.all()

class ClubMemberView(viewsets.ModelViewSet):
    serializer_class = ClubMemberSerializer
    queryset = ClubMember.objects.all()

