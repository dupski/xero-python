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


class Reports(BaseModel):
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
    openapi_types = {"reports": "list[Report]"}

    attribute_map = {"reports": "Reports"}

    def __init__(self, reports=None):  # noqa: E501
        """Reports - a model defined in OpenAPI"""  # noqa: E501

        self._reports = None
        self.discriminator = None

        if reports is not None:
            self.reports = reports

    @property
    def reports(self):
        """Gets the reports of this Reports.  # noqa: E501


        :return: The reports of this Reports.  # noqa: E501
        :rtype: list[Report]
        """
        return self._reports

    @reports.setter
    def reports(self, reports):
        """Sets the reports of this Reports.


        :param reports: The reports of this Reports.  # noqa: E501
        :type: list[Report]
        """

        self._reports = reports
