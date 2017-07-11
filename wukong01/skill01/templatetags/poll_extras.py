from django import template
from datetime import datetime


register=template.Library()

class  AllenDateNode(template.Node):
    def __init__(self,format_string):
        self.format_string=format_string

    def render(self, context):
        return datetime.now().strftime(self.format_string)


@register.tag(name="dateAllen")
def dateAllen(parse,token):
    try:
        tagname,format_string=token.split_contents()
    except ValueError:
        raise TemplateSyntaxError("invalid args")
    return AllenDateNode(format_string[1:-1])

#register.tag(name="dateAllen",compile_function=dateAllen())