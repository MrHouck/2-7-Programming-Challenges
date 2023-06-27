# IP / URL Obfuscation

# This may not work with some URLs, because some web hosting services use systems that place
# multiple websites at a single IP address, meaning that these websites cannot be addressed
# by the IP address alone.
import socket
import random
from urllib.parse import urlsplit, urlparse


URL = "https://iana.org/domains/reserved"

URL = input("Input a valid url: ")

# Gotta validate the input

try:
    result = urlparse(URL)
    if all([result.scheme, result.netloc]):
        pass
except:
    print("Invalid URL")
    exit()


#First Step : Obtain IP Address of Website

import socket
import random
from urllib.parse import urlsplit
split_url = urlsplit(URL) 
ip = socket.gethostbyname(split_url.netloc)


# Now that we have the IP Address, we convert it to a Dword...

ip_chunks = [int(i) for i in ip.split('.')]
dword = ((ip_chunks[0] * 256 + ip_chunks[1]) * 256 + ip_chunks[2]) * 256 + ip_chunks[3]
print(f'DworD: http://{dword}/{split_url.path}')

#We can further obfuscate by adding any multiple of 4294967296 (256^4)
#But..... it doesn't seem to work on my browser 
#Here's the implementation anyways
# dword += 256**4 * random.randint(1, 256)

#Octal Version
octal_chunks = [oct(component)[2:].zfill(4) for component in ip_chunks]

#Here's another way to obfuscate URLs, with hexadecimal (looks so much more shady)
hex_represenation = hex(dword)[2:]
hex_chunks = ['0x' + hex_represenation[i:i+2] for i in range(0, len(hex_represenation), 2)]



# At this point, we can create the ultimate obfuscated url

adjective = random.choice(open('./adjectives.txt','r').read().split('\n'))
nouns = random.choices(open('./nouns.txt','r').read().split('\n'), k=4)

url_final = f"http://www.{adjective}-{nouns[0]}.com:{''.join(random.sample(nouns[1]+nouns[2]+nouns[3],len(nouns[1])+len(nouns[2])+len(nouns[3])))}@"
for i in range(4):
    choice = random.randint(0, 2)
    match choice:
        case 0:
            url_final += str(ip_chunks[i])
        case 1:
            url_final += str(octal_chunks[i])
        case 2:
            url_final += str(hex_chunks[i])
    url_final+='.'

path = ""
for c in split_url.path:
    if c.isascii() and c != "/" :
        path += "%" + hex(ord(c))[2:]
    else:
        path += c


print(url_final[:-1]+path)