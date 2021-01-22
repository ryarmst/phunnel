# phunnel

A simple python script that takes an input wordlist and password complexity policy and outputs a wordlist filtering out passwords that do not meet the specified complexity policy.

## Usage

phunnel.py [-h] [-m M] [-u] [-l] [-n] [-s] [-ns] infile outfile

positional arguments:

  infile      Input file\
  outfile     Output file

optional arguments:

  -h, --help  show this help message and exit\
  -m M        Minimum password length\
  -u          Require at least 1 uppercase\
  -l          Require at least 1 lowercase\
  -n          Require at least 1 number\
  -s          Require at least 1 special\
  -ns         Password can contain NO special

## Password Lists

Obviously, this tool is useless without password lists. Check out some of the following resources:

- [SecLists](https://github.com/danielmiessler/SecLists) - massive wordlist collection that includes passwords
- [Skull Security Passwords](https://wiki.skullsecurity.org/Passwords) - assortment of PW lists
- [Probable Wordlists](https://github.com/berzerk0/Probable-Wordlists) - top passwords sorted by popularity
- [password-lists](https://github.com/lavalamp-/password-lists) - passwords broken up by TLD/language
- [Bruteforce Database](https://github.com/duyetdev/bruteforce-database)

## Password Generators

- [CUPP](https://github.com/Mebus/cupp)
- [BEWGor](https://github.com/berzerk0/BEWGor)
- [Crunch](https://sourceforge.net/projects/crunch-wordlist/)
- [RSMangler](https://github.com/digininja/RSMangler)
- [CEWL](https://github.com/digininja/CeWL/)

## Other Tools

As it turns out, there are other tools that can be used to filter password complexity as well.

- [PACK](https://github.com/iphelix/pack)
- [LavaPasswordFactory](https://github.com/lavalamp-/LavaPasswordFactory)
- [Password_Filter](https://github.com/rajnepali/Password_Filter)

