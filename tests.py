from namecheap import Namecheap

n = Namecheap()
renew = n.domains.renew(DomainName='xploit29.com', Years=1)
domains = n.domains.getList()
contacts = n.domains.getContacts(DomainName='xploit29.com')
