import enum
from utils.functions import db, generate_password_hash, check_password_hash,datetime


class BaseModel(object):
    # 定义基础的模型
    create_time = db.Column(db.DATETIME, default=datetime.now)
    update_time = db.Column(db.DATETIME, default=datetime.now, onupdate=datetime.now)

    def add_update(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()


# 用户信息
class Customer(BaseModel, db.Model):

    __tablename__ = 'customer'

    id = db.Column(db.INTEGER, primary_key=True, autoincrement=True)
    phone = db.Column(db.String(11), unique=True)  # 电话
    pwd_hash = db.Column(db.String(200))  # 密码 哈希
    name = db.Column(db.String(30), unique=True)   # 名字
    avatar = db.Column(db.String(100))  # 头像
    id_name = db.Column(db.String(30))  # 实名认证的姓名
    id_card = db.Column(db.String(18), unique=True)  # 实名认证的身份证号码

    is_merchant = db.Column(db.Boolean, default=False)  # 是否商家

    customer_shipping_address = db.relationship('CustomerShippingAddress', backref='user')  # 关联到收货地址
    goods = db.relationship('Goods', backref='user')  # 关联到商品表
    orders = db.relationship('Order', backref='user')  # 关联到订单表
    goods_comments = db.relationship('GoodsComments', backref='user')  # 关联商品评价



# 客户收获地址
class CustomerShippingAddress(BaseModel, db.Model):

    __tablename__ = 'customer_shipping_address'
    id = db.Column(db.INTEGER, primary_key=True, autoincrement=True)
    user_id = db.Column(db.Integer, db.ForeignKey("customer.id"), nullable=False)  # 客户编号
    area_id = db.Column(db.Integer, db.ForeignKey("citys.id"))  # 归属地编号
    name = db.Column(db.String(50))  # 收件人姓名
    tel = db.Column(db.String(50))  # 联系电话
    about_address = db.Column(db.String(255))  # 地址详情
    disabled = db.Column(db.Boolean, default=False)  # 是否默认地址


class Citys(BaseModel, db.Model):
    '''地区表'''
    __tablename__ = 'citys'
    id = db.Column(db.INTEGER, primary_key=True, autoincrement=True)  # id自增
    province = db.Column(db.String(200))  # 城市
    parent_id = db.Column(db.Integer, nullable=True)

    areas = db.relationship('CustomerShippingAddress', backref='city')  # 关联到客户收获地址


ORDER_ENUM = {
    'WAIT_ACCEPT': '待接单',
    'WAIT_PAYMENT': '待支付',
    'PAID': '已支付',
    'WAIT_COMMENT': '待评价',
    'COMPLETE': '已完成',
    'CANCELED': '已取消',
    'REJECTED': '已拒单'
}

ORDER_CODE = {
    'WAIT_ACCEPT': '1',
    'WAIT_PAYMENT': '2',
    'PAID': '3',
    'WAIT_COMMENT': '4',
    'COMPLETE': '5',
    'CANCELED': '6',
    'REJECTED': '0'
}

goodscomments_goods_order = db.Table(
    "goodscomments_goods_order",
    db.Column('goods_id', db.Integer, db.ForeignKey("goods.id"), primary_key=True),  # 商品id
    db.Column('order_id', db.Integer, db.ForeignKey("order.id"), primary_key=True),  # 订单id
    # db.Column('comments_id', db.Integer, db.ForeignKey("GoodsComments.id"), primary_key=True),  # 订单id
)

# inventory_goods_order = db.Table(
#     "inventory_goods_order",
#     db.Column('goods_id', db.Integer, db.ForeignKey("goods.id"), primary_key=True),  # 商品id
#     db.Column('order_id', db.Integer, db.ForeignKey("order.id"), primary_key=True),  # 订单id
#     db.Column('inventory_id', db.Integer, db.ForeignKey("Inventory.id"), primary_key=True),  # 订单id
# )
goods_goodsclassification = db.Table(
    "goods_goodsclassification",
    db.Column('goods_id', db.Integer, db.ForeignKey("goods.id"), primary_key=True),  # 商品id
    db.Column('good_classification_id', db.Integer, db.ForeignKey("good_classification.id"), primary_key=True),  # 订单id
    # db.Column('comments_id', db.Integer, db.ForeignKey("GoodsComments.id"), primary_key=True),  # 订单id
)

class Order(BaseModel, db.Model):
    # 订单
    __tablename__ = "order"
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("customer.id"), nullable=False)  # 客户id
    goods_id = db.Column(db.Integer, db.ForeignKey("goods.id"), nullable=False)  # 商品id
    goods_price = db.Column(db.Integer, nullable=False)  # 商品价格
    amount = db.Column(db.Integer, nullable=False)  # 总价格
    note = db.Column(db.String(200), nullable=True)  # 备注
    status = db.Column(
        db.Enum(*ORDER_ENUM.keys()),
        default="WAIT_ACCEPT", index=True)
    comment = db.Column(db.Text)  # 评论

    Goods = db.relationship("Goods", secondary=goodscomments_goods_order)
    GoodsComments = db.relationship("GoodsComments", secondary=goodscomments_goods_order)


