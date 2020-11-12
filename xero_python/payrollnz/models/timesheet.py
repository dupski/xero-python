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


class Timesheet(BaseModel):
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
        "timesheet_id": "str",
        "payroll_calendar_id": "str",
        "employee_id": "str",
        "start_date": "date",
        "end_date": "date",
        "status": "str",
        "total_hours": "float",
        "updated_date_utc": "datetime",
        "timesheet_lines": "list[TimesheetLine]",
    }

    attribute_map = {
        "timesheet_id": "timesheetID",
        "payroll_calendar_id": "payrollCalendarID",
        "employee_id": "employeeID",
        "start_date": "startDate",
        "end_date": "endDate",
        "status": "status",
        "total_hours": "totalHours",
        "updated_date_utc": "updatedDateUTC",
        "timesheet_lines": "timesheetLines",
    }

    def __init__(
        self,
        timesheet_id=None,
        payroll_calendar_id=None,
        employee_id=None,
        start_date=None,
        end_date=None,
        status=None,
        total_hours=None,
        updated_date_utc=None,
        timesheet_lines=None,
    ):  # noqa: E501
        """Timesheet - a model defined in OpenAPI"""  # noqa: E501

        self._timesheet_id = None
        self._payroll_calendar_id = None
        self._employee_id = None
        self._start_date = None
        self._end_date = None
        self._status = None
        self._total_hours = None
        self._updated_date_utc = None
        self._timesheet_lines = None
        self.discriminator = None

        if timesheet_id is not None:
            self.timesheet_id = timesheet_id
        self.payroll_calendar_id = payroll_calendar_id
        self.employee_id = employee_id
        self.start_date = start_date
        self.end_date = end_date
        if status is not None:
            self.status = status
        if total_hours is not None:
            self.total_hours = total_hours
        if updated_date_utc is not None:
            self.updated_date_utc = updated_date_utc
        if timesheet_lines is not None:
            self.timesheet_lines = timesheet_lines

    @property
    def timesheet_id(self):
        """Gets the timesheet_id of this Timesheet.  # noqa: E501

        The Xero identifier for a Timesheet  # noqa: E501

        :return: The timesheet_id of this Timesheet.  # noqa: E501
        :rtype: str
        """
        return self._timesheet_id

    @timesheet_id.setter
    def timesheet_id(self, timesheet_id):
        """Sets the timesheet_id of this Timesheet.

        The Xero identifier for a Timesheet  # noqa: E501

        :param timesheet_id: The timesheet_id of this Timesheet.  # noqa: E501
        :type: str
        """

        self._timesheet_id = timesheet_id

    @property
    def payroll_calendar_id(self):
        """Gets the payroll_calendar_id of this Timesheet.  # noqa: E501

        The Xero identifier for the Payroll Calandar that the Timesheet applies to  # noqa: E501

        :return: The payroll_calendar_id of this Timesheet.  # noqa: E501
        :rtype: str
        """
        return self._payroll_calendar_id

    @payroll_calendar_id.setter
    def payroll_calendar_id(self, payroll_calendar_id):
        """Sets the payroll_calendar_id of this Timesheet.

        The Xero identifier for the Payroll Calandar that the Timesheet applies to  # noqa: E501

        :param payroll_calendar_id: The payroll_calendar_id of this Timesheet.  # noqa: E501
        :type: str
        """
        if payroll_calendar_id is None:
            raise ValueError(
                "Invalid value for `payroll_calendar_id`, must not be `None`"
            )  # noqa: E501

        self._payroll_calendar_id = payroll_calendar_id

    @property
    def employee_id(self):
        """Gets the employee_id of this Timesheet.  # noqa: E501

        The Xero identifier for the Employee that the Timesheet is for  # noqa: E501

        :return: The employee_id of this Timesheet.  # noqa: E501
        :rtype: str
        """
        return self._employee_id

    @employee_id.setter
    def employee_id(self, employee_id):
        """Sets the employee_id of this Timesheet.

        The Xero identifier for the Employee that the Timesheet is for  # noqa: E501

        :param employee_id: The employee_id of this Timesheet.  # noqa: E501
        :type: str
        """
        if employee_id is None:
            raise ValueError(
                "Invalid value for `employee_id`, must not be `None`"
            )  # noqa: E501

        self._employee_id = employee_id

    @property
    def start_date(self):
        """Gets the start_date of this Timesheet.  # noqa: E501

        The Start Date of the Timesheet period (YYYY-MM-DD)  # noqa: E501

        :return: The start_date of this Timesheet.  # noqa: E501
        :rtype: date
        """
        return self._start_date

    @start_date.setter
    def start_date(self, start_date):
        """Sets the start_date of this Timesheet.

        The Start Date of the Timesheet period (YYYY-MM-DD)  # noqa: E501

        :param start_date: The start_date of this Timesheet.  # noqa: E501
        :type: date
        """
        if start_date is None:
            raise ValueError(
                "Invalid value for `start_date`, must not be `None`"
            )  # noqa: E501

        self._start_date = start_date

    @property
    def end_date(self):
        """Gets the end_date of this Timesheet.  # noqa: E501

        The End Date of the Timesheet period (YYYY-MM-DD)  # noqa: E501

        :return: The end_date of this Timesheet.  # noqa: E501
        :rtype: date
        """
        return self._end_date

    @end_date.setter
    def end_date(self, end_date):
        """Sets the end_date of this Timesheet.

        The End Date of the Timesheet period (YYYY-MM-DD)  # noqa: E501

        :param end_date: The end_date of this Timesheet.  # noqa: E501
        :type: date
        """
        if end_date is None:
            raise ValueError(
                "Invalid value for `end_date`, must not be `None`"
            )  # noqa: E501

        self._end_date = end_date

    @property
    def status(self):
        """Gets the status of this Timesheet.  # noqa: E501

        Status of the timesheet  # noqa: E501

        :return: The status of this Timesheet.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this Timesheet.

        Status of the timesheet  # noqa: E501

        :param status: The status of this Timesheet.  # noqa: E501
        :type: str
        """
        allowed_values = ["Draft", "Approved", "Completed", "None"]  # noqa: E501
        if status not in allowed_values:
            raise ValueError(
                "Invalid value for `status` ({0}), must be one of {1}".format(  # noqa: E501
                    status, allowed_values
                )
            )

        self._status = status

    @property
    def total_hours(self):
        """Gets the total_hours of this Timesheet.  # noqa: E501

        The Total Hours of the Timesheet  # noqa: E501

        :return: The total_hours of this Timesheet.  # noqa: E501
        :rtype: float
        """
        return self._total_hours

    @total_hours.setter
    def total_hours(self, total_hours):
        """Sets the total_hours of this Timesheet.

        The Total Hours of the Timesheet  # noqa: E501

        :param total_hours: The total_hours of this Timesheet.  # noqa: E501
        :type: float
        """

        self._total_hours = total_hours

    @property
    def updated_date_utc(self):
        """Gets the updated_date_utc of this Timesheet.  # noqa: E501

        The UTC date time that the Timesheet was last updated  # noqa: E501

        :return: The updated_date_utc of this Timesheet.  # noqa: E501
        :rtype: datetime
        """
        return self._updated_date_utc

    @updated_date_utc.setter
    def updated_date_utc(self, updated_date_utc):
        """Sets the updated_date_utc of this Timesheet.

        The UTC date time that the Timesheet was last updated  # noqa: E501

        :param updated_date_utc: The updated_date_utc of this Timesheet.  # noqa: E501
        :type: datetime
        """

        self._updated_date_utc = updated_date_utc

    @property
    def timesheet_lines(self):
        """Gets the timesheet_lines of this Timesheet.  # noqa: E501


        :return: The timesheet_lines of this Timesheet.  # noqa: E501
        :rtype: list[TimesheetLine]
        """
        return self._timesheet_lines

    @timesheet_lines.setter
    def timesheet_lines(self, timesheet_lines):
        """Sets the timesheet_lines of this Timesheet.


        :param timesheet_lines: The timesheet_lines of this Timesheet.  # noqa: E501
        :type: list[TimesheetLine]
        """

        self._timesheet_lines = timesheet_lines
