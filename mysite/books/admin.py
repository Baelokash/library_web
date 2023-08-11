from django.contrib import admin
from .models import Books
from .models import Readers
from .models import Issuance
from .models import Notice

class BooksTab(admin.ModelAdmin):
    list_display=['id_book','title','author','year_publication','place_publication','number_pages','price','category','type','method_issue']
    # редактировние сразу в таблице а не в карточке list_editable=['title','author','year_publication','place_publication','number_pages','price','category','type','method_issue']
    # количество записей на страице list_per_page = 10 
    search_fields = ['title' , 'author']

class ReadersTab(admin.ModelAdmin):
    list_display=['id_person','surname','name','patronymic','passport_birth_certificate','e_mail'] 
    search_fields = ['surname' , 'name' , 'patronymic'] 

class IssuanceTab(admin.ModelAdmin):
    list_display=['id_issuance','id_book','id_person','date','status'] 
    search_fields = ['id_book' , 'id_person']

class NoticeTab(admin.ModelAdmin):
    list_display=['id_notice','fio','count_books','e_mail','refund_period' , 'text_in'] 
    search_fields = ['fio' , 'text_in']      

admin.site.register(Readers , ReadersTab)
admin.site.register(Issuance , IssuanceTab)
admin.site.register(Books , BooksTab)
admin.site.register(Notice , NoticeTab) 
 

