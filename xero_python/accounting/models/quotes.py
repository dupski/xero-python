# coding: utf-8

"""
    Accounting API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    OpenAPI spec version: 2.2.14
    Contact: api@xero.com
    Generated by: https://openapi-generator.tech
"""


import re  # noqa: F401

from xero_python.models import BaseModel


class Quotes(BaseModel):
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
    openapi_types = {"quotes": "list[Quote]"}

    attribute_map = {"quotes": "Quotes"}

    def __init__(self, quotes=None):  # noqa: E501
        """Quotes - a model defined in OpenAPI"""  # noqa: E501

        self._quotes = None
        self.discriminator = None

        if quotes is not None:
            self.quotes = quotes

    @property
    def quotes(self):
        """Gets the quotes of this Quotes.  # noqa: E501


        :return: The quotes of this Quotes.  # noqa: E501
        :rtype: list[Quote]
        """
        return self._quotes

    @quotes.setter
    def quotes(self, quotes):
        """Sets the quotes of this Quotes.


        :param quotes: The quotes of this Quotes.  # noqa: E501
        :type: list[Quote]
        """

        self._quotes = quotes
