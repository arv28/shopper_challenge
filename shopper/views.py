# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.contrib import messages

import time
from .utils import logger
from .models import Shopper

def index(request):
    """
    API for '/shopper'
    """
    return render(request, 'shopper/index.html')

def login(request):
    """
    API for '/shopper/login'
    """
    if request.POST:
        email = request.POST['email']

        if not email:
            message = "Please enter a valid email."
            logger.error(message)
            messages.add_message(request, messages.ERROR, message)
            return render(request, 'shopper/index.html')

        if Shopper.objects.filter(email=email).exists():
            shopper = Shopper.objects.filter(email=email)[0]
            request.session['email'] = shopper.email
            context = {'shopper': shopper}
            return render(request,'shopper/login.html', context)
        else:
            logger.error("No application found for email : %s", email)
            messages.add_message(request, messages.ERROR, "Sorry, there is no application with this email.")
            return render(request,'shopper/index.html')

def logout(request):
    """
    API for '/shopper/logout'
    """
    try:
        del request.session['email']
    except Exception as e:
        logger.error("Failed to delete session. Email : %s, Error : %s", request.session['email'], str(e))
    return render(request,'shopper/index.html')

def register(request):
    """
    POST API for '/shopper/register'
    This API verifies that email and phone number don't match with any other existing applicant,  
    sets the user session details and redirects the user to background check page
    """

    if request.POST:
        #Obtain form data from the request and store in session variables so they can be accessed across functions
        user_info = request.POST
        is_valid_user = True

        if Shopper.objects.filter(email = user_info['email']).exists():
            is_valid_user = False
            error_message = "This email is already registered!"
            logger.error("This email is already registered. Email : %s", user_info['email'])
            messages.add_message(request, messages.ERROR, error_message)            

        if Shopper.objects.filter(phone = user_info['phone']).exists():
            is_valid_user = False
            error_message = "This phone number is already registered!"
            logger.error("This phone number is already registered. Phone : %s", user_info['phone'])
            messages.add_message(request, messages.ERROR, error_message)
        
        if not is_valid_user:           
            return render(request, 'shopper/index.html')

        # If the user is valid, set the user session details
        request.session['name'] = user_info['name']
        request.session['email'] = user_info['email']
        request.session['phone'] = user_info['phone']
        request.session['city'] = user_info['city']
        request.session['state'] = user_info['state']

        # redirect the user to background check page
        return render(request,'shopper/background_check.html')

def confirmation(request):
    """
    POST API which saves the credentials and session.
    """
    
    if request.POST:
        # Check if the user is already registered 
        shopper = Shopper.objects.filter(email=request.session['email'])
        if shopper:
            context = {'shopper': shopper[0]}
            return render(request,'shopper/confirmation.html', context)

        # Invalidate the cache for current week for funnel metrics as we got a new applicant
        #invalidate_cache(timezone.now())

        # Register the user and save user information in database
        name = request.session['name']
        email = request.session['email']
        phone = request.session['phone']
        city = request.session['city']
        state = request.session['state']
        shopper = Shopper(name=name, email=email, phone=phone, city=city, state=state)
        shopper.save()
        context = {'shopper' : shopper}
        
        # Delete all user's session data except for 'email' which is used to maintain user-session
        del request.session['name'] 
        del request.session['phone'] 
        del request.session['city']
        del request.session['state'] 

        logger.info("New shopper registered. Email : %s", email)

        # Redirect user to the registration confirmation page
        return render(request,'shopper/confirmation.html',context)


