from airflow.hooks.base_hook import BaseHook

import json
import requests

METHOD_MAP = {
    "GET": requests.get,
    "POST": requests.post
}

FLOW_LIST_CALL = ("GET", "flows")
FLOW_RUN_CALL = ("GET", "flows/{id}/run")
FLOW_STATUS_CALL = ("GET", "flowRuns/{id}/status")

class TrifactaHook(BaseHook):
    """
    Interact with Trifacta on-prem or
    """
    def __init__(self, conn_id):
        super().__init__()
        self._conn_id = conn_id
        self._session = None
        self._base_url = None

        self._conn = self.get_conn()


    @staticmethod
    def _get_headers(token: str) -> dict:
        return {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {token}"
        }

    @staticmethod
    def _construct_url(host: str, uri: str) -> str:
        return f"https://{host}/{uri}"

    def _call_api(self, target, body=None, template={}):
        """
        Make API requests to Trifacta
        """

        token = self._conn.extra_dejson.get('', None)
        if token:
            auth = _get_headers(token)
        else:
            raise ValueError("The connection did not contain an access token")

        method, uri = target
        url = _construct_url(self._conn.host, uri.format(**template))

        functor = METHOD_MAP.get(method, None)
        if not functor:
            raise AirflowException(f"Unsupported method: {method}")

        try:
            res = functor(
                    url,
                    json=body,
                    headers=_get_headers(),
                    timeout=1000)
            res.raise_for_status()
            return res.json()
        except requests_exceptions.RequestException as e:
            status_code = e.response.status_code
            res_content = e.response.content
            raise AirflowException(f"Status code: {status_code}, Content {res_content}")

    def get_conn(self):
        if self._session is None:
            config = self.get_connection(self._comm_id)

            schema = config.schema or "https"
            host = config.host or "localhost"
            port = config.port or "80"

            self._base_url = f"{schema}://{host}:{port}"

            self._session = requests.Session()

            if config.login:
                self._session.auth = (config.login, config.password)

        return self._session, self._base_url

    def _detect_flow(self, flow: str) -> str:
        """
        The Trifacta API uses integer ids, so we have
        some work to do to get the id associated with
        the name.
        """
        all_flows = self._call_api(FLOW_LIST_CALL, None)
        for flow in all_flows["data"]:
            if flow["name"] == flow:
                return flow

        return None

    def run_flow(self, flow: str, body: str):
        """
        Runs a flow, using the name of the flow as the key.
        The API requires a flow id, so we perform a lookup
        first to find the flow by name, then extract the flow id.
        """
        flow_data = self._detect_flow(flow)

        if flow_data:
            res = self._call_api(FLOW_RUN_CALL, None)
            self._wait_on_flow(res)
        else:
            raise ValueError(f"{flow} is not a valid flow identifier")

    def _get_flow_status(self, flow_run_id: str):
        """
        Given a flow run id, get the current status of the job.
        """
        res = self._call_api(FLOW_STATUS_CALL, None, {"id": flow_run_id})

    def _wait_on_flow(self, flow_run: dict):
        """
        Waits for a flow run to finish. This is a blocking loop.
        """
        flow_run_id = res["data"][0]["flowRun"]["id"]

        for idx in range(0,10):
            flow_run_status = self._get_flow_status(flow_run_id)

            # Status: Complete, InProgress, Cancelled, Created, Failed, Pending
            if flow_run_status == "Complete":
                break

            time.sleep(5)


