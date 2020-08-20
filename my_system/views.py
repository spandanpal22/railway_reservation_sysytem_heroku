from django.shortcuts import render, redirect, HttpResponse

from .models import Suggestion, UserRegistration, Train_Data, Ticket, Complaint

from django.contrib import messages
from django.http import HttpResponse

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.views.generic import View
from .forms import UserForm

from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from .serializers import TicketSerializer

import os
import requests
import json


@login_required(login_url='/signin')
def bookTicketsUser(request):
    username = request.user.username

    f=0

    url = "http://spandan-project.herokuapp.com/api"
    response = requests.request("GET", url)
    response = json.loads(response.text)
    t = {}
    for resp in response:
        t = resp
    ticket_no = int(t['ticket_no']) + 1
    tid = int(t['id']) + 1

    if request.method == 'POST':
        data = {}
        data['id'] = tid
        data['name'] = username
        data['address'] = request.POST.get('address')
        data['mobileNo'] = request.POST.get('mobileNo')
        data['email'] = request.POST.get('email')
        data['dob'] = request.POST.get('dob')
        data['from_station'] = request.POST.get('from_station')
        data['to_station'] = request.POST.get('to_station')
        data['doj'] = request.POST.get('doj')
        data['ticket_no'] = ticket_no
        data['train_no'] = request.POST.get('train_no')
        data['train_name'] = request.POST.get('train_name')
        response = requests.post(url, data)
        f=1

    return render(request, 'my_system/my_user/book_tickets_user.html',
                  {'username': username, 'tid': tid, 'ticket_no':ticket_no,'f':f})


@login_required(login_url='/signin')
def cancelTicketsUser(request):
    username = request.user.username
    if request.method == 'POST':
        url = "http://spandan-project.herokuapp.com/api"
        response = requests.request("GET", url)
        response = json.loads(response.text)
        arr = []
        arr2 = []
        f = 1
        for resp in response:
            if resp['name'] == username:
                arr.append(resp)
        for i in arr:
            arr2.append(i['id'])

        ticket_id_r = int(request.POST.get('tid'))

        if ticket_id_r in arr2:
            url = "http://spandan-project.herokuapp.com/api/{0}".format(ticket_id_r)
            response = requests.request("DELETE", url)
            print(response)
        else:
            f = 0
        return render(request, 'my_system/my_user/cancel_tickets_user.html', {'username': username, 'f': f})

    return render(request, 'my_system/my_user/cancel_tickets_user.html', {'username': username})


@login_required(login_url='/signin')
def viewTicketsUser(request):
    username = request.user.username
    url = "http://spandan-project.herokuapp.com/api"
    response = requests.request("GET", url)
    response = json.loads(response.text)
    arr = []
    f = 0
    for resp in response:
        if resp['name'] == username:
            arr.append(resp)
            f = 1
    return render(request, 'my_system/my_user/view_tickets_user.html', {'username': username, 'arr': arr, 'f': f})


@login_required(login_url='/signin')
def complaintsUser(request):
    username = request.user.username
    c_flag = 0
    if request.method == 'POST':
        print("##")
        username_r = username
        train_no_r = request.POST.get('trainNumber')
        ticket_no_r = request.POST.get('ticketNumber')
        doj_r = request.POST.get('doj')
        boarding_station_r = request.POST.get('boardingStation')
        destination_station_r = request.POST.get('destinationStation')
        complaint_r = request.POST.get('complaint')

        c = Complaint(username=username_r, train_no=train_no_r, ticket_no=ticket_no_r, doj=doj_r,
                      boarding_station=boarding_station_r,
                      destination_station=destination_station_r, complaint=complaint_r)
        c.save()

        c_flag = 1

        return render(request, 'my_system/my_user/complaints_user.html', {'c_flag': c_flag, 'username': username})
    return render(request, 'my_system/my_user/complaints_user.html', {'username': username})


@login_required(login_url='/signin')
def foreignHolidayUser(request):
    username = request.user.username
    return render(request, 'my_system/my_user/holiday_foreign_user.html', {'username': username})


@login_required(login_url='/signin')
def indiaHolidayUser(request):
    username = request.user.username
    return render(request, 'my_system/my_user/holiday_india_user.html', {'username': username})


@login_required(login_url='/signin')
def indexUser(request):
    username = request.user.username
    return render(request, 'my_system/my_user/index_user.html', {'username': username})


@login_required(login_url='/signin')
def suggestUser(request):
    username = request.user.username
    flag = 0
    if request.method == 'POST':
        name_r = username
        email_r = request.POST.get('Email')
        suggestion_r = request.POST.get('Suggestion')

        s = Suggestion(name=name_r, email=email_r, suggestion=suggestion_r)
        s.save()

        flag = 1

        return render(request, 'my_system/my_user/index_user.html', {'flag': flag, 'username': username})
    else:
        return render(request, 'my_system/my_user/index_user.html', {'flag': flag, 'username': username})


@login_required(login_url='/signin')
def animations(request):
    username = request.user.username
    return render(request, 'my_system/animations.html', {'username': username})


