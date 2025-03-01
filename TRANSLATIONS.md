# Current translations


| Language | Minimal Python version | Maximal Python version           |
|----------|------------------------|----------------------------------|
| fr       | 3.10                   | 3.10.16, 3.11.11, 3.12.9, 3.13.3 |
| de       | 3.10                   | 3.10.16, 3.11.11, 3.12.9, 3.13.3 |
| eo       | 3.10                   | 3.10.16, 3.11.11, 3.12.9, 3.13.3 |
| es       | 3.10                   | 3.10.16, 3.11.11, 3.12.9, 3.13.3 |
| nl       | 3.10                   | 3.10.16, 3.11.11, 3.12.9, 3.13.3 |
| pt_BR    | 3.10                   | 3.10.16, 3.11.11, 3.12.9, 3.13.3 |
| ro       | 3.10                   | 3.10.16, 3.11.11, 3.12.9, 3.13.3 |
| sl       | 3.10                   | 3.10.16, 3.11.11, 3.12.9, 3.13.3 |
| sv       | 3.10                   | 3.10.16, 3.11.11, 3.12.9, 3.13.3 |
| uk       | 3.10                   | 3.10.16, 3.11.11, 3.12.9, 3.13.3 |

But **beware**:
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


