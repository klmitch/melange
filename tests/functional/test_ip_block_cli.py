#!/usr/bin/env python
# vim: tabstop=4 shiftwidth=4 softtabstop=4

# Copyright 2011 OpenStack LLC.
# All Rights Reserved.
#
#    Licensed under the Apache License, Version 2.0 (the "License"); you may
#    not use this file except in compliance with the License. You may obtain
#    a copy of the License at
#
#         http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
#    WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
#    License for the specific language governing permissions and limitations
#    under the License.

# If ../melange/__init__.py exists, add ../ to Python search path, so that
# it will override what happens to be installed in /usr/(local/)lib/python...
import unittest
from melange.ipam.models import IpBlock

from tests.functional import execute
from tests.functional import get_api_port
from tests import BaseTest


class TestPublicIpBlock(BaseTest):

    def test_create(self):
        exitcode, out, err = execute("../bin/melange-manage --port=%s "
                                     "public_ip_block create 10.1.1.0/29"
                                     % get_api_port())

        self.assertEqual(exitcode, 0)
        ip_block = IpBlock.get_by(cidr="10.1.1.0/29", type='public')
        self.assertTrue(ip_block is not None)

    def test_list(self):
        exitcode, out, err = execute("../bin/melange-manage --port=%s "
                                     "public_ip_block list"
                                     % get_api_port())

        self.assertEqual(exitcode, 0)
        self.assertIn("ip_blocks", out)