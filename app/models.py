# coding: utf-8
from sqlalchemy import CHAR, Column, DECIMAL, Date, DateTime, Enum, Index, LargeBinary, String, TIMESTAMP, Table, Text, text
from sqlalchemy.dialects.mysql import BIGINT, CHAR, DECIMAL, INTEGER, LONGTEXT, MEDIUMINT, MEDIUMTEXT, SMALLINT, TINYINT, VARCHAR
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
metadata = Base.metadata


class EcsAccountLog(Base):
    __tablename__ = 'ecs_account_log'

    log_id = Column(MEDIUMINT(8), primary_key=True)
    user_id = Column(MEDIUMINT(8), nullable=False, index=True)
    user_money = Column(DECIMAL(10, 2), nullable=False)
    frozen_money = Column(DECIMAL(10, 2), nullable=False)
    rank_points = Column(MEDIUMINT(9), nullable=False)
    pay_points = Column(MEDIUMINT(9), nullable=False)
    change_time = Column(INTEGER(10), nullable=False)
    change_desc = Column(String(255), nullable=False)
    change_type = Column(TINYINT(3), nullable=False)


t_ecs_account_other_log = Table(
    'ecs_account_other_log', metadata,
    Column('user_id', MEDIUMINT(8), nullable=False),
    Column('order_id', MEDIUMINT(8), nullable=False),
    Column('order_sn', String(20), nullable=False),
    Column('money', DECIMAL(10, 2), nullable=False, server_default=text("'0.00'")),
    Column('pay_type', String(20), nullable=False),
    Column('pay_time', String(10), nullable=False),
    Column('change_desc', String(255), nullable=False)
)


class EcsAd(Base):
    __tablename__ = 'ecs_ad'

    ad_id = Column(SMALLINT(5), primary_key=True)
    position_id = Column(SMALLINT(5), nullable=False, index=True, server_default=text("'0'"))
    media_type = Column(TINYINT(3), nullable=False, server_default=text("'0'"))
    ad_name = Column(String(60), nullable=False, server_default=text("''"))
    ad_link = Column(String(255), nullable=False, server_default=text("''"))
    ad_code = Column(Text, nullable=False)
    start_time = Column(INTEGER(11), nullable=False, server_default=text("'0'"))
    end_time = Column(INTEGER(11), nullable=False, server_default=text("'0'"))
    link_man = Column(String(60), nullable=False, server_default=text("''"))
    link_email = Column(String(60), nullable=False, server_default=text("''"))
    link_phone = Column(String(60), nullable=False, server_default=text("''"))
    click_count = Column(MEDIUMINT(8), nullable=False, server_default=text("'0'"))
    enabled = Column(TINYINT(3), nullable=False, index=True, server_default=text("'1'"))


class EcsAdCustom(Base):
    __tablename__ = 'ecs_ad_custom'

    ad_id = Column(MEDIUMINT(8), primary_key=True)
    ad_type = Column(TINYINT(1), nullable=False, server_default=text("'1'"))
    ad_name = Column(String(60))
    add_time = Column(INTEGER(10), nullable=False, server_default=text("'0'"))
    content = Column(MEDIUMTEXT)
    url = Column(String(255))
    ad_status = Column(TINYINT(3), nullable=False, server_default=text("'0'"))


class EcsAdPosition(Base):
    __tablename__ = 'ecs_ad_position'

    position_id = Column(TINYINT(3), primary_key=True)
    position_name = Column(String(60), nullable=False, server_default=text("''"))
    ad_width = Column(SMALLINT(5), nullable=False, server_default=text("'0'"))
    ad_height = Column(SMALLINT(5), nullable=False, server_default=text("'0'"))
    position_desc = Column(String(255), nullable=False, server_default=text("''"))
    position_style = Column(Text, nullable=False)


class EcsAdminAction(Base):
    __tablename__ = 'ecs_admin_action'

    action_id = Column(TINYINT(3), primary_key=True)
    parent_id = Column(TINYINT(3), nullable=False, index=True, server_default=text("'0'"))
    action_code = Column(String(20), nullable=False, server_default=text("''"))
    relevance = Column(String(20), nullable=False, server_default=text("''"))


class EcsAdminLog(Base):
    __tablename__ = 'ecs_admin_log'

    log_id = Column(INTEGER(10), primary_key=True)
    log_time = Column(INTEGER(10), nullable=False, index=True, server_default=text("'0'"))
    user_id = Column(TINYINT(3), nullable=False, index=True, server_default=text("'0'"))
    log_info = Column(String(255), nullable=False, server_default=text("''"))
    ip_address = Column(String(15), nullable=False, server_default=text("''"))


class EcsAdminMessage(Base):
    __tablename__ = 'ecs_admin_message'
    __table_args__ = (
        Index('sender_id', 'sender_id', 'receiver_id'),
    )

    message_id = Column(SMALLINT(5), primary_key=True)
    sender_id = Column(TINYINT(3), nullable=False, server_default=text("'0'"))
    receiver_id = Column(TINYINT(3), nullable=False, index=True, server_default=text("'0'"))
    sent_time = Column(INTEGER(11), nullable=False, server_default=text("'0'"))
    read_time = Column(INTEGER(11), nullable=False, server_default=text("'0'"))
    readed = Column(TINYINT(1), nullable=False, server_default=text("'0'"))
    deleted = Column(TINYINT(1), nullable=False, server_default=text("'0'"))
    title = Column(String(150), nullable=False, server_default=text("''"))
    message = Column(Text, nullable=False)


class EcsAdminUser(Base):
    __tablename__ = 'ecs_admin_user'

    user_id = Column(SMALLINT(5), primary_key=True)
    user_name = Column(String(60), nullable=False, index=True, server_default=text("''"))
    email = Column(String(60), nullable=False, server_default=text("''"))
    password = Column(String(32), nullable=False, server_default=text("''"))
    ec_salt = Column(String(10))
    add_time = Column(INTEGER(11), nullable=False, server_default=text("'0'"))
    last_login = Column(INTEGER(11), nullable=False, server_default=text("'0'"))
    last_ip = Column(String(15), nullable=False, server_default=text("''"))
    action_list = Column(Text, nullable=False)
    nav_list = Column(Text, nullable=False)
    lang_type = Column(String(50), nullable=False, server_default=text("''"))
    agency_id = Column(SMALLINT(5), nullable=False, index=True)
    suppliers_id = Column(SMALLINT(5), server_default=text("'0'"))
    todolist = Column(LONGTEXT)
    role_id = Column(SMALLINT(5))
    passport_uid = Column(String(20))
    yq_create_time = Column(SMALLINT(11))


t_ecs_adsense = Table(
    'ecs_adsense', metadata,
    Column('from_ad', SMALLINT(5), nullable=False, index=True, server_default=text("'0'")),
    Column('referer', String(255), nullable=False, server_default=text("''")),
    Column('clicks', INTEGER(10), nullable=False, server_default=text("'0'"))
)


class EcsAffiliateLog(Base):
    __tablename__ = 'ecs_affiliate_log'

    log_id = Column(MEDIUMINT(8), primary_key=True)
    order_id = Column(MEDIUMINT(8), nullable=False)
    time = Column(INTEGER(10), nullable=False)
    user_id = Column(MEDIUMINT(8), nullable=False)
    user_name = Column(String(60))
    money = Column(DECIMAL(10, 2), nullable=False, server_default=text("'0.00'"))
    point = Column(INTEGER(10), nullable=False, server_default=text("'0'"))
    separate_type = Column(TINYINT(1), nullable=False, server_default=text("'0'"))


class EcsAgency(Base):
    __tablename__ = 'ecs_agency'

    agency_id = Column(SMALLINT(5), primary_key=True)
    agency_name = Column(String(255), nullable=False, index=True)
    agency_desc = Column(Text, nullable=False)


class EcsAreaRegion(Base):
    __tablename__ = 'ecs_area_region'

    shipping_area_id = Column(SMALLINT(5), primary_key=True, nullable=False, server_default=text("'0'"))
    region_id = Column(SMALLINT(5), primary_key=True, nullable=False, server_default=text("'0'"))


class EcsArticle(Base):
    __tablename__ = 'ecs_article'

    article_id = Column(MEDIUMINT(8), primary_key=True)
    cat_id = Column(SMALLINT(5), nullable=False, index=True, server_default=text("'0'"))
    title = Column(String(150), nullable=False, server_default=text("''"))
    content = Column(LONGTEXT, nullable=False)
    author = Column(String(30), nullable=False, server_default=text("''"))
    author_email = Column(String(60), nullable=False, server_default=text("''"))
    keywords = Column(String(255), nullable=False, server_default=text("''"))
    article_type = Column(TINYINT(1), nullable=False, server_default=text("'2'"))
    is_open = Column(TINYINT(1), nullable=False, server_default=text("'1'"))
    add_time = Column(INTEGER(10), nullable=False, server_default=text("'0'"))
    file_url = Column(String(255), nullable=False, server_default=text("''"))
    open_type = Column(TINYINT(1), nullable=False, server_default=text("'0'"))
    link = Column(String(255), nullable=False, server_default=text("''"))
    description = Column(String(255))


