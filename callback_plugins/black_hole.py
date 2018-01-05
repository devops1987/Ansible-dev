# (c) 2012-2014, Michael DeHaan <michael.dehaan@gmail.com>
#
# This file is part of Ansible
#
# Ansible is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# Ansible is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with Ansible.  If not, see <http://www.gnu.org/licenses/>.

# Make coding more python3-ish
from __future__ import (absolute_import, division, print_function)
__metaclass__ = type

from ansible.plugins.callback.default import CallbackModule as CallbackModule_default

class CallbackModule(CallbackModule_default):

    '''
    Magic black hole, nothing will show up.
    '''

    CALLBACK_VERSION = 2.0
    CALLBACK_TYPE = 'stdout'
    CALLBACK_NAME = 'black_hole'

    def on_any(self, *args, **kwargs):
        pass
    def runner_on_failed(self, host, res, ignore_errors=False):
        pass
    def runner_on_ok(self, host, res):
        pass
    def runner_on_skipped(self, host, item=None):
        pass
    def runner_on_unreachable(self, host, res):
        pass
    def runner_on_no_hosts(self):
        pass
    def runner_on_async_poll(self, host, res, jid, clock):
        pass
    def runner_on_async_ok(self, host, res, jid):
        pass
    def runner_on_async_failed(self, host, res, jid):
        pass
    def playbook_on_start(self):
        pass
    def playbook_on_notify(self, host, handler):
        pass
    def playbook_on_no_hosts_matched(self):
        pass
    def playbook_on_no_hosts_remaining(self):
        pass
    def playbook_on_task_start(self, name, is_conditional):
        pass
    def playbook_on_vars_prompt(self, varname, private=True, prompt=None, encrypt=None, confirm=False, salt_size=None, salt=None, default=None):
        pass
    def playbook_on_setup(self):
        pass
    def playbook_on_import_for_host(self, host, imported_file):
        pass
    def playbook_on_not_import_for_host(self, host, missing_file):
        pass
    def playbook_on_play_start(self, name):
        pass
    def playbook_on_stats(self, stats):
        pass
    def on_file_diff(self, host, diff):
        pass
    def v2_on_any(self, *args, **kwargs):
        pass
    def v2_runner_on_failed(self, result, ignore_errors=False):
        pass
    def v2_runner_on_ok(self, result):
        pass
    def v2_runner_on_skipped(self, result):
        pass
    def v2_runner_on_unreachable(self, result):
        pass
    def v2_runner_on_no_hosts(self, task):
        pass
    def v2_runner_on_async_poll(self, result):
        pass
    def v2_runner_on_async_ok(self, result):
        pass
    def v2_runner_on_async_failed(self, result):
        pass
    def v2_runner_on_file_diff(self, result, diff):
        pass
    def v2_playbook_on_start(self, playbook):
        pass
    def v2_playbook_on_notify(self, result, handler):
        pass
    def v2_playbook_on_no_hosts_matched(self):
        pass
    def v2_playbook_on_no_hosts_remaining(self):
        pass
    def v2_playbook_on_task_start(self, task, is_conditional):
        pass
    def v2_playbook_on_cleanup_task_start(self, task):
        pass
    def v2_playbook_on_handler_task_start(self, task):
        pass
    def v2_playbook_on_vars_prompt(self, varname, private=True, prompt=None, encrypt=None, confirm=False, salt_size=None, salt=None, default=None):
        pass
    def v2_playbook_on_setup(self):
        pass
    def v2_playbook_on_import_for_host(self, result, imported_file):
        pass
    def v2_playbook_on_not_import_for_host(self, result, missing_file):
        pass
    def v2_playbook_on_play_start(self, play):
        pass
    def v2_playbook_on_stats(self, stats):
        pass
    def v2_on_file_diff(self, result):
        pass
    def v2_playbook_on_include(self, included_file):
        pass
    def v2_runner_item_on_ok(self, result):
        pass
    def v2_runner_item_on_failed(self, result):
        pass
    def v2_runner_item_on_skipped(self, result):
        pass
    def v2_runner_retry(self, result):
        pass
