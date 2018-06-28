"""MxShop URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
# from django.contrib import admin
import xadmin
from MxShop.settings import MEDIA_ROOT
from django.views.static import serve

from rest_framework.documentation import include_docs_urls
from rest_framework.routers import DefaultRouter
from rest_framework_jwt.views import obtain_jwt_token
from rest_framework.authtoken import views


# view_base url

# from goods.views_base import GoodsListView


from goods.views import GoodsListViewSet, CategoryViewset
from user_operation.views import UserFavViewset


router = DefaultRouter()

# 配置 goods 的 url
router.register(r'goods', GoodsListViewSet, base_name='goods')

# 配置 categorys 的 url
router.register(r'categorys', CategoryViewset, base_name='categorys')

# 用户收藏 的 url
router.register(r'userfavs', UserFavViewset, base_name='userfavs')


urlpatterns = [

    url(r'^xadmin/', xadmin.site.urls),

    # 配置上传文件的访问处理函数
    url(r'^media/(?P<path>.*)$', serve, {'document_root': MEDIA_ROOT}),

    # DRF 自动文档URL
    url(r'^docs/', include_docs_urls(title='慕学生鲜')),

    # DRF 登陆
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),

    # TokenAuthentication
    url(r'^api-token-auth/', views.obtain_auth_token),

    # The API URLs are now determined automatically by the router.
    url(r'^', include(router.urls)),


    # JWT 的认证接口
    url(r'^login/', obtain_jwt_token),
]