class EcsArticleCat(Base):
    __tablename__ = 'ecs_article_cat'

    cat_id = Column(SMALLINT(5), primary_key=True)
    cat_name = Column(String(255), nullable=False, server_default=text("''"))
    cat_type = Column(TINYINT(1), nullable=False, index=True, server_default=text("'1'"))
    keywords = Column(String(255), nullable=False, server_default=text("''"))
    cat_desc = Column(String(255), nullable=False, server_default=text("''"))
    sort_order = Column(TINYINT(3), nullable=False, index=True, server_default=text("'50'"))
    show_in_nav = Column(TINYINT(1), nullable=False, server_default=text("'0'"))
    parent_id = Column(SMALLINT(5), nullable=False, index=True, server_default=text("'0'"))


class EcsAttribute(Base):
    __tablename__ = 'ecs_attribute'

    attr_id = Column(SMALLINT(5), primary_key=True)
    cat_id = Column(SMALLINT(5), nullable=False, index=True, server_default=text("'0'"))
    attr_name = Column(String(60), nullable=False, server_default=text("''"))
    attr_input_type = Column(TINYINT(1), nullable=False, server_default=text("'1'"))
    attr_type = Column(TINYINT(1), nullable=False, server_default=text("'1'"))
    attr_values = Column(Text, nullable=False)
    attr_index = Column(TINYINT(1), nullable=False, server_default=text("'0'"))
    sort_order = Column(TINYINT(3), nullable=False, server_default=text("'0'"))
    is_linked = Column(TINYINT(1), nullable=False, server_default=text("'0'"))
    attr_group = Column(TINYINT(1), nullable=False, server_default=text("'0'"))


class EcsAuctionLog(Base):
    __tablename__ = 'ecs_auction_log'

    log_id = Column(MEDIUMINT(8), primary_key=True)
    act_id = Column(MEDIUMINT(8), nullable=False, index=True)
    bid_user = Column(MEDIUMINT(8), nullable=False)
    bid_price = Column(DECIMAL(10, 2), nullable=False)
    bid_time = Column(INTEGER(10), nullable=False)


class EcsAutoManage(Base):
    __tablename__ = 'ecs_auto_manage'

    item_id = Column(MEDIUMINT(8), primary_key=True, nullable=False)
    type = Column(String(10), primary_key=True, nullable=False)
    starttime = Column(INTEGER(10), nullable=False)
    endtime = Column(INTEGER(10), nullable=False)


class EcsBackGood(Base):
    __tablename__ = 'ecs_back_goods'

    rec_id = Column(MEDIUMINT(8), primary_key=True)
    back_id = Column(MEDIUMINT(8), index=True, server_default=text("'0'"))
    goods_id = Column(MEDIUMINT(8), nullable=False, index=True, server_default=text("'0'"))
    product_id = Column(MEDIUMINT(8), nullable=False, server_default=text("'0'"))
    product_sn = Column(String(60))
    goods_name = Column(String(120))
    brand_name = Column(String(60))
    goods_sn = Column(String(60))
    is_real = Column(TINYINT(1), server_default=text("'0'"))
    send_number = Column(SMALLINT(5), server_default=text("'0'"))
    goods_attr = Column(Text)


class EcsBackOrder(Base):
    __tablename__ = 'ecs_back_order'

    back_id = Column(MEDIUMINT(8), primary_key=True)
    delivery_sn = Column(String(20), nullable=False)
    order_sn = Column(String(20), nullable=False)
    order_id = Column(MEDIUMINT(8), nullable=False, index=True, server_default=text("'0'"))
    invoice_no = Column(String(50))
    add_time = Column(INTEGER(10), server_default=text("'0'"))
    shipping_id = Column(TINYINT(3), server_default=text("'0'"))
    shipping_name = Column(String(120))
    user_id = Column(MEDIUMINT(8), index=True, server_default=text("'0'"))
    action_user = Column(String(30))
    consignee = Column(String(60))
    address = Column(String(250))
    country = Column(SMALLINT(5), server_default=text("'0'"))
    province = Column(SMALLINT(5), server_default=text("'0'"))
    city = Column(SMALLINT(5), server_default=text("'0'"))
    district = Column(SMALLINT(5), server_default=text("'0'"))
    sign_building = Column(String(120))
    email = Column(String(60))
    zipcode = Column(String(60))
    tel = Column(String(60))
    mobile = Column(String(60))
    best_time = Column(String(120))
    postscript = Column(String(255))
    how_oos = Column(String(120))
    insure_fee = Column(DECIMAL(10, 2), server_default=text("'0.00'"))
    shipping_fee = Column(DECIMAL(10, 2), server_default=text("'0.00'"))
    update_time = Column(INTEGER(10), server_default=text("'0'"))
    suppliers_id = Column(SMALLINT(5), server_default=text("'0'"))
    status = Column(TINYINT(1), nullable=False, server_default=text("'0'"))
    return_time = Column(INTEGER(10), server_default=text("'0'"))
    agency_id = Column(SMALLINT(5), server_default=text("'0'"))


class EcsBonusType(Base):
    __tablename__ = 'ecs_bonus_type'

    type_id = Column(SMALLINT(5), primary_key=True)
    type_name = Column(String(60), nullable=False, server_default=text("''"))
    type_money = Column(DECIMAL(10, 2), nullable=False, server_default=text("'0.00'"))
    send_type = Column(TINYINT(3), nullable=False, server_default=text("'0'"))
    min_amount = Column(DECIMAL(10, 2), nullable=False, server_default=text("'0.00'"))
    max_amount = Column(DECIMAL(10, 2), nullable=False, server_default=text("'0.00'"))
    send_start_date = Column(INTEGER(11), nullable=False, server_default=text("'0'"))
    send_end_date = Column(INTEGER(11), nullable=False, server_default=text("'0'"))
    use_start_date = Column(INTEGER(11), nullable=False, server_default=text("'0'"))
    use_end_date = Column(INTEGER(11), nullable=False, server_default=text("'0'"))
    min_goods_amount = Column(DECIMAL(10, 2), nullable=False, server_default=text("'0.00'"))


class EcsBookingGood(Base):
    __tablename__ = 'ecs_booking_goods'

    rec_id = Column(MEDIUMINT(8), primary_key=True)
    user_id = Column(MEDIUMINT(8), nullable=False, index=True, server_default=text("'0'"))
    email = Column(String(60), nullable=False, server_default=text("''"))
    link_man = Column(String(60), nullable=False, server_default=text("''"))
    tel = Column(String(60), nullable=False, server_default=text("''"))
    goods_id = Column(MEDIUMINT(8), nullable=False, server_default=text("'0'"))
    goods_desc = Column(String(255), nullable=False, server_default=text("''"))
    goods_number = Column(SMALLINT(5), nullable=False, server_default=text("'0'"))
    booking_time = Column(INTEGER(10), nullable=False, server_default=text("'0'"))
    is_dispose = Column(TINYINT(1), nullable=False, server_default=text("'0'"))
    dispose_user = Column(String(30), nullable=False, server_default=text("''"))
    dispose_time = Column(INTEGER(10), nullable=False, server_default=text("'0'"))
    dispose_note = Column(String(255), nullable=False, server_default=text("''"))


class EcsBrand(Base):
    __tablename__ = 'ecs_brand'

    brand_id = Column(SMALLINT(5), primary_key=True)
    brand_name = Column(String(60), nullable=False, server_default=text("''"))
    brand_logo = Column(String(80), nullable=False, server_default=text("''"))
    brand_desc = Column(Text, nullable=False)
    site_url = Column(String(255), nullable=False, server_default=text("''"))
    sort_order = Column(TINYINT(3), nullable=False, server_default=text("'50'"))
    is_show = Column(TINYINT(1), nullable=False, index=True, server_default=text("'1'"))


class EcsCallbackStatu(Base):
    __tablename__ = 'ecs_callback_status'
    __table_args__ = (
        Index('ind_type_type_id', 'type', 'type_id', unique=True),
    )

    id = Column(BIGINT(20), primary_key=True)
    msg_id = Column(String(50), server_default=text("''"))
    type = Column(String(100))
    status = Column(Enum('true', 'false', 'running'), index=True, server_default=text("'false'"))
    type_id = Column(String(50))
    date_time = Column(INTEGER(11), index=True)
    data = Column(Text)
    disabled = Column(Enum('true', 'false'), server_default=text("'false'"))
    times = Column(TINYINT(4), server_default=text("'0'"))
    method = Column(String(100), nullable=False)
    http_type = Column(String(20), nullable=False)


class EcsCard(Base):
    __tablename__ = 'ecs_card'

    card_id = Column(TINYINT(3), primary_key=True)
    card_name = Column(String(120), nullable=False, server_default=text("''"))
    card_img = Column(String(255), nullable=False, server_default=text("''"))
    card_fee = Column(DECIMAL(6, 2), nullable=False, server_default=text("'0.00'"))
    free_money = Column(DECIMAL(6, 2), nullable=False, server_default=text("'0.00'"))
    card_desc = Column(String(255), nullable=False, server_default=text("''"))