@login_required(login_url='/signin')
def profile(request):
    username = request.user.username
    if request.method == 'GET':
        all_data = UserRegistration.objects.all()
        for users in all_data:
            if username == users.username:
                fn = users.firstName
                ln = users.lastName
                add = users.address
                gen = users.gender
                dob = users.dob
                em = users.email
                mn = users.mobileNumber
                occ = users.occupation

                return render(request, 'my_system/my_user/my_profile.html',
                              {'username': username, 'fn': fn, 'ln': ln, 'add': add, 'gen': gen, 'dob': dob, 'em': em,
                               'mn': mn, 'occ': occ})

    return render(request, 'my_system/my_user/my_profile.html', {'username': username})


def index(request):
    return render(request, 'my_system/index.html')


def signin(request):
    return render(request, 'my_system/signin.html')


def signup(request):
    return render(request, 'my_system/signup.html')


def suggest(request):
    flag = 0
    if request.method == 'POST':
        name_r = request.POST.get('Name')
        email_r = request.POST.get('Email')
        suggestion_r = request.POST.get('Suggestion')

        s = Suggestion(name=name_r, email=email_r, suggestion=suggestion_r)
        s.save()

        flag = 1

        return render(request, 'my_system/index.html', {'flag': flag})
    else:
        return render(request, 'my_system/index.html', {'flag': flag})


class UserFormView(View):
    form_class = UserForm
    template_name = 'my_system/signup.html'

    def get(self, request):
        form = self.form_class(None)
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = self.form_class(request.POST)
        flag_userReg = 0

        if form.is_valid():
            firstName_r = request.POST.get('firstName')
            lastName_r = request.POST.get('lastName')
            username_r = request.POST.get('username')
            address_r = request.POST.get('address')
            gender_r = request.POST.get('gender')
            dob_r = request.POST.get('dob')
            email_r = request.POST.get('email')
            mobileNumber_r = request.POST.get('mobileNumber')
            occupation_r = request.POST.get('occupation')
            ur = UserRegistration(firstName=firstName_r, lastName=lastName_r, username=username_r, address=address_r,
                                  gender=gender_r, dob=dob_r, email=email_r, mobileNumber=mobileNumber_r,
                                  occupation=occupation_r)
            ur.save()

            user = form.save(
                commit=False)  # this will save the entered data in user object but won't save in database

            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            user.set_password(password)

            user.save()

            flag_userReg = 1
            return render(request, 'my_system/signup.html', {'flag_userReg': flag_userReg})

        return render(request, self.template_name, {'form': form, 'flag_userReg': flag_userReg})


class SignInFormView(View):
    form_class = UserForm
    template_name = 'my_system/signin.html'

    def get(self, request):
        form = self.form_class(None)
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = self.form_class(request.POST)
        flag_userSignIn = 0

        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            flag_userSignIn = 1
            return render(request, 'my_system/my_user/index_user.html',
                          {'flag_userSignIn': flag_userSignIn, 'username': username})

        return render(request, self.template_name, {'form': form, 'flag_userSignIn': flag_userSignIn})


def signout(request):
    logout(request)
    return render(request, 'my_system/index.html')


@login_required(login_url='/signin')
def searchTrainsUser(request):
    username = request.user.username
    if request.method == 'POST':
        from_r = request.POST.get('from')
        from_r = from_r.lower()
        to_r = request.POST.get('to')
        to_r = to_r.lower()
        req_t = {}
        all_trains = Train_Data.objects.all()

        c = 0
        arr = []
        req_t['trains'] = arr
        req_t['flag'] = 3
        for train in all_trains:
            flag_to = 0
            flag_from = 0
            train_no = train.trainNumber

            filename = '{0}.txt'.format(train_no)

            ts = os.path.join('uploads/train_stoppages', filename)

            f = open(ts, "r")
            stops = f.readlines()
            print(stops)
            for stop in stops:
                stop = stop.lower()
                if (to_r + '\n' == stop or to_r == stop) and flag_from==1:
                    flag_to = 1
                if from_r + '\n' == stop or from_r == stop:
                    flag_from = 1
                if flag_to == 1 and flag_from == 1:
                    req_t['trains'].append(
                        str(train.trainNumber) + "  /  " + str(train.trainName) + "  /  " + str(train.runningDays))
                    req_t['flag'] = 2
                    break

            f.close()
        req_t['username'] = request.user.username
        return render(request, 'my_system/my_user/search_trains_user.html', req_t)

    return render(request, 'my_system/my_user/search_trains_user.html', {'username': username})


"""
API Part below
"""


class TicketView(APIView):
    def get(self, request):
        tickets = Ticket.objects.all()
        # the many param informs the serializer that it will be serializing more than a single article.
        serializer = TicketSerializer(tickets, many=True)
        return Response(serializer.data)

    def post(self, request):
        ticket = request.data.get('ticket')

        """
        # Create an article from the above data
        serializer = ArticleSerializer(data=article)
        if serializer.is_valid(raise_exception=True):
            article_saved = serializer.save()
            return Response({"success": "Article '{}' created successfully".format(article_saved.title)})

        """

        serializer = TicketSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk):

        saved_ticket = get_object_or_404(Ticket.objects.all(), pk=pk)
        serializer = TicketSerializer(saved_ticket, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        # Get object with this pk
        ticket = get_object_or_404(Ticket.objects.all(), pk=pk)
        ticket.delete()
        return Response({"message": "Ticket with id `{}` has been deleted.".format(pk)}, status=204)
