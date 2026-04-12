from django.contrib import admin
from .models import Article, MediaCard, HyperlinkAnnotation, ExpandableSection


# MediaCard inline for managing media cards directly from the Article admin page
class MediaCardInline(admin.TabularInline):
    model = MediaCard
    extra = 0
    fields = (
        "title",
        "css_class",
        "card_type",
        "icon",
        "file",
        "youtube_url",
        "text_content",
        "order",
    )


# HyperlinkAnnotation inline for managing annotations directly from the Article admin page
class HyperlinkAnnotationInline(admin.StackedInline):
    model = HyperlinkAnnotation
    extra = 0


# ExpandableSection inline for managing collapsible sections directly from the Article admin page
class ExpandableSectionInline(admin.StackedInline):
    model = ExpandableSection
    extra = 0


# Registered the Article model with the custom admin configuration
@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}
    inlines = [MediaCardInline, HyperlinkAnnotationInline, ExpandableSectionInline]