class EcsCart(Base):
    __tablename__ = 'ecs_cart'

    rec_id = Column(MEDIUMINT(8), primary_key=True)
    user_id = Column(MEDIUMINT(8), nullable=False, server_default=text("'0'"))
    session_id = Column(CHAR(32), nullable=False, index=True, server_default=text("''"))
    goods_id = Column(MEDIUMINT(8), nullable=False, server_default=text("'0'"))
    goods_sn = Column(String(60), nullable=False, server_default=text("''"))
    product_id = Column(MEDIUMINT(8), nullable=False, server_default=text("'0'"))
    goods_name = Column(String(120), nullable=False, server_default=text("''"))
    market_price = Column(DECIMAL(10, 2), nullable=False, server_default=text("'0.00'"))
    goods_price = Column(DECIMAL(10, 2), nullable=False, server_default=text("'0.00'"))
    goods_number = Column(SMALLINT(5), nullable=False, server_default=text("'0'"))
    goods_attr = Column(Text, nullable=False)
    is_real = Column(TINYINT(1), nullable=False, server_default=text("'0'"))
    extension_code = Column(String(30), nullable=False, server_default=text("''"))
    parent_id = Column(MEDIUMINT(8), nullable=False, server_default=text("'0'"))
    rec_type = Column(TINYINT(1), nullable=False, server_default=text("'0'"))
    is_gift = Column(SMALLINT(5), nullable=False, server_default=text("'0'"))
    is_shipping = Column(TINYINT(1), nullable=False, server_default=text("'0'"))
    can_handsel = Column(TINYINT(3), nullable=False, server_default=text("'0'"))
    goods_attr_id = Column(String(255), nullable=False, server_default=text("''"))


class EcsCatRecommend(Base):
    __tablename__ = 'ecs_cat_recommend'

    cat_id = Column(SMALLINT(5), primary_key=True, nullable=False)
    recommend_type = Column(TINYINT(1), primary_key=True, nullable=False)


class EcsCategory(Base):
    __tablename__ = 'ecs_category'

    cat_id = Column(SMALLINT(5), primary_key=True)
    cat_name = Column(String(90), nullable=False, server_default=text("''"))
    keywords = Column(String(255), nullable=False, server_default=text("''"))
    cat_desc = Column(String(255), nullable=False, server_default=text("''"))
    parent_id = Column(SMALLINT(5), nullable=False, index=True, server_default=text("'0'"))
    sort_order = Column(TINYINT(1), nullable=False, server_default=text("'50'"))
    template_file = Column(String(50), nullable=False, server_default=text("''"))
    measure_unit = Column(String(15), nullable=False, server_default=text("''"))
    show_in_nav = Column(TINYINT(1), nullable=False, server_default=text("'0'"))
    style = Column(String(150), nullable=False)
    is_show = Column(TINYINT(1), nullable=False, server_default=text("'1'"))
    grade = Column(TINYINT(4), nullable=False, server_default=text("'0'"))
    filter_attr = Column(String(255), nullable=False, server_default=text("'0'"))


class EcsCert(Base):
    __tablename__ = 'ecs_cert'

    id = Column(INTEGER(10), primary_key=True)
    config_id = Column(TINYINT(4), nullable=False, index=True)
    file = Column(LargeBinary, nullable=False)


class EcsCoincidence(Base):
    __tablename__ = 'ecs_coincidence'

    type_id = Column(String(100), primary_key=True, nullable=False)
    type = Column(String(20), primary_key=True, nullable=False)
    time = Column(INTEGER(11))


class EcsCollectGood(Base):
    __tablename__ = 'ecs_collect_goods'

    rec_id = Column(MEDIUMINT(8), primary_key=True)
    user_id = Column(MEDIUMINT(8), nullable=False, index=True, server_default=text("'0'"))
    goods_id = Column(MEDIUMINT(8), nullable=False, index=True, server_default=text("'0'"))
    add_time = Column(INTEGER(11), nullable=False, server_default=text("'0'"))
    is_attention = Column(TINYINT(1), nullable=False, index=True, server_default=text("'0'"))


class EcsComment(Base):
    __tablename__ = 'ecs_comment'

    comment_id = Column(INTEGER(10), primary_key=True)
    comment_type = Column(TINYINT(3), nullable=False, server_default=text("'0'"))
    id_value = Column(MEDIUMINT(8), nullable=False, index=True, server_default=text("'0'"))
    email = Column(String(60), nullable=False, server_default=text("''"))
    user_name = Column(String(60), nullable=False, server_default=text("''"))
    content = Column(Text, nullable=False)
    comment_rank = Column(TINYINT(1), nullable=False, server_default=text("'0'"))
    add_time = Column(INTEGER(10), nullable=False, server_default=text("'0'"))
    ip_address = Column(String(15), nullable=False, server_default=text("''"))
    status = Column(TINYINT(3), nullable=False, server_default=text("'0'"))
    parent_id = Column(INTEGER(10), nullable=False, index=True, server_default=text("'0'"))
    user_id = Column(INTEGER(10), nullable=False, server_default=text("'0'"))


class EcsConfig(Base):
    __tablename__ = 'ecs_config'

    id = Column(INTEGER(10), primary_key=True)
    name = Column(String(50), nullable=False)
    type = Column(String(50), nullable=False)
    description = Column(String(255), nullable=False)
    code = Column(String(50), nullable=False)
    config = Column(Text, nullable=False)
    status = Column(TINYINT(4), nullable=False, server_default=text("'0'"))
    created_at = Column(TIMESTAMP)
    updated_at = Column(TIMESTAMP)


class EcsCron(Base):
    __tablename__ = 'ecs_crons'

    cron_id = Column(TINYINT(3), primary_key=True)
    cron_code = Column(String(20), nullable=False, index=True)
    cron_name = Column(String(120), nullable=False)
    cron_desc = Column(Text)
    cron_order = Column(TINYINT(3), nullable=False, server_default=text("'0'"))
    cron_config = Column(Text, nullable=False)
    thistime = Column(INTEGER(10), nullable=False, server_default=text("'0'"))
    nextime = Column(INTEGER(10), nullable=False, index=True)
    day = Column(TINYINT(2), nullable=False)
    week = Column(String(1), nullable=False)
    hour = Column(String(2), nullable=False)
    minute = Column(String(255), nullable=False)
    enable = Column(TINYINT(1), nullable=False, index=True, server_default=text("'1'"))
    run_once = Column(TINYINT(1), nullable=False, server_default=text("'0'"))
    allow_ip = Column(String(100), nullable=False, server_default=text("''"))
    alow_files = Column(String(255), nullable=False)


class EcsDeliveryGood(Base):
    __tablename__ = 'ecs_delivery_goods'
    __table_args__ = (
        Index('delivery_id', 'delivery_id', 'goods_id'),
    )

    rec_id = Column(MEDIUMINT(8), primary_key=True)
    delivery_id = Column(MEDIUMINT(8), nullable=False, server_default=text("'0'"))
    goods_id = Column(MEDIUMINT(8), nullable=False, index=True, server_default=text("'0'"))
    product_id = Column(MEDIUMINT(8), server_default=text("'0'"))
    product_sn = Column(String(60))
    goods_name = Column(String(120))
    brand_name = Column(String(60))
    goods_sn = Column(String(60))
    is_real = Column(TINYINT(1), server_default=text("'0'"))
    extension_code = Column(String(30))
    parent_id = Column(MEDIUMINT(8), server_default=text("'0'"))
    send_number = Column(SMALLINT(5), server_default=text("'0'"))
    goods_attr = Column(Text)


class EcsDeliveryOrder(Base):
    __tablename__ = 'ecs_delivery_order'

    delivery_id = Column(MEDIUMINT(8), primary_key=True)
    delivery_sn = Column(String(20), nullable=False)
    order_sn = Column(String(20), nullable=False)
    order_id = Column(MEDIUMINT(8), nullable=False, index=True, server_default=text("'0'"))
    invoice_no = Column(String(50))
    add_time = Column(INTEGER(10), server_default=text("'0'"))
    shipping_id = Column(TINYINT(3), server_default=text("'0'"))
    shipping_name = Column(String(120))
    user_id = Column(MEDIUMINT(8), index=True, server_default=text("'0'"))
    action_user = Column(String(30))
    consignee = Column(String(60))
    address = Column(String(250))
    country = Column(SMALLINT(5), server_default=text("'0'"))
    province = Column(SMALLINT(5), server_default=text("'0'"))
    city = Column(SMALLINT(5), server_default=text("'0'"))
    district = Column(SMALLINT(5), server_default=text("'0'"))
    sign_building = Column(String(120))
    email = Column(String(60))
    zipcode = Column(String(60))
    tel = Column(String(60))
    mobile = Column(String(60))
    best_time = Column(String(120))
    postscript = Column(String(255))
    how_oos = Column(String(120))
    insure_fee = Column(DECIMAL(10, 2), server_default=text("'0.00'"))
    shipping_fee = Column(DECIMAL(10, 2), server_default=text("'0.00'"))
    update_time = Column(INTEGER(10), server_default=text("'0'"))
    suppliers_id = Column(SMALLINT(5), server_default=text("'0'"))
    status = Column(TINYINT(1), nullable=False, server_default=text("'0'"))
    agency_id = Column(SMALLINT(5), server_default=text("'0'"))


t_ecs_device = Table(
    'ecs_device', metadata,
    Column('user_id', INTEGER(11), nullable=False, unique=True),
    Column('device_id', String(200), nullable=False, index=True),
    Column('device_type', String(200), nullable=False, index=True),
    Column('platform_type', String(200), nullable=False, index=True),
    Column('status', TINYINT(4), nullable=False, index=True, server_default=text("'1'")),
    Column('created_at', TIMESTAMP),
    Column('updated_at', TIMESTAMP)
)


