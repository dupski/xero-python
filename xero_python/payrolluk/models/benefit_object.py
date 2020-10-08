# coding: utf-8

"""
    Xero Payroll UK

    This is the Xero Payroll API for orgs in the UK region.  # noqa: E501

    OpenAPI spec version: 2.3.3
    Contact: api@xero.com
    Generated by: https://openapi-generator.tech
"""


import re  # noqa: F401

from xero_python.models import BaseModel


class BenefitObject(BaseModel):
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
        "benefit": "Benefit",
    }

    attribute_map = {
        "pagination": "pagination",
        "problem": "problem",
        "benefit": "benefit",
    }

    def __init__(self, pagination=None, problem=None, benefit=None):  # noqa: E501
        """BenefitObject - a model defined in OpenAPI"""  # noqa: E501

        self._pagination = None
        self._problem = None
        self._benefit = None
        self.discriminator = None

        if pagination is not None:
            self.pagination = pagination
        if problem is not None:
            self.problem = problem
        if benefit is not None:
            self.benefit = benefit

    @property
    def pagination(self):
        """Gets the pagination of this BenefitObject.  # noqa: E501


        :return: The pagination of this BenefitObject.  # noqa: E501
        :rtype: Pagination
        """
        return self._pagination

    @pagination.setter
    def pagination(self, pagination):
        """Sets the pagination of this BenefitObject.


        :param pagination: The pagination of this BenefitObject.  # noqa: E501
        :type: Pagination
        """

        self._pagination = pagination

    @property
    def problem(self):
        """Gets the problem of this BenefitObject.  # noqa: E501


        :return: The problem of this BenefitObject.  # noqa: E501
        :rtype: Problem
        """
        return self._problem

    @problem.setter
    def problem(self, problem):
        """Sets the problem of this BenefitObject.


        :param problem: The problem of this BenefitObject.  # noqa: E501
        :type: Problem
        """

        self._problem = problem

    @property
    def benefit(self):
        """Gets the benefit of this BenefitObject.  # noqa: E501


        :return: The benefit of this BenefitObject.  # noqa: E501
        :rtype: Benefit
        """
        return self._benefit

    @benefit.setter
    def benefit(self, benefit):
        """Sets the benefit of this BenefitObject.


        :param benefit: The benefit of this BenefitObject.  # noqa: E501
        :type: Benefit
        """

        self._benefit = benefit
