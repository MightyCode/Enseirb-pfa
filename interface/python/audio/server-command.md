## Jackd - ubuntu

https://doc.ubuntu-fr.org/jackd

## List all sound cards on your computer 

```bash
qjackctl
```

```bash
aplay -l
```

## Start jackd server

```
jackd -Rd alsa -d hw:1 -r 48000 -p 1024 -n 2
```
