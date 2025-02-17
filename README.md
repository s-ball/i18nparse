# i18nparse
Localization of the Python argparse module

## Goals
The argparse module makes it easy to write user-friendly command-line interfaces.
Specifically, it automatically generates help and usage messages and issues errors
when users give the program invalid arguments. Unfortunately, even if the module
is able to use `gettext` type localization strings, none is provided by the standard library.

This module provides some translations and is  simply installable through `pip`

## Current status
Starting with the 1.0.0 release this package is announced as Production grade.
The translations are provided by the [Translation Project](https://translationproject.org/),
except for the French one which is still provided by the developer.

The binary wheel file contains little endian mo translation files. Users of big endian systems should use the source distribution to generate the mo files on their own system.

The list of the translations and the Python versions for which they are in sync is available
in the [TRANSLATIONS.md](https://github.com/s-ball/i18nparse/blob/master/TRANSLATIONS.md) file.

Nevertheless, even
if the translation is too old or too recent, the worst
effect will be some texts still appearing in English
language.

### Known bugs and limitations

When you pass the option `-h` to a program using `i18nparse` the text for
the *version* option will appear in English for all Python releases before 3.11.9,
3.12.3 or 3.13.0 . For example for a French locale you would get:

```
usage : ProgName [-h] [--version]

options:
-h, --help  affiche ce message et termine le programme
--version   show program's version number and exit
```

The problem in not in `i18nparse`. The string
`"show program's version number and exit"` is simply not marked for
translation is the module `argparse.py` before those Python versions.

## Installing

### End user installation

With pip: `pip install i18nparse`.

### Developer installation

If you want to contribute, you should get a copy of the full tree from [GitHub](https://github.com/s-ball/i18nparse):

```
git clone https://github.com/s-ball/i18nparse.git [your_working_copy_folder]
```

#### Building
The `i18nparse` project now uses [hatch](https://hatch.pypa.io/) as its build system.

## Usage

The `i18nparse` module defines 2 functions:

```
def activate(lang = None)
```

which activates the usage of the translation for the required language.
By default, the language for `locale.getlocale()` is used.
Note: In order to use the expected locale, it should be loaded prior to
the call to `activate` with `locale.setlocale(locale.LC_ALL, locale_name)`
where `locale_name` is the name of a known locale or `''` (empty string) for
the default locale.

```
def deactivate()
```

which reverts to the original texts.

Example:

```
import argparse
import i18nparse
import locale

locale.setlocale(locale.LC_ALL, '') # sets a locale
i18nparse.activate()     # Ok use current locale (if translation file exists)

parser = argparse.ArgumentParser('foo')
parser.print_help()      # displays the help message for the current locale
```

Assuming a `fr_FR` locale, this displays:

```
usage : foo [-h]

options:
  -h, --help  affiche ce message et termine le programme
```

## Contributing

Contribution for new language translations or improvement of existing ones should
be addressed to the [Translation Project](https://translationproject.org/).
Only remarks on the project itself should lead to issues on GitHub. See [CONTRIBUTING](https://raw.githubusercontent.com/s-ball/i18nparse/master/CONTRIBUTING) for details

## Versioning

This project uses a standard Major.Minor.Patch versioning pattern.
Inside a major version, public API stability is expected. Inside
a minor version, the matrix of compatibility with Python versions 
should remain unchanged.

## License

This project is licensed under the MIT License - see the [LICENSE](https://raw.githubusercontent.com/s-ball/i18nparse/master/i18nparse/LICENSE) file for details
