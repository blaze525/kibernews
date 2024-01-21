from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        db_table = 'category'
        verbose_name = 'category'
        verbose_name_plural = 'categories'
        
    def __str__(self) -> str:
        return self.name
     
    
    
class News(models.Model):
    title = models.TextField()
    description = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    img = models.ImageField(null=False, blank=True, upload_to='news/')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        db_table = 'news'
        verbose_name = 'news'
        verbose_name_plural = 'news'
        
    def __str__(self) -> str:
        return self.title
    
    
class Banner(models.Model):
    news = models.ForeignKey(News, on_delete=models.CASCADE)
    img = models.ImageField(upload_to='banners/')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        db_table = 'banners'
        verbose_name = 'banners'
        verbose_name_plural = 'banners'
        
    def __str__(self) -> str:
        return self.news.title