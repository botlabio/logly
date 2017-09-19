# logly
Set of useful and battle tested tools for logfile analysis

## Example Use

```bash

# get two different sets of hosting blacklists
denylist = lo.blacklist('denylist')
client9 = lo.blacklist('client9')

# combine them in to one list with no duplicates
datacenter = lo.combine_sets(denylist, client9)

# check ip addresses from logfile against the blacklist
lo.check_ip(norway_ip[0], datacenter)

```
