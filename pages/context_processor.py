from pages.models import Page

# Get Pages:
def get_pages(request):
    pages = Page.objects.filter(visible=True).order_by('order').values_list('id', 'title', 'slug')
    return {'pages': pages}