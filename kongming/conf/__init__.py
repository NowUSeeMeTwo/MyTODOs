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

from oslo_config import cfg

from kongming.conf import agent
from kongming.conf import api
from kongming.conf import database
from kongming.conf import default
from kongming.conf import notification_handler
from kongming.conf import nova

CONF = cfg.CONF
api.register_opts(CONF)
database.register_opts(CONF)
default.register_opts(CONF)
agent.register_opts(CONF)
notification_handler.register_opts(CONF)
nova.register_opts(CONF)
