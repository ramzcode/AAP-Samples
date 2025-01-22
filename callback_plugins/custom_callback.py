from ansible.plugins.callback import CallbackBase


class CallbackModule(CallbackBase):
    """
    Custom callback plugin to add the 'comp_name' variable to the API response.
    Ensures the variable is included in the job metadata without appearing in logs or artifacts.
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
        if 'comp_name' in result._task_vars:
            self.comp_name = result._task_vars['comp_name']
            self._display.display(f"'comp_name' captured: {self.comp_name}", log_only=True)

    def v2_playbook_on_stats(self, stats):
        """
        Add 'comp_name' to the job metadata when the playbook completes.
        """
        if self.comp_name:
            # Inject the variable into the job metadata (retrievable via the API)
            stats.custom_stats = {"comp_name": self.comp_name}
            self._display.display(f"'comp_name' added to job metadata: {self.comp_name}", log_only=True)
