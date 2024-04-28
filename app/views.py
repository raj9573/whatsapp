from django.shortcuts import render

# Create your views here.


from app.models import *

from rest_framework.response import Response

from app.serializers import *

from rest_framework.views import APIView

from django.db.models import Q

class DisplayFriends(APIView):
    def get(self,request,user_id):

        UO = user.objects.get(id = user_id)

        all_friends =  friends.objects.filter(Q(current_user=UO))
    
        serializer = friendsserializer(all_friends,many=True,context = {'request':request}).data

        return Response(serializer)

class DisplayMessages(APIView):
    def get(self,request,currentuser,otheruser):
        sender = user.objects.get(id =  currentuser)
        receiver = user.objects.get(id = otheruser) 
        messages_object = messages.objects.filter(Q(sender=sender,receiver=receiver)|Q(sender=receiver,receiver=sender)).order_by('created_at')

        serializer = messagesserializer(messages_object,many=True,context={'request':request}).data
    
        return Response(serializer)

    def post(self,request,currentuser,otheruser):
        message = request.data.get('message')
        sender  = user.objects.get(id=currentuser)
        receiver = user.objects.get(id=otheruser)
        messages.objects.create(sender=sender,receiver=receiver,message=message)
        return Response("Message sent succesfully")
        

class UserLogin(APIView):
    def post(self,request):

        username = request.data.get('username')
        password = request.data.get('password')

        if user.objects.filter(name=username,password=password).exists():
            UO = user.objects.get(name = username)
            serializer = userserializer(UO,context={'request':request}).data
            return Response(serializer)
        else:
            return Response(False)


class UserDetails(APIView):
    def get(self,request,user_id):
        UO = user.objects.get(id = user_id)

        serializer = userserializer(UO,context={'request':request}).data    
        
        return Response(serializer)
    
    def post(self,request,user_id):
        UO = user.objects.get(id = user_id)

        data = request.data
        print(data)
        serializer = userserializer(UO,data=data,partial=True,context={'request':request})
        if serializer.is_valid():
            serializer.save()
            return Response("data updated successfully")
        else:
            print(serializer.errors)
            return Response(serializer.errors)

class ChangePassword(APIView):
    def post(self,request,user_id):
        try:

            user_obj =  user.objects.get(id=user_id)
            user_obj.password=request.data.get('password')
            user_obj.save()

            # print(request.data)
            return Response("Hello")
        except Exception as e:
            print(e)
            return Response(e)

class BlockUserView(APIView):
    def post(self,request,user_id,cuser):
        BUO =  user.objects.get(id= user_id)
        UO =  user.objects.get(id= cuser)
        if BlockUser.objects.filter(blocking_user=UO,blocked_user=BUO).exists():
            return Response("ALready Blocked")
        else:

            BlockUser.objects.create(blocking_user=UO,blocked_user=BUO)

            return Response("Blocked Successfully")