from rest_framework import serializers
from .models import Post, ClubMember
from .getStudentDataWithEmail import getStudentDataWithEmail

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model=Post
        fields='__all__'

class ClubMemberSerializer(serializers.Serializer):
    email = serializers.EmailField(required=True)
    display_name = serializers.CharField(required=False)
    photo=serializers.URLField(required=False)

    def create(self, validated_data):
        student_data = getStudentDataWithEmail(validated_data['email'])
        validated_data['display_name'] = student_data['display_name']
        validated_data["photo"] = student_data['photo']
        return ClubMember.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        Update and return an existing `Snippet` instance, given the validated data.
        """
        instance.email = validated_data.get('email', instance.email)
        instance.display_name = validated_data.get('display_name', instance.display_name)
        instance.photo = validated_data.get('photo', instance.photo)
        instance.save()
        return instance
