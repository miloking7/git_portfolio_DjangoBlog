from django.contrib import admin
from photo.models import Photo, Album

# Register your models here.
#1. 외래 키로 연결된 album, photo 테이블 간 1대 다 관계 성립이 된다. 앨범 객체를 보여줄 때 객체에 열결된 사진 객체를 보여준다. 
#같이 보여주는 형식은 stackedInline과 TabularInline 두 가지가 있는데 여기서는 StackedlInline 세로로 나열되는 형식
#PhotoInline 클래스에서는 이런 사항을 정의하고 있다. 

class PhotoInline(admin.StackedInline):
#2 추가로 보여주눈 테이블은 Photo 테이블
    model = Photo
#3.이미 존재하는 객체 외에 추가로 입력할 수 있는 포토 테이블 객체 수는 2개 
    extra=2 
    
#4.앨범 객체 수정 화면을 보여줄 때 PhotoInline 클래스에서 정의한 사항 같이 보여준다
@admin.register(Album)
class AlbumAdmin(admin.ModelAdmin): 
    inlines=(PhotoInline,) 
    list_display=('id','name','description')
#5. Photo 와 PhotoAdmin 클래스 등록시 admin.site.register() 함수를 사용하지만 데코레이터를 사용하면 더 간단하다  
@admin.register(Photo)
class PhotoAdmin(admin.ModelAdmin): 
    list_display=('id','title','upload_dt')
    
