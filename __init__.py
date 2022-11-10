import sys
import os
import json
from .json_stringify import *
from .sort_js_imports import sort_js_imports
from cuda_fmt import get_config_filename

sys.path.append(os.path.dirname(__file__))
import jsbeautifier
import slimit

def options():

    op = jsbeautifier.default_options()
    fn = get_config_filename('JS Beautify')
    if not os.path.isfile(fn):
        return op

    with open(fn) as f:
        d = json.load(f)    
        op.indent_size               = d.get('indent_size', 4)
        op.indent_char               = d.get('indent_char', ' ')
        op.indent_with_tabs          = d.get('indent_with_tabs', False)
        op.preserve_newlines         = d.get('preserve_newlines', True)
        op.max_preserve_newlines     = d.get('max_preserve_newlines', 10)
        op.space_in_paren            = d.get('space_in_paren', False)
        op.e4x                       = d.get('e4x', False)
        op.jslint_happy              = d.get('jslint_happy', False)
        op.brace_style               = d.get('brace_style', 'collapse')
        op.keep_array_indentation    = d.get('keep_array_indentation', False)
        op.keep_function_indentation = d.get('keep_function_indentation', False)
        op.eval_code                 = d.get('eval_code', False)
        op.unescape_strings          = d.get('unescape_strings', False)
        op.wrap_line_length          = d.get('wrap_line_length', 0)
        op.break_chained_methods     = d.get('break_chained_methods', False)
    return op

def do_format(text):

    return jsbeautifier.beautify(text, options())

def do_minify(text):

    return slimit.minify(text, mangle=True, mangle_toplevel=True)

def do_stringify(text):

    return invert_json_string(text)

def do_sort_imports(text):

    lines = text.splitlines()
    lines = sort_js_imports(lines)
    return '\n'.join(lines)

def do_minify_json(text):

    obj = json.loads(text, encoding='utf-8')
    text = json.dumps(obj, separators=(',', ':'))
    return text
