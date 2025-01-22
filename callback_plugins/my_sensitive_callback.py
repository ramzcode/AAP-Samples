from ansible.plugins.callback import CallbackBase

class CallbackModule(CallbackBase):
    CALLBACK_VERSION = 2.0
    CALLBACK_TYPE = 'aggregate'
    CALLBACK_NAME = 'my_sensitive_callback'

    def __init__(self):
        super(CallbackModule, self).__init__()
        self.god6 = None

    def v2_runner_on_ok(self, result):
        print('running')
        # Capture the sensitive variable from the task result
        if 'god6' in result._result:
            print('running')
            self.god6 = result._result['god6']
            self._display.display(f"Captured god6: {self.god6}")

    def v2_playbook_on_stats(self, stats):
        # Attach the sensitive data to the job result
        if self.god6 is not None::
            # Use the custom_stats feature to attach data to the job result
            self._display.display(f"Attaching sensitive data to job result")
            if not hasattr(stats, 'custom'):
                stats.custom = {}
            stats.custom['god6'] = self.god6
            stats.custom= {"six": self.god6}