class EcsEmailList(Base):
    __tablename__ = 'ecs_email_list'

    id = Column(MEDIUMINT(8), primary_key=True)
    email = Column(String(60), nullable=False)
    stat = Column(TINYINT(1), nullable=False, server_default=text("'0'"))
    hash = Column(String(10), nullable=False)


class EcsEmailSendlist(Base):
    __tablename__ = 'ecs_email_sendlist'

    id = Column(MEDIUMINT(8), primary_key=True)
    email = Column(String(100), nullable=False)
    template_id = Column(MEDIUMINT(8), nullable=False)
    email_content = Column(Text, nullable=False)
    error = Column(TINYINT(1), nullable=False, server_default=text("'0'"))
    pri = Column(TINYINT(10), nullable=False)
    last_send = Column(INTEGER(10), nullable=False)


class EcsErrorLog(Base):
    __tablename__ = 'ecs_error_log'

    id = Column(INTEGER(10), primary_key=True)
    info = Column(String(255), nullable=False)
    file = Column(String(100), nullable=False)
    time = Column(INTEGER(10), nullable=False, index=True)


class EcsExchangeGood(Base):
    __tablename__ = 'ecs_exchange_goods'

    goods_id = Column(MEDIUMINT(8), primary_key=True, server_default=text("'0'"))
    exchange_integral = Column(INTEGER(10), nullable=False, server_default=text("'0'"))
    is_exchange = Column(TINYINT(1), nullable=False, server_default=text("'0'"))
    is_hot = Column(TINYINT(1), nullable=False, server_default=text("'0'"))


class EcsFavourableActivity(Base):
    __tablename__ = 'ecs_favourable_activity'

    act_id = Column(SMALLINT(5), primary_key=True)
    act_name = Column(String(255), nullable=False, index=True)
    start_time = Column(INTEGER(10), nullable=False)
    end_time = Column(INTEGER(10), nullable=False)
    user_rank = Column(String(255), nullable=False)
    act_range = Column(TINYINT(3), nullable=False)
    act_range_ext = Column(String(255), nullable=False)
    min_amount = Column(DECIMAL(10, 2), nullable=False)
    max_amount = Column(DECIMAL(10, 2), nullable=False)
    act_type = Column(TINYINT(3), nullable=False)
    act_type_ext = Column(DECIMAL(10, 2), nullable=False)
    gift = Column(Text, nullable=False)
    sort_order = Column(TINYINT(3), nullable=False, server_default=text("'50'"))


class EcsFeedback(Base):
    __tablename__ = 'ecs_feedback'

    msg_id = Column(MEDIUMINT(8), primary_key=True)
    parent_id = Column(MEDIUMINT(8), nullable=False, server_default=text("'0'"))
    user_id = Column(MEDIUMINT(8), nullable=False, index=True, server_default=text("'0'"))
    user_name = Column(String(60), nullable=False, server_default=text("''"))
    user_email = Column(String(60), nullable=False, server_default=text("''"))
    msg_title = Column(String(200), nullable=False, server_default=text("''"))
    msg_type = Column(TINYINT(1), nullable=False, server_default=text("'0'"))
    msg_status = Column(TINYINT(1), nullable=False, server_default=text("'0'"))
    msg_content = Column(Text, nullable=False)
    msg_time = Column(INTEGER(10), nullable=False, server_default=text("'0'"))
    message_img = Column(String(255), nullable=False, server_default=text("'0'"))
    order_id = Column(INTEGER(11), nullable=False, server_default=text("'0'"))
    msg_area = Column(TINYINT(1), nullable=False, server_default=text("'0'"))


class EcsFriendLink(Base):
    __tablename__ = 'ecs_friend_link'

    link_id = Column(SMALLINT(5), primary_key=True)
    link_name = Column(String(255), nullable=False, server_default=text("''"))
    link_url = Column(String(255), nullable=False, server_default=text("''"))
    link_logo = Column(String(255), nullable=False, server_default=text("''"))
    show_order = Column(TINYINT(3), nullable=False, index=True, server_default=text("'50'"))


class EcsGood(Base):
    __tablename__ = 'ecs_goods'

    goods_id = Column(MEDIUMINT(8), primary_key=True)
    cat_id = Column(SMALLINT(5), nullable=False, index=True, server_default=text("'0'"))
    goods_sn = Column(String(60), nullable=False, index=True, server_default=text("''"))
    goods_name = Column(String(120), nullable=False, server_default=text("''"))
    goods_name_style = Column(String(60), nullable=False, server_default=text("'+'"))
    click_count = Column(INTEGER(10), nullable=False, server_default=text("'0'"))
    brand_id = Column(SMALLINT(5), nullable=False, index=True, server_default=text("'0'"))
    provider_name = Column(String(100), nullable=False, server_default=text("''"))
    goods_number = Column(MEDIUMINT(8), nullable=False, index=True, server_default=text("'0'"))
    goods_weight = Column(DECIMAL(10, 3), nullable=False, index=True, server_default=text("'0.000'"))
    market_price = Column(DECIMAL(10, 2), nullable=False, server_default=text("'0.00'"))
    virtual_sales = Column(SMALLINT(5), nullable=False, server_default=text("'0'"))
    shop_price = Column(DECIMAL(10, 2), nullable=False, server_default=text("'0.00'"))
    promote_price = Column(DECIMAL(10, 2), nullable=False, server_default=text("'0.00'"))
    promote_start_date = Column(INTEGER(11), nullable=False, index=True, server_default=text("'0'"))
    promote_end_date = Column(INTEGER(11), nullable=False, index=True, server_default=text("'0'"))
    warn_number = Column(TINYINT(3), nullable=False, server_default=text("'1'"))
    keywords = Column(String(255), nullable=False, server_default=text("''"))
    goods_brief = Column(String(255), nullable=False, server_default=text("''"))
    goods_desc = Column(Text, nullable=False)
    goods_thumb = Column(String(255), nullable=False, server_default=text("''"))
    goods_img = Column(String(255), nullable=False, server_default=text("''"))
    original_img = Column(String(255), nullable=False, server_default=text("''"))
    is_real = Column(TINYINT(3), nullable=False, server_default=text("'1'"))
    extension_code = Column(String(30), nullable=False, server_default=text("''"))
    is_on_sale = Column(TINYINT(1), nullable=False, server_default=text("'1'"))
    is_alone_sale = Column(TINYINT(1), nullable=False, server_default=text("'1'"))
    is_shipping = Column(TINYINT(1), nullable=False, server_default=text("'0'"))
    integral = Column(INTEGER(10), nullable=False, server_default=text("'0'"))
    add_time = Column(INTEGER(10), nullable=False, server_default=text("'0'"))
    sort_order = Column(SMALLINT(4), nullable=False, index=True, server_default=text("'100'"))
    is_delete = Column(TINYINT(1), nullable=False, server_default=text("'0'"))
    is_best = Column(TINYINT(1), nullable=False, server_default=text("'0'"))
    is_new = Column(TINYINT(1), nullable=False, server_default=text("'0'"))
    is_hot = Column(TINYINT(1), nullable=False, server_default=text("'0'"))
    is_promote = Column(TINYINT(1), nullable=False, server_default=text("'0'"))
    bonus_type_id = Column(TINYINT(3), nullable=False, server_default=text("'0'"))
    last_update = Column(INTEGER(10), nullable=False, index=True, server_default=text("'0'"))
    goods_type = Column(SMALLINT(5), nullable=False, server_default=text("'0'"))
    seller_note = Column(String(255), nullable=False, server_default=text("''"))
    give_integral = Column(INTEGER(11), nullable=False, server_default=text("'-1'"))
    rank_integral = Column(INTEGER(11), nullable=False, server_default=text("'-1'"))
    suppliers_id = Column(SMALLINT(5))
    is_check = Column(TINYINT(1))


class EcsGoodsActivity(Base):
    __tablename__ = 'ecs_goods_activity'
    __table_args__ = (
        Index('act_name', 'act_name', 'act_type', 'goods_id'),
    )

    act_id = Column(MEDIUMINT(8), primary_key=True)
    act_name = Column(String(255), nullable=False)
    act_desc = Column(Text, nullable=False)
    act_type = Column(TINYINT(3), nullable=False)
    goods_id = Column(MEDIUMINT(8), nullable=False)
    product_id = Column(MEDIUMINT(8), nullable=False, server_default=text("'0'"))
    goods_name = Column(String(255), nullable=False)
    start_time = Column(INTEGER(10), nullable=False)
    end_time = Column(INTEGER(10), nullable=False)
    is_finished = Column(TINYINT(3), nullable=False)
    ext_info = Column(Text, nullable=False)


class EcsGoodsArticle(Base):
    __tablename__ = 'ecs_goods_article'

    goods_id = Column(MEDIUMINT(8), primary_key=True, nullable=False, server_default=text("'0'"))
    article_id = Column(MEDIUMINT(8), primary_key=True, nullable=False, server_default=text("'0'"))
    admin_id = Column(TINYINT(3), primary_key=True, nullable=False, server_default=text("'0'"))


class EcsGoodsAttr(Base):
    __tablename__ = 'ecs_goods_attr'

    goods_attr_id = Column(INTEGER(10), primary_key=True)
    goods_id = Column(MEDIUMINT(8), nullable=False, index=True, server_default=text("'0'"))
    attr_id = Column(SMALLINT(5), nullable=False, index=True, server_default=text("'0'"))
    attr_value = Column(Text, nullable=False)
    attr_price = Column(String(255), nullable=False, server_default=text("''"))


