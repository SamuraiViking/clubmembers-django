from rest_framework import viewsets
from .serializers import PostSerializer, ClubMemberSerializer
from .models import Post, ClubMember

from rest_framework import mixins
from rest_framework import generics

class PostView(viewsets.ModelViewSet):
    serializer_class = PostSerializer
    queryset = Post.objects.all()



class ClubMemberList(mixins.ListModelMixin,
                  mixins.CreateModelMixin,
                  generics.GenericAPIView):

    queryset = ClubMember.objects.all()
    serializer_class = ClubMemberSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        request.POST._mutable = True
        request.POST['email'] = 'nelson67@stolaf.edu'
        request.POST['display_name'] = 'Kevin Nelson'
        request.POST['photo'] = 'https://stackoverflow.com/questions/18930234/django-modifying-the-request-object'
        print(request.POST)
        return self.create(request, *args, **kwargs)

class ClubMemberDetail(mixins.RetrieveModelMixin,
                       mixins.UpdateModelMixin,
                       mixins.DestroyModelMixin,
                       generics.GenericAPIView):

    queryset = ClubMember.objects.all()
    serializer_class = ClubMemberSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)