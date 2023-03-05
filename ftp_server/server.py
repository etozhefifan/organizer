from twisted.cred.checkers import (
    AllowAnonymousAccess,
    InMemoryUsernamePasswordDatabaseDontUse,
)
from twisted.cred.portal import Portal
from twisted.internet import reactor
from twisted.protocols.ftp import FTPFactory, FTPRealm

portal = Portal(FTPRealm("./public"), [AllowAnonymousAccess()])

factory = FTPFactory(portal)

reactor.listenTCP(8000, factory)
reactor.run()
