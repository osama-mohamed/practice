from django.template import Library
from django.contrib.auth import get_user_model

from accounts.models import UserProfile

register = Library()
User = get_user_model()

# short way
@register.inclusion_tag("accounts/snippets/recommend.html")
def recommended(user):
  if isinstance(user, User):
    qs = UserProfile.objects.recommended(user)
    return {"recommended": qs}



# long way
# from django.template.loader import get_template
# from django.utils.safestring import mark_safe

# @register.simple_tag(is_safe=True)
# def recommended(user):
#   if isinstance(user, User):
#     template = get_template("accounts/snippets/recommeded.html")
#     context = {"recommended": UserProfile.objects.recommended(user)}
#     data = template.render(context=context, request=None)
#     content = mark_safe(data) # or @register.filter(is_safe=True)
#     return content
#   return ""
