from namecheap import Namecheap

n = Namecheap()
domains = n.domains.getList()
contacts = n.domains.getContacts(DomainName='xploit29.com')
