from django.http import JsonResponse
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken

from .serializer import Loginserializer
from .serializer import SignUpserializer


@api_view(['GET', 'POST'])
def user_login(request):
    # if request.method=='GET':
    #     infos = Info.objects.all()
    #     serializer = Loginserializer(infos, many = True)
    #     return Response(serializer.data)
    # if request.method=='POST':
    serializer = Loginserializer(data=request.data)
    print(serializer.is_valid())
    if serializer.is_valid(raise_exception=True):
        user_id = serializer.validated_data['user_id']
        user_pw = serializer.validated_data['user_pw']
        access = serializer.validated_data['access']
        refresh = serializer.validated_data['refresh']

        return JsonResponse({
            'user_id': user_id,
            'user_pw': user_pw,
            'access': access,
            'refresh': refresh,
            'error': 'rr'
        })
        # return Response(status=status.HTTP_200_OK, data=data)
    # else:
    #     return Response(status=status.HTTP_200_OK)

    # return Response(status=status.HTTP_400_BAD_REQUEST)
    # if request.method =='GET':
    #     infos = Info.objects.all()
    #     serializer = Infoserializer(infos, many = True)
    #     return Response(serializer.data)
    # elif request.method=='POST':
    #     serializer = Infoserializer(data=request.data)
    #     print(request.data)
    #     print(serializer)
    #     if serializer.is_valid():
    #         serializer.save()
    #         print(serializer)
    #         return Response(serializer.data, status=status.HTTP_201_CREATED)
    #     return Response(status=status.HTTP_400_BAD_REQUEST)


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
