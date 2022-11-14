from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class Group(models.Model):
    # Тут смотрим, чтобы max_length не был слишком маленький,
    # студенты любят тут написать что-нибудь около 10 :)
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)
    description = models.TextField()

    # Можно лучше:
    # Добавляем __str__.
    # В постах можно не добавлять, так как там нет чего-то
    # короткого и содержательного как title здесь.
    def __str__(self):
        return f"<Group {self.title}>"


class Post(models.Model):
    text = models.TextField()
    pub_date = models.DateTimeField("date published", auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    group = models.ForeignKey(
        Group,
        # Надо исправить:
        # Объясняем, почему тут SET_NULL
        on_delete=models.SET_NULL,
        related_name="posts",
        blank=True,
        null=True
    )

    class Meta:
        # Можно лучше: Перенести ордеринг из вьюх в метакласс
        ordering = ("-pub_date",)
