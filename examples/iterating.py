from somewhere import *

def promotions(request):
    """
    Have you ever tried to write to (or delete from) memory you don't have acces to in python?
    Let's hack!
    """
    promotions = list(get_request_promotions(request))

    # We want to filter out promotions that aren't visible to this user
    for index, promotion_link in enumerate(list(promotions)):
        promotion = promotion_link.content_object
        if promotion.code == 'singleproduct' and not promotion.product.is_visible_to(request.user):
            del promotions[index]

    return promotions
