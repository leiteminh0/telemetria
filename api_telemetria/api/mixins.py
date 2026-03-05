from drf_yasg.utils import swagger_auto_schema


class SwaggerDocMixin:
    """
    Mixin para adicionar documentação Swagger automática em todos os métodos do ViewSet.
    Elimina a necessidade de decorar manualmente cada método.
    """
    
    def get_entity_name(self):
        """Retorna o nome da entidade baseado no serializer"""
        return self.serializer_class.Meta.model._meta.verbose_name or 'registro'
    
    @swagger_auto_schema(operation_description="Lista todos os registros")
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)
    
    @swagger_auto_schema(operation_description="Cria um novo registro")
    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)
    
    @swagger_auto_schema(operation_description="Retorna um registro específico por ID")
    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)
    
    @swagger_auto_schema(operation_description="Atualiza completamente um registro existente")
    def update(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)
    
    @swagger_auto_schema(operation_description="Atualiza parcialmente um registro existente")
    def partial_update(self, request, *args, **kwargs):
        return super().partial_update(request, *args, **kwargs)
    
    @swagger_auto_schema(operation_description="Remove um registro por ID")
    def destroy(self, request, *args, **kwargs):
        return super().destroy(request, *args, **kwargs)
