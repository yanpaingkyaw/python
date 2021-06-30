from requests import get

ip = get('https://api.my-ip.io/ip').text
print('My IP address is: {}'.format(ip))
input("Press Any Key to stop it.. ") 