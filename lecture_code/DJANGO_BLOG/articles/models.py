from django.db import models

# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=10)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True) #최초 생성된 시간만 등록함
    updated_at = models.DateTimeField(auto_now=True) #수정될때 마다 시간이 변경
 
    def __str__(self):
        return f'{self.id}번 글 = {self.title} : {self.content}'
        
class Comment(models.Model):
    content = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    # on_delete=models.CASCADE : 게시물 삭제했을때 댓글도 삭제시키기 위해 
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    
    def __str__(self):
        return f'<Article({self.article_id}) : Comment({self.id})> - {self.content}'