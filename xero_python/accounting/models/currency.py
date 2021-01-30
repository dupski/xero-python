# coding: utf-8

"""
    Accounting API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    Contact: api@xero.com
    Generated by: https://openapi-generator.tech
"""


import re  # noqa: F401

from xero_python.models import BaseModel


class Currency(BaseModel):
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
    openapi_types = {"code": "CurrencyCode", "description": "str"}

    attribute_map = {"code": "Code", "description": "Description"}

    def __init__(self, code=None, description=None):  # noqa: E501
        """Currency - a model defined in OpenAPI"""  # noqa: E501

        self._code = None
        self._description = None
        self.discriminator = None

        if code is not None:
            self.code = code
        if description is not None:
            self.description = description

    @property
    def code(self):
        """Gets the code of this Currency.  # noqa: E501


        :return: The code of this Currency.  # noqa: E501
        :rtype: CurrencyCode
        """
        return self._code

    @code.setter
    def code(self, code):
        """Sets the code of this Currency.


        :param code: The code of this Currency.  # noqa: E501
        :type: CurrencyCode
        """

        self._code = code

    @property
    def description(self):
        """Gets the description of this Currency.  # noqa: E501

        Name of Currency  # noqa: E501

        :return: The description of this Currency.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this Currency.

        Name of Currency  # noqa: E501

        :param description: The description of this Currency.  # noqa: E501
        :type: str
        """

        self._description = description
