import os

import kazoo.client
import kazoo.exceptions


class zk_client():
    """zookeeper client class.

    This Class enables the usage of zookeeper as backend.

    ZK Quorum Endpoints must be configured in the ZK environment variable.
    """

    kz_retry = kazoo.client.KazooRetry(max_tries=-1, delay=0.5, max_delay=30)

    def __init__(self):
        if 'ZK' not in os.environ:
            raise RuntimeError('zookeeper ensemble service has not been configured.')

        self.state = None
        self.connect()

        # just to be sure basepath of configurations is always on zookeeper
        if not self.zk.exists('/haproxy'):
            self.zk.create(path='/haproxy', ephemeral=False)

    def connect(self):
        self.zk = kazoo.client.KazooClient(hosts=os.environ['ZK'], connection_retry=zk_client.kz_retry)
        self.zk.start(timeout=30)

    def check_session_state(self):
        if self.zk.state != kazoo.client.KazooState.CONNECTED:
            self.connect()

    def write(self, path, val):
        self.check_session_state()

        if not self.zk.exists(path):
            self.zk.create(path=path, value=val.encode('utf-8'), ephemeral=True, makepath=True)
