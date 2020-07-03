# coding: utf-8

"""
    Accounting API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    OpenAPI spec version: 2.2.6
    Contact: api@xero.com
    Generated by: https://openapi-generator.tech
"""


import re  # noqa: F401

from xero_python.models import BaseModel


class Address(BaseModel):
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
    openapi_types = {
        "address_type": "str",
        "address_line1": "str",
        "address_line2": "str",
        "address_line3": "str",
        "address_line4": "str",
        "city": "str",
        "region": "str",
        "postal_code": "str",
        "country": "str",
        "attention_to": "str",
    }

    attribute_map = {
        "address_type": "AddressType",
        "address_line1": "AddressLine1",
        "address_line2": "AddressLine2",
        "address_line3": "AddressLine3",
        "address_line4": "AddressLine4",
        "city": "City",
        "region": "Region",
        "postal_code": "PostalCode",
        "country": "Country",
        "attention_to": "AttentionTo",
    }

    def __init__(
        self,
        address_type=None,
        address_line1=None,
        address_line2=None,
        address_line3=None,
        address_line4=None,
        city=None,
        region=None,
        postal_code=None,
        country=None,
        attention_to=None,
    ):  # noqa: E501
        """Address - a model defined in OpenAPI"""  # noqa: E501

        self._address_type = None
        self._address_line1 = None
        self._address_line2 = None
        self._address_line3 = None
        self._address_line4 = None
        self._city = None
        self._region = None
        self._postal_code = None
        self._country = None
        self._attention_to = None
        self.discriminator = None

        if address_type is not None:
            self.address_type = address_type
        if address_line1 is not None:
            self.address_line1 = address_line1
        if address_line2 is not None:
            self.address_line2 = address_line2
        if address_line3 is not None:
            self.address_line3 = address_line3
        if address_line4 is not None:
            self.address_line4 = address_line4
        if city is not None:
            self.city = city
        if region is not None:
            self.region = region
        if postal_code is not None:
            self.postal_code = postal_code
        if country is not None:
            self.country = country
        if attention_to is not None:
            self.attention_to = attention_to

    @property
    def address_type(self):
        """Gets the address_type of this Address.  # noqa: E501

        define the type of address  # noqa: E501

        :return: The address_type of this Address.  # noqa: E501
        :rtype: str
        """
        return self._address_type

    @address_type.setter
    def address_type(self, address_type):
        """Sets the address_type of this Address.

        define the type of address  # noqa: E501

        :param address_type: The address_type of this Address.  # noqa: E501
        :type: str
        """
        allowed_values = ["POBOX", "STREET", "DELIVERY"]  # noqa: E501
        if address_type not in allowed_values:
            raise ValueError(
                "Invalid value for `address_type` ({0}), must be one of {1}".format(  # noqa: E501
                    address_type, allowed_values
                )
            )

        self._address_type = address_type

    @property
    def address_line1(self):
        """Gets the address_line1 of this Address.  # noqa: E501

        max length = 500  # noqa: E501

        :return: The address_line1 of this Address.  # noqa: E501
        :rtype: str
        """
        return self._address_line1

    @address_line1.setter
    def address_line1(self, address_line1):
        """Sets the address_line1 of this Address.

        max length = 500  # noqa: E501

        :param address_line1: The address_line1 of this Address.  # noqa: E501
        :type: str
        """
        if address_line1 is not None and len(address_line1) > 500:
            raise ValueError(
                "Invalid value for `address_line1`, "
                "length must be less than or equal to `500`"
            )  # noqa: E501

        self._address_line1 = address_line1

    @property
    def address_line2(self):
        """Gets the address_line2 of this Address.  # noqa: E501

        max length = 500  # noqa: E501

        :return: The address_line2 of this Address.  # noqa: E501
        :rtype: str
        """
        return self._address_line2

    @address_line2.setter
    def address_line2(self, address_line2):
        """Sets the address_line2 of this Address.

        max length = 500  # noqa: E501

        :param address_line2: The address_line2 of this Address.  # noqa: E501
        :type: str
        """
        if address_line2 is not None and len(address_line2) > 500:
            raise ValueError(
                "Invalid value for `address_line2`, "
                "length must be less than or equal to `500`"
            )  # noqa: E501

        self._address_line2 = address_line2

    @property
    def address_line3(self):
        """Gets the address_line3 of this Address.  # noqa: E501

        max length = 500  # noqa: E501

        :return: The address_line3 of this Address.  # noqa: E501
        :rtype: str
        """
        return self._address_line3

    @address_line3.setter
    def address_line3(self, address_line3):
        """Sets the address_line3 of this Address.

        max length = 500  # noqa: E501

        :param address_line3: The address_line3 of this Address.  # noqa: E501
        :type: str
        """
        if address_line3 is not None and len(address_line3) > 500:
            raise ValueError(
                "Invalid value for `address_line3`, "
                "length must be less than or equal to `500`"
            )  # noqa: E501

        self._address_line3 = address_line3

    @property
    def address_line4(self):
        """Gets the address_line4 of this Address.  # noqa: E501

        max length = 500  # noqa: E501

        :return: The address_line4 of this Address.  # noqa: E501
        :rtype: str
        """
        return self._address_line4

    @address_line4.setter
    def address_line4(self, address_line4):
        """Sets the address_line4 of this Address.

        max length = 500  # noqa: E501

        :param address_line4: The address_line4 of this Address.  # noqa: E501
        :type: str
        """
        if address_line4 is not None and len(address_line4) > 500:
            raise ValueError(
                "Invalid value for `address_line4`, "
                "length must be less than or equal to `500`"
            )  # noqa: E501

        self._address_line4 = address_line4

    @property
    def city(self):
        """Gets the city of this Address.  # noqa: E501

        max length = 255  # noqa: E501

        :return: The city of this Address.  # noqa: E501
        :rtype: str
        """
        return self._city

    @city.setter
    def city(self, city):
        """Sets the city of this Address.

        max length = 255  # noqa: E501

        :param city: The city of this Address.  # noqa: E501
        :type: str
        """
        if city is not None and len(city) > 255:
            raise ValueError(
                "Invalid value for `city`, "
                "length must be less than or equal to `255`"
            )  # noqa: E501

        self._city = city

    @property
    def region(self):
        """Gets the region of this Address.  # noqa: E501

        max length = 255  # noqa: E501

        :return: The region of this Address.  # noqa: E501
        :rtype: str
        """
        return self._region

    @region.setter
    def region(self, region):
        """Sets the region of this Address.

        max length = 255  # noqa: E501

        :param region: The region of this Address.  # noqa: E501
        :type: str
        """
        if region is not None and len(region) > 255:
            raise ValueError(
                "Invalid value for `region`, "
                "length must be less than or equal to `255`"
            )  # noqa: E501

        self._region = region

    @property
    def postal_code(self):
        """Gets the postal_code of this Address.  # noqa: E501

        max length = 50  # noqa: E501

        :return: The postal_code of this Address.  # noqa: E501
        :rtype: str
        """
        return self._postal_code

    @postal_code.setter
    def postal_code(self, postal_code):
        """Sets the postal_code of this Address.

        max length = 50  # noqa: E501

        :param postal_code: The postal_code of this Address.  # noqa: E501
        :type: str
        """
        if postal_code is not None and len(postal_code) > 50:
            raise ValueError(
                "Invalid value for `postal_code`, "
                "length must be less than or equal to `50`"
            )  # noqa: E501

        self._postal_code = postal_code

    @property
    def country(self):
        """Gets the country of this Address.  # noqa: E501

        max length = 50, [A-Z], [a-z] only  # noqa: E501

        :return: The country of this Address.  # noqa: E501
        :rtype: str
        """
        return self._country

    @country.setter
    def country(self, country):
        """Sets the country of this Address.

        max length = 50, [A-Z], [a-z] only  # noqa: E501

        :param country: The country of this Address.  # noqa: E501
        :type: str
        """
        if country is not None and len(country) > 50:
            raise ValueError(
                "Invalid value for `country`, "
                "length must be less than or equal to `50`"
            )  # noqa: E501

        self._country = country

    @property
    def attention_to(self):
        """Gets the attention_to of this Address.  # noqa: E501

        max length = 255  # noqa: E501

        :return: The attention_to of this Address.  # noqa: E501
        :rtype: str
        """
        return self._attention_to

    @attention_to.setter
    def attention_to(self, attention_to):
        """Sets the attention_to of this Address.

        max length = 255  # noqa: E501

        :param attention_to: The attention_to of this Address.  # noqa: E501
        :type: str
        """
        if attention_to is not None and len(attention_to) > 255:
            raise ValueError(
                "Invalid value for `attention_to`, "
                "length must be less than or equal to `255`"
            )  # noqa: E501

        self._attention_to = attention_to