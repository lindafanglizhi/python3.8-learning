import pytest

@pytest.mark.usefixtures("login")
def test_pay(con_db):
    print("支付")

@pytest.mark.usefixtures("login")
def test_addcart(con_db):
    print("添加到购物车")

def test_see_shop():
    print("查询想要的商品")
