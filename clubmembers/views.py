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

        print(request.data)

        # student_email = request.POST['email']
        # student_data = getStudentDataWithEmail(student_email)


        # request.POST['display_name'] = student_data['display_name']
        # request.POST['photo'] = student_data['photo']

        # request.POST._mutable = True
        # request.POST = request.POST.copy()

        # request.POST['email'] = 'nelson67@stolaf.edu'
        # request.POST['display_name'] = "Kevin Nelson"
        # request.POST['photo'] = "https://www.stolaf.edu/stofaces/face.cfm?username=nelson67&v=E3B0C44&fullsize"

        # print(request.POST)

        return self.create(request, *args, **kwargs)

class ClubMemberDetail(generics.RetrieveUpdateDestroyAPIView):

    queryset = ClubMember.objects.all()
    serializer_class = ClubMemberSerializer