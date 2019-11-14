from rest_framework import viewsets
from .serializers import PostSerializer, ClubMemberSerializer
from .models import Post, ClubMember


from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser

class PostView(viewsets.ModelViewSet):
    serializer_class = PostSerializer
    queryset = Post.objects.all()

@csrf_exempt
def club_members_list(request):
    if request.method == 'GET':
        club_members = ClubMember.objects.all()
        serializer = ClubMemberSerializer(club_members, many=True)
        return JsonResponse(serializer.data, safe=False)
    
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = ClubMemberSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)

@csrf_exempt
def club_member_detail(request, pk):
    try:
        club_member = ClubMember.objects.get(pk=pk)
    except ClubMember.DoesNotExist:
        return HttpResponse(status=404)
    
    if request.method == 'GET':
        serializer = ClubMemberSerializer(club_member)
        return JsonResponse(serializer.data)
    
    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = ClubMemberSerializer(club_member, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)
    
    elif request.method == 'DELETE':
        club_member.delete()
        return HttpResponse(status=204)

