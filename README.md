# Interactive Teaching Platform

**Author:** Tamim Islam

**Role:** Project Engineer, Raktch Technology & Software

A Django-based web application for creating and displaying rich, interactive learning articles. Authors manage content through the Django admin panel; students view a fully interactive frontend with multimedia cards, clickable annotation terms, and expandable sections.

---

## Features

- **Rich Article Editor** — Body content powered by CKEditor 5, supporting text formatting, images, tables, and embedded YouTube videos.
- **Media Cards** — Grid of clickable cards (text, image, audio, video, YouTube) that open in a modal overlay.
- **Hyperlink Annotations** — Highlight specific terms in the article body; clicking a term opens a popup with rich supporting information.
- **Expandable Sections** — Accordion-style sidebar panels with CKEditor content, open/collapsed individually.
- **YouTube Auto-Embed** — YouTube URLs pasted into any CKEditor field (article body, annotations, expandable sections) are automatically rendered as responsive video players on the frontend.
- **Inline Search** — Article list page includes a live client-side search that filters by title and body preview.
- **Mobile Responsive** — All pages are fully responsive across phones, tablets, and desktops.

---

## Tech Stack

| Layer        | Technology                          |
|--------------|-------------------------------------|
| Backend      | Python 3.12, Django 6.0             |
| Editor       | django-ckeditor-5 0.2.20            |
| Frontend     | Bootstrap 5.3, Bootstrap Icons 1.10 |
| Database     | SQLite (development)                |
| Media        | Pillow 12 (image/file uploads)      |

---

## Project Structure

```
Interactive-Teaching-Platform/
├── core/                        # Django project config
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py / asgi.py
├── teaching_platform/           # Main app
│   ├── models.py                # Article, MediaCard, HyperlinkAnnotation, ExpandableSection
│   ├── views.py                 # article_list, article_detail
│   ├── admin.py                 # Admin registrations
│   ├── urls.py
│   ├── migrations/
│   └── templates/
│       └── teaching/
│           ├── article_list.html
│           └── article_detail.html
├── media/                       # Uploaded files (icons, images, audio, video)
├── manage.py
└── requirements.txt
```

---

## Data Models

### `Article`
The top-level content object. Has a `slug` for clean URLs.

| Field          | Type             | Notes                    |
|----------------|------------------|--------------------------|
| `title`        | CharField        |                          |
| `slug`         | SlugField        | Unique, used in URL      |
| `body_content` | CKEditor5Field   | Supports rich HTML + embeds |
| `created_at`   | DateTimeField    | Auto-set on creation     |

### `MediaCard`
Clickable cards attached to an article. Displayed in a grid at the top of the article page.

| Field          | Type       | Notes                                      |
|----------------|------------|--------------------------------------------|
| `article`      | ForeignKey |                                            |
| `title`        | CharField  |                                            |
| `card_type`    | CharField  | `text`, `image`, `audio`, `video`, `youtube` |
| `icon`         | FileField  | Optional custom icon image                 |
| `file`         | FileField  | Used for image/audio/video types           |
| `youtube_url`  | URLField   | Used for youtube type                      |
| `text_content` | TextField  | Used for text type                         |
| `css_class`    | CharField  | Bootstrap classes applied to card title    |
| `order`        | IntegerField | Controls display order                   |

### `HyperlinkAnnotation`
Terms that get highlighted inline within the article body. Clicking them opens a modal.

| Field      | Type           | Notes                          |
|------------|----------------|--------------------------------|
| `article`  | ForeignKey     |                                |
| `term`     | CharField      | Exact text matched in body     |
| `info_body`| CKEditor5Field | Rich content shown in modal    |
| `css_class`| CharField      | Styling applied to the term span |
| `order`    | IntegerField   |                                |

### `ExpandableSection`
Accordion panels in the right sidebar.

| Field          | Type           | Notes                     |
|----------------|----------------|---------------------------|
| `article`      | ForeignKey     |                           |
| `title`        | CharField      |                           |
| `content_body` | CKEditor5Field | Rich content inside panel |
| `order`        | IntegerField   |                           |
| `is_open`      | BooleanField   | Default expanded state    |

---

## Setup & Installation

### 1. Clone the repository

```bash
git clone <repo-url>
cd Interview
```

### 2. Create and activate a virtual environment

```bash
python -m venv venv
# Windows
venv\Scripts\activate
# macOS / Linux
source venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Apply migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

### 5. Create a superuser

```bash
python manage.py createsuperuser
```

### 6. Run the development server

```bash
python manage.py runserver
```

Open [http://127.0.0.1:8000/](http://127.0.0.1:8000/) in your browser.

---

## Usage

1. Go to [http://127.0.0.1:8000/admin/](http://127.0.0.1:8000/admin/) and log in.
2. Create an **Article** — fill in the title, slug, and body content. You can paste a YouTube URL directly in the CKEditor body; it will render as an embedded player on the frontend.
3. Add **Media Cards** linked to the article — choose the type and fill in the relevant file/URL/text fields.
4. Add **Hyperlink Annotations** — enter the exact term as it appears in the body; the view will auto-wrap it in a clickable span.
5. Add **Expandable Sections** for sidebar content.
6. Visit [http://127.0.0.1:8000/](http://127.0.0.1:8000/) to see the article list, then click an article to view the interactive detail page.

---

## URL Routes

| URL                  | View             | Name             |
|----------------------|------------------|------------------|
| `/`                  | `article_list`   | `article_list`   |
| `/<slug>/`           | `article_detail` | `article_detail` |
| `/admin/`            | Django Admin     | —                |

---

## Notes

- The project uses SQLite for development. For production, switch to PostgreSQL or another robust database in `settings.py`.
- `DEBUG = True` and `SECRET_KEY` are currently hardcoded. Move them to environment variables before any deployment.
- Uploaded media files are served via Django's development media server (`MEDIA_URL`). Configure a proper static/media file server (e.g. Nginx, AWS S3) for production.

