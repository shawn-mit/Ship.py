from django.test import TestCase

# Create your tests here.

"""



```def get_products_of_type(request, pk):
    product_type = models.ProductType.objects.filter(id=pk)
    products = models.Product.objects.filter(product_type=pk)
    return render(request, 'initial_site/product_list.html', {
        'product_list': products,
        'product_type': product_type[0]
    })
```

[7:50]  
so that return render takes in: 
`request` which comes in automatically to a view,
`template` aka initial_site/product_list.html,
`dictionary` this can have as many key value pairs as you want for the needed data

[7:50]  
`return render(request, template, dictionary)` (edited)

"""