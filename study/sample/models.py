from django.db import models


class Company(models.Model):
    """事業者"""
    name = models.CharField('名称', max_length=255)

    def __str__(self):
        return self.name


class BalancingGroup(models.Model):
    """発電BG"""
    name = models.CharField('名称', max_length=255)
    company =  models.ForeignKey(Company, verbose_name='名称', related_name='balancing_groups', on_delete=models.CASCADE)
    
    def __str__(self):
        return self.name


class PowerPlant(models.Model):
    """発電所"""
    name = models.CharField('名称', max_length=255)
    balancing_group =  models.ForeignKey(BalancingGroup, verbose_name='名称', related_name='power_plants', on_delete=models.CASCADE)
    
    def __str__(self):
        return self.name


class Generator(models.Model):
    """発電機"""
    name = models.CharField('名称', max_length=255)
    power_plant =  models.ForeignKey(PowerPlant, verbose_name='名称', related_name='generator', on_delete=models.CASCADE)
    
    def __str__(self):
        return self.name
