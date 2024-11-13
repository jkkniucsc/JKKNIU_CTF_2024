## Solution for Shadow_mind 🕵️‍♂️

1. Unzip the archive file using the password `Shadow_mind` to get `passwd` and `shadow` files.
1. Use `john` or `hashcat` to crack hashes:
```bash
john shadow --format=crypt
```

### Flag: JKKNIUCTF{abigael:password1_secrets:123}


#### Ref: [Link](https://security.stackexchange.com/questions/252665/does-john-the-ripper-not-support-yescrypt)
