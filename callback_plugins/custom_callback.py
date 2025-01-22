from ansible.plugins.callback import CallbackBase

class CallbackModule(CallbackBase):
    """
    Custom callback plugin to securely capture 'comp_name' and add it to job metadata.
    """
    CALLBACK_VERSION = 2.0
    CALLBACK_TYPE = 'aggregate'
    CALLBACK_NAME = 'custom_comp_name'

    def __init__(self):
        super(CallbackModule, self).__init__()
        self.comp_name = None

    def v2_runner_on_ok(self, result, **kwargs):
        """
        Capture the 'comp_name' variable when the task succeeds.
        """
        task_vars = result._result.get('ansible_facts', {})
        if not task_vars:
            task_vars = result._result.get('results', {})

        # Safely check for 'comp_name' in task_vars
        if 'comp_name' in task_vars:
            self.comp_name = task_vars['comp_name']
            self._display.display(f"'comp_name' captured: {self.comp_name}", log_only=True)

    def v2_playbook_on_stats(self, stats):
        """
        Add 'comp_name' to job metadata when the playbook completes.
        """
        if self.comp_name:
            # Inject 'comp_name' into job metadata
            stats.custom_stats = {"comp_name": self.comp_name}
            self._display.display(f"'comp_name' added to job metadata: {self.comp_name}", log_only=True)
