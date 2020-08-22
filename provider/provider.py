import shlex
import subprocess

from autobahn.twisted.wamp import ApplicationSession, ApplicationRunner


class OpenerSession(ApplicationSession):

    def _open_url(self, url):
        subprocess.check_call(shlex.split(f"/usr/bin/xdg-open {url}"))

    async def onJoin(self, details):
        reg = await self.register(self._open_url, "org.deskconn.url.open")
        self.log.info("Registered procedure {procedure}", procedure=reg.procedure)


if __name__ == '__main__':
    runner = ApplicationRunner("ws://192.168.100.30:9001/ws", realm="main")
    runner.run(OpenerSession)
