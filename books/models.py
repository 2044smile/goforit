from django.db import models

from taggit.managers import TaggableManager


class Books(models.Model):  # 책 이름(title)을 정하고, 주제나 간단한 정리문을 적는다.
    id = models.BigAutoField(help_text="Books", primary_key=True)
    title = models.CharField(max_length=50)
    subject = models.CharField(max_length=100, null=True)
    tags = TaggableManager()  # "red, blue, green"

    total_page = models.IntegerField(null=True)  # page 673 , 한번만 실행

    created_at = models.DateTimeField(auto_now_add=True)  # 해당 레코드 생성 시 현재 시간 자동저장
    updated_at = models.DateTimeField(auto_now=True)  # 해당 레코드 갱신 시 현재 시간 자동저장

    def __str__(self):
        return self.title


class Pages(models.Model):
    id = models.BigAutoField(help_text="Pages", primary_key=True)
    books_id = models.ForeignKey("Books", related_name="books", on_delete=models.CASCADE, db_column="books_id")
    read_page = models.IntegerField(null=True)  # page 23, 53, 99 , 여러번 실행
    save_time = models.DateTimeField(auto_now=True)

    def __str__(self):
        return '{} - {}page'.format(self.books_id.title, self.read_page)


