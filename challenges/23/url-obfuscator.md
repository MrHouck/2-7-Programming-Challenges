# Challenge #23 - IP/URL Obfuscator

This script will obfuscate MOST urls
The reason it isn't capable of obfuscating every URL is that some web hosting providers will redirect multiple websites to the same one IP address, meaning that the website cannot be addressed solely by the IP address, rendering the whole obfuscation process irrelevant. 
This script follows most of what is outlined at http://www.pc-help.org/obscure.htm

The basic process this involves is:
1. Get the IP Address of the nameserver
2. Convert the parts of the IP address into the Dword, octal, and hexadecimal format
3. Replace the IP address with either the original IP, the octal format, or the hexadecimal format (I didn't use the dword version of the IP in this step)
4. Convert any extraneous text (url paths) to hex-encoded strings (%6e, etc)
5. Add bogus url to beginning 

## Examples:
Example I/O 1: 
Input a valid url: https://github.com/MrHouck
Dword: http://2354213380/MrHouck
http://www.uncomfortable-mouth.com:slvlcvheearelav@0x8c.82.114.0004/%4d%72%48%6f%75%63%6b

Example I/O 2:
Input a valid url: https://xkcd.com/1247/
DworD: http://2540011587//1247/
http://www.pure-ego.com:isanrrbofsdctk@0227.101.128.67/%31%32%34%37/

Example #2 is one such website on which this trick unfortunately does not work. You can see an example of this by repeatedly running the command `ping xkcd.com` on your terminal, and notice how the IP changes each time.