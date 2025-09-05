from plone.app.testing import applyProfile
from plone.app.testing import IntegrationTesting
from plone.app.testing import PloneSandboxLayer
from plone.app.testing.layers import PLONE_FIXTURE

import collective.js.fancytree


class PloneStaticresourcesLayer(PloneSandboxLayer):
    defaultBases = (PLONE_FIXTURE,)

    def setUpZope(self, app, configurationContext):
        self.loadZCML(package=collective.js.fancytree)

    def setUpPloneSite(self, portal):
        applyProfile(portal, "collective.js.fancytree:default")


FIXTURE = PloneStaticresourcesLayer()


INTEGRATION_TESTING = IntegrationTesting(
    bases=(FIXTURE,),
    name="FancytreeLayer:IntegrationTesting",
)
