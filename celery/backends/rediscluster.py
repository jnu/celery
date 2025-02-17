from .redis import RedisBackend

from redis import RedisCluster


class RedisClusterBackend(RedisBackend):

    def _get_client(self):
        return RedisCluster

    def _params_from_url(self, url, defaults):
        url = url.replace("cluster", "")
        return super()._params_from_url(url, defaults)
