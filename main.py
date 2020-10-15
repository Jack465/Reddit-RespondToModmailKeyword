import praw
import os
import re

keywords = ['hi', 'carrots', 'oranges', 'pears', 'whatever', 'keywords']

reddit = praw.Reddit(client_id='###',
                client_secret='###',
                user_agent='pascalprv r_RequestABot Request',
                username='####',
                password='####')

if os.path.isfile('processed_mail.txt'):
	with open('processed_mail.txt', 'r') as file:
		processed_mail = [line.rstrip('\n') for line in file]

waiting_list = []

conversations = reddit.subreddit('musicbottesting').modmail.conversations(state='all', sort='unread')
for conv in conversations:
    if conv.id not in processed_mail:
        for message in conv.messages:
            body = message.body_markdown.lower()
            if any(keyword in body for keyword in keywords):
                print("Found keyword in message with ID {} from user {}".format(conv.id, conv.user.name))
                conv.reply("Hi, we have found keyword in your message. Whatever message you want here")
                waiting_list.append(conv.id)
                print("Replied to message ID {} from user {} with the preset response\n".format(conv.id,conv.user.name))
    else:
        break

with open('processed_mail.txt','a') as file:
	for item in waiting_list:
		file.write('{}\n'.format(item))