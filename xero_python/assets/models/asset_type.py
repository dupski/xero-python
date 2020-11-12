# coding: utf-8

"""
    Xero Assets API

    This is the Xero Assets API  # noqa: E501

    OpenAPI spec version: 2.4.4
    Contact: api@xero.com
    Generated by: https://openapi-generator.tech
"""


import re  # noqa: F401

from xero_python.models import BaseModel


class AssetType(BaseModel):
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
        "asset_type_id": "str",
        "asset_type_name": "str",
        "fixed_asset_account_id": "str",
        "depreciation_expense_account_id": "str",
        "accumulated_depreciation_account_id": "str",
        "book_depreciation_setting": "BookDepreciationSetting",
        "locks": "int",
    }

    attribute_map = {
        "asset_type_id": "assetTypeId",
        "asset_type_name": "assetTypeName",
        "fixed_asset_account_id": "fixedAssetAccountId",
        "depreciation_expense_account_id": "depreciationExpenseAccountId",
        "accumulated_depreciation_account_id": "accumulatedDepreciationAccountId",
        "book_depreciation_setting": "bookDepreciationSetting",
        "locks": "locks",
    }

    def __init__(
        self,
        asset_type_id=None,
        asset_type_name=None,
        fixed_asset_account_id=None,
        depreciation_expense_account_id=None,
        accumulated_depreciation_account_id=None,
        book_depreciation_setting=None,
        locks=None,
    ):  # noqa: E501
        """AssetType - a model defined in OpenAPI"""  # noqa: E501

        self._asset_type_id = None
        self._asset_type_name = None
        self._fixed_asset_account_id = None
        self._depreciation_expense_account_id = None
        self._accumulated_depreciation_account_id = None
        self._book_depreciation_setting = None
        self._locks = None
        self.discriminator = None

        if asset_type_id is not None:
            self.asset_type_id = asset_type_id
        self.asset_type_name = asset_type_name
        if fixed_asset_account_id is not None:
            self.fixed_asset_account_id = fixed_asset_account_id
        if depreciation_expense_account_id is not None:
            self.depreciation_expense_account_id = depreciation_expense_account_id
        if accumulated_depreciation_account_id is not None:
            self.accumulated_depreciation_account_id = (
                accumulated_depreciation_account_id
            )
        self.book_depreciation_setting = book_depreciation_setting
        if locks is not None:
            self.locks = locks

    @property
    def asset_type_id(self):
        """Gets the asset_type_id of this AssetType.  # noqa: E501

        Xero generated unique identifier for asset types  # noqa: E501

        :return: The asset_type_id of this AssetType.  # noqa: E501
        :rtype: str
        """
        return self._asset_type_id

    @asset_type_id.setter
    def asset_type_id(self, asset_type_id):
        """Sets the asset_type_id of this AssetType.

        Xero generated unique identifier for asset types  # noqa: E501

        :param asset_type_id: The asset_type_id of this AssetType.  # noqa: E501
        :type: str
        """

        self._asset_type_id = asset_type_id

    @property
    def asset_type_name(self):
        """Gets the asset_type_name of this AssetType.  # noqa: E501

        The name of the asset type  # noqa: E501

        :return: The asset_type_name of this AssetType.  # noqa: E501
        :rtype: str
        """
        return self._asset_type_name

    @asset_type_name.setter
    def asset_type_name(self, asset_type_name):
        """Sets the asset_type_name of this AssetType.

        The name of the asset type  # noqa: E501

        :param asset_type_name: The asset_type_name of this AssetType.  # noqa: E501
        :type: str
        """
        if asset_type_name is None:
            raise ValueError(
                "Invalid value for `asset_type_name`, must not be `None`"
            )  # noqa: E501

        self._asset_type_name = asset_type_name

    @property
    def fixed_asset_account_id(self):
        """Gets the fixed_asset_account_id of this AssetType.  # noqa: E501

        The asset account for fixed assets of this type  # noqa: E501

        :return: The fixed_asset_account_id of this AssetType.  # noqa: E501
        :rtype: str
        """
        return self._fixed_asset_account_id

    @fixed_asset_account_id.setter
    def fixed_asset_account_id(self, fixed_asset_account_id):
        """Sets the fixed_asset_account_id of this AssetType.

        The asset account for fixed assets of this type  # noqa: E501

        :param fixed_asset_account_id: The fixed_asset_account_id of this AssetType.  # noqa: E501
        :type: str
        """

        self._fixed_asset_account_id = fixed_asset_account_id

    @property
    def depreciation_expense_account_id(self):
        """Gets the depreciation_expense_account_id of this AssetType.  # noqa: E501

        The expense account for the depreciation of fixed assets of this type  # noqa: E501

        :return: The depreciation_expense_account_id of this AssetType.  # noqa: E501
        :rtype: str
        """
        return self._depreciation_expense_account_id

    @depreciation_expense_account_id.setter
    def depreciation_expense_account_id(self, depreciation_expense_account_id):
        """Sets the depreciation_expense_account_id of this AssetType.

        The expense account for the depreciation of fixed assets of this type  # noqa: E501

        :param depreciation_expense_account_id: The depreciation_expense_account_id of this AssetType.  # noqa: E501
        :type: str
        """

        self._depreciation_expense_account_id = depreciation_expense_account_id

    @property
    def accumulated_depreciation_account_id(self):
        """Gets the accumulated_depreciation_account_id of this AssetType.  # noqa: E501

        The account for accumulated depreciation of fixed assets of this type  # noqa: E501

        :return: The accumulated_depreciation_account_id of this AssetType.  # noqa: E501
        :rtype: str
        """
        return self._accumulated_depreciation_account_id

    @accumulated_depreciation_account_id.setter
    def accumulated_depreciation_account_id(self, accumulated_depreciation_account_id):
        """Sets the accumulated_depreciation_account_id of this AssetType.

        The account for accumulated depreciation of fixed assets of this type  # noqa: E501

        :param accumulated_depreciation_account_id: The accumulated_depreciation_account_id of this AssetType.  # noqa: E501
        :type: str
        """

        self._accumulated_depreciation_account_id = accumulated_depreciation_account_id

    @property
    def book_depreciation_setting(self):
        """Gets the book_depreciation_setting of this AssetType.  # noqa: E501


        :return: The book_depreciation_setting of this AssetType.  # noqa: E501
        :rtype: BookDepreciationSetting
        """
        return self._book_depreciation_setting

    @book_depreciation_setting.setter
    def book_depreciation_setting(self, book_depreciation_setting):
        """Sets the book_depreciation_setting of this AssetType.


        :param book_depreciation_setting: The book_depreciation_setting of this AssetType.  # noqa: E501
        :type: BookDepreciationSetting
        """
        if book_depreciation_setting is None:
            raise ValueError(
                "Invalid value for `book_depreciation_setting`, must not be `None`"
            )  # noqa: E501

        self._book_depreciation_setting = book_depreciation_setting

    @property
    def locks(self):
        """Gets the locks of this AssetType.  # noqa: E501

        All asset types that have accumulated depreciation for any assets that use them are deemed ‘locked’ and cannot be removed.  # noqa: E501

        :return: The locks of this AssetType.  # noqa: E501
        :rtype: int
        """
        return self._locks

    @locks.setter
    def locks(self, locks):
        """Sets the locks of this AssetType.

        All asset types that have accumulated depreciation for any assets that use them are deemed ‘locked’ and cannot be removed.  # noqa: E501

        :param locks: The locks of this AssetType.  # noqa: E501
        :type: int
        """

        self._locks = locks
