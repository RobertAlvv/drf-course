from django.db import models
from apps.base.models import BaseModel

class MeasureUnit(BaseModel):
    
    description = models.CharField('Descripcion', max_length=50, blank=False, null=False, unique=True)

    def __str__(self):
        return self.description

    class Meta:
        verbose_name = 'Unidad de medida'
        verbose_name_plural = 'Unidades de medidas'


class CategoryProduct(BaseModel):
    
    description = models.CharField('Descripcion', max_length=50, unique=True, null=False, blank= False)
    measure_unit = models.ForeignKey(MeasureUnit, on_delete=models.CASCADE, verbose_name='Unidad de medida')


    def __str__(self):
        return self.description

    class Meta:
        verbose_name = 'Categoria de producto'
        verbose_name_plural = 'Categorias de productos'
        
class Indicator(BaseModel):
    
    descount_value = models.PositiveSmallIntegerField(default=0)
    category_product = models.ForeignKey(CategoryProduct, on_delete=models.CASCADE, verbose_name='Indicador de Oferta')

    def __str__(self):
        return f'Oferta de la categoria {self.category_product} : {self.descount_value}%'

    class Meta:
        verbose_name = 'Indicador de oferta'
        verbose_name_plural = 'Indicadores de ofertas'
        
class Product(BaseModel):
    
    name = models.CharField('Nombre de Producto', max_length=150, unique= True, blank=False, null=False)
    description = models.TextField('Descripcion de Producto', blank=False, null=False)
    image = models.ImageField('Imagen del Producto', upload_to='products/', blank=True, null=True)
    measure_unit = models.ForeignKey(MeasureUnit, on_delete=models.CASCADE, verbose_name='Unidad de medida', null=True)
    category_product = models.ForeignKey(CategoryProduct, on_delete=models.CASCADE, verbose_name='Categoria de producto', null=True)

    class Meta:
        db_table = ''
        managed = True
        verbose_name = 'Producto'
        verbose_name_plural = 'Productos'
        
    def __str__(self):
        return self.name
    
    @property
    def stock(self):
        from django.db.models import Sum
        from apps.expense_manager.models import Expense
        
        expense = Expense.objects.filter(
            product = self,
            state=True
        ).aggregate(Sum('quantity'))
        
        return expense