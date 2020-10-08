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


class TimesheetLine(BaseModel):
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
        "timesheet_line_id": "str",
        "date": "date",
        "earnings_rate_id": "str",
        "tracking_item_id": "str",
        "number_of_units": "float",
    }

    attribute_map = {
        "timesheet_line_id": "timesheetLineID",
        "date": "date",
        "earnings_rate_id": "earningsRateID",
        "tracking_item_id": "trackingItemID",
        "number_of_units": "numberOfUnits",
    }

    def __init__(
        self,
        timesheet_line_id=None,
        date=None,
        earnings_rate_id=None,
        tracking_item_id=None,
        number_of_units=None,
    ):  # noqa: E501
        """TimesheetLine - a model defined in OpenAPI"""  # noqa: E501

        self._timesheet_line_id = None
        self._date = None
        self._earnings_rate_id = None
        self._tracking_item_id = None
        self._number_of_units = None
        self.discriminator = None

        if timesheet_line_id is not None:
            self.timesheet_line_id = timesheet_line_id
        self.date = date
        self.earnings_rate_id = earnings_rate_id
        if tracking_item_id is not None:
            self.tracking_item_id = tracking_item_id
        self.number_of_units = number_of_units

    @property
    def timesheet_line_id(self):
        """Gets the timesheet_line_id of this TimesheetLine.  # noqa: E501

        The Xero identifier for a Timesheet Line  # noqa: E501

        :return: The timesheet_line_id of this TimesheetLine.  # noqa: E501
        :rtype: str
        """
        return self._timesheet_line_id

    @timesheet_line_id.setter
    def timesheet_line_id(self, timesheet_line_id):
        """Sets the timesheet_line_id of this TimesheetLine.

        The Xero identifier for a Timesheet Line  # noqa: E501

        :param timesheet_line_id: The timesheet_line_id of this TimesheetLine.  # noqa: E501
        :type: str
        """

        self._timesheet_line_id = timesheet_line_id

    @property
    def date(self):
        """Gets the date of this TimesheetLine.  # noqa: E501

        The Date that this Timesheet Line is for (YYYY-MM-DD)  # noqa: E501

        :return: The date of this TimesheetLine.  # noqa: E501
        :rtype: date
        """
        return self._date

    @date.setter
    def date(self, date):
        """Sets the date of this TimesheetLine.

        The Date that this Timesheet Line is for (YYYY-MM-DD)  # noqa: E501

        :param date: The date of this TimesheetLine.  # noqa: E501
        :type: date
        """
        if date is None:
            raise ValueError(
                "Invalid value for `date`, must not be `None`"
            )  # noqa: E501

        self._date = date

    @property
    def earnings_rate_id(self):
        """Gets the earnings_rate_id of this TimesheetLine.  # noqa: E501

        The Xero identifier for the Earnings Rate that the Timesheet is for  # noqa: E501

        :return: The earnings_rate_id of this TimesheetLine.  # noqa: E501
        :rtype: str
        """
        return self._earnings_rate_id

    @earnings_rate_id.setter
    def earnings_rate_id(self, earnings_rate_id):
        """Sets the earnings_rate_id of this TimesheetLine.

        The Xero identifier for the Earnings Rate that the Timesheet is for  # noqa: E501

        :param earnings_rate_id: The earnings_rate_id of this TimesheetLine.  # noqa: E501
        :type: str
        """
        if earnings_rate_id is None:
            raise ValueError(
                "Invalid value for `earnings_rate_id`, must not be `None`"
            )  # noqa: E501

        self._earnings_rate_id = earnings_rate_id

    @property
    def tracking_item_id(self):
        """Gets the tracking_item_id of this TimesheetLine.  # noqa: E501

        The Xero identifier for the Tracking Item that the Timesheet is for  # noqa: E501

        :return: The tracking_item_id of this TimesheetLine.  # noqa: E501
        :rtype: str
        """
        return self._tracking_item_id

    @tracking_item_id.setter
    def tracking_item_id(self, tracking_item_id):
        """Sets the tracking_item_id of this TimesheetLine.

        The Xero identifier for the Tracking Item that the Timesheet is for  # noqa: E501

        :param tracking_item_id: The tracking_item_id of this TimesheetLine.  # noqa: E501
        :type: str
        """

        self._tracking_item_id = tracking_item_id

    @property
    def number_of_units(self):
        """Gets the number_of_units of this TimesheetLine.  # noqa: E501

        The Number of Units of the Timesheet Line  # noqa: E501

        :return: The number_of_units of this TimesheetLine.  # noqa: E501
        :rtype: float
        """
        return self._number_of_units

    @number_of_units.setter
    def number_of_units(self, number_of_units):
        """Sets the number_of_units of this TimesheetLine.

        The Number of Units of the Timesheet Line  # noqa: E501

        :param number_of_units: The number_of_units of this TimesheetLine.  # noqa: E501
        :type: float
        """
        if number_of_units is None:
            raise ValueError(
                "Invalid value for `number_of_units`, must not be `None`"
            )  # noqa: E501

        self._number_of_units = number_of_units
