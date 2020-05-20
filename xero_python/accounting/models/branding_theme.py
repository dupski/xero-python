# coding: utf-8

"""
    Accounting API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    OpenAPI spec version: 2.1.2
    Contact: api@xero.com
    Generated by: https://openapi-generator.tech
"""


import re  # noqa: F401

from xero_python.models import BaseModel


class BrandingTheme(BaseModel):
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
        "branding_theme_id": "str",
        "name": "str",
        "logo_url": "str",
        "type": "str",
        "sort_order": "int",
        "created_date_utc": "datetime[ms-format]",
    }

    attribute_map = {
        "branding_theme_id": "BrandingThemeID",
        "name": "Name",
        "logo_url": "LogoUrl",
        "type": "Type",
        "sort_order": "SortOrder",
        "created_date_utc": "CreatedDateUTC",
    }

    def __init__(
        self,
        branding_theme_id=None,
        name=None,
        logo_url=None,
        type=None,
        sort_order=None,
        created_date_utc=None,
    ):  # noqa: E501
        """BrandingTheme - a model defined in OpenAPI"""  # noqa: E501

        self._branding_theme_id = None
        self._name = None
        self._logo_url = None
        self._type = None
        self._sort_order = None
        self._created_date_utc = None
        self.discriminator = None

        if branding_theme_id is not None:
            self.branding_theme_id = branding_theme_id
        if name is not None:
            self.name = name
        if logo_url is not None:
            self.logo_url = logo_url
        if type is not None:
            self.type = type
        if sort_order is not None:
            self.sort_order = sort_order
        if created_date_utc is not None:
            self.created_date_utc = created_date_utc

    @property
    def branding_theme_id(self):
        """Gets the branding_theme_id of this BrandingTheme.  # noqa: E501

        Xero identifier  # noqa: E501

        :return: The branding_theme_id of this BrandingTheme.  # noqa: E501
        :rtype: str
        """
        return self._branding_theme_id

    @branding_theme_id.setter
    def branding_theme_id(self, branding_theme_id):
        """Sets the branding_theme_id of this BrandingTheme.

        Xero identifier  # noqa: E501

        :param branding_theme_id: The branding_theme_id of this BrandingTheme.  # noqa: E501
        :type: str
        """

        self._branding_theme_id = branding_theme_id

    @property
    def name(self):
        """Gets the name of this BrandingTheme.  # noqa: E501

        Name of branding theme  # noqa: E501

        :return: The name of this BrandingTheme.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this BrandingTheme.

        Name of branding theme  # noqa: E501

        :param name: The name of this BrandingTheme.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def logo_url(self):
        """Gets the logo_url of this BrandingTheme.  # noqa: E501

        The location of the image file used as the logo on this branding theme  # noqa: E501

        :return: The logo_url of this BrandingTheme.  # noqa: E501
        :rtype: str
        """
        return self._logo_url

    @logo_url.setter
    def logo_url(self, logo_url):
        """Sets the logo_url of this BrandingTheme.

        The location of the image file used as the logo on this branding theme  # noqa: E501

        :param logo_url: The logo_url of this BrandingTheme.  # noqa: E501
        :type: str
        """

        self._logo_url = logo_url

    @property
    def type(self):
        """Gets the type of this BrandingTheme.  # noqa: E501

        Always INVOICE  # noqa: E501

        :return: The type of this BrandingTheme.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this BrandingTheme.

        Always INVOICE  # noqa: E501

        :param type: The type of this BrandingTheme.  # noqa: E501
        :type: str
        """
        allowed_values = ["INVOICE"]  # noqa: E501
        if type not in allowed_values:
            raise ValueError(
                "Invalid value for `type` ({0}), must be one of {1}".format(  # noqa: E501
                    type, allowed_values
                )
            )

        self._type = type

    @property
    def sort_order(self):
        """Gets the sort_order of this BrandingTheme.  # noqa: E501

        Integer – ranked order of branding theme. The default branding theme has a value of 0  # noqa: E501

        :return: The sort_order of this BrandingTheme.  # noqa: E501
        :rtype: int
        """
        return self._sort_order

    @sort_order.setter
    def sort_order(self, sort_order):
        """Sets the sort_order of this BrandingTheme.

        Integer – ranked order of branding theme. The default branding theme has a value of 0  # noqa: E501

        :param sort_order: The sort_order of this BrandingTheme.  # noqa: E501
        :type: int
        """

        self._sort_order = sort_order

    @property
    def created_date_utc(self):
        """Gets the created_date_utc of this BrandingTheme.  # noqa: E501

        UTC timestamp of creation date of branding theme  # noqa: E501

        :return: The created_date_utc of this BrandingTheme.  # noqa: E501
        :rtype: datetime
        """
        return self._created_date_utc

    @created_date_utc.setter
    def created_date_utc(self, created_date_utc):
        """Sets the created_date_utc of this BrandingTheme.

        UTC timestamp of creation date of branding theme  # noqa: E501

        :param created_date_utc: The created_date_utc of this BrandingTheme.  # noqa: E501
        :type: datetime
        """

        self._created_date_utc = created_date_utc