class EcsGoodsCat(Base):
    __tablename__ = 'ecs_goods_cat'

    goods_id = Column(MEDIUMINT(8), primary_key=True, nullable=False, server_default=text("'0'"))
    cat_id = Column(SMALLINT(5), primary_key=True, nullable=False, server_default=text("'0'"))


class EcsGoodsGallery(Base):
    __tablename__ = 'ecs_goods_gallery'

    img_id = Column(MEDIUMINT(8), primary_key=True)
    goods_id = Column(MEDIUMINT(8), nullable=False, index=True, server_default=text("'0'"))
    img_url = Column(String(255), nullable=False, server_default=text("''"))
    img_desc = Column(String(255), nullable=False, server_default=text("''"))
    thumb_url = Column(String(255), nullable=False, server_default=text("''"))
    img_original = Column(String(255), nullable=False, server_default=text("''"))
    sort_order = Column(SMALLINT(4), nullable=False, server_default=text("'30'"))


class EcsGoodsType(Base):
    __tablename__ = 'ecs_goods_type'

    cat_id = Column(SMALLINT(5), primary_key=True)
    cat_name = Column(String(60), nullable=False, server_default=text("''"))
    enabled = Column(TINYINT(1), nullable=False, server_default=text("'1'"))
    attr_group = Column(String(255), nullable=False)


class EcsGroupGood(Base):
    __tablename__ = 'ecs_group_goods'

    parent_id = Column(MEDIUMINT(8), primary_key=True, nullable=False, server_default=text("'0'"))
    goods_id = Column(MEDIUMINT(8), primary_key=True, nullable=False, server_default=text("'0'"))
    goods_price = Column(DECIMAL(10, 2), nullable=False, server_default=text("'0.00'"))
    admin_id = Column(TINYINT(3), primary_key=True, nullable=False, server_default=text("'0'"))


class EcsKeyword(Base):
    __tablename__ = 'ecs_keywords'

    date = Column(Date, primary_key=True, nullable=False, server_default=text("'0000-00-00'"))
    searchengine = Column(String(20), primary_key=True, nullable=False, server_default=text("''"))
    keyword = Column(String(90), primary_key=True, nullable=False, server_default=text("''"))
    count = Column(MEDIUMINT(8), nullable=False, server_default=text("'0'"))


class EcsLinkGood(Base):
    __tablename__ = 'ecs_link_goods'

    goods_id = Column(MEDIUMINT(8), primary_key=True, nullable=False, server_default=text("'0'"))
    link_goods_id = Column(MEDIUMINT(8), primary_key=True, nullable=False, server_default=text("'0'"))
    is_double = Column(TINYINT(1), nullable=False, server_default=text("'0'"))
    admin_id = Column(TINYINT(3), primary_key=True, nullable=False, server_default=text("'0'"))


class EcsMailTemplate(Base):
    __tablename__ = 'ecs_mail_templates'

    template_id = Column(TINYINT(1), primary_key=True)
    template_code = Column(String(30), nullable=False, unique=True, server_default=text("''"))
    is_html = Column(TINYINT(1), nullable=False, server_default=text("'0'"))
    template_subject = Column(String(200), nullable=False, server_default=text("''"))
    template_content = Column(Text, nullable=False)
    last_modify = Column(INTEGER(10), nullable=False, server_default=text("'0'"))
    last_send = Column(INTEGER(10), nullable=False, server_default=text("'0'"))
    type = Column(String(10), nullable=False, index=True)


class EcsMemberPrice(Base):
    __tablename__ = 'ecs_member_price'
    __table_args__ = (
        Index('goods_id', 'goods_id', 'user_rank'),
    )

    price_id = Column(MEDIUMINT(8), primary_key=True)
    goods_id = Column(MEDIUMINT(8), nullable=False, server_default=text("'0'"))
    user_rank = Column(TINYINT(3), nullable=False, server_default=text("'0'"))
    user_price = Column(DECIMAL(10, 2), nullable=False, server_default=text("'0.00'"))


class EcsNav(Base):
    __tablename__ = 'ecs_nav'

    id = Column(MEDIUMINT(8), primary_key=True)
    ctype = Column(String(10))
    cid = Column(SMALLINT(5))
    name = Column(String(255), nullable=False)
    ifshow = Column(TINYINT(1), nullable=False, index=True)
    vieworder = Column(TINYINT(1), nullable=False)
    opennew = Column(TINYINT(1), nullable=False)
    url = Column(String(255), nullable=False)
    type = Column(String(10), nullable=False, index=True)


class EcsOrderAction(Base):
    __tablename__ = 'ecs_order_action'

    action_id = Column(MEDIUMINT(8), primary_key=True)
    order_id = Column(MEDIUMINT(8), nullable=False, index=True, server_default=text("'0'"))
    action_user = Column(String(30), nullable=False, server_default=text("''"))
    order_status = Column(TINYINT(1), nullable=False, server_default=text("'0'"))
    shipping_status = Column(TINYINT(1), nullable=False, server_default=text("'0'"))
    pay_status = Column(TINYINT(1), nullable=False, server_default=text("'0'"))
    action_place = Column(TINYINT(1), nullable=False, server_default=text("'0'"))
    action_note = Column(String(255), nullable=False, server_default=text("''"))
    log_time = Column(INTEGER(11), nullable=False, server_default=text("'0'"))


class EcsOrderGood(Base):
    __tablename__ = 'ecs_order_goods'

    rec_id = Column(MEDIUMINT(8), primary_key=True)
    order_id = Column(MEDIUMINT(8), nullable=False, index=True, server_default=text("'0'"))
    goods_id = Column(MEDIUMINT(8), nullable=False, index=True, server_default=text("'0'"))
    goods_name = Column(String(120), nullable=False, server_default=text("''"))
    goods_sn = Column(String(60), nullable=False, server_default=text("''"))
    product_id = Column(MEDIUMINT(8), nullable=False, server_default=text("'0'"))
    goods_number = Column(SMALLINT(5), nullable=False, server_default=text("'1'"))
    market_price = Column(DECIMAL(10, 2), nullable=False, server_default=text("'0.00'"))
    goods_price = Column(DECIMAL(10, 2), nullable=False, server_default=text("'0.00'"))
    discount_fee = Column(DECIMAL(10, 2), nullable=False, server_default=text("'0.00'"))
    goods_attr = Column(Text, nullable=False)
    send_number = Column(SMALLINT(5), nullable=False, server_default=text("'0'"))
    is_real = Column(TINYINT(1), nullable=False, server_default=text("'0'"))
    extension_code = Column(String(30), nullable=False, server_default=text("''"))
    parent_id = Column(MEDIUMINT(8), nullable=False, server_default=text("'0'"))
    is_gift = Column(SMALLINT(5), nullable=False, server_default=text("'0'"))
    goods_attr_id = Column(String(255), nullable=False, server_default=text("''"))


