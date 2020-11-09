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


class ManifestListAttributes(Model):
    """ManifestListAttributes.

    :param media_type: The MIME type of the referenced object. This will
     generally be application/vnd.docker.image.manifest.v2+json, but it could
     also be application/vnd.docker.image.manifest.v1+json
    :type media_type: str
    :param size: The size in bytes of the object
    :type size: long
    :param digest: The digest of the content, as defined by the Registry V2
     HTTP API Specification
    :type digest: str
    :param platform:
    :type platform: ~azure.containerregistry.models.Platform
    """

    _attribute_map = {
        'media_type': {'key': 'mediaType', 'type': 'str'},
        'size': {'key': 'size', 'type': 'long'},
        'digest': {'key': 'digest', 'type': 'str'},
        'platform': {'key': 'platform', 'type': 'Platform'},
    }

    def __init__(self, **kwargs):
        super(ManifestListAttributes, self).__init__(**kwargs)
        self.media_type = kwargs.get('media_type', None)
        self.size = kwargs.get('size', None)
        self.digest = kwargs.get('digest', None)
        self.platform = kwargs.get('platform', None)
