from django.shortcuts import render
from django.core.paginator import Paginator
from django.shortcuts import get_object_or_404

# Create your views here.

from .models import Listing


def index(request):
    listings = Listing.objects.order_by('-list_date').filter(is_published=True)
    paginator = Paginator(listings, 3)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    context = {
        'listings': page_obj,
        'page_obj': page_obj,
        'has_next': page_obj.has_next(),
        'has_previous': page_obj.has_previous(),
    }
    return render(request, 'listings/listings.html', context)


def listing(request, listing_id):
    listing = get_object_or_404(Listing, pk=listing_id)

    context = {
        'listing': listing
    }

    return render(request, 'listings/listing.html', context)



