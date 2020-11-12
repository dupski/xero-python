# coding: utf-8

"""
    Xero Payroll NZ

    This is the Xero Payroll API for orgs in the NZ region.  # noqa: E501

    OpenAPI spec version: 2.4.4
    Contact: api@xero.com
    Generated by: https://openapi-generator.tech
"""


import re  # noqa: F401

from xero_python.models import BaseModel


class GrossEarningsHistory(BaseModel):
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
    openapi_types = {"days_paid": "int", "unpaid_weeks": "int"}

    attribute_map = {"days_paid": "daysPaid", "unpaid_weeks": "unpaidWeeks"}

    def __init__(self, days_paid=None, unpaid_weeks=None):  # noqa: E501
        """GrossEarningsHistory - a model defined in OpenAPI"""  # noqa: E501

        self._days_paid = None
        self._unpaid_weeks = None
        self.discriminator = None

        if days_paid is not None:
            self.days_paid = days_paid
        if unpaid_weeks is not None:
            self.unpaid_weeks = unpaid_weeks

    @property
    def days_paid(self):
        """Gets the days_paid of this GrossEarningsHistory.  # noqa: E501

        Number of days the employee worked in the pay period (0 - 365)  # noqa: E501

        :return: The days_paid of this GrossEarningsHistory.  # noqa: E501
        :rtype: int
        """
        return self._days_paid

    @days_paid.setter
    def days_paid(self, days_paid):
        """Sets the days_paid of this GrossEarningsHistory.

        Number of days the employee worked in the pay period (0 - 365)  # noqa: E501

        :param days_paid: The days_paid of this GrossEarningsHistory.  # noqa: E501
        :type: int
        """

        self._days_paid = days_paid

    @property
    def unpaid_weeks(self):
        """Gets the unpaid_weeks of this GrossEarningsHistory.  # noqa: E501

        Number of full weeks the employee didn't work in the pay period (0 - 52)  # noqa: E501

        :return: The unpaid_weeks of this GrossEarningsHistory.  # noqa: E501
        :rtype: int
        """
        return self._unpaid_weeks

    @unpaid_weeks.setter
    def unpaid_weeks(self, unpaid_weeks):
        """Sets the unpaid_weeks of this GrossEarningsHistory.

        Number of full weeks the employee didn't work in the pay period (0 - 52)  # noqa: E501

        :param unpaid_weeks: The unpaid_weeks of this GrossEarningsHistory.  # noqa: E501
        :type: int
        """

        self._unpaid_weeks = unpaid_weeks
