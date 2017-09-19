import netaddr
import pandas as pd

from range_to_cidr import range_to_cidr

def blacklist(mode):

	'''Blacklist Loader

	WHAT: Loads blacklists in to a set of IPs for 
		  queries to be made using netaddr

	HOW: blacklist('bogon')

	INPUT: lo.blacklist('bogon')

	OUTPUT: an IPSet object to be with netaddr

	'''

	# client9 datacenter IP 

	if mode is 'client9':
		out = pd.read_csv('https://raw.githubusercontent.com/client9/ipcat/master/datacenters.csv',
						  header=None)
		out = out[[0,1]]
		out = range_to_cidr(out)

	else:
		# full bogon list
		if mode is 'bogon':
			out = pd.read_csv('https://www.cidr-report.org/bogons/allocspace-prefix.txt',
							  header=None)

		# Botlab datacenter IP
		elif mode is 'denylist':
			out = pd.read_csv('https://raw.githubusercontent.com/botlabio/deny-hosting-IP/master/cidr.txt',
	  						   header=None)


		# cymru bogons
		elif mode is 'cymru':
			out = pd.read_csv('http://www.team-cymru.org/Services/Bogons/fullbogons-ipv4.txt',
						      header=None)
			out = out[1:]

		elif mode is 'firehol1':
			out = pd.read_csv('https://raw.githubusercontent.com/ktsaou/blocklist-ipsets/master/firehol_level1.netset',
							  header=None,
							  comment='#')

		elif mode is 'firehol2':
			out = pd.read_csv('https://raw.githubusercontent.com/ktsaou/blocklist-ipsets/master/firehol_level2.netset',
							  header=None,
							  comment='#')

		elif mode is 'firehol3':
			out = pd.read_csv('https://raw.githubusercontent.com/ktsaou/blocklist-ipsets/master/firehol_level3.netset',
						      header=None,
						      comment='#')

		elif mode is 'firehol4':
			out = pd.read_csv('https://raw.githubusercontent.com/ktsaou/blocklist-ipsets/master/firehol_level4.netset',
							  header=None,
							  comment='#')

		out = netaddr.IPSet(out[0])

	return out