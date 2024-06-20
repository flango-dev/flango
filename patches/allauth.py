from allauth.account.adapter import DefaultAccountAdapter


class NoEspAccountAdapter(DefaultAccountAdapter):
     def send_mail(self, template_prefix, email, context):
         return
