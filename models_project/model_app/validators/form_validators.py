from django.core.exceptions import ValidationError

def check_gmail(value):
    if not value.endswith('@gmail.com'):
        raise ValidationError('Yalniz gmail hesablari qebul edilir!')
