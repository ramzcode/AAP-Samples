from ansible.plugins.callback import CallbackBase

class CallbackModule(CallbackBase):
    CALLBACK_VERSION = 2.0
    CALLBACK_TYPE = 'notification'
    CALLBACK_NAME = 'my_sensitive_callback'

    def __init__(self):
        super(CallbackModule, self).__init__()
        self.sensitive_data = None

    def v2_runner_on_ok(self, result):
        # Capture the sensitive variable from the task result
        if 'sensitive_variable' in result._result:
            self.sensitive_data = result._result['sensitive_variable']

    def v2_playbook_on_stats(self, stats):
        # Attach the sensitive data to the job result
        if self.sensitive_data:
            # Use the custom_stats feature to attach data to the job result
            self._display.display(f"Attaching sensitive data to job result")
            stats.custom['sensitive_variable'] = self.sensitive_data