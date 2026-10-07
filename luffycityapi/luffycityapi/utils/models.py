from django.db import models


class BaseModel(models.Model):
    """公共模型基类（抽象模型）"""
    orders = models.IntegerField(verbose_name='排序', default=0)
    is_show = models.BooleanField(verbose_name='是否显示', default=True)
    is_deleted = models.BooleanField(verbose_name='是否删除', default=False)
    created_time = models.DateTimeField(verbose_name='创建时间', auto_now_add=True)
    updated_time = models.DateTimeField(verbose_name='更新时间', auto_now=True)

    class Meta:
        # 设置为抽象模型，迁移时不会为该类生成独立的数据表
        abstract = True