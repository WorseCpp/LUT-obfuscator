from util import *
name_dict = []

def compile_c_code(code, v = True):

    open("code.c","w+").write(code)
    compile_command = ["gcc", "-O3", "-c", "code.c"]
    result = subprocess.run(compile_command, capture_output=True, text=True)
    if result.returncode != 0:
        if (v):
            print(f"Compilation failed: {result.stderr}")
        return False
    else:
        if v:
            print(f"Compilation succeeded: {result.stdout}")
        return True

def compile_and_test(code):
    if not compile_c_code(code, False):
        return False
    
    fname = "out"

    compile_command = ["gcc", "-O3", "-o", fname, "main.o", "code.o"]

    try:
        res = subprocess.run(compile_command, capture_output=True, text=True, timeout=1.0)
    except subprocess.TimeoutExpired:
        return False
    
    if res.returncode != 0:
        return False
    
    test_cmd = ["./"+fname]
    
    try:
        res = subprocess.run(test_cmd, capture_output=True, text=True, timeout=1.0)
        return bool(res.returncode)
    except subprocess.TimeoutExpired:
        return False



def rand_name():
    choice = random.choice(name_dict)
    name_dict.remove(choice)
    return choice

def init_rand_names():
    global name_dict
    name_dict = open("../words_alpha.txt", 'r').read().split("\n")
    name_dict = [i for i in name_dict if len(i) > 2]

img_ctr = 0

def get_img_name():
    global img_ctr
    img_ctr += 1
    return f"c_cfg_{img_ctr}"

def render_cfg(cfg):
    # Render and view the CFG as a PNG image.
    cfg.dot.render(get_img_name(), format="png", view=True)


def show_cfg(ast):
        
    cfg = CFG()
    
    # Process each function definition in the AST.
    for ext in ast.ext:
        if isinstance(ext, c_ast.FuncDef):
            build_cfg_from_func(ext, cfg)
    
    # Render and view the CFG as a PNG image.
    cfg.dot.render(get_img_name(), format="png", view=True)