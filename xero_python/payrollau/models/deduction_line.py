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


class DeductionLine(BaseModel):
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
        "deduction_type_id": "str",
        "calculation_type": "DeductionTypeCalculationType",
        "amount": "float",
        "percentage": "float",
        "number_of_units": "float",
    }

    attribute_map = {
        "deduction_type_id": "DeductionTypeID",
        "calculation_type": "CalculationType",
        "amount": "Amount",
        "percentage": "Percentage",
        "number_of_units": "NumberOfUnits",
    }

    def __init__(
        self,
        deduction_type_id=None,
        calculation_type=None,
        amount=None,
        percentage=None,
        number_of_units=None,
    ):  # noqa: E501
        """DeductionLine - a model defined in OpenAPI"""  # noqa: E501

        self._deduction_type_id = None
        self._calculation_type = None
        self._amount = None
        self._percentage = None
        self._number_of_units = None
        self.discriminator = None

        self.deduction_type_id = deduction_type_id
        self.calculation_type = calculation_type
        if amount is not None:
            self.amount = amount
        if percentage is not None:
            self.percentage = percentage
        if number_of_units is not None:
            self.number_of_units = number_of_units

    @property
    def deduction_type_id(self):
        """Gets the deduction_type_id of this DeductionLine.  # noqa: E501

        Xero deduction type identifier  # noqa: E501

        :return: The deduction_type_id of this DeductionLine.  # noqa: E501
        :rtype: str
        """
        return self._deduction_type_id

    @deduction_type_id.setter
    def deduction_type_id(self, deduction_type_id):
        """Sets the deduction_type_id of this DeductionLine.

        Xero deduction type identifier  # noqa: E501

        :param deduction_type_id: The deduction_type_id of this DeductionLine.  # noqa: E501
        :type: str
        """
        if deduction_type_id is None:
            raise ValueError(
                "Invalid value for `deduction_type_id`, must not be `None`"
            )  # noqa: E501

        self._deduction_type_id = deduction_type_id

    @property
    def calculation_type(self):
        """Gets the calculation_type of this DeductionLine.  # noqa: E501


        :return: The calculation_type of this DeductionLine.  # noqa: E501
        :rtype: DeductionTypeCalculationType
        """
        return self._calculation_type

    @calculation_type.setter
    def calculation_type(self, calculation_type):
        """Sets the calculation_type of this DeductionLine.


        :param calculation_type: The calculation_type of this DeductionLine.  # noqa: E501
        :type: DeductionTypeCalculationType
        """
        if calculation_type is None:
            raise ValueError(
                "Invalid value for `calculation_type`, must not be `None`"
            )  # noqa: E501

        self._calculation_type = calculation_type

    @property
    def amount(self):
        """Gets the amount of this DeductionLine.  # noqa: E501

        Deduction type amount  # noqa: E501

        :return: The amount of this DeductionLine.  # noqa: E501
        :rtype: float
        """
        return self._amount

    @amount.setter
    def amount(self, amount):
        """Sets the amount of this DeductionLine.

        Deduction type amount  # noqa: E501

        :param amount: The amount of this DeductionLine.  # noqa: E501
        :type: float
        """

        self._amount = amount

    @property
    def percentage(self):
        """Gets the percentage of this DeductionLine.  # noqa: E501

        The Percentage of the Deduction  # noqa: E501

        :return: The percentage of this DeductionLine.  # noqa: E501
        :rtype: float
        """
        return self._percentage

    @percentage.setter
    def percentage(self, percentage):
        """Sets the percentage of this DeductionLine.

        The Percentage of the Deduction  # noqa: E501

        :param percentage: The percentage of this DeductionLine.  # noqa: E501
        :type: float
        """

        self._percentage = percentage

    @property
    def number_of_units(self):
        """Gets the number_of_units of this DeductionLine.  # noqa: E501

        Deduction number of units  # noqa: E501

        :return: The number_of_units of this DeductionLine.  # noqa: E501
        :rtype: float
        """
        return self._number_of_units

    @number_of_units.setter
    def number_of_units(self, number_of_units):
        """Sets the number_of_units of this DeductionLine.

        Deduction number of units  # noqa: E501

        :param number_of_units: The number_of_units of this DeductionLine.  # noqa: E501
        :type: float
        """

        self._number_of_units = number_of_units
