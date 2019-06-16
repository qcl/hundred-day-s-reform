class Solution(object):
    def numUniqueEmails(self, emails):
        """
        :type emails: List[str]
        :rtype: int
        """
        address = {}
        for email in emails:
            name, domain = email.split('@')
            name = name.split('+')[0].replace('.','')
            mailAddress = '%s@%s' % (name, domain)
            if not mailAddress in address:
                address[mailAddress] = 1
            else:
                address[mailAddress] += 1
        
        return len(address.keys())
