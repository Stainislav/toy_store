from django.db import models

'''
# Район города.
class District(models.Model):

    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Район города"
        verbose_name_plural = "Районы города"


# Категория.
class Category(models.Model):

    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"


# Сеть предприятий.
class EnterpriseNetwork(models.Model):

    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Сеть предприятий"
        verbose_name_plural = "Сети предприятий"


# Предприятие.
class Organization(models.Model):

    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)
    description = models.TextField(max_length=200)
    organization_network = models.ForeignKey(EnterpriseNetwork, on_delete=models.CASCADE)
    district = models.ManyToManyField(District)

    goods = models.ManyToManyField('Goods', through='GoodsPriceConnection')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Предприятие"
        verbose_name_plural = "Предприятия"


# Товары.
class Goods(models.Model):

    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Товар"
        verbose_name_plural = "Товары"


# Связь 'товар-цена'.
class GoodsPriceConnection(models.Model):

    id = models.AutoField(primary_key=True)
    organization = models.ForeignKey(Organization, on_delete=models.CASCADE)
    goods = models.ForeignKey(Goods, on_delete=models.CASCADE)

    price = models.CharField(max_length=200)

    class Meta:
        verbose_name = "Связь 'товар-цена'"
        verbose_name_plural = "Связи 'товар-цена'"
'''
