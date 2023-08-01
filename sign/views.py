from django.http import JsonResponse
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken

from .models import Info
from .serializer import Loginserializer, InfoSerializer
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

        return JsonResponse({
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


@api_view(['GET'])
def find_id(request):
    nickname = request.GET.get('nickname', None)
    print('ni', nickname)
    my_info = Info.objects.filter(nickname=nickname)
    return Response(my_info[0].user_id, status=status.HTTP_200_OK)

