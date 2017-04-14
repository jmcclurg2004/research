#author Jerry McClurg
#Version 1 3/11/2017

import urllib.request
import os

print("Enter Website URL: ")
url=input()
print("")

with urllib.request.urlopen(url) as response:
    headers = response.info()
print(headers)

print("Header Analysis Results: ")
print("")
searcha = ("X-Frame-Options")
searchb = ("Strict-Transport-Security")
searchc = ("Public-Key-Pins")
searchd = ("X-Xss-Protection")
searche = ("X-Content-Type-Options")
searchf = ("Content-Security-Policy")

if searcha in headers:
    print('1.  Not Vulnerable - X-Frame-Options in website!')
else:
    print('1.  Vulnerable!  No X-Frame-Options - clickjacking!')
if searchb in headers:
    print('2.  Not Vulnerable - HSTS is in website!')
else:
    print('2.  Vulnerable!  No HSTS - Vulnerable to HTTP downgrade attacks!')
if searchc in headers:
    print('3.  Not Vulnerable - Certificate pinning configured!')
else:
    print('3.  Vulnerable!  No certificate pinning - Vulnerable to MITM!')
if searchd in headers:
    print('4.  Not Vulnerable - XSS Header Protection configured!')
else:
    print('4.  Vulnerable!  No XSS Headers - potential XSS vulnerabilities!')
if searche in headers:
    print('5.  Not Vulnerable - Content type options configured!')
else:
    print('5.  Vulnerable!  No Content Type Options configured - potentially vulnerable to MIME sniffing and attacks!')
if searchf in headers:
    print('6.  Not Vulnerable - Content security policy configured!')
else:
    print('6.  Vulnerable!  No Content Security Policy configured - no whitelisting of approved sources!')
print("")

import os
os.system("pause")