class EcsOrderInfo(Base):
    __tablename__ = 'ecs_order_info'
    __table_args__ = (
        Index('extension_code', 'extension_code', 'extension_id'),
    )

    order_id = Column(MEDIUMINT(8), primary_key=True)
    order_sn = Column(String(20), nullable=False, unique=True, server_default=text("''"))
    user_id = Column(MEDIUMINT(8), nullable=False, index=True, server_default=text("'0'"))
    order_status = Column(TINYINT(1), nullable=False, index=True, server_default=text("'0'"))
    shipping_status = Column(TINYINT(1), nullable=False, index=True, server_default=text("'0'"))
    pay_status = Column(TINYINT(1), nullable=False, index=True, server_default=text("'0'"))
    consignee = Column(String(60), nullable=False, server_default=text("''"))
    country = Column(SMALLINT(5), nullable=False, server_default=text("'0'"))
    province = Column(SMALLINT(5), nullable=False, server_default=text("'0'"))
    city = Column(SMALLINT(5), nullable=False, server_default=text("'0'"))
    district = Column(SMALLINT(5), nullable=False, server_default=text("'0'"))
    address = Column(String(255), nullable=False, server_default=text("''"))
    zipcode = Column(String(60), nullable=False, server_default=text("''"))
    tel = Column(String(60), nullable=False, server_default=text("''"))
    mobile = Column(String(60), nullable=False, server_default=text("''"))
    email = Column(String(60), nullable=False, server_default=text("''"))
    best_time = Column(String(120), nullable=False, server_default=text("''"))
    sign_building = Column(String(120), nullable=False, server_default=text("''"))
    postscript = Column(String(255), nullable=False, server_default=text("''"))
    shipping_id = Column(TINYINT(3), nullable=False, index=True, server_default=text("'0'"))
    shipping_name = Column(String(120), nullable=False, server_default=text("''"))
    pay_id = Column(TINYINT(3), nullable=False, index=True, server_default=text("'0'"))
    pay_name = Column(String(120), nullable=False, server_default=text("''"))
    how_oos = Column(String(120), nullable=False, server_default=text("''"))
    how_surplus = Column(String(120), nullable=False, server_default=text("''"))
    pack_name = Column(String(120), nullable=False, server_default=text("''"))
    card_name = Column(String(120), nullable=False, server_default=text("''"))
    card_message = Column(String(255), nullable=False, server_default=text("''"))
    inv_payee = Column(String(120), nullable=False, server_default=text("''"))
    inv_content = Column(String(120), nullable=False, server_default=text("''"))
    goods_amount = Column(DECIMAL(10, 2), nullable=False, server_default=text("'0.00'"))
    shipping_fee = Column(DECIMAL(10, 2), nullable=False, server_default=text("'0.00'"))
    insure_fee = Column(DECIMAL(10, 2), nullable=False, server_default=text("'0.00'"))
    pay_fee = Column(DECIMAL(10, 2), nullable=False, server_default=text("'0.00'"))
    pack_fee = Column(DECIMAL(10, 2), nullable=False, server_default=text("'0.00'"))
    card_fee = Column(DECIMAL(10, 2), nullable=False, server_default=text("'0.00'"))
    goods_discount_fee = Column(DECIMAL(10, 2), nullable=False, server_default=text("'0.00'"))
    money_paid = Column(DECIMAL(10, 2), nullable=False, server_default=text("'0.00'"))
    surplus = Column(DECIMAL(10, 2), nullable=False, server_default=text("'0.00'"))
    integral = Column(INTEGER(10), nullable=False, server_default=text("'0'"))
    integral_money = Column(DECIMAL(10, 2), nullable=False, server_default=text("'0.00'"))
    bonus = Column(DECIMAL(10, 2), nullable=False, server_default=text("'0.00'"))
    order_amount = Column(DECIMAL(10, 2), nullable=False, server_default=text("'0.00'"))
    from_ad = Column(SMALLINT(5), nullable=False, server_default=text("'0'"))
    referer = Column(String(255), nullable=False, server_default=text("''"))
    add_time = Column(INTEGER(10), nullable=False, server_default=text("'0'"))
    confirm_time = Column(INTEGER(10), nullable=False, server_default=text("'0'"))
    pay_time = Column(INTEGER(10), nullable=False, server_default=text("'0'"))
    shipping_time = Column(INTEGER(10), nullable=False, server_default=text("'0'"))
    pack_id = Column(TINYINT(3), nullable=False, server_default=text("'0'"))
    card_id = Column(TINYINT(3), nullable=False, server_default=text("'0'"))
    bonus_id = Column(MEDIUMINT(8), nullable=False, server_default=text("'0'"))
    invoice_no = Column(String(255), nullable=False, server_default=text("''"))
    extension_code = Column(String(30), nullable=False, server_default=text("''"))
    extension_id = Column(MEDIUMINT(8), nullable=False, server_default=text("'0'"))
    to_buyer = Column(String(255), nullable=False, server_default=text("''"))
    pay_note = Column(String(255), nullable=False, server_default=text("''"))
    agency_id = Column(SMALLINT(5), nullable=False, index=True)
    inv_type = Column(String(60), nullable=False)
    tax = Column(DECIMAL(10, 2), nullable=False)
    is_separate = Column(TINYINT(1), nullable=False, server_default=text("'0'"))
    parent_id = Column(MEDIUMINT(8), nullable=False, server_default=text("'0'"))
    discount = Column(DECIMAL(10, 2), nullable=False)
    callback_status = Column(Enum('true', 'false'), server_default=text("'true'"))
    lastmodify = Column(INTEGER(10), nullable=False, server_default=text("'0'"))


t_ecs_order_review = Table(
    'ecs_order_review', metadata,
    Column('user_id', INTEGER(11), nullable=False),
    Column('order_id', INTEGER(11), nullable=False),
    Column('goods_id', INTEGER(11), nullable=False),
    Index('order_review_user_id_order_id_goods_id_unique', 'user_id', 'order_id', 'goods_id', unique=True)
)


class EcsPack(Base):
    __tablename__ = 'ecs_pack'

    pack_id = Column(TINYINT(3), primary_key=True)
    pack_name = Column(String(120), nullable=False, server_default=text("''"))
    pack_img = Column(String(255), nullable=False, server_default=text("''"))
    pack_fee = Column(DECIMAL(6, 2), nullable=False, server_default=text("'0.00'"))
    free_money = Column(SMALLINT(5), nullable=False, server_default=text("'0'"))
    pack_desc = Column(String(255), nullable=False, server_default=text("''"))


class EcsPackageGood(Base):
    __tablename__ = 'ecs_package_goods'

    package_id = Column(MEDIUMINT(8), primary_key=True, nullable=False, server_default=text("'0'"))
    goods_id = Column(MEDIUMINT(8), primary_key=True, nullable=False, server_default=text("'0'"))
    product_id = Column(MEDIUMINT(8), primary_key=True, nullable=False, server_default=text("'0'"))
    goods_number = Column(SMALLINT(5), nullable=False, server_default=text("'1'"))
    admin_id = Column(TINYINT(3), primary_key=True, nullable=False, server_default=text("'0'"))


class EcsPayLog(Base):
    __tablename__ = 'ecs_pay_log'

    log_id = Column(INTEGER(10), primary_key=True)
    order_id = Column(MEDIUMINT(8), nullable=False, server_default=text("'0'"))
    order_amount = Column(DECIMAL(10, 2), nullable=False)
    order_type = Column(TINYINT(1), nullable=False, server_default=text("'0'"))
    is_paid = Column(TINYINT(1), nullable=False, server_default=text("'0'"))


class EcsPayment(Base):
    __tablename__ = 'ecs_payment'

    pay_id = Column(TINYINT(3), primary_key=True)
    pay_code = Column(String(20), nullable=False, unique=True, server_default=text("''"))
    pay_name = Column(String(120), nullable=False, server_default=text("''"))
    pay_fee = Column(String(10), nullable=False, server_default=text("'0'"))
    pay_desc = Column(Text, nullable=False)
    pay_order = Column(TINYINT(3), nullable=False, server_default=text("'0'"))
    pay_config = Column(Text, nullable=False)
    enabled = Column(TINYINT(1), nullable=False, server_default=text("'0'"))
    is_cod = Column(TINYINT(1), nullable=False, server_default=text("'0'"))
    is_online = Column(TINYINT(1), nullable=False, server_default=text("'0'"))


class EcsPlugin(Base):
    __tablename__ = 'ecs_plugins'

    code = Column(String(30), primary_key=True, server_default=text("''"))
    version = Column(String(10), nullable=False, server_default=text("''"))
    library = Column(String(255), nullable=False, server_default=text("''"))
    assign = Column(TINYINT(1), nullable=False, server_default=text("'0'"))
    install_date = Column(INTEGER(10), nullable=False, server_default=text("'0'"))


class EcsProduct(Base):
    __tablename__ = 'ecs_products'

    product_id = Column(MEDIUMINT(8), primary_key=True)
    goods_id = Column(MEDIUMINT(8), nullable=False, server_default=text("'0'"))
    goods_attr = Column(String(50))
    product_sn = Column(String(60))
    product_number = Column(MEDIUMINT(8), server_default=text("'0'"))


class EcsPush(Base):
    __tablename__ = 'ecs_push'

    id = Column(INTEGER(10), primary_key=True)
    user_id = Column(INTEGER(11), nullable=False, index=True, server_default=text("'0'"))
    title = Column(String(200), nullable=False, index=True)
    content = Column(String(200), nullable=False, index=True)
    photo = Column(String(200), index=True)
    objectId = Column(String(200), index=True)
    link = Column(String(200), index=True)
    platform = Column(TINYINT(4), nullable=False, server_default=text("'3'"))
    push_type = Column(TINYINT(4), server_default=text("'0'"))
    message_type = Column(TINYINT(4), server_default=text("'1'"))
    isPush = Column(TINYINT(4), server_default=text("'0'"))
    push_at = Column(TIMESTAMP)
    status = Column(TINYINT(4), nullable=False, index=True, server_default=text("'1'"))
    created_at = Column(TIMESTAMP)
    updated_at = Column(TIMESTAMP)


class EcsRegExtendInfo(Base):
    __tablename__ = 'ecs_reg_extend_info'

    Id = Column(INTEGER(10), primary_key=True)
    user_id = Column(MEDIUMINT(8), nullable=False)
    reg_field_id = Column(INTEGER(10), nullable=False)
    content = Column(Text, nullable=False)


class EcsRegField(Base):
    __tablename__ = 'ecs_reg_fields'

    id = Column(TINYINT(3), primary_key=True)
    reg_field_name = Column(String(60), nullable=False)
    dis_order = Column(TINYINT(3), nullable=False, server_default=text("'100'"))
    display = Column(TINYINT(1), nullable=False, server_default=text("'1'"))
    type = Column(TINYINT(1), nullable=False, server_default=text("'0'"))
    is_need = Column(TINYINT(1), nullable=False, server_default=text("'1'"))


class EcsRegion(Base):
    __tablename__ = 'ecs_region'

    region_id = Column(SMALLINT(5), primary_key=True)
    parent_id = Column(SMALLINT(5), nullable=False, index=True, server_default=text("'0'"))
    region_name = Column(String(120), nullable=False, server_default=text("''"))
    region_type = Column(TINYINT(1), nullable=False, index=True, server_default=text("'2'"))
    agency_id = Column(SMALLINT(5), nullable=False, index=True, server_default=text("'0'"))


class EcsRole(Base):
    __tablename__ = 'ecs_role'

    role_id = Column(SMALLINT(5), primary_key=True)
    role_name = Column(String(60), nullable=False, index=True, server_default=text("''"))
    action_list = Column(Text, nullable=False)
    role_describe = Column(Text)


