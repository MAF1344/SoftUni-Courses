class EmailValidator:
    def __init__(self, min_length, mails, domains):
        self.min_length = min_length
        self.mails = mails
        self.domains = domains

    def __is_name_valid(self, name):
        return len(name) >= self.min_length

    def __is_mail_valid(self, mail):
        return mail in self.mails

    def __is_domain_valid(self, domain):
        return domain in self.domains

    def validate(self, email):
        try:
            name, rest = email.split('@')
            mail, domain = rest.split('.')
            return (self.__is_name_valid(name) and
                    self.__is_mail_valid(mail) and
                    self.__is_domain_valid(domain))
        except ValueError:
            return False


mails = ["gmail", "softuni"]
domains = ["com", "bg"]
email_validator = EmailValidator(6, mails, domains)
print(email_validator.validate("pe77er@gmail.com"))  # True
print(email_validator.validate("georgios@gmail.net"))  # False
print(email_validator.validate("stamatito@abv.net"))  # False
print(email_validator.validate("abv@softuni.bg"))  # False
