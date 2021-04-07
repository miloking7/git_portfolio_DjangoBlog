from django.contrib import admin
from blog.models import Post

# Register your models here.

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('id','title','modify_dt', 'tag_list')
    list_filter =('modify_dt',)    #수정 날짜 중심으로 필터링할 수 있도록
    search_fields=('title','content')
    prepopulated_fields ={'slug':('title',)} #타이틀을 가지고 슬러그라는 캄럼에 미리 채워지도록한다
    
    #admin.site.register(Post)
    #두 메소드 추가
    def get_queryset(self, request):
        return super().get_queryset(request).prefetch_related('tags') 
    
    def tag_list(self, obj):
        return ',' .join(o.name for o in obj.tags.all())