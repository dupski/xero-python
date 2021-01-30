# coding: utf-8

"""
    Xero Payroll UK

    This is the Xero Payroll API for orgs in the UK region.  # noqa: E501

    Contact: api@xero.com
    Generated by: https://openapi-generator.tech
"""


import re  # noqa: F401

from xero_python.models import BaseModel


class EmployeeOpeningBalancesObject(BaseModel):
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
        "pagination": "Pagination",
        "problem": "Problem",
        "opening_balances": "EmployeeOpeningBalances",
    }

    attribute_map = {
        "pagination": "pagination",
        "problem": "problem",
        "opening_balances": "openingBalances",
    }

    def __init__(
        self, pagination=None, problem=None, opening_balances=None
    ):  # noqa: E501
        """EmployeeOpeningBalancesObject - a model defined in OpenAPI"""  # noqa: E501

        self._pagination = None
        self._problem = None
        self._opening_balances = None
        self.discriminator = None

        if pagination is not None:
            self.pagination = pagination
        if problem is not None:
            self.problem = problem
        if opening_balances is not None:
            self.opening_balances = opening_balances

    @property
    def pagination(self):
        """Gets the pagination of this EmployeeOpeningBalancesObject.  # noqa: E501


        :return: The pagination of this EmployeeOpeningBalancesObject.  # noqa: E501
        :rtype: Pagination
        """
        return self._pagination

    @pagination.setter
    def pagination(self, pagination):
        """Sets the pagination of this EmployeeOpeningBalancesObject.


        :param pagination: The pagination of this EmployeeOpeningBalancesObject.  # noqa: E501
        :type: Pagination
        """

        self._pagination = pagination

    @property
    def problem(self):
        """Gets the problem of this EmployeeOpeningBalancesObject.  # noqa: E501


        :return: The problem of this EmployeeOpeningBalancesObject.  # noqa: E501
        :rtype: Problem
        """
        return self._problem

    @problem.setter
    def problem(self, problem):
        """Sets the problem of this EmployeeOpeningBalancesObject.


        :param problem: The problem of this EmployeeOpeningBalancesObject.  # noqa: E501
        :type: Problem
        """

        self._problem = problem

    @property
    def opening_balances(self):
        """Gets the opening_balances of this EmployeeOpeningBalancesObject.  # noqa: E501


        :return: The opening_balances of this EmployeeOpeningBalancesObject.  # noqa: E501
        :rtype: EmployeeOpeningBalances
        """
        return self._opening_balances

    @opening_balances.setter
    def opening_balances(self, opening_balances):
        """Sets the opening_balances of this EmployeeOpeningBalancesObject.


        :param opening_balances: The opening_balances of this EmployeeOpeningBalancesObject.  # noqa: E501
        :type: EmployeeOpeningBalances
        """

        self._opening_balances = opening_balances
