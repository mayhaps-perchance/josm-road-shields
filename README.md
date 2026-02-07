# Road shields

Renders up to 6 road shields parallel to the respective way(s).

<img width="33%" alt="Example render." src="https://github.com/user-attachments/assets/36834d74-8fb8-4778-b012-0d3104c45ce5" />

## Usage

Install and enable as you would any other MapCSS style.

Shields are rendered parallel to ways belonging to road route relations[^1] with a valid image link stored in the <samp><code>symbol</code></samp> tag.
Shield modifiers are rendered above the respective shield using a valid image stored in the non-standard <samp><code>`symbol:modifier`</code></samp> tag.
If the road route relation has no `symbol` tag, then the sign

![](https://commons.wikimedia.org/w/index.php?title=Special:Redirect/file/MUTCD_W18-1.svg)

is displayed. If the `symbol` tag neither does not exist nor contain an invalid link, then a small white square will be displayed.

[^1]: Relations with the tags <samp><code>type=route</code></samp> and <samp><code>route=road</code></samp>.

The style works for all zoom levels, though your results will depend significantly on your chosen settings.

### Settings

There are four MapCSS settings for this style:

- <samp>DPI scale factor</samp>: the scale factor for upscaling or downscaling the shield to an ideal size for you monitor;
- <samp>Minimum icon size</samp>: the smallest on-screen shield size;
- <samp>Maximum icon size</samp>: the largest on-screen shield size; and
- <samp>Way badge frequency</samp>: the number of ways to skip before re-drawing shields.

You should set the scaling factor to match the scaling factor of your display. On Windows, this is the percent scale in the <samp>Display</samp> settings.

You should set the minimum icon size no lower than 16 pixels, post-scaling.
For comfortable viewing, adjust the maximum icon size with respect to the highest zoom level you will work in and adjust the minimum icon size with respect to the lowest zoom level you will work in.

Internally, I’ve setup rendering so that a given shield appears along the way no more than once.
However, if you need to further reduce visual clutter, you can increase the frequency control.

### Quirks

There are some things that I cannot currently fix:

1. Shields are ordered randomly, without respect to their intuitive priority (e.g., in the US: Interstates > US Routes > State Routes > …).
2. On long, curved ways, shields will render strangely.
3. Shields cannot be consistently rotated to match the vertical.
4. Shield sizes are inherently limited by way lengths in the screen space: at low zoom levels ($\ge1\ \text{km}$), it is virtually impossible to meaningfully render a shield.

Otherwise, I think it’s neat `(^_^)`.

## Possible additions

- option to switch between perpendicular or parallel rendering;
- warnings for ways with road references but no associated road relation;[^2]
- warnings for suspicious image links; and
- fixing all those quirks.

[^2]: These are almost entirely collector-distributor roads or whatever doesn’t appear as-is on Wikipedia.
