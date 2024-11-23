from django.core.exceptions import ValidationError # type: ignore
#verifica se o arquivo é png
def validate_png(image):
    if not image.name.lower().endswith('.png'):
        
        raise ValidationError('Arquivo precisa ser PNG')