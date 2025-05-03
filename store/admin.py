from django.contrib import admin
<<<<<<< HEAD
from .models import Product, Variation, ReviewRating, ProductGallery
import admin_thumbnails

@admin_thumbnails.thumbnail('image')
class ProductGalleryInline(admin.TabularInline):
    model = ProductGallery
    extra = 1
=======
from .models import Product, Variation, ReviewRating    

>>>>>>> 6279ca3506e3df2c5e607c86e0ec763a2aeae867

class ProductAdmin(admin.ModelAdmin):
    list_display = ('product_name', 'price', 'stock', 'category', 'modified_date', 'is_available')
    prepopulated_fields = {'slug': ('product_name',)}
<<<<<<< HEAD
    inlines = [ProductGalleryInline]
=======
>>>>>>> 6279ca3506e3df2c5e607c86e0ec763a2aeae867

class variationAdmin(admin.ModelAdmin):
    list_display = ('product', 'variation_category', 'variation_value', 'is_active')
    list_filter = ('product', 'variation_category', 'variation_value')
    list_editable = ('is_active',)

admin.site.register(Product, ProductAdmin)
admin.site.register(Variation, variationAdmin)
admin.site.register(ReviewRating)
<<<<<<< HEAD
admin.site.register(ProductGallery)

=======
>>>>>>> 6279ca3506e3df2c5e607c86e0ec763a2aeae867
