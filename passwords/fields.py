from django.forms import CharField, PasswordInput

from passwords.validators import (validate_length,
                                  common_sequences,
                                  dictionary_words,
                                  complexity,
                                  only_ansi_symbols,
                                  validate_whitespaces)
from widgets import PasswordFieldWidget


class PasswordField(CharField):
    default_validators = [validate_length,
                          common_sequences,
                          dictionary_words,
                          complexity,
                          only_ansi_symbols,
                          validate_whitespaces]

    def __init__(self, *args, **kwargs):
        if not kwargs.has_key("widget"):
            kwargs["widget"] = PasswordFieldWidget(render_value=False, validate_url=kwargs.get('validate_url'))
        if 'validate_url' in kwargs:
            del kwargs['validate_url']
        super(PasswordField, self).__init__(*args, **kwargs)
