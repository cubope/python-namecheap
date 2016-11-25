from .base import Response


class Domains(Response):
    def getList(self, **kwargs):
        """
        Command: `namecheap.domains.getList`
        [Online documentation](
            https://www.namecheap.com/support/api/methods/domains/get-list.aspx
        )
        """
        return self._request(
            command='namecheap.domains.getList',
            placeholder='DomainGetListResult',
        )

    def getContacts(self, **kwargs):
        """
        Command: `namecheap.domains.getContacts`
        [Online documentation](
            https://www.namecheap.com/support/api/methods/domains/get-contacts.aspx
        )
        """
        if 'DomainName' not in kwargs:
            raise Exception('DomainName parameter is required')

        return self._request(
            'namecheap.domains.getContacts',
            placeholder='DomainContactsResult',
            args=kwargs
        )

    def create(self, **kwargs):
        """
        Command: `namecheap.domains.getList`
        [Online documentation](
            https://www.namecheap.com/support/api/methods/domains/create.aspx
        )
        """
        required_kwargs = (
           'DomainName', 'Years', 'RegistrantFirstName', 'RegistrantLastName',
           'RegistrantAddress1', 'RegistrantCity', 'RegistrantStateProvince',
           'RegistrantPostalCode', 'RegistrantCountry', 'RegistrantPhone',
           'RegistrantEmailAddress', 'TechFirstName', 'TechLastName',
           'TechAddress1', 'TechCity', 'TechStateProvince', 'TechPostalCode',
           'TechCountry', 'TechPhone', 'TechEmailAddress', 'AdminFirstName',
           'AdminLastName', 'AdminAddress1', 'AdminCity', 'AdminStateProvince',
           'AdminPostalCode', 'AdminCountry', 'AdminPhone',
           'AdminEmailAddress', 'AuxBillingFirstName', 'AuxBillingLastName',
           'AuxBillingAddress1', 'AuxBillingCity', 'AuxBillingStateProvince',
           'AuxBillingPostalCode', 'AuxBillingCountry', 'AuxBillingPhone',
           'AuxBillingEmailAddress'
        )

        if not all(k in kwargs for k in required_kwargs):
            raise Exception('Missing parameters, check the documentation.')

        return self._request(
            'namecheap.domains.create',
            placeholder='DomainContactsResult',
            args=kwargs
        )

    def renew(self, **kwargs):
        """
        Command: `namecheap.domains.renew`
        [Online documentation](
            https://www.namecheap.com/support/api/methods/domains/renew.aspx
        )
        """
        required_kwargs = (
           'DomainName', 'Years',
        )

        if not all(k in kwargs for k in required_kwargs):
            raise Exception('Missing parameters, check the documentation.')

        return self._request(
            'namecheap.domains.renew',
            placeholder='DomainRenewResult',
            args=kwargs
        )
