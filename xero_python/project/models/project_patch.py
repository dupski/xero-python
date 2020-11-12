# coding: utf-8

"""
    Xero Projects API

    This is the Xero Projects API  # noqa: E501

    OpenAPI spec version: 2.4.4
    Contact: api@xero.com
    Generated by: https://openapi-generator.tech
"""


import re  # noqa: F401

from xero_python.models import BaseModel


class ProjectPatch(BaseModel):
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
    openapi_types = {"status": "ProjectStatus"}

    attribute_map = {"status": "status"}

    def __init__(self, status=None):  # noqa: E501
        """ProjectPatch - a model defined in OpenAPI"""  # noqa: E501

        self._status = None
        self.discriminator = None

        self.status = status

    @property
    def status(self):
        """Gets the status of this ProjectPatch.  # noqa: E501


        :return: The status of this ProjectPatch.  # noqa: E501
        :rtype: ProjectStatus
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this ProjectPatch.


        :param status: The status of this ProjectPatch.  # noqa: E501
        :type: ProjectStatus
        """
        if status is None:
            raise ValueError(
                "Invalid value for `status`, must not be `None`"
            )  # noqa: E501

        self._status = status
