from django import template


register = template.Library()

@register.inclusion_tag(filename = "user_app/inclusion_tags/custom_form.html") 
def render_custom_form(form):
    '''
    Ця функція вмикаючого тегу, що відповідає за відображення кастомної форми
    '''
    return {"form": form}  
    
