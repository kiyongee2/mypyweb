# 장바구니 - 세션(session)
from django.conf import settings


class Cart:
    def __init__(self, request):
        self.session = request.session # 세션 발급
        cart = self.session.get(settings.CART_ID) # 장바구니 생성
        if not cart:
            cart = self.session[settings.CART_ID] = {}  #빈 딕셔너리 생성
        self.cart = cart  #세션에서 가져온 카트

    def __len__(self): # 수량 합계
        return sum(item['quantity'] for item in self.cart.values())

    def __iter__(self):  #반복 매세드
        products_ids = self.cart.keys()  #제품 번호 리스트