class EcsSearchHistory(Base):
    __tablename__ = 'ecs_search_history'

    id = Column(INTEGER(10), primary_key=True)
    keyword = Column(CHAR(50), nullable=False)
    count = Column(INTEGER(11), nullable=False)
    type = Column(Enum('goods', 'store'), nullable=False)
    store_id = Column(INTEGER(11), nullable=False)
    updated = Column(INTEGER(11), nullable=False)


class EcsSearchengine(Base):
    __tablename__ = 'ecs_searchengine'

    date = Column(Date, primary_key=True, nullable=False, server_default=text("'0000-00-00'"))
    searchengine = Column(String(20), primary_key=True, nullable=False, server_default=text("''"))
    count = Column(MEDIUMINT(8), nullable=False, server_default=text("'0'"))


class EcsSession(Base):
    __tablename__ = 'ecs_sessions'

    sesskey = Column(CHAR(32), primary_key=True, server_default=text("''"))
    expiry = Column(INTEGER(10), nullable=False, index=True, server_default=text("'0'"))
    userid = Column(MEDIUMINT(8), nullable=False, server_default=text("'0'"))
    adminid = Column(MEDIUMINT(8), nullable=False, server_default=text("'0'"))
    ip = Column(CHAR(15), nullable=False, server_default=text("''"))
    user_name = Column(String(60), nullable=False)
    user_rank = Column(TINYINT(3), nullable=False)
    discount = Column(DECIMAL(3, 2), nullable=False)
    email = Column(String(60), nullable=False)
    data = Column(CHAR(255), nullable=False, server_default=text("''"))


class EcsSessionsDatum(Base):
    __tablename__ = 'ecs_sessions_data'

    sesskey = Column(VARCHAR(32), primary_key=True, server_default=text("''"))
    expiry = Column(INTEGER(10), nullable=False, index=True, server_default=text("'0'"))
    data = Column(LONGTEXT, nullable=False)


class EcsShipping(Base):
    __tablename__ = 'ecs_shipping'
    __table_args__ = (
        Index('shipping_code', 'shipping_code', 'enabled'),
    )

    shipping_id = Column(TINYINT(3), primary_key=True)
    shipping_code = Column(String(20), nullable=False, server_default=text("''"))
    shipping_name = Column(String(120), nullable=False, server_default=text("''"))
    shipping_desc = Column(String(255), nullable=False, server_default=text("''"))
    insure = Column(String(10), nullable=False, server_default=text("'0'"))
    support_cod = Column(TINYINT(1), nullable=False, server_default=text("'0'"))
    enabled = Column(TINYINT(1), nullable=False, server_default=text("'0'"))
    shipping_print = Column(Text, nullable=False)
    print_bg = Column(String(255))
    config_lable = Column(Text)
    print_model = Column(TINYINT(1), server_default=text("'0'"))
    shipping_order = Column(TINYINT(3), nullable=False, server_default=text("'0'"))


class EcsShippingArea(Base):
    __tablename__ = 'ecs_shipping_area'

    shipping_area_id = Column(SMALLINT(5), primary_key=True)
    shipping_area_name = Column(String(150), nullable=False, server_default=text("''"))
    shipping_id = Column(TINYINT(3), nullable=False, index=True, server_default=text("'0'"))
    configure = Column(Text, nullable=False)


class EcsShopBind(Base):
    __tablename__ = 'ecs_shop_bind'

    shop_id = Column(INTEGER(8), primary_key=True)
    name = Column(String(255))
    node_id = Column(String(32))
    node_type = Column(String(128))
    status = Column(Enum('bind', 'unbind'))
    app_url = Column(String(200))


class EcsShopConfig(Base):
    __tablename__ = 'ecs_shop_config'

    id = Column(SMALLINT(5), primary_key=True)
    parent_id = Column(SMALLINT(5), nullable=False, index=True, server_default=text("'0'"))
    code = Column(String(30), nullable=False, unique=True, server_default=text("''"))
    type = Column(String(10), nullable=False, server_default=text("''"))
    store_range = Column(String(255), nullable=False, server_default=text("''"))
    store_dir = Column(String(255), nullable=False, server_default=text("''"))
    value = Column(Text, nullable=False)
    sort_order = Column(TINYINT(3), nullable=False, server_default=text("'1'"))


class EcsSnatchLog(Base):
    __tablename__ = 'ecs_snatch_log'

    log_id = Column(MEDIUMINT(8), primary_key=True)
    snatch_id = Column(TINYINT(3), nullable=False, index=True, server_default=text("'0'"))
    user_id = Column(MEDIUMINT(8), nullable=False, server_default=text("'0'"))
    bid_price = Column(DECIMAL(10, 2), nullable=False, server_default=text("'0.00'"))
    bid_time = Column(INTEGER(10), nullable=False, server_default=text("'0'"))


t_ecs_sns = Table(
    'ecs_sns', metadata,
    Column('user_id', INTEGER(11), nullable=False, unique=True),
    Column('open_id', String(255), nullable=False, index=True),
    Column('vendor', TINYINT(4), nullable=False, index=True),
    Column('created_at', TIMESTAMP),
    Column('updated_at', TIMESTAMP)
)


t_ecs_stats = Table(
    'ecs_stats', metadata,
    Column('access_time', INTEGER(10), nullable=False, index=True, server_default=text("'0'")),
    Column('ip_address', String(15), nullable=False, server_default=text("''")),
    Column('visit_times', SMALLINT(5), nullable=False, server_default=text("'1'")),
    Column('browser', String(60), nullable=False, server_default=text("''")),
    Column('system', String(20), nullable=False, server_default=text("''")),
    Column('language', String(20), nullable=False, server_default=text("''")),
    Column('area', String(30), nullable=False, server_default=text("''")),
    Column('referer_domain', String(100), nullable=False, server_default=text("''")),
    Column('referer_path', String(200), nullable=False, server_default=text("''")),
    Column('access_url', String(255), nullable=False, server_default=text("''"))
)


class EcsSupplier(Base):
    __tablename__ = 'ecs_suppliers'

    suppliers_id = Column(SMALLINT(5), primary_key=True)
    suppliers_name = Column(String(255))
    suppliers_desc = Column(MEDIUMTEXT)
    is_check = Column(TINYINT(1), nullable=False, server_default=text("'1'"))


class EcsTag(Base):
    __tablename__ = 'ecs_tag'

    tag_id = Column(MEDIUMINT(8), primary_key=True)
    user_id = Column(MEDIUMINT(8), nullable=False, index=True, server_default=text("'0'"))
    goods_id = Column(MEDIUMINT(8), nullable=False, index=True, server_default=text("'0'"))
    tag_words = Column(String(255), nullable=False, server_default=text("''"))


t_ecs_template = Table(
    'ecs_template', metadata,
    Column('filename', String(30), nullable=False, server_default=text("''")),
    Column('region', String(40), nullable=False, server_default=text("''")),
    Column('library', String(40), nullable=False, server_default=text("''")),
    Column('sort_order', TINYINT(1), nullable=False, server_default=text("'0'")),
    Column('id', SMALLINT(5), nullable=False, server_default=text("'0'")),
    Column('number', TINYINT(1), nullable=False, server_default=text("'5'")),
    Column('type', TINYINT(1), nullable=False, server_default=text("'0'")),
    Column('theme', String(60), nullable=False, index=True, server_default=text("''")),
    Column('remarks', String(30), nullable=False, index=True, server_default=text("''")),
    Index('filename', 'filename', 'region')
)


t_ecs_topic = Table(
    'ecs_topic', metadata,
    Column('topic_id', INTEGER(10), nullable=False, index=True),
    Column('title', String(255), nullable=False, server_default=text("''''''")),
    Column('intro', Text, nullable=False),
    Column('start_time', INTEGER(11), nullable=False, server_default=text("'0'")),
    Column('end_time', INTEGER(10), nullable=False, server_default=text("'0'")),
    Column('data', Text, nullable=False),
    Column('template', String(255), nullable=False, server_default=text("''''''")),
    Column('css', Text, nullable=False),
    Column('topic_img', String(255)),
    Column('title_pic', String(255)),
    Column('base_style', CHAR(6)),
    Column('htmls', MEDIUMTEXT),
    Column('keywords', String(255)),
    Column('description', String(255))
)


class EcsUserAccount(Base):
    __tablename__ = 'ecs_user_account'

    id = Column(MEDIUMINT(8), primary_key=True)
    user_id = Column(MEDIUMINT(8), nullable=False, index=True, server_default=text("'0'"))
    admin_user = Column(String(255), nullable=False)
    amount = Column(DECIMAL(10, 2), nullable=False)
    add_time = Column(INTEGER(10), nullable=False, server_default=text("'0'"))
    paid_time = Column(INTEGER(10), nullable=False, server_default=text("'0'"))
    admin_note = Column(String(255), nullable=False)
    user_note = Column(String(255), nullable=False)
    process_type = Column(TINYINT(1), nullable=False, server_default=text("'0'"))
    payment = Column(String(90), nullable=False)
    is_paid = Column(TINYINT(1), nullable=False, index=True, server_default=text("'0'"))


