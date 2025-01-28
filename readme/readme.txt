Formatters for JavaScript and JSON.

- "JS Beautify"
Format code for lexers JavaScript and JSON, using Python engine from jsbeautifier.org.

- "JS Minify"
Minifier for JS code.
Always formats entire file.

- "JS Sort Imports"
This is port of plugin for Sublime Text: https://github.com/insin/sublime-sort-javascript-imports
Always formats entire file.
It sorts selected lines containing JavaScript import statements or require() calls by the module path they're importing.
Lines will be sorted based on the module path being imported, respecting (and normalising) any blank lines used to divide imports into different categories.
Any non-import lines in the selection will be moved to the end, separated by a new blank line if necessary.

Import ordering:
Where top-level imports and path-based imports are mixed in the same block, they will be ordered as follows:
    Top-level imports
    Imports which traverse up out of the current directory, from furthest away to closest
    Imports within the current directory

Note: if you're using Webpack aliases or a Babel alises plugin for top-level importing of your app's own code, you might want to put those in a separate block for clarity.
    
- "JSON Stringify"
It's taken from https://github.com/Nadock/json_stringify

- "JS fix via ESLint"
It runs ESLint tool with '--fix' parameter.
See this intro to ESLint:
https://masteringjs.io/tutorials/eslint/fix
You need the program (ie Node.js package) ESLint, so that "eslint" can be run from the command line. Only local installation of Node ESLint package is not enough.


------------------
"JS Format" has configuration file. Use CudaFormatter commands to edit it.
Options [default]

- "indent_size"                Indentation size [4]
- "indent_char"                Indentation character [" "]
- "indent_with_tabs"           Indent with tabs
- "preserve_newlines"          Preserve line-breaks
- "max_preserve_newlines"      Number of line-breaks to be preserved in one chunk [10]
- "space_in_paren"             Add padding spaces within paren, ie. f( a, b )
- "e4x"                        Pass E4X XML literals through untouched
- "jslint_happy"               Enable jslint-stricter mode
- "brace_style"                Possible values: "collapse", "expand", "end-expand" ["collapse"]
- "keep_array_indentation"     Preserve array indentation
- "keep_function_indentation"  Preserve function indentation
- "unescape_strings"           Decode printable characters encoded in xNN notation
- "wrap_line_length"           Wrap lines at next opportunity after N characters [0]
- "break_chained_methods"      Break chained method calls across subsequent lines


Author: Alexey Torgashin (CudaText)
License: MIT
