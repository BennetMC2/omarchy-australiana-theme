# Australiana

A warm, nostalgic Australian theme for Omarchy: bush-green surfaces, soft gold text, wattle-gold accents, eucalyptus greens and outback rust.

![Australiana bush evening wallpaper](preview.png)

## Install

```sh
git clone https://github.com/BennetMC2/omarchy-australiana-theme ~/.config/omarchy/themes/australiana
bash ~/.config/omarchy/themes/australiana/install.sh
```

Installation applies the theme. Designed for Omarchy 4 / Quattro's semantic colour templates; locally checked on Omarchy 4.0.4-1.

To select it later or choose a wallpaper:

```sh
omarchy theme set australiana
omarchy theme bg-switcher
```

## Wallpapers

Four backgrounds are included:

| Bush evening | Summer cricket |
| --- | --- |
| ![Bush evening](backgrounds/01-bush-evening.png) | ![Summer cricket](backgrounds/02-summer-cricket.png) |
| Coastal road | Main street |
| ![Coastal road](backgrounds/03-coastal-road.png) | ![Main street](backgrounds/04-main-street.png) |

## Palette

| Role | Colour |
| --- | --- |
| Background | `#102C23` |
| Deep forest | `#0B2119` |
| Soft gold text | `#E8C778` |
| Wattle gold accent | `#E7AD35` |
| Eucalyptus | `#A3B980` |
| Coastal blue | `#89B4C1` |
| Warm rust | `#E58A68` |

Omarchy generates the terminal, editor, shell and other supported application configurations from `colors.toml`. Folder icons use `Yaru-yellow`.

## Kangaroo About logo

The installer registers a theme-change hook. Selecting Australiana displays a gold kangaroo in terminal dot art; switching to another theme restores the previous About logo. Your Fastfetch configuration is preserved. Python 3 is required for the hook.

If you already installed the palette with `omarchy theme install`, run the `install.sh` command above once to enable the kangaroo integration. Ordinary theme installation does not execute repository scripts automatically.

Preview with `omarchy launch about`. The source silhouette and dot art are included in `branding/`.

To disable the integration, switch to another theme first, then remove only `~/.config/omarchy/hooks/theme-set.d/australiana-about`.

## Artwork

The bush-evening wallpaper and kangaroo silhouette were generated with OpenAI's image generation tool. The three nostalgic photographic-style wallpapers were supplied for this theme. The preview is the bush-evening wallpaper, not a desktop screenshot. Prompts are retained in `wallpaper-prompt.txt` and `branding/kangaroo-prompt.txt`; the wallpaper prompt uses the theme's final name.

No separate licence for the artwork is declared in this repository.
