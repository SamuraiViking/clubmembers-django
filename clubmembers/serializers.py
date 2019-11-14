from rest_framework import serializers
from .models import Post, ClubMember


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model=Post
        fields='__all__'

class ClubMemberSerializer(serializers.ModelSerializer):
    class Meta:
        model=ClubMember
        fields='__all__'
