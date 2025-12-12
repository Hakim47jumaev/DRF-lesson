

def price_filter(data,request):
    min_price=request.GET.get('min_price')
    max_price=request.GET.get('max_price')

    if min_price:
        data=data.filter(price__gte=min_price)
    if max_price:
        data=data.filter(price__lte=max_price)
    

    return data