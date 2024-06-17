from django.core.validators import RegexValidator, EmailValidator

nip_validator = RegexValidator(
    regex=r'^\d{10}$',
    message="The NIP must consist of 10 digits.",
    code='invalid_nip'
)
regon_validator = RegexValidator(
    regex=r'^\d{9}$|^\d{14}$',
    message="The REGON must consist of 9 or 14 digits.",
    code='invalid_regon'
)
phone_validator = RegexValidator(
    regex=r'^\d{9}$',
    message="The phone number must consist of exactly 9 digits.",
    code='invalid_phone'
)

email_validator = EmailValidator(
    message="The email address you provided is invalid.",
    code='invalid_email'
)