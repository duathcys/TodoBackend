from django.contrib.auth.hashers import check_password, make_password
from django.http import JsonResponse
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken

from .models import Info
from .serializer import Loginserializer, InfoSerializer, InfoFindSerializer
from .serializer import SignUpserializer


@api_view(['POST'])
def user_login(request):
    serializer = Loginserializer(data=request.data)
    print(serializer.is_valid())
    if serializer.is_valid(raise_exception=True):
        user_id = serializer.validated_data['user_id']
        user_pw = serializer.validated_data['user_pw']
        access = serializer.validated_data['access']
        refresh = serializer.validated_data['refresh']
        nickname = serializer.validated_data['nickname']

        return JsonResponse({
            'nickname': nickname,
            'user_id': user_id,
            'user_pw': user_pw,
            'access': access,
            'refresh': refresh,
            'error': 'rr'
        })


@api_view(['POST'])
def user_signUp(request):
    serializer = SignUpserializer(data=request.data)
    print('request', request.data)
    print(serializer)
    if serializer.is_valid(raise_exception=True):
        user = serializer.save(request)
        print(user, "www")
        _user = str(user.id)
        print(_user)

        token = RefreshToken.for_user(user)
        print(token)
        refresh = str(token)
        print(refresh)
        access = str(token.access_token)
        print(access)

        return JsonResponse({
            'user': _user,
            'access': access,
            'refresh': refresh
        })
    else:
        return Response(status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def user_auth(request):
    try:
        userId = request.GET.get('user_id', None)
        info = Info.objects.get(user_id=userId)
        print(info)
    except Info.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        serializer = InfoFindSerializer(info)
        print(serializer)
        return Response(serializer.data)
    elif request.method == 'DELETE':
        info.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    elif request.method == 'PUT':
        userPw = request.data.get('user_pw')
        new_password = request.data.get('new_pw')
        new_nickname = request.data.get('nickname')
        print(new_password)
        print(new_nickname)
        if check_password(userPw, info.user_pw):
            print('kdk')
            print(new_password)
            if new_password:
                info.user_pw = make_password(new_password)
                info.nickname = new_nickname
            else:
                info.nickname = new_nickname
            info.save()
            serializer = SignUpserializer(info)
            print(serializer.data)
            return Response(serializer.data)
        else:
            return Response("현재 비밀번호가 일치하지 않습니다.", status=status.HTTP_400_BAD_REQUEST)
    return Response(status=status.HTTP_400_BAD_REQUEST)


@api_view(['PUT'])
def user_change(request):
    try:
        userId = request.GET.get('user_id', None)
        print(userId)
        info = Info.objects.get(user_id=userId)
        print(info)
    except Info.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    serializer = SignUpserializer(info, data=request.data)
    print('request', request.data)
    print(serializer)
    if serializer.is_valid():
        print("valid")
        serializer.save()
        # _user = str(user.id)
        #
        # token = RefreshToken.for_user(user)
        # print(token)
        # refresh = str(token)
        # print(refresh)
        # access = str(token.access_token)
        # print(access)

        # return JsonResponse({
        #     'user': _user,
        #     'access': access,
        #     'refresh': refresh
        # })
        return Response(serializer.data, status=status.HTTP_200_OK)
    else:
        return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def find_id(request):
    nickname = request.GET.get('nickname', None)
    my_info = Info.objects.filter(nickname=nickname)
    return Response(my_info[0].user_id, status=status.HTTP_200_OK)
