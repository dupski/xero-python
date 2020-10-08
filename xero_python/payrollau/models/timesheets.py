# coding: utf-8

"""
    Xero Payroll AU

    This is the Xero Payroll API for orgs in Australia region.  # noqa: E501

    OpenAPI spec version: 2.3.3
    Contact: api@xero.com
    Generated by: https://openapi-generator.tech
"""


import re  # noqa: F401

from xero_python.models import BaseModel


class Timesheets(BaseModel):
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
    openapi_types = {"timesheets": "list[Timesheet]"}

    attribute_map = {"timesheets": "Timesheets"}

    def __init__(self, timesheets=None):  # noqa: E501
        """Timesheets - a model defined in OpenAPI"""  # noqa: E501

        self._timesheets = None
        self.discriminator = None

        if timesheets is not None:
            self.timesheets = timesheets

    @property
    def timesheets(self):
        """Gets the timesheets of this Timesheets.  # noqa: E501


        :return: The timesheets of this Timesheets.  # noqa: E501
        :rtype: list[Timesheet]
        """
        return self._timesheets

    @timesheets.setter
    def timesheets(self, timesheets):
        """Sets the timesheets of this Timesheets.


        :param timesheets: The timesheets of this Timesheets.  # noqa: E501
        :type: list[Timesheet]
        """

        self._timesheets = timesheets
