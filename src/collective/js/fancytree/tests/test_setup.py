"""Setup tests for this package."""

from collective.js.fancytree.testing import INTEGRATION_TESTING
from plone import api
from plone.base.interfaces import IBundleRegistry
from plone.base.utils import get_installer
from plone.registry.interfaces import IRegistry
from Products.CMFPlone.resources.browser.resource import REQUEST_CACHE_KEY
from Products.CMFPlone.resources.browser.resource import ScriptsView
from Products.CMFPlone.resources.browser.resource import StylesView
from zope.component import getUtility

import unittest


class TestSetup(unittest.TestCase):
    """Test that collective.js.fancytree is properly installed."""

    layer = INTEGRATION_TESTING

    def setUp(self):
        """Custom shared utility setup for tests."""
        self.portal = self.layer["portal"]
        self.request = self.layer["request"]
        self.installer = get_installer(self.portal, self.request)
        self.setup_tool = api.portal.get_tool("portal_setup")
        self.registry = getUtility(IRegistry)
        self.bundles = self.registry.collectionOfInterface(
            IBundleRegistry, prefix="plone.bundles"
        )

    def test_install_default(self):
        self.assertTrue(self.installer.is_product_installed("collective.js.fancytree"))
        self.assertIn("fancytree", self.bundles)
        scripts = ScriptsView(self.layer["portal"], self.layer["request"], None)
        scripts.update()
        results = scripts.render()
        self.assertIn(
            "++resource++collective.js.fancytree/jquery.fancytree.min.js", results
        )

    def test_install_all(self):
        self.assertTrue(self.installer.is_product_installed("collective.js.fancytree"))
        self.assertIn("fancytree", self.bundles)
        scripts = ScriptsView(self.layer["portal"], self.layer["request"], None)
        scripts.update()
        results = scripts.render()
        self.assertIn(
            "++resource++collective.js.fancytree/jquery.fancytree.min.js", results
        )
        self.setup_tool.runAllImportStepsFromProfile(
            "profile-collective.js.fancytree:all"
        )
        setattr(self.request, REQUEST_CACHE_KEY, None)
        scripts = ScriptsView(self.layer["portal"], self.layer["request"], None)
        scripts.update()
        results = scripts.render()
        self.assertIn(
            "++resource++collective.js.fancytree/jquery.fancytree-all.min.js", results
        )

    def test_install_theme_lion(self):
        self.assertNotIn("fancytree-theme", self.bundles)
        self.setup_tool.runAllImportStepsFromProfile(
            "profile-collective.js.fancytree:theme-lion"
        )
        styles = StylesView(self.layer["portal"], self.layer["request"], None)
        styles.update()
        results = styles.render()
        self.assertIn(
            "++resource++collective.js.fancytree.theme-lion/ui.fancytree.min.css",
            results,
        )
        self.assertNotIn(
            "++resource++collective.js.fancytree.theme-vista/ui.fancytree.min.css",
            results,
        )

    def test_install_theme_vista(self):
        self.assertNotIn("fancytree-theme", self.bundles)
        self.setup_tool.runAllImportStepsFromProfile(
            "profile-collective.js.fancytree:theme-vista"
        )
        styles = StylesView(self.layer["portal"], self.layer["request"], None)
        styles.update()
        results = styles.render()
        self.assertIn(
            "++resource++collective.js.fancytree.theme-vista/ui.fancytree.min.css",
            results,
        )
        self.assertNotIn(
            "++resource++collective.js.fancytree.theme-lion/ui.fancytree.min.css",
            results,
        )

    def test_uninstall(self):
        self.installer.uninstall_product("collective.js.fancytree")
        self.assertFalse(self.installer.is_product_installed("collective.js.fancytree"))
        self.assertNotIn("fancytree", self.bundles)
        self.assertNotIn("fancytree-theme", self.bundles)
        scripts = ScriptsView(self.layer["portal"], self.layer["request"], None)
        scripts.update()
        results = scripts.render()
        self.assertNotIn(
            "++resource++collective.js.fancytree/jquery.fancytree.min.js", results
        )
        self.assertNotIn(
            "++resource++collective.js.fancytree/jquery.fancytree-all.min.js", results
        )
        self.assertNotIn(
            "++resource++collective.js.fancytree.theme-vista/ui.fancytree.min.css",
            results,
        )
        self.assertNotIn(
            "++resource++collective.js.fancytree.theme-lion/ui.fancytree.min.css",
            results,
        )
