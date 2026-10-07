# # import constants
# from rest_framework.generics import ListAPIView
# from .models import Nav
# from .serializers import NavModelSerializer
#
#
# class NavHeaderListAPIView(ListAPIView):
#     """
#     头部导航
#     """
#     queryset = Nav.objects.filter(position=constants.NAV_HEADER_POSITION, is_show=True, is_deleted=False).order_by("orders", "-id")[:constants.NAV_HEADER_SIZE]
#     serializer_class = NavModelSerializer
#
#
# class NavFooterListAPIView(ListAPIView):
#     """
#     脚部导航
#     """
#     queryset = Nav.objects.filter(position=constants.NAV_FOOTER_POSITION, is_show=True, is_deleted=False).order_by("orders", "-id")[:constants.NAV_FOOTER_SIZE]
#     serializer_class = NavModelSerializer

import constants
from rest_framework.generics import ListAPIView
from .models import Nav
from .serializers import NavModelSerializer

NAV_HEADER_POSITION = 0
NAV_FOOTER_POSITION = 1
NAV_HEADER_SIZE = 5
NAV_FOOTER_SIZE = 10


class NavHeaderListAPIView(ListAPIView):
    """
    头部导航
    """
    queryset = Nav.objects.filter(position=constants.NAV_HEADER_POSITION, is_show=True, is_deleted=False).order_by("orders", "-id")[:NAV_HEADER_SIZE]
    serializer_class = NavModelSerializer


class NavFooterListAPIView(ListAPIView):
    """
    脚部导航
    """
    queryset = Nav.objects.filter(position=constants.NAV_FOOTER_POSITION, is_show=True, is_deleted=False).order_by("orders", "-id")[:NAV_FOOTER_SIZE]
    serializer_class = NavModelSerializer