class EcsUserAddres(Base):
    __tablename__ = 'ecs_user_address'

    address_id = Column(MEDIUMINT(8), primary_key=True)
    address_name = Column(String(50), nullable=False, server_default=text("''"))
    user_id = Column(MEDIUMINT(8), nullable=False, index=True, server_default=text("'0'"))
    consignee = Column(String(60), nullable=False, server_default=text("''"))
    email = Column(String(60), nullable=False, server_default=text("''"))
    country = Column(SMALLINT(5), nullable=False, server_default=text("'0'"))
    province = Column(SMALLINT(5), nullable=False, server_default=text("'0'"))
    city = Column(SMALLINT(5), nullable=False, server_default=text("'0'"))
    district = Column(SMALLINT(5), nullable=False, server_default=text("'0'"))
    address = Column(String(120), nullable=False, server_default=text("''"))
    zipcode = Column(String(60), nullable=False, server_default=text("''"))
    tel = Column(String(60), nullable=False, server_default=text("''"))
    mobile = Column(String(60), nullable=False, server_default=text("''"))
    sign_building = Column(String(120), nullable=False, server_default=text("''"))
    best_time = Column(String(120), nullable=False, server_default=text("''"))


class EcsUserBonu(Base):
    __tablename__ = 'ecs_user_bonus'

    bonus_id = Column(MEDIUMINT(8), primary_key=True)
    bonus_type_id = Column(TINYINT(3), nullable=False, server_default=text("'0'"))
    bonus_sn = Column(BIGINT(20), nullable=False, server_default=text("'0'"))
    user_id = Column(MEDIUMINT(8), nullable=False, index=True, server_default=text("'0'"))
    used_time = Column(INTEGER(10), nullable=False, server_default=text("'0'"))
    order_id = Column(MEDIUMINT(8), nullable=False, server_default=text("'0'"))
    emailed = Column(TINYINT(3), nullable=False, server_default=text("'0'"))


class EcsUserFeed(Base):
    __tablename__ = 'ecs_user_feed'

    feed_id = Column(MEDIUMINT(8), primary_key=True)
    user_id = Column(MEDIUMINT(8), nullable=False, server_default=text("'0'"))
    value_id = Column(MEDIUMINT(8), nullable=False, server_default=text("'0'"))
    goods_id = Column(MEDIUMINT(8), nullable=False, server_default=text("'0'"))
    feed_type = Column(TINYINT(1), nullable=False, server_default=text("'0'"))
    is_feed = Column(TINYINT(1), nullable=False, server_default=text("'0'"))


class EcsUserRank(Base):
    __tablename__ = 'ecs_user_rank'

    rank_id = Column(TINYINT(3), primary_key=True)
    rank_name = Column(String(30), nullable=False, server_default=text("''"))
    min_points = Column(INTEGER(10), nullable=False, server_default=text("'0'"))
    max_points = Column(INTEGER(10), nullable=False, server_default=text("'0'"))
    discount = Column(TINYINT(3), nullable=False, server_default=text("'0'"))
    show_price = Column(TINYINT(1), nullable=False, server_default=text("'1'"))
    special_rank = Column(TINYINT(1), nullable=False, server_default=text("'0'"))


t_ecs_user_reg_status = Table(
    'ecs_user_reg_status', metadata,
    Column('user_id', INTEGER(11), nullable=False),
    Column('is_completed', TINYINT(4), nullable=False)
)


class EcsUser(Base):
    __tablename__ = 'ecs_users'

    user_id = Column(MEDIUMINT(8), primary_key=True)
    email = Column(String(60), nullable=False, index=True, server_default=text("''"))
    user_name = Column(String(60), nullable=False, unique=True, server_default=text("''"))
    password = Column(String(32), nullable=False, server_default=text("''"))
    question = Column(String(255), nullable=False, server_default=text("''"))
    answer = Column(String(255), nullable=False, server_default=text("''"))
    sex = Column(TINYINT(1), nullable=False, server_default=text("'0'"))
    birthday = Column(Date, nullable=False, server_default=text("'0000-00-00'"))
    user_money = Column(DECIMAL(10, 2), nullable=False, server_default=text("'0.00'"))
    frozen_money = Column(DECIMAL(10, 2), nullable=False, server_default=text("'0.00'"))
    pay_points = Column(INTEGER(10), nullable=False, server_default=text("'0'"))
    rank_points = Column(INTEGER(10), nullable=False, server_default=text("'0'"))
    address_id = Column(MEDIUMINT(8), nullable=False, server_default=text("'0'"))
    reg_time = Column(INTEGER(10), nullable=False, server_default=text("'0'"))
    last_login = Column(INTEGER(11), nullable=False, server_default=text("'0'"))
    last_time = Column(DateTime, nullable=False, server_default=text("'0000-00-00 00:00:00'"))
    last_ip = Column(String(15), nullable=False, server_default=text("''"))
    visit_count = Column(SMALLINT(5), nullable=False, server_default=text("'0'"))
    user_rank = Column(TINYINT(3), nullable=False, server_default=text("'0'"))
    is_special = Column(TINYINT(3), nullable=False, server_default=text("'0'"))
    ec_salt = Column(String(10))
    salt = Column(String(10), nullable=False, server_default=text("'0'"))
    parent_id = Column(MEDIUMINT(9), nullable=False, index=True, server_default=text("'0'"))
    flag = Column(TINYINT(3), nullable=False, index=True, server_default=text("'0'"))
    alias = Column(String(60), nullable=False)
    msn = Column(String(60), nullable=False)
    qq = Column(String(20), nullable=False)
    office_phone = Column(String(20), nullable=False)
    home_phone = Column(String(20), nullable=False)
    mobile_phone = Column(String(20), nullable=False)
    is_validated = Column(TINYINT(3), nullable=False, server_default=text("'0'"))
    credit_line = Column(DECIMAL(10, 2), nullable=False)
    passwd_question = Column(String(50))
    passwd_answer = Column(String(255))


class EcsVersion(Base):
    __tablename__ = 'ecs_version'

    id = Column(INTEGER(10), primary_key=True)
    platform = Column(TINYINT(4), nullable=False, server_default=text("'3'"))
    version = Column(CHAR(50))
    url = Column(CHAR(200))
    content = Column(CHAR(255), nullable=False)
    status = Column(TINYINT(4), nullable=False, server_default=text("'1'"))
    created_at = Column(TIMESTAMP)
    updated_at = Column(TIMESTAMP)


class EcsVirtualCard(Base):
    __tablename__ = 'ecs_virtual_card'

    card_id = Column(MEDIUMINT(8), primary_key=True)
    goods_id = Column(MEDIUMINT(8), nullable=False, index=True, server_default=text("'0'"))
    card_sn = Column(String(60), nullable=False, index=True, server_default=text("''"))
    card_password = Column(String(60), nullable=False, server_default=text("''"))
    add_date = Column(INTEGER(11), nullable=False, server_default=text("'0'"))
    end_date = Column(INTEGER(11), nullable=False, server_default=text("'0'"))
    is_saled = Column(TINYINT(1), nullable=False, index=True, server_default=text("'0'"))
    order_sn = Column(String(20), nullable=False, server_default=text("''"))
    crc32 = Column(String(12), nullable=False, server_default=text("'0'"))


class EcsVolumePrice(Base):
    __tablename__ = 'ecs_volume_price'

    price_type = Column(TINYINT(1), primary_key=True, nullable=False)
    goods_id = Column(MEDIUMINT(8), primary_key=True, nullable=False)
    volume_number = Column(SMALLINT(5), primary_key=True, nullable=False, server_default=text("'0'"))
    volume_price = Column(DECIMAL(10, 2), nullable=False, server_default=text("'0.00'"))


class EcsVote(Base):
    __tablename__ = 'ecs_vote'

    vote_id = Column(SMALLINT(5), primary_key=True)
    vote_name = Column(String(250), nullable=False, server_default=text("''"))
    start_time = Column(INTEGER(11), nullable=False, server_default=text("'0'"))
    end_time = Column(INTEGER(11), nullable=False, server_default=text("'0'"))
    can_multi = Column(TINYINT(1), nullable=False, server_default=text("'0'"))
    vote_count = Column(INTEGER(10), nullable=False, server_default=text("'0'"))


class EcsVoteLog(Base):
    __tablename__ = 'ecs_vote_log'

    log_id = Column(MEDIUMINT(8), primary_key=True)
    vote_id = Column(SMALLINT(5), nullable=False, index=True, server_default=text("'0'"))
    ip_address = Column(String(15), nullable=False, server_default=text("''"))
    vote_time = Column(INTEGER(10), nullable=False, server_default=text("'0'"))


class EcsVoteOption(Base):
    __tablename__ = 'ecs_vote_option'

    option_id = Column(SMALLINT(5), primary_key=True)
    vote_id = Column(SMALLINT(5), nullable=False, index=True, server_default=text("'0'"))
    option_name = Column(String(250), nullable=False, server_default=text("''"))
    option_count = Column(INTEGER(8), nullable=False, server_default=text("'0'"))
    option_order = Column(TINYINT(3), nullable=False, server_default=text("'100'"))


class EcsWholesale(Base):
    __tablename__ = 'ecs_wholesale'

    act_id = Column(MEDIUMINT(8), primary_key=True)
    goods_id = Column(MEDIUMINT(8), nullable=False, index=True)
    goods_name = Column(String(255), nullable=False)
    rank_ids = Column(String(255), nullable=False)
    prices = Column(Text, nullable=False)
    enabled = Column(TINYINT(3), nullable=False)
