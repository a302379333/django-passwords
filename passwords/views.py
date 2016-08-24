# coding: utf-8
import json
from django.http import HttpResponse
from django.core.exceptions import ValidationError
from django.conf import settings

from passwords.validators import (validate_length, common_sequences,
                                  dictionary_words, complexity,
                                  only_ansi_symbols, validate_whitespaces)

from project.settings import PASSWORD_MAX_LENGTH


# ignore whitespaces: if True - check whitespaces
PASSWORD_WITHOUT_WHITESPACES = getattr(settings, 'PASSWORD_WITHOUT_WHITESPACES', False)


def password_validator(request):
    # Заполненость бара пароля - зависит от длины пароля
    if not request.POST.get('password', 0):
        bar_width = 0
    elif len(request.POST.get('password', 0)) >= PASSWORD_MAX_LENGTH:
        bar_width = 100
    else:
        bar_width = int((float(len(request.POST.get('password', 0)))/PASSWORD_MAX_LENGTH)*100)
    # В случае отсутствия ошибок вернутся следующие поля
    result = {'success': True,
              'bar_type': 'progress-success',
              'error_messages': '',
              'width': bar_width}
    try:
        only_ansi_symbols(request.POST.get('password'))
        complexity(request.POST.get('password'))
        dictionary_words(request.POST.get('password'))
        validate_length(request.POST.get('password'))
        common_sequences(request.POST.get('password'))
        if PASSWORD_WITHOUT_WHITESPACES:
            validate_whitespaces(request.POST.get('password'))
    except ValidationError, err:
        # произошла ошибка валидации
        result = {'success': False,
                  'error_messages': err.messages[0],
                  'width': bar_width,
                  'bar_type': 'progress-danger'}
    return HttpResponse(json.dumps(result), content_type='application/json')
