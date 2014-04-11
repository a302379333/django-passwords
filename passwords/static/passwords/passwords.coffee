# must have underscore.js, jquery, coffeescript
jQuery ($) ->
  bar_template = '<div class="progress password <%=bar_type%>"><div class="bar" style="width: <%=width%>%;"></div></div><div class="password-validation-error"><%=error_messages%></div>'
  render_bar = _.template(bar_template)
  $('input[name="password"]').keyup ->
    $.post(window.password_validator_url, {password: $(this).val()}, (response) ->
      $(@).closest('p.help-block').remove()
      $('.status_bar').html render_bar(response)
      )
