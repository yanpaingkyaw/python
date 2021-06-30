
#
# 
# Before Run this code need to ENABLE "Less Secure App"
#
from imapclient import IMAPClient
mail = IMAPClient('imap.gmail.com', ssl=True, port=993)
mail.login("yanpaingkyaw@gmail.com", "ITM@n@ger")
totalMail = mail.select_folder('INBOX')
#Shows how many messages are there - both read and unread
print('You have total %d messages in your folder' % totalMail[b'EXISTS'])
delMsg = mail.search(('UNSEEN'))
mail.delete_messages(delMsg)
  
#Shows number of unread messages that have been deleted now
print('%d unread messages in your folder have been deleted' % len(delMsg))
mail.logout()

# mail.set_gmail_labels(mail.search(), '\\Trash')  
# mail.delete_messages(mail.search())  
# mail.expunge() 
# mail.logout()