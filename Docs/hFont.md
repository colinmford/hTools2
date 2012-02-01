hFont
=====

...

Attributes
----------

### project

The parent `hProject` object to which the `hFont` belongs.

### ufo

The UFO file containing the actual font.

For more information about the UFO format, see [unifiedfontobject.org](http://unifiedfontobject.org/).

### file_name

The name of the UFO file, for example `Publica.ufo`. 

### style_name

The style name of the font, imported from the name of the ufo file on initialization.

See the documentation of the method `init_from_filename()` (below).

### libs

A dictionary containing all data libs in project.

Each lib is a dictionary, imported from a .plist file when the `hProject` is initiated.

Methods
-------

### init_from_filename()

Initiates the `hFont` object from a ufo file in `hFont.ufo`.

Parses the .ufo font file name to get the parent `hProject` objects, and saves it at `hFont.project`.

It also sets the attributes `file_name` and `style_name` from the file name. 

For this system to work, the .ufo font files should be named using a specific pattern:

	'%s_%s.ufo' % (family_name, style_name)

For example:

	Publica_55.ufo

### get_glyphs()

Get the selected glyphs in the currently open ufo font.

If a glyph window is open, a `CurrentGlyph()` is returned.

If no glyph window is open, a list with the names of the selected glyphs in the font window is returned.

### auto_unicodes()

Automatically sets unicodes for the glyphs in `hFont.ufo`.

### order_glyphs()

Automatically sets the order of the glyphs in the font, based on the list in `hFont.project.libs['groups']['order']`.

### paint_groups()

Paint and order glyphs according to their group.

Uses glyph groups and order from the project, in `hFont.project/libs.group['groups']['glyphs']` (a dict with group and glyph names) and `hFont.project.libs['groups']['order']` (a list of groups names).

### print_info()

Print different kinds of font information.

### import_groups_from_encoding()

Import glyph names and order from the project’s encoding file.

### full_name()

The full name of the font, made of the project’s name (family name) in `hFont.project.name` and the style name in `hFont.style_name`.

### otf_path()

### woff_path()

### generate_otf()

### generate_woff()

### upload_woff()