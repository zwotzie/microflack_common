import os

from kazoo.client import KazooClient


class zk_client():
    """zookeeper client class.

    This Class enables the useage of zookeeper as backend.

    Endpoints must be configured in the ZK environment variable.
    """

    def __init__(self):
        if 'ZK' not in os.environ:
            raise RuntimeError('zookeeper ensemble service has not been configured.')

        self.connect()

    def connect(self):
        self.zk = KazooClient(hosts=os.environ['ZK'])
        self.zk.start()


    def write(self, node, val):
        # Determine if a node exists
        if self.zk.exists(node):
            self.zk.set(node, val)
        else:
            self.zk.ensure_path(node)
            self.zk.set(node, val)
