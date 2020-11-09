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


class ImageSignature(Model):
    """Signature of a signed manifest.

    :param header: A JSON web signature
    :type header: ~azure.containerregistry.models.JWK
    :param signature: A signature for the image manifest, signed by a libtrust
     private key
    :type signature: str
    :param protected: The signed protected header
    :type protected: str
    """

    _attribute_map = {
        'header': {'key': 'header', 'type': 'JWK'},
        'signature': {'key': 'signature', 'type': 'str'},
        'protected': {'key': 'protected', 'type': 'str'},
    }

    def __init__(self, **kwargs):
        super(ImageSignature, self).__init__(**kwargs)
        self.header = kwargs.get('header', None)
        self.signature = kwargs.get('signature', None)
        self.protected = kwargs.get('protected', None)
