# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class ChangeableAttributes(Model):
    """ChangeableAttributes.

    :param delete_enabled: Delete enabled
    :type delete_enabled: bool
    :param write_enabled: Write enabled
    :type write_enabled: bool
    :param list_enabled: List enabled
    :type list_enabled: bool
    :param read_enabled: Read enabled
    :type read_enabled: bool
    """

    _attribute_map = {
        'delete_enabled': {'key': 'deleteEnabled', 'type': 'bool'},
        'write_enabled': {'key': 'writeEnabled', 'type': 'bool'},
        'list_enabled': {'key': 'listEnabled', 'type': 'bool'},
        'read_enabled': {'key': 'readEnabled', 'type': 'bool'},
    }

    def __init__(self, **kwargs):
        super(ChangeableAttributes, self).__init__(**kwargs)
        self.delete_enabled = kwargs.get('delete_enabled', None)
        self.write_enabled = kwargs.get('write_enabled', None)
        self.list_enabled = kwargs.get('list_enabled', None)
        self.read_enabled = kwargs.get('read_enabled', None)
