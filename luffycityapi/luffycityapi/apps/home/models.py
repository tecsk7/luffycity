from django.db import models
from luffycityapi.utils.models import BaseModel  # 请根据实际项目目录导入公共基类


class Nav(BaseModel):
    """导航栏模型"""
    POSITION_CHOICES = (
        (0, '顶部导航'),
        (1, '脚部导航'),
    )

    name = models.CharField(max_length=64, verbose_name='导航名称')
    link = models.CharField(max_length=255, verbose_name='导航链接')
    position = models.SmallIntegerField(choices=POSITION_CHOICES, default=1, verbose_name='导航位置')
    is_http = models.BooleanField(verbose_name='是否是外部链接', default=False)

    class Meta:
        db_table = 'ly_nav'
        verbose_name = '导航菜单'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name