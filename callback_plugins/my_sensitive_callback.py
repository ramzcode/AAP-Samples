from ansible.plugins.callback import CallbackBase
from ansible.module_utils.six import iteritems
from ansible.utils.vars import isidentifier

class CallbackModule(CallbackBase):
    CALLBACK_VERSION = 2.0
    CALLBACK_TYPE = 'notification'
    CALLBACK_NAME = 'my_sensitive_callback'

    def __init__(self):
        super(CallbackModule, self).__init__()
        self.god6 = None

    def v2_runner_on_ok(self, result):
        # Capture the variable from the task result
        if 'god6' in result._result:
            self.god6 = result._result['god6']
            self._display.display(f"Captured god6: {self.god6}")

    def v2_playbook_on_stats(self, stats):
        # Prepare the data structure
        custom_stats = {'data': {}, 'per_host': False, 'aggregate': True}

        # Validate and template the key
        key = 'god6'
        if not isidentifier(key):
            self._display.display(f"Invalid variable name: {key}")
            return

        # Template the value
        value = self.god6

        # Set the data
        custom_stats['data'][key] = value

        # Attach the custom stats to the job result
        if not hasattr(stats, 'custom'):
            stats.custom = {}
        stats.custom.update(custom_stats)

        self._display.display(f"Successfully attached custom stats: {custom_stats}")