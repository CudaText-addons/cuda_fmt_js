import os

def format_eslint(text):

    import cudatext as app
    import subprocess
    from cuda_fmt import fmtconfig # we require original filename

    fn = fmtconfig.ed_filename
    if not fn: return
    fn = os.path.join(os.path.dirname(fn), '_cud_eslint.js')
    #print('eslint fn:', fn)
    with open(fn, 'w', encoding='utf-8') as f:
        f.write(text)

    try:
        subprocess.call(['eslint', '--fix', fn], shell=False)
    except:
        app.msg_box('CudaFormatter: cannot find program "eslint" in system PATH', 
            app.MB_OK+app.MB_ICONERROR)
        return

    with open(fn, 'r', encoding='utf-8') as f:
        text = f.read()
    os.remove(fn)
    return text
