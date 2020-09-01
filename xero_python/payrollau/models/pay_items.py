# coding: utf-8

"""
    Xero Payroll AU

    This is the Xero Payroll API for orgs in Australia region.  # noqa: E501

    OpenAPI spec version: 2.2.14
    Contact: api@xero.com
    Generated by: https://openapi-generator.tech
"""


import re  # noqa: F401

from xero_python.models import BaseModel


class PayItems(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    openapi_types = {"pay_items": "PayItem"}

    attribute_map = {"pay_items": "PayItems"}

    def __init__(self, pay_items=None):  # noqa: E501
        """PayItems - a model defined in OpenAPI"""  # noqa: E501

        self._pay_items = None
        self.discriminator = None

        if pay_items is not None:
            self.pay_items = pay_items

    @property
    def pay_items(self):
        """Gets the pay_items of this PayItems.  # noqa: E501


        :return: The pay_items of this PayItems.  # noqa: E501
        :rtype: PayItem
        """
        return self._pay_items

    @pay_items.setter
    def pay_items(self, pay_items):
        """Sets the pay_items of this PayItems.


        :param pay_items: The pay_items of this PayItems.  # noqa: E501
        :type: PayItem
        """

        self._pay_items = pay_items
