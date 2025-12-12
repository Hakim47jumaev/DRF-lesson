

def search_by_title(data,request):
    search=request.GET.get('search')
    if search:
        data=data.filter(title__icontains=search)
    
    return data