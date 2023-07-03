import json

from rest_framework import serializers
from rest_framework_simplejwt.tokens import RefreshToken
from .models import Info

class Loginserializer(serializers.ModelSerializer):
    user_id = serializers.CharField(
        required=True,
        write_only=True,
    )
    user_pw = serializers.CharField(
        required=True,
        write_only=True,
        style={'input_type':'password'}
    )
    class Meta:
        model = Info
        fields = '__all__'
        
    def validate(self, data):
        id = data.get('user_id', None)
        pw = data.get('user_pw', None)

        if Info.objects.filter(user_id=id).exists():
            user_id = Info.objects.get(user_id=id).user_id
            user_pw = Info.objects.get(user_id=id).user_pw
            if user_pw==pw:
                user = Info.objects.get(user_id=id)
            else:
                error_msg = '비밀번호가 올바르지 않습니다'
                raise serializers.ValidationError(error_msg)
        else:
            error_msg = "계정이 존재하지 않습니다"
            raise serializers.ValidationError(error_msg)


        token = RefreshToken.for_user(user)
        print('token', token)
        refresh = str(token)
        print('refresh', refresh)
        access=str(token.access_token)
        print('access', access)

        data={
            'user_id':user_id,
            'user_pw':user_pw,
            'refresh':refresh,
            'access':access,
            # 'error':'rr'
        }
        print(data)
        return data





class SignUpserializer(serializers.ModelSerializer):
    user_id = serializers.CharField(
        required=True,
        write_only=True,
    )
    user_pw = serializers.CharField(
        required=True,
        write_only=True,
        style={'input_type':'password'}
    )
    nickname = serializers.CharField(
        required=True,
    )

    class Meta:
        model = Info
        fields = '__all__'

    def save(self, request):
        user = super().save()
        user.user_id = self.validated_data['user_id']
        user.user_pw = self.validated_data['user_pw']
        print(user.user_id)
        print(user.user_pw)
        user.save()
        print(Info)
        print(user.user_id)
        return user

    def validate(self, data):
        user_id = data.get('user_id', None)
        user_pw = data.get('user_pw', None)
        nickname = data.get('nickname', None)
        print('id', user_id)
        if Info.objects.filter(user_id=user_id).exists():
            raise serializers.ValidationError('사용할 수 없는 ID입니다.')
        if Info.objects.filter(nickname=nickname).exists():
            raise serializers.ValidationError('사용할 수 없는 이름입니다.')
        return data


class InfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Info
        fields = '__all__'