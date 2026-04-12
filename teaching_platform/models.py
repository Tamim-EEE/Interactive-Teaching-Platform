from django.db import models
from django_ckeditor_5.fields import CKEditor5Field


# Article model representing an article with rich text content
class Article(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(unique=True)
    body_content = CKEditor5Field(config_name="default")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


# MediaCard model for different types of media content associated with an article
CARD_TYPES = [
    ("text", "Text"),
    ("image", "Image"),
    ("audio", "Audio"),
    ("video", "Video (File)"),
    ("youtube", "YouTube"),
]


class MediaCard(models.Model):
    article = models.ForeignKey(
        Article, on_delete=models.CASCADE, related_name="media_cards"
    )
    title = models.CharField(max_length=100)
    card_type = models.CharField(max_length=10, choices=CARD_TYPES)
    icon = models.FileField(upload_to="media_card_icons/", blank=True, null=True)
    file = models.FileField(upload_to="media_cards/", blank=True, null=True)
    youtube_url = models.URLField(blank=True, null=True)
    text_content = models.TextField(blank=True, null=True)
    css_class = models.CharField(
        max_length=50, blank=True, default="text-danger fw-bold"
    )
    order = models.IntegerField(default=0)

    class Meta:
        ordering = ["order"]

    def __str__(self):
        return f"{self.title} ({self.card_type})"


# HyperlinkAnnotation model for annotating terms in the article body
class HyperlinkAnnotation(models.Model):
    article = models.ForeignKey(
        Article, on_delete=models.CASCADE, related_name="annotations"
    )
    term = models.CharField(max_length=100)
    info_body = CKEditor5Field(config_name="default")
    css_class = models.CharField(
        max_length=50, default="text-danger fw-bold", blank=True
    )
    order = models.IntegerField(default=0)

    class Meta:
        ordering = ["order"]

    def __str__(self):
        return self.term


# ExpandableSection model for collapsible sections in the article
class ExpandableSection(models.Model):
    article = models.ForeignKey(
        Article, on_delete=models.CASCADE, related_name="expandable_sections"
    )
    title = models.CharField(max_length=255)
    content_body = CKEditor5Field(config_name="default")
    order = models.IntegerField(default=0)
    is_open = models.BooleanField(default=False)

    class Meta:
        ordering = ["order"]

    def __str__(self):
        return self.title
