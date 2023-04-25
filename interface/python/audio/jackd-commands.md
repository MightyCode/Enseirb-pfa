## Jackd - ubuntu

https://doc.ubuntu-jacfr.org/jackd

## List all sound cards on your computer 

```bash
aplay -l
```

## Start jackd server

```bash
jackd -Rd alsa -d hw:1 -r 48000 -p 1024 -n 2
```
