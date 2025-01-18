# i18nparse
Localization of the Python argparse module

## Current status
Only the French language translation was initially provided. Thanks to [anselmobd](https://github.com/anselmobd) and [blackstream-x](https://github.com/blackstream-x),
the project now contains Portuguese and German language translations.

Translations for German, Spanish and Slovene are also provided.

The binary wheel file contains little endian mo translation files. Users of big endian systems should use the source distribution to generate the mo files on their own system.

The list of the translations and the date of their last update is available
in the [TRANSLATIONS.md](https://github.com/s-ball/i18nparse/blob/master/TRANSLATIONS.md) file.

*That last update is a hint for the Python versions where the `argparse.py` is acutely translated*. Some
identifiers may be missing for older or more recent versions. Nevertheless, even
if the translation is too old or too recent, the worst
effect will be some texts still appearing in English
language.

## Goals
The argparse module makes it easy to write user-friendly command-line interfaces. Specifically, it automatically generates help and usage messages and issues errors when users give the program invalid arguments. Unfortunately, even if the module is able to use `gettext` type localization strings, none is provided by the standard library.

This module provides some translations (at least a French one) and will be simply installable through `pip`

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

arguments optionnels:
  -h, --help  affiche ce message et termine le programme
```

## Contributing

Contribution for new language translations or improvement of existing ones are welcome. See [CONTRIBUTING](https://raw.githubusercontent.com/s-ball/i18nparse/master/CONTRIBUTING) for details

## Versioning

This project uses a standard Major.Minor.Patch versioning pattern. Inside a major version, public API stability is expected (at least after 1.0.0 version will be published).

## License

This project is licensed under the MIT License - see the [LICENSE](https://raw.githubusercontent.com/s-ball/i18nparse/master/i18nparse/LICENSE) file for details
