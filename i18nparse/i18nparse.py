""" This module allows to activate a translation for the module argparse
"""
import gettext
import argparse
import locale
import os.path

# noinspection PyUnresolvedReferences,PyProtectedMember
_orig = { "_": argparse._, "ngettext": argparse.ngettext }

locpath = os.path.dirname(__file__)
def activate(lang=None):
    """Activate a translation for lang.

If lang is None, then the language of locale.getdefaultlocale() is used.
If the translation file does not exist, the original messages will be used.
"""
    if lang is None:
        lang = locale.getlocale()[0]
    if lang is not None:
        tr = gettext.translation("i18nparse", os.path.join(locpath, "locale"),
                                 [lang], fallback=True)
        argparse._ = tr.gettext
        argparse.ngettext = tr.ngettext

def deactivate():
    """Revert to original messages"""
    argparse._ = _orig["_"]
    argparse.ngettext = _orig["ngettext"]

