from django.shortcuts import render, redirect
from django.http import HttpResponse
from rest_framework import permissions, generics
from rest_framework.response import Response
from rest_framework import status, mixins, viewsets
from rest_framework.decorators import api_view
from django.contrib.auth import login
# from UserAccount.helper import CommonHelper
from UserAccount.models import User
from UserAccount.serializers import UserRegSerializer, UserLoginSerializer, UserChangePasswordSerializer
from django.shortcuts import get_object_or_404
from django.db.models import Q
import requests
import random
import re
import decimal
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.permissions import IsAuthenticated, AllowAny
from django.core.mail import send_mail
from django.contrib import auth
# from validate_email import validate_email
from email_validator import validate_email, EmailNotValidError
from django.conf import settings
from Events.models import Organizer, Participant, Event
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth import authenticate




regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'

# Create your views here.
class RegisterAPIview(APIView):
    '''Takes Email and Password and creates a new user only if otp was verified and mobile number is new'''

    def post(self, request, *args, **kwargs):

        password = request.data.get('password', False)
        email = request.data.get('email', False)
        mobile = request.data.get('mobile', False)
        first_name = request.data.get('first_name', False)
        last_name = request.data.get('last_name', False)
        role = request.data.get('role', False)
        gender = request.data.get('gender', False)

        check_email = User.objects.filter(email=email).first()


        try:
            # Validate & take the normalized form of the email
            # address for all logic beyond this point (especially
            # before going to a database query where equality
            # does not take into account normalization).
            email = validate_email(email).email
        except EmailNotValidError as e:
            # email is not valid, exception message is human-readable
            print(str(e))
            return Response("Email is not Valid!!", status=status.HTTP_400_BAD_REQUEST)

        errors = {}
        if not email:
            errors['email'] = ['This email is required']
        if len(email) < 10:
            errors['email'] = ['Email must be 10 char long or more']
        
        if (not mobile):
            errors['mobile'] = ['This email is required']
        if len(mobile) < 10:
            errors['mobile'] = ['Mobile Number must be 10 digit or more']
        if len(mobile) > 13:
            errors['mobile'] = ['Mobile Number must be less than 13 digit']

        if not first_name:
            errors['first_name'] = ['This email is required']
        if len(first_name) <= 2:
            errors['first_name'] = ['First Name must be 2 char long or more']
        if not last_name:
            errors['last_name'] = ['This email is required']
        if len(last_name) <= 2:
            errors['first_name'] = ['Last Name must be 2 char long or more']
        if errors:
            return Response({'error': True, 'errors': errors}, status=status.HTTP_400_BAD_REQUEST)

        elif check_email:
            context = {'message': "Hello!" + " " +
                       email + " " + "This Email already exists"}
            return Response({"status": False, "context": context}, status=status.HTTP_200_OK)

        UserRegSerializerData = UserRegSerializer(data=request.data)
        if UserRegSerializerData.is_valid():
            # tempPassword="Test@191"
            otp = str(random.randint(1234, 9999))
            tempPassword = first_name+"@"+otp
            user = User(email=email, first_name = first_name, last_name = last_name, mobile = mobile,  role = role, gender = gender)
            user.set_password(tempPassword)
            user.save()

            


            created_at = user.created_at
            updated_at = user.updated_at

            if user.role == "Admin":
                name = first_name + " " + last_name
                organizer = Organizer(user=user, name=name, contact_email=email, contact_number=mobile, created_at=created_at, )
                organizer.save()
            
            else:
                participant = Participant(user=user, first_name = first_name, last_name = last_name, email=email)
                participant.save()

            try:
                mailSubject="Welcome to Event!!!"
                mailMessage = "Hello "+first_name+"! Thanks for joining with us. Your username: "+email+" and your temporary password: "+tempPassword+" . Please Change your password and login to your account.| Team Event Management"
                mailFrom=settings.EMAIL_HOST_USER
                mailTo=[email]
                send_mail(mailSubject,mailMessage,mailFrom,mailTo,fail_silently=False)


                return Response({"status":"success","message":"Register success! Thanks for joining with us. Please Check your email for Username and Password. | Team Event Management"},status=200)
            except:
                return Response({"status":"success","message":"Register success!", "error":"Email send fail, Email temporary password: "+tempPassword},status=200)
                #return Response({"status":"success","message":"Registration success! Temporary password sent fail!!!"},status=200)
        
            
        else:
            return Response({"status":"warning","message":"Invalid inputes!","errors":UserRegSerializerData.errors}, status=400)    



        
class UserLoginAPIview(APIView):
    def get(self, request):
        return Response({"status": "success","message":"login api"},status=200)
    
    def post(self, request, *args, **kwargs):
        userLoginSerializer = UserLoginSerializer(data=request.data)
        if userLoginSerializer.is_valid():
            email = request.data.get('email', False)
            password = request.data.get('password', False)
            check_email = User.objects.filter(email=email).first()
            if check_email:
                user = authenticate(email=email, password=password)
                if user is not None:
                    refresh = RefreshToken.for_user(user)
                    return Response({
                        "status": "success",
                        "message":"login successful",
                        "data": {"access": str(refresh.access_token),"refresh": str(refresh)}
                        },status=200)
                else:
                   return Response({"status": "warning","message":"Invalid credentials"},status=401)
            else:
                return Response({"status": "warning","message":"Email does not exist!"},status=401)
            
        return Response({"status": "warning","message":"Invalid inputes!","errors":userLoginSerializer.errors},status=400)

        
class UserChangePasswordAPIview(APIView):

    permission_classes = [IsAuthenticated]

    def post(self, request):
        changePasswordSerializer = UserChangePasswordSerializer(data=request.data)
        if changePasswordSerializer.is_valid():
            if self.request.user.check_password(request.data["old_password"]):
                self.request.user.set_password(changePasswordSerializer.data.get("new_password"))
                self.request.user.save()
                return Response({"status": "success","message":"Password changed success"},status=200)
            return Response({"status": "warning","message":"Old password is incorrect!!"},status=401)
        return Response({"status": "warning","message":"Invalid inputes","errors":changePasswordSerializer.errors},status=400)



# Forgot Password with sending Password through Email.
class ForgotPasswordToEmail(APIView):

    def post(self, request, *args, **kwargs):

        email = request.data.get('email', False)
        userObj = User.objects.get(email=email)
        print(userObj)
        try:
            otp = str(random.randint(1000, 9999))
            tempPassword = userObj.first_name+"@"+otp
            
            
            try:
                user = userObj
                user.set_password(tempPassword)
                user.save()
            except User.DoesNotExist:
                return Response({"status": "warning", "message": "Opps! Profile doesn't Exist, please try again with valid email!!"}, status=401)
            
            # Send Otp on Email
            mailSubject = "Welcome to Event!!!"
            mailMessage = "Hello " + userObj.first_name + " " + userObj.last_name +  "! Thanks for joining with us. Your email: " + email + ". This is Your Otp for reset Password: " + tempPassword + " . Please reset the password and Enjoy Our Service. Thanks Again! Happy Business! Event Management Team."
            mailFrom = settings.EMAIL_HOST_USER
            mailTo = [email]
            otpResponse = send_mail(mailSubject, mailMessage, mailFrom, mailTo, fail_silently=False)

           

            if otpResponse == True:
                return Response({"status": "success", "message": "Password send on your registerd email successfully"}, status=200)
            else:
                return Response({"status": "warning", "message": "Opps! Password send fail, try again!!"}, status=200)

        except User.DoesNotExist:
            return Response({"status": "warning", "message": "email is Not Valid"}, status=status.HTTP_200_OK)