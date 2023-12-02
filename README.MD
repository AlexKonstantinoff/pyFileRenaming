# Files renaming by sequence in current directory
---

## Usage
---
```bash
renamedir [-h] -A {rename,undo} [-D [DELIMITER]] [-B [BEGINVAL]] [-P [PREFIX]] [-O [{name,modified}]]
```

***options***:  
  `-h, --help`            show help message and exit  
  `--action {rename,undo}, -A {rename,undo}` - Rename all files in current directory OR undo previous sequence renaming  
  `--delimiter [DELIMITER], -D [DELIMITER]` - Delimiter for renamed files prefix and sequence values  
  `--beginVal [BEGINVAL], -B [BEGINVAL]` - Begin value for rename sequence  
  `--prefix [PREFIX], -P [PREFIX]` - Prefix for renamed files. Will be placed before each sequence value  
  `-O [{name,modified}], --order [{name,modified}]`- Specify file order for renaming sequence  


`renamedir` is recommended alias to a program name.  
If you wouldn't use it, you may just call it by standard way:  
    `python {path to your working directory}/pyFileRenaming`.

You cannot use symbols `/` or `\` as a delimiters.

## Examples
---
```bash
renamedir -A rename -D _ -B 1 -P prefix -O modified

renamedir -A undo -D _ -P prefix
```
