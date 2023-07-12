# Writeup

## Description
I decided to try something noone else has before. I made a bot to automatically trade stonks for me using AI and machine learning. I wouldn't believe you if you told me it's unsecure! vuln.c nc mercury.picoctf.net 20195

## Hints
Okay, maybe I'd believe you if you find my API key.

## Solution
This problem honestly kinda tricky for me. I actually had to see some writeups after eventually I decided to see an explanation video instead. If we try to look at the code and understand it, the program acutally reads the `flag.txt` file and add the flag into the stack. And if we see at the program, it prompts input from us with the `scanf()` function and print the output with `printf()` function.

The thing is, those functions can use specifiers like `%d`, `%c`, etc. After typing the specifiers that we need, we can type the "thing" we want to scan or print, whether it is a variable or something else. Now here is the interesting part, if we just put the specifiers only in a `printf` function, **it spits out the contents that are in the stack**

We can utilize this to see the flag that is indeed contained in the stack. We can use Python to make a pattern of `%x`'s like this.
```print("%x" * 100) #outputs "%x"'s 100 times```

And finally, we can connect to the given address by typing `nc mercury.picoctf.net 20195`. After that, type `1` to buy the stocks and when the program prompts for the API token, paste the pattern that we generate before.

We can see that the program will give us a gibberish message, written in hexadecimal. Copy it and paste it to a hex-ascii converter (I use https://www.rapidtables.com/convert/number/hex-to-decimal.html) and then we can see a string that starts with `ocip` that really just `pico` reversed. We can take that string and use this [program](sol-stonks.py) to make reveal the flag.

## Flag
**picoCTF{I_l05t_4ll_my_m0n3y_6045d60d}**
