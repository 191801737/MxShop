from django.views.generic.base import View
# from django.views.generic import ListView
from goods.models import Goods

# 方式一 传统的写法
"""
class GoodsListView(View):
    def get(self, request):

        json_list = []
        goods = Goods.objects.all()[:10]
        for good in goods:
            json_dict = {}
            json_dict['name'] = good.name
            json_dict['category'] = good.category.name
            json_dict['market_price'] = good.market_price
            # json_dict['add_time'] = good.add_time  # Object of type 'datetime' is not JSON serializable
            json_list.append(json_dict)

        from django.http import HttpResponse, JsonResponse
        import json
        return HttpResponse(json.dumps(json_list), content_type='application/json')
        
"""


# 方法2 迭代写法 虽然代码已经很精简 但是传说drf更强大
class GoodsListView(View):
    def get(self, request):

        goods = Goods.objects.all()[:10]

        from django.core import serializers
        json_data = serializers.serialize('json', goods)

        from django.http import JsonResponse
        return JsonResponse(json_data, safe=False)
