from django.http import JsonResponse
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken

from .models import Info
from .serializer import Loginserializer
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


# @api_view(['GET', 'PUT', 'DELETE'])
# def user_auth(request, pk):
#     userId = request.GET.get('userId', None)
# except Info.DoesNotExist:
#     return Response(status=status.HTTP_404_NOT_FOUND)
# if request.method == 'GET':
#     serializer = InfoFindSerializer(info)
#     print(serializer)
#     return Response(serializer.data)
# elif request.method == 'DELETE':
#     info.delete()
#     return Response(status=status.HTTP_204_NO_CONTENT)
# elif request.method == 'PUT':
#     serializer = InfoSerializer(info, data=request.data)
#     if serializer. is_valid():
#         serializer.save()
#         return Response(serializer.data)
#     return Response(status=status.HTTP_400_BAD_REQUEST)
@api_view(['DELETE'])
def user_delete(request):
    try:
        userId = request.GET.get('user_id', None)
        info = Info.objects.get(user_id=userId)
    except Info.DoesNotExist:
        return Response(status=status.HTTP_400_BAD_REQUEST)
    info.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['PUT'])
def user_change(request):
    try:
        userId = request.GET.get('user_id', None)
        info = Info.objects.get(user_id=userId)
    except Info.DoesNotExist:
        return Response(status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def find_id(request):
    nickname = request.GET.get('nickname', None)
    my_info = Info.objects.filter(nickname=nickname)
    return Response(my_info[0].user_id, status=status.HTTP_200_OK)
