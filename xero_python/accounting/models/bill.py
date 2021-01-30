# coding: utf-8

"""
    Accounting API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    Contact: api@xero.com
    Generated by: https://openapi-generator.tech
"""


import re  # noqa: F401

from xero_python.models import BaseModel


class Bill(BaseModel):
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
    openapi_types = {"day": "int", "type": "PaymentTermType"}

    attribute_map = {"day": "Day", "type": "Type"}

    def __init__(self, day=None, type=None):  # noqa: E501
        """Bill - a model defined in OpenAPI"""  # noqa: E501

        self._day = None
        self._type = None
        self.discriminator = None

        if day is not None:
            self.day = day
        if type is not None:
            self.type = type

    @property
    def day(self):
        """Gets the day of this Bill.  # noqa: E501

        Day of Month (0-31)  # noqa: E501

        :return: The day of this Bill.  # noqa: E501
        :rtype: int
        """
        return self._day

    @day.setter
    def day(self, day):
        """Sets the day of this Bill.

        Day of Month (0-31)  # noqa: E501

        :param day: The day of this Bill.  # noqa: E501
        :type: int
        """

        self._day = day

    @property
    def type(self):
        """Gets the type of this Bill.  # noqa: E501


        :return: The type of this Bill.  # noqa: E501
        :rtype: PaymentTermType
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this Bill.


        :param type: The type of this Bill.  # noqa: E501
        :type: PaymentTermType
        """

        self._type = type
