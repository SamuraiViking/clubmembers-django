from rest_framework import viewsets
from .serializers import PostSerializer, ClubMemberSerializer
from .models import Post, ClubMember

from rest_framework import mixins
from rest_framework import generics

from .getStudentDataWithEmail import getStudentDataWithEmail

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

        email = request.POST['email']

        student_data = getStudentDataWithEmail(email)

        request.POST['display_name'] = student_data['display_name']
        request.POST['photo'] = student_data['photo']

        return self.create(request, *args, **kwargs)

class ClubMemberDetail(generics.RetrieveUpdateDestroyAPIView):

    queryset = ClubMember.objects.all()
    serializer_class = ClubMemberSerializer