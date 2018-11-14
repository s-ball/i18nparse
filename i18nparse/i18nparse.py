import gettext
import argparse
import locale
import os.path

_orig = { "_": argparse._, "ngettext": argparse.ngettext }

locpath = os.path.dirname(__file__)
def activate(lang=None):
    if lang is None:
        lang = locale.getdefaultlocale()[0]
    tr = gettext.translation("argparse", os.path.join(locpath, "locale"),
                             [lang])
    argparse._ = tr.gettext
    argparse.ngettext = tr.ngettext

def deactivate():
    argparse._ = _orig["_"]
    argparse.ngettext = _orig["ngettext"]

