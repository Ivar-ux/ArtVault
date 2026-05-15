from django.shortcuts import render, get_object_or_404, redirect
from .models import Artwork, Bid  # Added Bid here
from .forms import BidForm, FinalizationForm  # Added FinalizationForm here

def artwork_catalogue(request):
    """
    Handles UC-02: Search and Browse.
    """
    artworks = Artwork.objects.all()
    query = request.GET.get('search')
    if query:
        artworks = artworks.filter(title__icontains=query)
    return render(request, 'catalogue.html', {'artworks': artworks})


def artwork_detail(request, artwork_id):
    """
    Handles UC-03 (Details) and UC-04 (Bidding).
    """
    # 1. FIXED: Changed pk=pk to id=artwork_id
    artwork = get_object_or_404(Artwork, id=artwork_id)

    # 2. FIXED: Changed exclude(pk=pk) to exclude(id=artwork_id)
    other_artworks = Artwork.objects.filter(seller=artwork.seller).exclude(id=artwork_id)

    if request.method == 'POST':
        if not request.user.is_authenticated:
            return redirect('admin:login')

        form = BidForm(request.POST)
        if form.is_valid():
            bid = form.save(commit=False)
            bid.artwork = artwork
            bid.user = request.user
            bid.save()
            # 3. FIXED: Changed pk=pk to artwork_id=artwork_id to match your main urls.py name
            return redirect('artwork_detail', artwork_id=artwork_id)
    else:
        form = BidForm()

    return render(request, 'artwork_detail.html', {
        'artwork': artwork,
        'other_artworks': other_artworks,
        'form': form
    })

def checkout_step(request, bid_id):
    """
    Handles UC-05: 3-step checkout and finalization.
    """
    bid = get_object_or_404(Bid, id=bid_id)

    # Security check: Only the user who placed the bid can finalize
    if bid.user != request.user:
        return redirect('catalogue')

    if request.method == 'POST':
        form = FinalizationForm(request.POST)
        if form.is_valid():
            finalization = form.save(commit=False)
            finalization.bid = bid
            finalization.save()

            # Update Artwork status to 'Sold' per requirements
            bid.artwork.sold_status = 'Sold'
            bid.artwork.save()

            return render(request, 'checkout_success.html', {'artwork': bid.artwork})
    else:
        form = FinalizationForm()

    return render(request, 'checkout.html', {'form': form, 'bid': bid})