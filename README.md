# Pokédex Data

Pokémon data (up to Gen 7) and assets ready for inserting into a ROM hack. This repository is meant to provide the supporting data for automated Pokédex expansion tools.

  - Cries
  - Sprites
  - Icons

## Data

The data is stored in subdirectories, one for each Pokémon forme, residing under `data/`. The directories are named for the Pokémon's Showdown ID. This ID consists of the Pokémon's name and the forme name concatenated with all non-alphanumeric characters (as well as '?' and '!') removed. Some formes that do not appear in the Showdown data are assigned an ID using the same rules, like `sawsbuckwinter`.

The subdirectory contains the data for that forme. If a file is missing, then it is inherited from the parent forme instead of being duplicated.

### Party Icons

Saved as `icon.png`. This is a 32x64 indexed (4bpp) PNG image that contains both frames for the party icon. The palette must be one of the 3 available icon palettes.

### Cries

Saved as `cry.aif`. This is a AIFF file containing signed 8-bit mono PCM data sampled at 10512 Hz.

### Sprites

Saved as `sprite.png`. This is a 64x256 or 128x256 RGBA PNG image that contains the front and backsprites for the Pokémon. It contains the front sprite, shiny front sprite, back sprite and shiny back sprite in that order, overlayed on a transparent background.

If the image is 128x256, the lower strip contains the female variation sprites. This strip does not contain the shiny images.

## Credits

  - **The DS-style 64x64 sprite teams**: For the updated Pokémon sprites and icons.
  - **Pokémon Showdown! Project**: For the original Pokémon cry audio files and data.
  - **Spherical Ice**: For allowing me to rip the indexed Pokémon icons from Pokémon Gaia.
