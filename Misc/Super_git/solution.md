## Solution of Super Git!!

> [!NOTE]
> Reverse the encryption code from the previous commit in flag.py. Use the solver script below to decode the flag:
> ```python
> import pyaes
> import base64
> key = "aibThfZPKly8INIXbMjCCt1NuRtQzVdG"
> flag_enc = "b5fhuO/XNayuoNtD25Oxqw+zXqwgwg4J6/pEN7VvAYRa"
> flag_enc_bytes = base64.b64decode(flag_enc.encode())
> aes = pyaes.AESModeOfOperationCTR(key.encode())
> flag_plaintext = aes.decrypt(flag_enc_bytes)
> print(":v :v :v vlag: %s" % flag_plaintext.decode())
>```
>
> ### **Flag**: `JKKNIUCTF{Sup3R_S3cR3t_Fl4g_1337}`
