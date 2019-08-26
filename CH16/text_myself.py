#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug 26 12:57:13 2019

@author: Soo Hyeon Kim
"""

# Preset Values:
account_sid = 'Axxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx'
auth_token = '9xxxxxxxxxxxxxxxxxxxxxxxxxxxxxx5'
my_number = '+1xxxxxxxxxx'
twilio_number = '+16784986617'

from twilio.rest import Client

def text_myself(message):
    twilio_client = Client(account_sid, auth_token)
    twilio_client.messages.create(body=message, from_=twilio_number, to=my_number)