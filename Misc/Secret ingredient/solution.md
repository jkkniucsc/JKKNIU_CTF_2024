## **How to solve this challenge and other info**

## **Flag**: `JKKNIUCTF{i5_iT_r34lLY_Cr!M3_Bl4BL4bl4!}`


- **Password for pdf**:	`freedom`

1. Crack the pdfs password --> [`pdfrip`](https://github.com/mufeedvh/pdfrip)
```sh
pdfrip -f init.pdf wordlist $PAYLOADS/seclists/Passwords/xato-net-10-million-passwords-1000.txt 
```
> Password: `freedom`

2. The pdf will extract first part of the flag.

3. Check comments for jsfuck code. This site can be used to decoding the hash: <br>
[jsfuck](https://jsfuck.com/)
- How to check comment in alternative way:
```sh
binwalk -e *.pdf
```
Then
```sh
cat _ingredient.pdf.extracted/word/comments.xml
```
4. Done!!!
