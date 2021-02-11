from airflow.exceptions import AirflowException
from airflow.contrib.hooks.trifacta_hook import TrifactaHook
from airflow.models import BaseOperator
from airflow.utils.decorators import apply_defaults


XCOM_FLOW_RUN_ID = "flow_id"

class TrifactaOperator(BaseOperator):
    """
    Operator that runs Trifacta Flows.

    Parameters
    -----
    conn_id : str
        ID of the connection to use to connect to the Trifacta.
    flow : str
        The name of the flow that will be executed.
    """

    @apply_defaults
    def __init__(
            self,
            conn_id: str,
            flow: str,
            **kwargs) -> None:
        super(TrifactaOperator, self).__init__(**kwargs)

        self._conn_id = conn_id
        self._flow = flow

    def get_hook(self):
        return TrifactaHook(self._conn_id)

    def execute(self, context):
        hook = self.get_hook()
        flow_id = hook.run_flow(self._flow)
        # Poll for job, return when done

