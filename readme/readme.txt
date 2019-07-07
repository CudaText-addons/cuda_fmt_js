Formatters for JavaScript and JSON.

- "Format JS": Format code for lexers JavaScript and JSON, using Python engine from jsbeautifier.org.
- "Minify JS": Minifier for JS code. Always formats entire file.
- "JSON Stringify": It's taken from https://github.com/Nadock/json_stringify

"Format JS" has configuration file. Use CudaFormatter commands to edit it.
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
