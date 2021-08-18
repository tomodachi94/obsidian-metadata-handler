# Obsidian Metadata Handler

:warning: **This script is in early alpha! Backup and version control your Obsidian files before attempting to run this script.** :warning:

> A small Python script to update system metadata and then put it into the YAML frontmatter.

**Note: This is unoffical and is not associated with the developers of Obsidian.**

So far, this script is able to fill in the created and modified dates. Filenames are coming soon.

## Use cases

- You want to move some files around, but are scared of losing the metadata?
- You want to make sure your grandchildren can read the metadata?
- You want to use the metadata in a Dataview script?

This is for you!

## Running from source

**It's recommended to do modified date first, as the modified date *will* be overrided when updating the YAML frontmatter.**

This assumes you have Python and `pip` installed as a prerequisite.

### Modified dates

```bash
pip install -r requirements.txt
python obsidain-metadata-handler/modified.py -p "full_path_to_your_vault"
```

### Creation dates

```bash
pip install -r requirements.txt
python obsidain-metadata-handler/created.py -p "full_path_to_your_vault"
```

## Native builds

These are being worked on, stay tuned!

## See also

- [Forum post](https://forum.obsidian.md/t/yaml-metadata-prefixer-a-python-script/22738)
