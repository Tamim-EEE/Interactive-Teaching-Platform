from django.shortcuts import get_object_or_404, render
from .models import Article
import json


# Get Article List
def article_list(request):
    articles = Article.objects.all().order_by("-created_at")
    return render(request, "teaching/article_list.html", {"articles": articles})


# Get Article Detail
def article_detail(request, slug):
    article = get_object_or_404(Article, slug=slug)

    annotations = {}
    annotation_css = {}
    for a in article.annotations.all():
        annotations[a.term] = a.info_body
        annotation_css[a.term] = a.css_class or "text-danger fw-bold"

    def annotate_html(raw_html):
        annotated = raw_html
        for term, css_class in annotation_css.items():
            span = (
                f'<span class="annotation-link {css_class}" '
                f'style="cursor:pointer;" '
                f'data-term="{term}">{term}</span>'
            )
            annotated = annotated.replace(term, span, 1)
        return annotated

    body = annotate_html(article.body_content)

    sections = []
    for section in article.expandable_sections.all():
        sections.append(
            {
                "id": section.id,
                "title": annotate_html(section.title),
                "content_body": annotate_html(section.content_body),
                "is_open": section.is_open,
            }
        )

    return render(
        request,
        "teaching/article_detail.html",
        {
            "article": article,
            "annotated_body": body,
            "media_cards": article.media_cards.all(),
            "sections": sections,
            "annotations_json": json.dumps(annotations),
        },
    )
