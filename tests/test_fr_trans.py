import pytest
import argparse
import i18nparse


def test_help(mocker):
    """Controls that the text for HelpAction is translated"""
    i18nparse.activate('fr_FR')
    mocker.patch('argparse.ArgumentParser.exit')
    mocker.patch('argparse.ArgumentParser._print_message')
    parser = argparse.ArgumentParser('ProgName')
    parser.parse_args(['--help'])
    assert parser.exit.call_count == 1
    assert 'affiche ce message' in parser._print_message.call_args[0][0]


def test_version(mocker):
    """Controls that the help text for VersionAction is translated"""
    i18nparse.activate('fr_FR')
    mocker.patch('argparse.ArgumentParser.exit')
    mocker.patch('argparse.ArgumentParser._print_message')
    parser = argparse.ArgumentParser('ProgName')
    parser.add_argument('--version', action='version', version='1.2.3')
    parser.parse_args(['--help'])
    assert parser.exit.call_count == 1
    assert 'affiche la version' in parser._print_message.call_args[0][0]
