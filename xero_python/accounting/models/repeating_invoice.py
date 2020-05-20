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


class RepeatingInvoice(BaseModel):
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
        "type": "str",
        "contact": "Contact",
        "schedule": "Schedule",
        "line_items": "list[LineItem]",
        "line_amount_types": "LineAmountTypes",
        "reference": "str",
        "branding_theme_id": "str",
        "currency_code": "CurrencyCode",
        "status": "str",
        "sub_total": "float",
        "total_tax": "float",
        "total": "float",
        "repeating_invoice_id": "str",
        "id": "str",
        "has_attachments": "bool",
        "attachments": "list[Attachment]",
    }

    attribute_map = {
        "type": "Type",
        "contact": "Contact",
        "schedule": "Schedule",
        "line_items": "LineItems",
        "line_amount_types": "LineAmountTypes",
        "reference": "Reference",
        "branding_theme_id": "BrandingThemeID",
        "currency_code": "CurrencyCode",
        "status": "Status",
        "sub_total": "SubTotal",
        "total_tax": "TotalTax",
        "total": "Total",
        "repeating_invoice_id": "RepeatingInvoiceID",
        "id": "ID",
        "has_attachments": "HasAttachments",
        "attachments": "Attachments",
    }

    def __init__(
        self,
        type=None,
        contact=None,
        schedule=None,
        line_items=None,
        line_amount_types=None,
        reference=None,
        branding_theme_id=None,
        currency_code=None,
        status=None,
        sub_total=None,
        total_tax=None,
        total=None,
        repeating_invoice_id=None,
        id=None,
        has_attachments=False,
        attachments=None,
    ):  # noqa: E501
        """RepeatingInvoice - a model defined in OpenAPI"""  # noqa: E501

        self._type = None
        self._contact = None
        self._schedule = None
        self._line_items = None
        self._line_amount_types = None
        self._reference = None
        self._branding_theme_id = None
        self._currency_code = None
        self._status = None
        self._sub_total = None
        self._total_tax = None
        self._total = None
        self._repeating_invoice_id = None
        self._id = None
        self._has_attachments = None
        self._attachments = None
        self.discriminator = None

        if type is not None:
            self.type = type
        if contact is not None:
            self.contact = contact
        if schedule is not None:
            self.schedule = schedule
        if line_items is not None:
            self.line_items = line_items
        if line_amount_types is not None:
            self.line_amount_types = line_amount_types
        if reference is not None:
            self.reference = reference
        if branding_theme_id is not None:
            self.branding_theme_id = branding_theme_id
        if currency_code is not None:
            self.currency_code = currency_code
        if status is not None:
            self.status = status
        if sub_total is not None:
            self.sub_total = sub_total
        if total_tax is not None:
            self.total_tax = total_tax
        if total is not None:
            self.total = total
        if repeating_invoice_id is not None:
            self.repeating_invoice_id = repeating_invoice_id
        if id is not None:
            self.id = id
        if has_attachments is not None:
            self.has_attachments = has_attachments
        if attachments is not None:
            self.attachments = attachments

    @property
    def type(self):
        """Gets the type of this RepeatingInvoice.  # noqa: E501

        See Invoice Types  # noqa: E501

        :return: The type of this RepeatingInvoice.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this RepeatingInvoice.

        See Invoice Types  # noqa: E501

        :param type: The type of this RepeatingInvoice.  # noqa: E501
        :type: str
        """
        allowed_values = ["ACCPAY", "ACCREC"]  # noqa: E501
        if type not in allowed_values:
            raise ValueError(
                "Invalid value for `type` ({0}), must be one of {1}".format(  # noqa: E501
                    type, allowed_values
                )
            )

        self._type = type

    @property
    def contact(self):
        """Gets the contact of this RepeatingInvoice.  # noqa: E501


        :return: The contact of this RepeatingInvoice.  # noqa: E501
        :rtype: Contact
        """
        return self._contact

    @contact.setter
    def contact(self, contact):
        """Sets the contact of this RepeatingInvoice.


        :param contact: The contact of this RepeatingInvoice.  # noqa: E501
        :type: Contact
        """

        self._contact = contact

    @property
    def schedule(self):
        """Gets the schedule of this RepeatingInvoice.  # noqa: E501


        :return: The schedule of this RepeatingInvoice.  # noqa: E501
        :rtype: Schedule
        """
        return self._schedule

    @schedule.setter
    def schedule(self, schedule):
        """Sets the schedule of this RepeatingInvoice.


        :param schedule: The schedule of this RepeatingInvoice.  # noqa: E501
        :type: Schedule
        """

        self._schedule = schedule

    @property
    def line_items(self):
        """Gets the line_items of this RepeatingInvoice.  # noqa: E501

        See LineItems  # noqa: E501

        :return: The line_items of this RepeatingInvoice.  # noqa: E501
        :rtype: list[LineItem]
        """
        return self._line_items

    @line_items.setter
    def line_items(self, line_items):
        """Sets the line_items of this RepeatingInvoice.

        See LineItems  # noqa: E501

        :param line_items: The line_items of this RepeatingInvoice.  # noqa: E501
        :type: list[LineItem]
        """

        self._line_items = line_items

    @property
    def line_amount_types(self):
        """Gets the line_amount_types of this RepeatingInvoice.  # noqa: E501


        :return: The line_amount_types of this RepeatingInvoice.  # noqa: E501
        :rtype: LineAmountTypes
        """
        return self._line_amount_types

    @line_amount_types.setter
    def line_amount_types(self, line_amount_types):
        """Sets the line_amount_types of this RepeatingInvoice.


        :param line_amount_types: The line_amount_types of this RepeatingInvoice.  # noqa: E501
        :type: LineAmountTypes
        """

        self._line_amount_types = line_amount_types

    @property
    def reference(self):
        """Gets the reference of this RepeatingInvoice.  # noqa: E501

        ACCREC only – additional reference number  # noqa: E501

        :return: The reference of this RepeatingInvoice.  # noqa: E501
        :rtype: str
        """
        return self._reference

    @reference.setter
    def reference(self, reference):
        """Sets the reference of this RepeatingInvoice.

        ACCREC only – additional reference number  # noqa: E501

        :param reference: The reference of this RepeatingInvoice.  # noqa: E501
        :type: str
        """

        self._reference = reference

    @property
    def branding_theme_id(self):
        """Gets the branding_theme_id of this RepeatingInvoice.  # noqa: E501

        See BrandingThemes  # noqa: E501

        :return: The branding_theme_id of this RepeatingInvoice.  # noqa: E501
        :rtype: str
        """
        return self._branding_theme_id

    @branding_theme_id.setter
    def branding_theme_id(self, branding_theme_id):
        """Sets the branding_theme_id of this RepeatingInvoice.

        See BrandingThemes  # noqa: E501

        :param branding_theme_id: The branding_theme_id of this RepeatingInvoice.  # noqa: E501
        :type: str
        """

        self._branding_theme_id = branding_theme_id

    @property
    def currency_code(self):
        """Gets the currency_code of this RepeatingInvoice.  # noqa: E501


        :return: The currency_code of this RepeatingInvoice.  # noqa: E501
        :rtype: CurrencyCode
        """
        return self._currency_code

    @currency_code.setter
    def currency_code(self, currency_code):
        """Sets the currency_code of this RepeatingInvoice.


        :param currency_code: The currency_code of this RepeatingInvoice.  # noqa: E501
        :type: CurrencyCode
        """

        self._currency_code = currency_code

    @property
    def status(self):
        """Gets the status of this RepeatingInvoice.  # noqa: E501

        One of the following - DRAFT or AUTHORISED – See Invoice Status Codes  # noqa: E501

        :return: The status of this RepeatingInvoice.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this RepeatingInvoice.

        One of the following - DRAFT or AUTHORISED – See Invoice Status Codes  # noqa: E501

        :param status: The status of this RepeatingInvoice.  # noqa: E501
        :type: str
        """
        allowed_values = ["DRAFT", "AUTHORISED", "DELETED"]  # noqa: E501
        if status not in allowed_values:
            raise ValueError(
                "Invalid value for `status` ({0}), must be one of {1}".format(  # noqa: E501
                    status, allowed_values
                )
            )

        self._status = status

    @property
    def sub_total(self):
        """Gets the sub_total of this RepeatingInvoice.  # noqa: E501

        Total of invoice excluding taxes  # noqa: E501

        :return: The sub_total of this RepeatingInvoice.  # noqa: E501
        :rtype: float
        """
        return self._sub_total

    @sub_total.setter
    def sub_total(self, sub_total):
        """Sets the sub_total of this RepeatingInvoice.

        Total of invoice excluding taxes  # noqa: E501

        :param sub_total: The sub_total of this RepeatingInvoice.  # noqa: E501
        :type: float
        """

        self._sub_total = sub_total

    @property
    def total_tax(self):
        """Gets the total_tax of this RepeatingInvoice.  # noqa: E501

        Total tax on invoice  # noqa: E501

        :return: The total_tax of this RepeatingInvoice.  # noqa: E501
        :rtype: float
        """
        return self._total_tax

    @total_tax.setter
    def total_tax(self, total_tax):
        """Sets the total_tax of this RepeatingInvoice.

        Total tax on invoice  # noqa: E501

        :param total_tax: The total_tax of this RepeatingInvoice.  # noqa: E501
        :type: float
        """

        self._total_tax = total_tax

    @property
    def total(self):
        """Gets the total of this RepeatingInvoice.  # noqa: E501

        Total of Invoice tax inclusive (i.e. SubTotal + TotalTax)  # noqa: E501

        :return: The total of this RepeatingInvoice.  # noqa: E501
        :rtype: float
        """
        return self._total

    @total.setter
    def total(self, total):
        """Sets the total of this RepeatingInvoice.

        Total of Invoice tax inclusive (i.e. SubTotal + TotalTax)  # noqa: E501

        :param total: The total of this RepeatingInvoice.  # noqa: E501
        :type: float
        """

        self._total = total

    @property
    def repeating_invoice_id(self):
        """Gets the repeating_invoice_id of this RepeatingInvoice.  # noqa: E501

        Xero generated unique identifier for repeating invoice template  # noqa: E501

        :return: The repeating_invoice_id of this RepeatingInvoice.  # noqa: E501
        :rtype: str
        """
        return self._repeating_invoice_id

    @repeating_invoice_id.setter
    def repeating_invoice_id(self, repeating_invoice_id):
        """Sets the repeating_invoice_id of this RepeatingInvoice.

        Xero generated unique identifier for repeating invoice template  # noqa: E501

        :param repeating_invoice_id: The repeating_invoice_id of this RepeatingInvoice.  # noqa: E501
        :type: str
        """

        self._repeating_invoice_id = repeating_invoice_id

    @property
    def id(self):
        """Gets the id of this RepeatingInvoice.  # noqa: E501

        Xero generated unique identifier for repeating invoice template  # noqa: E501

        :return: The id of this RepeatingInvoice.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this RepeatingInvoice.

        Xero generated unique identifier for repeating invoice template  # noqa: E501

        :param id: The id of this RepeatingInvoice.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def has_attachments(self):
        """Gets the has_attachments of this RepeatingInvoice.  # noqa: E501

        boolean to indicate if an invoice has an attachment  # noqa: E501

        :return: The has_attachments of this RepeatingInvoice.  # noqa: E501
        :rtype: bool
        """
        return self._has_attachments

    @has_attachments.setter
    def has_attachments(self, has_attachments):
        """Sets the has_attachments of this RepeatingInvoice.

        boolean to indicate if an invoice has an attachment  # noqa: E501

        :param has_attachments: The has_attachments of this RepeatingInvoice.  # noqa: E501
        :type: bool
        """

        self._has_attachments = has_attachments

    @property
    def attachments(self):
        """Gets the attachments of this RepeatingInvoice.  # noqa: E501

        Displays array of attachments from the API  # noqa: E501

        :return: The attachments of this RepeatingInvoice.  # noqa: E501
        :rtype: list[Attachment]
        """
        return self._attachments

    @attachments.setter
    def attachments(self, attachments):
        """Sets the attachments of this RepeatingInvoice.

        Displays array of attachments from the API  # noqa: E501

        :param attachments: The attachments of this RepeatingInvoice.  # noqa: E501
        :type: list[Attachment]
        """

        self._attachments = attachments
