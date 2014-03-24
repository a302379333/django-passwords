# coding: utf-8
from django.forms import PasswordInput
from django.utils.safestring import mark_safe


class PasswordFieldWidget(PasswordInput):
    class Media:
        css = {'all': ('passwords/passwords.css',)}
        js = ('passwords/passwords.js',)

    def __init__(self, attrs=None, render_value=False, validate_url=None):
        super(PasswordFieldWidget, self).__init__(attrs)
        self.render_value = render_value
        self.validate_url = validate_url

    def render(self, name, value, attrs=None):
        data_render = ''
        if not self.render_value:
            value = None
        if self.validate_url:
            data_render = """<div class="status_bar"><div class="progress password "><div class="bar" style="width: 0%;"></div></div></div>
            <script type="text/javascript">//global var for password validation url
                window.password_validator_url = '{url}';
            </script>""".format(url=self.validate_url)
        else:
            data_render = '<div>Укажите урл для валидации поля</div>'
        return mark_safe(str(super(PasswordFieldWidget, self).render(name, value, attrs)) + data_render)