class Goods(BaseModel, db.Model):
    '''商品'''
    __tablename__ = 'goods'
    id = db.Column(db.INTEGER, primary_key=True, autoincrement=True)  # id自增
    title = db.Column(db.String(64), nullable=False)  # 标题
    price = db.Column(db.Integer, default=0)  # 单价
    introduce = db.Column(db.String(200), nullable=False)  # 介绍
    details = db.Column(db.Text)  # 详情
    index_image_url = db.Column(db.String(255), default="")  # 商品图片的路径

    images = db.relationship('GoodsImage', backref='goods')  # 关联到商品的图片
    # orders = db.relationship('Order', backref='goods')  # 关联到订单
    # goods_comments = db.relationship('GoodsComments', backref='goods')  # 关联评价
    # good_classification_id = db.Column(db.Integer, db.ForeignKey("GoodsClassification.id"), nullable=False)  # 关联分类

    GoodsClassification = db.relationship("GoodsClassification", secondary=goods_goodsclassification)
    Order = db.relationship("Order", secondary=goodscomments_goods_order)
    GoodsComments = db.relationship("GoodsComments", secondary=goodscomments_goods_order)


class GoodsComments(BaseModel, db.Model):
    '''商品评价表'''
    __tablename__ = "goods_comments"
    id = db.Column(db.INTEGER, primary_key=True, autoincrement=True)
    user_id = db.Column(db.Integer, db.ForeignKey("customer.id"))  # 客户id
    # order_status = db.Column(db.String(255), db.ForeignKey("order.status"))  # 订单状态
    evaluate = db.Column(db.String(255))  # 评价
    reply_id = db.Column(db.Integer, nullable=True)  # 回复id

    Order = db.relationship("Order", secondary=goodscomments_goods_order)
    Goods = db.relationship("Goods", secondary=goodscomments_goods_order)


class GoodsClassification(BaseModel, db.Model):
    '''商品分类'''
    __tablename__ = 'good_classification'
    id = db.Column(db.INTEGER, primary_key=True, autoincrement=True)  # id自增
    c_title = db.Column(db.String(64), nullable=False)  # 标题
    parent_id = db.Column(db.INTEGER)
    # goods = db.relationship('Goods', backref='good_classification')  # 关联到商品
    goods = db.relationship("Goods", secondary=goods_goodsclassification)


class GoodsImage(BaseModel, db.Model):
    """商品图片"""
    __tablename__ = "goods_image"
    id = db.Column(db.Integer, primary_key=True)
    goods_id = db.Column(db.Integer, db.ForeignKey("goods.id"), nullable=False)  # 商品id
    url = db.Column(db.String(255), nullable=False)  # 图片的路径

class Inventory(BaseModel, db.Model):
    '''库存'''
    __tablename__ = "inventory"
    id = db.Column(db.INTEGER, primary_key=True, autoincrement=True)  # id自增
    goods_id = db.Column(db.Integer)  # 商品id
    order_id = db.Column(db.Integer)  # 订单id
    order_status = db.Column(db.String(255))  # 订单状态
    i_number = db.Column(db.Integer, default=0)  # 库存数量
    shape_code = db.Column(db.String(200))  # 条形码


class ReportedLoss(BaseModel, db.Model):
    '''报损失'''
    __tablename__ = "reportedloss"
    id = db.Column(db.INTEGER, primary_key=True, autoincrement=True)  # id自增
    # create_time = db.Column(db.DATETIME, default=datetime.now)  # 创建时间
    goods_id = db.Column(db.Integer)  # 商品id
    inventory = db.Column(db.Integer)  # 库存id
