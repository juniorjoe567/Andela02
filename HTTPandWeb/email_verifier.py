import requests

class EmailVerifier:
    """ Prompts for an email address and validates it using the
        mailboxlayer API
    """
    
    def __init__(self):
        print('****** Email Address Verifier ******')
        print('Use this tool to check whether an')
        print('email address is valid (or exists)')
        print('************************************\n')
        self.check_email()

    def get_email(self):
        """ Prompts for and returns an email """
        email = input('Enter an email address: ')
        return email

    def check_email(self):
        """ Calls mailbox layer API to validate the emial """

        # Prompt user for an email to verify
        email = self.get_email()
        if email is None:
            print('Enter an email you want to check')
            email = self.get_email()

        base_url = 'http://apilayer.net/api/check'
        apiKey = 'db934f36d19940ba24cae4af699569da'

        # Construct the final URL
        url = '{0}?access_key={1}&email={2}&smtp=1&format=0'.format(
            base_url, apiKey, email)
        
        response = requests.get(url)

        # If the request was successful
        if response.status_code == 200:
            result = response.json()
            if result["format_valid"]:
                email_format = 'valid'
            else:
                email_format = 'invalid'

            if result["smtp_check"]:
                exists = 'exists'
            else:
                exists = 'does not exist'

            print('The email format is {0} and the address {1}'
                  .format(email_format, exists))

        else:
            print('Sorry mate, seems we can\'t validate that email at this time')

if __name__ == '__main__':
    EmailVerifier()
