from django.db import models
from accounts.models import CustomUser

class Product_num(models.Model):
    title = models.CharField(verbose_name='品番',max_length=20)
    def __str__(self) -> str:
        return self.title
    
class inv_Post(models.Model):
    user = models.ForeignKey(CustomUser,verbose_name='ユーザー',on_delete=models.PROTECT)
    product_num = models.ForeignKey(Product_num,verbose_name='品番',on_delete=models.PROTECT)
    # product_name = models.CharField(verbose_name='品名',max_length=20)
    quantity = models.IntegerField(verbose_name='数量')
    comment = models.CharField(verbose_name='備考',max_length=50)
    posted_at = models.DateTimeField(verbose_name='投稿日時',auto_now_add=True)
    def __int__(self) -> int:
        return self.quantity