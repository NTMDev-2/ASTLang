module_return_code = 0
try:
    import io, sys, time, traceback, inspect, math, threading, queue
    from tkinter import messagebox
    import tkinter as tk
    from random import randint
    module_return_code += 1
except ModuleNotFoundError:
    print('System exception ; ModuleNotFoundError ; Do you have Python installed correctly?')
    print("Module Error Return Code: [{}] - INTERRUPTED".format(module_return_code))
    exit()
verno = 'ASTLang 39, Release 2 [PRE-RELEASE]'
pcks = 'traceback, random, ast, re, pickle, tkinter, sys, io, time, builtins, inspect, math, threading, queue'
class Stack():
    def IsStack(self):
        return __name__ == '__main__'
context: dict[str, object] = dict() # Initialize main register
info = f"""
DEFAULT MESSAGE FROM IDE:
'NTMDev ...'
Note from NTMDev: ASTLang 35 is now unsupported
----------------------------------------------------------------------------------------------------------------
ASTLang for PC, Local based (IDE)
Supports IDE usuage and file saving with .astlang

Python 3.12 Build 2025, Version 3.12.0 "NEWEST"

Designed with GitHub Copilot
Created by NTMDev (2025)

Packages used: {pcks}
Subpackages: random.randint, tkinter.messagebox, tkinter.filedialog

Current Version Stored: {verno}

Currently Known Bugs:
- No file updating permissions for file I/O commands.
- Updating dictionaries is currently very buggy
- When sending HTTP requests, you will get a NoneType warning 

COMING SOON: More HTTP requests and potentially web sockets

Added: LoadHTTPDriver, SendHTTPRequest, HTTPQueryParameters (unfinished)
Updated: NewInstance parameter constructor evaluator: fixed "self" evaluation
----------------------------------------------------------------------------------------------------------------
"""

print(info)
print("Module Error Return Code: [{}] - OK".format(module_return_code))
signature_box = None
runnable = True
class IntepreterParent:
    global main
    main = (__name__ == '__main__')
class NodeParent(IntepreterParent):
    pass
class ValueParent(IntepreterParent):
    pass
class FunctionParent(IntepreterParent):
    pass
class TestCode(FunctionParent):
    pass 

class Pass(NodeParent):
    pass

class cheesestick():
    pass

def get_keywords():
    return [cls.__name__ for cls in NodeParent.__subclasses__()]
def get_funcs():
    return [cls.__name__ for cls in FunctionParent.__subclasses__()]
def get_values():
    return [cls.__name__ for cls in ValueParent.__subclasses__()]
def get_systemfuncs():
    return [cls.__name__ for cls in IntepreterParent.__subclasses__()]
def get_by_Id():
    return get_keywords() + get_funcs() + get_values() + get_systemfuncs()
def txteditor_ui(initial=''):
    import re
    content = ''
    global code_text
    autocomplete_box = None

    def submit(event=None):
        nonlocal content
        raw_text = code_text.get("1.0", tk.END).strip()
        try:
            content = eval(raw_text, globals())
        except Exception as e:
            print(f"Error: {e}")
            content = None
        root.destroy()
    def update_line_numbers(event=None):
        try:
            if not code_text.winfo_exists():
                return
            lines = code_text.get("1.0", "end-1c").split("\n")
            line_numbers_text = "\n".join(str(i + 1) for i in range(len(lines)))
            if line_numbers.winfo_exists():
                line_numbers.config(state='normal')
                line_numbers.delete("1.0", tk.END)
                line_numbers.insert("1.0", line_numbers_text)
                line_numbers.config(state='disabled')
                line_numbers.yview_moveto(code_text.yview()[0])
        except tk.TclError:
            pass
    def on_scroll(*args):
        if args[0] in ("moveto", "scroll"):
            code_text.yview(*args)
            line_numbers.yview(*args)
        else:
            code_text.yview("moveto", args[0])
            line_numbers.yview("moveto", args[0])
    def get_all_exceptions(base=Exception):
        result = []
        for cls in base.__subclasses__():
            result.append(cls.__name__)
            result.extend(get_all_exceptions(cls))
        return result
    EXCEPTIONS = get_all_exceptions()
    def highlight(event=None):
        KEYWORDS = get_keywords()
        FUNCS = get_systemfuncs()
        IDEFUNCS = get_funcs()
        VALUES = get_values()
        for tag in ("keyword", "func", "idefunc", "value", "arg",
                    "paren_yellow", "paren_blue", "paren_pink",
                    "error", "integer", "string", "comment", "docstring",
                    "exception", "return_tag", "break_tag", "continue_tag"):
            code_text.tag_remove(tag, "1.0", tk.END)
        code_text.tag_configure("keyword", foreground="orange", font=('Consolas', 12, 'bold'))
        code_text.tag_configure("idefunc", foreground="red", font=('Consolas', 12, 'bold'))
        code_text.tag_configure("func", foreground="#E0B0FF", font=('Consolas', 12, 'italic'))
        code_text.tag_configure("value", foreground="#4EC9B0", font=('Consolas', 12, 'bold'))
        code_text.tag_configure("arg", foreground="#DCDCAA", font=('Consolas', 12, 'italic bold'))
        code_text.tag_configure("paren_yellow", foreground="yellow", font=('Consolas', 12, 'bold'))
        code_text.tag_configure("paren_blue", foreground="blue", font=('Consolas', 12, 'bold'))
        code_text.tag_configure("paren_pink", foreground="green", font=('Consolas', 12, 'bold'))
        code_text.tag_configure("error", underline=True, foreground="red")
        code_text.tag_configure("integer", foreground="#BF77F6", font=('Consolas', 12, 'bold'))
        code_text.tag_configure("string", foreground="#9CDCFE", font=('Consolas', 12))
        code_text.tag_configure("comment", foreground="#0CAA00", font=('Consolas', 12, 'italic'))
        code_text.tag_configure("docstring", foreground="#FFD700", font=('Consolas', 12, 'italic'))

        exception_color = "#FF4500"
        code_text.tag_configure("exception", foreground=exception_color, font=('Consolas', 12, 'bold'))
        code_text.tag_configure("return_tag", foreground=exception_color, font=('Consolas', 12, 'bold'))
        code_text.tag_configure("break_tag", foreground=exception_color, font=('Consolas', 12, 'bold'))
        code_text.tag_configure("continue_tag", foreground=exception_color, font=('Consolas', 12, 'bold'))

        def safe_tag_add(word, tag):
            start_idx = "1.0"
            while True:
                pos = code_text.search(word, start_idx, stopindex=tk.END)
                if not pos:
                    break
                end_pos = f"{pos}+{len(word)}c"
                before = code_text.get(f"{pos}-1c", pos) if pos != "1.0" else ""
                after = code_text.get(end_pos, f"{end_pos}+1c")
                if (before == "" or not before.isalnum()) and (after == "" or not after.isalnum()):
                    code_text.tag_add(tag, pos, end_pos)
                start_idx = end_pos
        for kw in KEYWORDS:
            safe_tag_add(kw, "keyword")
        for func in FUNCS:
            safe_tag_add(func, "func")
        for idefunc in IDEFUNCS:
            safe_tag_add(idefunc, "idefunc")
        for val in VALUES:
            safe_tag_add(val, "value")

        text_content = code_text.get("1.0", "end-1c")
        for match in re.finditer(r'\b(\w+)\s*=', text_content):
            start, end = match.span(1)
            start_idx = f"1.0 + {start}c"
            end_idx = f"1.0 + {end}c"
            code_text.tag_add("arg", start_idx, end_idx)
        for match in re.finditer(r'#.*', text_content):
            start, end = match.span()
            start_idx = f"1.0 + {start}c"
            end_idx = f"1.0 + {end}c"
            code_text.tag_add("comment", start_idx, end_idx)
        for match in re.finditer(r'("""|\'\'\')(.*?)\1', text_content, re.DOTALL):
            start, end = match.span()
            start_idx = f"1.0 + {start}c"
            end_idx = f"1.0 + {end}c"
            code_text.tag_add("docstring", start_idx, end_idx)
        def get_all_exceptions(base=Exception):
            result = []
            for cls in base.__subclasses__():
                if isinstance(cls, type):
                    result.append(cls.__name__)
                    result.extend(get_all_exceptions(cls))
            return result
        for exc in get_all_exceptions():
            safe_tag_add(exc, "exception")
        for keyword in ["return", "break", "continue"]:
            safe_tag_add(keyword, f"{keyword}_tag")
        stack = []
        opening = "([{"
        closing = ")]}"
        color_tags = ["paren_yellow", "paren_blue", "paren_pink"]
        index = "1.0"
        while True:
            char = code_text.get(index)
            if char == "":
                break
            if char in opening:
                stack.append((char, index))
            elif char in closing:
                if stack:
                    open_char, open_idx = stack.pop()
                    depth = len(stack) % 3
                    code_text.tag_add(color_tags[depth], open_idx, f"{open_idx}+1c")
                    code_text.tag_add(color_tags[depth], index, f"{index}+1c")
            index = code_text.index(f"{index}+1c")

        try:
            tree = ast.parse(text_content)
        except SyntaxError as e:
            lineno = e.lineno
            col_offset = e.offset
            if lineno and col_offset:
                start = f"{lineno}.{col_offset-1}"
                end = f"{lineno}.{col_offset}"
            return

        defined = set()
        for node in ast.walk(tree):
            if isinstance(node, ast.FunctionDef):
                defined.add(node.name)
            elif isinstance(node, ast.ClassDef):
                defined.add(node.name)
            elif isinstance(node, ast.Assign):
                for target in node.targets:
                    if isinstance(target, ast.Name):
                        defined.add(target.id)

        for node in ast.walk(tree):
            if isinstance(node, ast.Name):
                if (node.id not in defined
                    and node.id not in KEYWORDS
                    and node.id not in FUNCS
                    and node.id not in IDEFUNCS
                    and node.id not in VALUES
                    and not isinstance(node.ctx, ast.Store)):
                    lineno = node.lineno
                    col_offset = node.col_offset
                    start = f"{lineno}.{col_offset}"
                    end = f"{lineno}.{col_offset + len(node.id)}"
                    code_text.tag_add("error", start, end)

        for match in re.finditer(r'\b\d+(\.\d+)?\b', text_content):
            start, end = match.span()
            start_idx = f"1.0 + {start}c"
            end_idx = f"1.0 + {end}c"
            code_text.tag_add("integer", start_idx, end_idx)
        for match in re.finditer(r'(\".*?\"|\'.*?\')', text_content):
            start, end = match.span()
            start_idx = f"1.0 + {start}c"
            end_idx = f"1.0 + {end}c"
            code_text.tag_add("string", start_idx, end_idx)

    autocomplete_box = None
    listbox = None

    def get_current_word():
        cursor_idx = code_text.index(tk.INSERT)
        start_idx = f"{cursor_idx} - 50c"
        text_before_cursor = code_text.get(start_idx, cursor_idx)
        match = re.search(r'([\w]+)$', text_before_cursor)
        return match.group(1) if match else ''
    def hide_autocomplete():
        nonlocal autocomplete_box, listbox
        if autocomplete_box:
            try:
                if autocomplete_box.winfo_exists():
                    autocomplete_box.destroy()
            except tk.TclError:
                pass
            finally:
                autocomplete_box = None
                listbox = None
        
        try:
            code_text.bind("<Down>", lambda e: "break")
            code_text.bind("<Up>", lambda e: "break")
        except:
            pass

    def hide_signature():
        global signature_box
        if signature_box:
            try:
                if signature_box.winfo_exists():
                    signature_box.destroy()
            except tk.TclError:
                pass
            finally:
                signature_box = None  
    def get_signature(name):
        try:
            obj = eval(name, globals())
            sig = inspect.signature(obj)
            
            params = []
            for param_name, param in sig.parameters.items():
                if param.default == inspect.Parameter.empty:
                    params.append(param_name)
                else:
                    if hasattr(param.default, '__class__') and hasattr(param.default.__class__, '__name__'):
                        if param.default.__class__.__name__ == 'ObjNONE':
                            default_name = "[None]"
                        else:
                            default_name = repr(param.default)
                    else:
                        default_name = repr(param.default)
                    params.append(f"{param_name}={default_name}")
            
            result = f"{name}({', '.join(params)})"
            return result
        except Exception as e:
            return f"{name}(...)"
    def show_autocomplete(suggestions):
        nonlocal autocomplete_box, listbox
        hide_autocomplete()
        if not suggestions:
            return
        bbox = code_text.bbox(tk.INSERT)
        if not bbox:
            return
        x, y, width, height = bbox

        autocomplete_box = tk.Toplevel(root)
        autocomplete_box.wm_overrideredirect(True)
        autocomplete_box.attributes("-topmost", True)

        listbox = tk.Listbox(
            autocomplete_box,
            height=min(len(suggestions), 6),
            font=('Consolas', 12),
            bg="#363636",
            fg="#00EEFF",
        )
        listbox.pack()

        for s in suggestions:
            listbox.insert(tk.END, s)
        global insert_selection_from_listbox
        def insert_selection_from_listbox(e=None):
            if not listbox or not listbox.curselection(): 
                return
            original = listbox.get(listbox.curselection()).strip()
            current_word = get_current_word()
            cursor_idx = code_text.index(tk.INSERT)
            start_idx = code_text.index(f"{cursor_idx} - {len(current_word)}c")
            code_text.delete(start_idx, cursor_idx)
            code_text.insert(start_idx, original)
            code_text.mark_set("insert", f"{start_idx}+{len(original)}c")
            hide_autocomplete()
            code_text.focus_set()

        listbox.bind("<Double-Button-1>", insert_selection_from_listbox)
        listbox.bind("<Return>", insert_selection_from_listbox)
        listbox.bind("<Tab>", insert_selection_from_listbox)

        def move_selection(delta):
            if not listbox or not listbox.winfo_exists(): 
                return
            if listbox.size() == 0: 
                return
            cur = listbox.curselection()
            if cur:
                idx = (cur[0] + delta) % listbox.size()
            else:
                idx = 0 if delta > 0 else listbox.size() - 1
            listbox.selection_clear(0, tk.END)
            listbox.selection_set(idx)
            listbox.activate(idx)
        code_text.bind("<Down>", lambda e: (move_selection(1), "break"))
        code_text.bind("<Up>", lambda e: (move_selection(-1), "break"))

        x_root = code_text.winfo_rootx() + x
        y_root = code_text.winfo_rooty() + y + height
        autocomplete_box.geometry(f"+{x_root}+{y_root}")

        if listbox.size() > 0:
            listbox.selection_set(0)
            listbox.activate(0)
    def show_signature(sig_text, arg_index=0):
        global signature_box
        hide_signature()
        if not sig_text:
            return
        bbox = code_text.bbox(tk.INSERT)
        if not bbox:
            return
        x, y, w, h = bbox
        x_root = code_text.winfo_rootx() + x
        y_root = code_text.winfo_rooty() + y + h
        parts = sig_text.split("(")
        if len(parts) > 1:
            args = parts[1].rstrip(")")
            arg_list = args.split(",")
            highlighted = []
            for i, a in enumerate(arg_list):
                if i == arg_index:
                    highlighted.append(f"[{a.strip()}]")
                else:
                    highlighted.append(a.strip())
            sig_text = parts[0] + "(" + ", ".join(highlighted) + ")"

        signature_box = tk.Toplevel(root)
        signature_box.wm_overrideredirect(True)
        signature_box.attributes("-topmost", True)

        label = tk.Label(signature_box, text=sig_text, font=("Consolas", 11),
                        background="#333333", foreground="#ffffff", padx=5, pady=2)
        label.pack()
        signature_box.geometry(f"+{x_root}+{y_root+20}")
        def auto_hide():
            try:
                if signature_box and signature_box.winfo_exists():
                    signature_box.after(5000, hide_signature) 
            except tk.TclError:
                pass
        def on_click(event=None):
            hide_signature()
        
        code_text.bind("<Button-1>", on_click, add="+")
        root.bind("<Button-1>", on_click, add="+")

    def handle_autocomplete(event=None):
        word = get_current_word()
        if len(word) < 1:
            hide_autocomplete()
            return
        ALL_CANDIDATES = get_keywords() + get_systemfuncs() + get_funcs() + get_values() + EXCEPTIONS
        matches = [w for w in ALL_CANDIDATES if w.startswith(word) and w != word]
        show_autocomplete(matches) if matches else hide_autocomplete()

    def handle_signature(event=None):
        if not code_text.winfo_exists():
            return
        text_before = code_text.get("1.0", tk.INSERT)
        if not text_before:
            hide_signature()
            return

        # Look for normal calls first
        depth = 0
        for i in range(len(text_before) - 1, -1, -1):
            c = text_before[i]
            if c == ')':
                depth += 1
            elif c == '(':
                if depth == 0:
                    j = i - 1
                    while j >= 0 and (text_before[j].isalnum() or text_before[j] == '_'):
                        j -= 1
                    fname = text_before[j+1:i]
                    if fname != "Module" and fname:
                        args_so_far = text_before[i+1:]
                        arg_index = args_so_far.count(',')
                        sig_text = get_signature(fname)
                        if sig_text:
                            show_signature(sig_text, arg_index)
                            return
                else:
                    depth -= 1

        m = re.search(r'FuncCall\s*\(\s*Function\s*=\s*([\w_]+)', text_before)
        if m:
            fname = m.group(1)
            after = text_before[m.end():]
            arg_index = after.count(',')
            sig_text = get_signature(fname)
            if sig_text:
                show_signature(sig_text, arg_index)
                return

        hide_signature()

    root = tk.Tk()
    root.title('ASTLang IDE')
    root.geometry('800x700')

    button_frame = tk.Frame(root)
    button_frame.pack(side='bottom', fill='x', padx=5, pady=5)
    tk.Button(button_frame, text="RUN ASTLANG PROGRAM (CTRL+ENTER)", command=submit, background="#000000", foreground="white",
                font=('Consolas', 12, 'bold')).pack(side='left', fill='x', expand=True, padx=5)

    editor_frame = tk.Frame(root)
    editor_frame.pack(expand=True, fill='both')
    scrollbar = tk.Scrollbar(editor_frame)
    scrollbar.pack(side='right', fill='y')
    line_numbers = tk.Text(
    editor_frame, width=4, padx=3, takefocus=0, border=0,
            background='lightgray', state='disabled', font=('Consolas', 12, 'bold'),
            yscrollcommand=on_scroll
        )
    line_numbers.pack(side='left', fill='y')

    code_text = tk.Text(editor_frame, font=('Consolas', 12),
                            yscrollcommand=on_scroll, background="#1E1E1E", foreground="#D4D4D4",
                            insertbackground="white", wrap='none')
    code_text.config(
            insertwidth=float(2.5), 
            insertofftime=300, 
            insertontime=600, 
            insertbackground="#FFFFFF", 
            insertborderwidth=1
        )
    code_text.pack(expand=True, fill='both')
    code_text.insert(tk.END, initial)
    scrollbar.config(command=on_scroll)
    def safe_update_ui():
        try:
            if code_text.winfo_exists():
                update_line_numbers()
                highlight()
                if code_text.focus_get() == code_text:
                    handle_autocomplete()
                    handle_signature()
                else:
                    hide_autocomplete()
                    hide_signature()
        except tk.TclError:
            pass
        except Exception as e:
            print(f"UI update error: {e}")
    for ev in ("<KeyRelease>", "<Return>", "<BackSpace>", ",", "(", ")"):
        code_text.bind(ev, lambda e: safe_update_ui())
    def insert_two_spaces(event):
        code_text.insert(tk.INSERT, "  ")
        return "break"
    def handle_tab(event=None):
        nonlocal autocomplete_box, listbox
        if autocomplete_box and listbox and listbox.curselection():
            return insert_selection_from_listbox(event) 
        else:
            return insert_two_spaces(event) 
    import pickle
    import ast

    def node_to_dict(node):
        if isinstance(node, ast.Call):
            func_name = getattr(node.func, "id", None) or getattr(node.func, "attr", None)
            kwargs = {}
            for kw in node.keywords:
                try:
                    kwargs[kw.arg] = ast.literal_eval(kw.value)
                except:
                    kwargs[kw.arg] = ast.unparse(kw.value)
            args = []
            for arg in node.args:
                args.append(node_to_dict(arg))
            d = {"type": func_name}
            if args:
                d["args"] = args
            if kwargs:
                d.update(kwargs)
            return d
        elif isinstance(node, ast.Expr):
            return node_to_dict(node.value)
        elif isinstance(node, ast.Constant):
            return node.value
        elif isinstance(node, ast.Name):
            return node.id
        else:
            try:
                return ast.unparse(node)
            except:
                return str(node)
    def parse_astlang_to_dict(code_text):
        try:
            tree = ast.parse(code_text)
        except:
            messagebox.showerror('ERROR', 'ASTLang code is either missing, moved, renamed or corrupted and cannot be read at this time.')
            return {"type": "Module", "body": ['unknown.unknown.null()']}

        result = {"type": "Module", "body": []}
        for node in tree.body:
            result["body"].append(node_to_dict(node))
        return result
    def save_ast_text(filename, text):
        if not filename.endswith(".astlang"):
            filename += ".astlang"

        ast_dict = parse_astlang_to_dict(text)

        obj = {
            "ast": ast_dict,
            "raw": text 
        }

        with open(filename, "wb") as f:
            pickle.dump(obj, f)
    def load_ast_text(filename):
        with open(filename, "rb") as f:
            return pickle.load(f)

        # Add these focus event handlers after the show_signature function (around line 320):
    
    def on_focus_out(event=None):
        """Hide signature box when IDE loses focus"""
        hide_signature()
        hide_autocomplete()
    def on_focus_in(event=None):
        """Optionally handle focus in events"""
        pass
    root.bind("<FocusOut>", on_focus_out)
    code_text.bind("<FocusOut>", on_focus_out)
    code_text.bind("<FocusIn>", on_focus_in)
    root.bind("<Unmap>", on_focus_out) 
    root.bind("<Map>", on_focus_in) 
    root.bind("<Deactivate>", on_focus_out)
    root.bind("<Activate>", on_focus_in)

    from tkinter import filedialog

    current_file = None 

    def save_file(event=None):
        nonlocal current_file
        text = code_text.get("1.0", "end-1c")

        if current_file:
            save_ast_text(current_file, text)
        else:
            filename = filedialog.asksaveasfilename(
                defaultextension=".ast",
                filetypes=[("ASTLang", "*.astlang")]
            )
            if filename:
                save_ast_text(filename, text)
                current_file = filename
    def dict_to_code(d, indent=0):
        if isinstance(d, dict):
            type_name = d.get("type", "")
            args = d.get("args", [])
            kwargs = {k: v for k, v in d.items() if k not in ("type", "args")}
            
            parts = []
            for arg in args:
                parts.append(dict_to_code(arg, indent+1))
            for k, v in kwargs.items():
                val = dict_to_code(v, indent+1)
                parts.append(f"{k}={val}")

            joined = ",\n" + "\t" * (indent+1)
            return f"{type_name}(\n{'\t'*(indent+1)}{joined.join(parts)}\n{'\t'*indent})"
        
        elif isinstance(d, list):
            return "[" + ", ".join(dict_to_code(x, indent+1) for x in d) + "]"
        else:
            return repr(d)

    def open_file(event=None):
        nonlocal current_file
        filename = filedialog.askopenfilename(
            filetypes=[("ASTLang", "*.astlang")]
        )
        if not filename:
            return 

        loaded_obj = load_ast_text(filename)

        if isinstance(loaded_obj, dict):
            if "raw" in loaded_obj:
                code_as_text = loaded_obj["raw"]
            elif "ast" in loaded_obj: 
                code_as_text = dict_to_code(loaded_obj["ast"])
            else: 
                code_as_text = dict_to_code(loaded_obj)
        else:
            code_as_text = str(loaded_obj)

        code_text.delete("1.0", "end")
        code_text.insert("1.0", code_as_text)
        current_file = filename

    content = ''

    code_text.bind("<Control-o>", lambda e: open_file(e))
    code_text.bind("<Control-s>", lambda e: save_file(e))

    code_text.bind("<Tab>", handle_tab)
    code_text.bind("<Control-Return>", submit)

    update_line_numbers()
    highlight()
    root.mainloop()
    return content
def get_user_input(prompt=""):
    result = {"value": None}
    root2 = tk.Tk()
    root2.withdraw()
    popup = tk.Toplevel(root2)
    popup.title("User Input (STDIN CALL)")
    popup.geometry("500x250")
    popup.grab_set()
    popup.focus_set()
    
    prompt_text = prompt if prompt else "Enter input:"
    prompt_label = tk.Label(popup, text=prompt_text, font=("Consolas", 12, "bold"), 
                           wraplength=450, justify="left")
    prompt_label.pack(pady=(10, 5), padx=10, fill="x")
    
    text_widget = tk.Text(popup, height=5, font=("Consolas", 12),
                         bg="#2d2d2d", fg="#ffffff", insertbackground="#ffffff")
    text_widget.pack(expand=True, fill="both", padx=10, pady=5)
    text_widget.focus_set()
    
    def submit():
        result["value"] = text_widget.get("1.0", "end-1c")
        popup.destroy()
        root2.destroy()
    
    def on_enter(event=None):
        if event and event.state & 0x4:
            submit()
        return "break"
    
    # Button frame
    button_frame = tk.Frame(popup)
    button_frame.pack(side="bottom", fill="x", padx=10, pady=5)
    
    submit_btn = tk.Button(button_frame, text="Submit (Ctrl+Enter)", command=submit, 
                          font=("Consolas", 11, "bold"), bg="#4CAF50", fg="white")
    submit_btn.pack(side="right", padx=5)
    
    def cancel_action():
        result["value"] = "" 
        popup.destroy()
        root2.destroy()

    cancel_btn = tk.Button(button_frame, text="Cancel", command=cancel_action,
                        font=("Consolas", 11), bg="#f44336", fg="white")
    cancel_btn.pack(side="right")
    
    text_widget.bind("<Control-Return>", on_enter)
    popup.bind("<Escape>", lambda e: (setattr(result, 'value', ""), popup.destroy(), root2.destroy()))
    popup.update_idletasks()
    x = (popup.winfo_screenwidth() // 2) - (popup.winfo_width() // 2)
    y = (popup.winfo_screenheight() // 2) - (popup.winfo_height() // 2)
    popup.geometry(f"+{x}+{y}")
    
    popup.wait_window() 
    return result["value"]

class Module(NodeParent):
    def __init__(self, *ModuleCode):
        self.ModuleCode = ModuleCode
class PrimitiveWrapper(IntepreterParent):

    def __init__(self, V):
        self.V = V
    def __str__(self):
        return str(self.V)

class Integer(ValueParent):
    def __init__(self, Int):
        self.Int = Int
class String(FunctionParent):
    def __init__(self, Str):
        self.Str = Str
class Float(ValueParent):
    def __init__(self, Flt):
        self.Flt = Flt
class Boolean(NodeParent):
    def __init__(self, Bool):
        self.Bool = Bool
class ObjNONE(FunctionParent):
    def __init__(self):
        pass
    def __repr__(self):
        return "ObjNONE()"
class Iterable(IntepreterParent):
    def __init__(self, Iter):
        self.Iter = Iter
class CastToValue(NodeParent):
    def __init__(self, Var, CastVal):
        self.Var = Var
        self.CastVal = CastVal
class GetInfo(IntepreterParent):
    pass

class Abs(NodeParent):
    def __init__(self, Val):
        self.Val = Val
class Power(NodeParent):
    def __init__(self, Base, Exp):
        self.Base = Base
        self.Exp = Exp
class RandomInt(IntepreterParent):
    def __init__(self, Min, Max):
        self.Min = Min
        self.Max = Max
class RandomChoice(NodeParent):
    def __init__(self, List):
        self.List = List
class Sum(NodeParent):
    def __init__(self, Var):
        self.Var = Var
class Round(ValueParent):
    def __init__(self, Flt, DecPoints):
        self.Flt = Flt
        self.DecPoints = DecPoints
class AugAssignment(NodeParent):
    def __init__(self, Name, Operator, Value):
        self.Name = Name
        self.Operator = Operator
        self.Value = Value

class Floor(NodeParent):
    def __init__(self, Value):
        self.Value = Value
class Ceil(NodeParent):
    def __init__(self, Value):
        self.Value = Value
class Sqrt(NodeParent):
    def __init__(self, Value):
        self.Value = Value
class Log(NodeParent):
    def __init__(self, Value, Base=ObjNONE()):
        self.Value = Value
        self.Base = Base
class Exp(NodeParent):
    def __init__(self, Value):
        self.Value = Value
class Sin(NodeParent):
    def __init__(self, Value):
        self.Value = Value
class Cos(NodeParent):
    def __init__(self, Value):
        self.Value = Value
class Tan(NodeParent):
    def __init__(self, Value):
        self.Value = Value
class Factorial(NodeParent):
    def __init__(self, Value):
        self.Value = Value
class Gcd(NodeParent):
    def __init__(self, A, B):
        self.A = A
        self.B = B
class Lcm(NodeParent):
    def __init__(self, A, B):
        self.A = A
        self.B = B
class Mod(NodeParent):
    def __init__(self, Value, Divisor):
        self.Value = Value
        self.Divisor = Divisor
class MathConstants(NodeParent):
    def __init__(self, Constant):
        self.Constant = Constant

class Lambda(NodeParent):
    def __init__(self, Parameters, Body):
        self.Parameters = Parameters
        self.Body = Body
class MapFunction(FunctionParent):
    def __init__(self, Function, Iterable):
        self.Function = Function
        self.Iterable = Iterable
class FilterFunction(FunctionParent):
    def __init__(self, Function, Iterable):
        self.Function = Function
        self.Iterable = Iterable     
class ReduceFunction(FunctionParent):
    def __init__(self, Function, Iterable, InitialValue=ObjNONE()):
        self.Function = Function
        self.Iterable = Iterable
        self.InitialValue = InitialValue 

class ListAssignment(ValueParent):
    def __init__(self, *LstElements):
        self.Lst = LstElements
class ListCall(NodeParent):
    def __init__(self, ListName, Index):
        self.ListName = ListName
        self.Index = Index
class ListEdit(NodeParent):
    def __init__(self, Name, EditType, AppendVal=ObjNONE(), \
    DelVal=ObjNONE(), DelIndex=ObjNONE(), PopIndex=ObjNONE(), \
    ReversedSort=Boolean('False')):
        self.Name = Name
        self.EditType = EditType
        self.AppendVal = AppendVal
        self.DelVal =DelVal
        self.DelIndex= DelIndex
        self.PopIndex = PopIndex
        self.ReversedSort = ReversedSort
class ListContains(NodeParent):
    def __init__(self, List, Element):
        self.List = List
        self.Element = Element
class InsertElement(NodeParent):
    def __init__(self, Name, Var, IndexPos):
        self.Name = Name
        self.Var = Var 
        self.IndexPos = IndexPos
class Range(FunctionParent):
    def __init__(self, BoundMin, BoundMax, Step=Integer(1)):
        self.BoundMin = BoundMin
        self.BoundMax = BoundMax
        self.Step = Step

class Variable(NodeParent):
    def __init__(self, Name):
        self.Name = Name
class Operation(NodeParent):
    def __init__(self, Left, Operator, Right):
        self.Left = Left
        self.Operator = Operator
        self.Right = Right
class Assignment(NodeParent):
    def __init__ (self, Name, Val):
        self.Name = Name
        self.Val = Val
class InitVariable(NodeParent):
    def __init__(self, Name):
        self.Name = Name

class FuncCall(IntepreterParent): #Simple Function Call
    def __init__(self, Function):
        self.Function = Function
class Print(FunctionParent):
    def __init__(self, Contents, End=PrimitiveWrapper('\n')):
        self.Contents = Contents
        self.End = End
class Len(NodeParent):
    def __init__(self, Var):
        self.Var = Var
class Max(FunctionParent):
    def __init__(self, Var):
        self.Var = Var
class Min(FunctionParent):
    def __init__(self, Var):
        self.Var = Var

class Mean(NodeParent):
    def __init__(self, List):
        self.List = List
class Median(NodeParent):
    def __init__(self, List):
        self.List = List
class Mode(NodeParent):
    def __init__(self, List):
        self.List = List

class IfCondition(NodeParent):
    def __init__(self, Expression, Body, ElseBody=ObjNONE(), Elif=ObjNONE(),\
    ElifBody=ObjNONE()):
        self.Expression = Expression
        self.Body = Body
        self.ElseBody = ElseBody
        self.Elif = Elif
        self.ElifBody = ElifBody
class Condition(NodeParent):
    def __init__(self, Right, Operator, Left):
        self.Right = Right
        self.Operator = Operator
        self.Left = Left
class AnyCondition(NodeParent):
    def __init__(self, Condition):
        self.Condition = Condition
class AllCondition(NodeParent):
    def __init__(self, Condition):
        self.Condition = Condition
class LogicalOperation(NodeParent):
    def __init__(self, RightOp, Op, LeftOp):
        self.RightOp = RightOp
        self.Op = Op
        self.LeftOp = LeftOp

class Switch(NodeParent):
    def __init__(self, Scenarios, SwitchVar, Default=ObjNONE()):
        self.Scenarios = Scenarios
        self.SwitchVar = SwitchVar
        self.Default = Default
class Scenario(NodeParent):
    def __init__(self, Var, Body, Fallthrough=PrimitiveWrapper(False)):
        self.Var = Var
        self.Body = Body
        self.Fallthrough = Fallthrough

class Loop(FunctionParent):
    def __init__(self, LoopType, Body, Iterable=ObjNONE(),\
    Expression=ObjNONE(), ControlVar=ObjNONE()):
        self.LoopType = LoopType
        self.Iterable = Iterable
        self.Body = Body
        self.Expression = Expression
        self.ControlVar = ControlVar
class EnumerateObjects(FunctionParent):
    def __init__(self, Iterable, Start=PrimitiveWrapper(0)):
          self.Iterable = Iterable
          self.Start = Start
class Break(Exception, NodeParent):
    def __init__(self, ExitMessage=str()):
        self.ExitMessage = ExitMessage
class Continue(Exception, NodeParent):
    pass
class Return(Exception, NodeParent):
    def __init__(self, Value):
        self.Value = Value

class DisplayContext(IntepreterParent):
    pass
class DisplayCreditInfo(IntepreterParent):
    pass

class DefineFunction(FunctionParent):
    def __init__(self, Name, Body, Param):
      self.Name = Name
      self.Body = Body
      self.Param = Param
class UserFunction(FunctionParent):
    def __init__(self, FuncName, Args, Global=Boolean('True')):
      self.FuncName = FuncName
      self.Args = Args
      self.Global = Global

class UserSTDIn(IntepreterParent):
    def __init__(self, Text, Echo=Boolean('True')):
      self.Text = Text
      self.Echo = Echo
class ASTLangDir(FunctionParent):
    pass

class Join(NodeParent):
    def __init__(self, Delimiter, Items):
        self.Delimiter = Delimiter  
        self.Items = Items
class StringUpper(NodeParent):
    def __init__(self, Str):
        self.Str = Str
class StringLower(NodeParent):
    def __init__(self, Str):
        self.Str = Str
class StringOperation(NodeParent):
    def __init__(self, Var, OpType, Arg=ObjNONE()):
        self.Var = Var 
        self.OpType = OpType 
        self.Arg = Arg 
class StringContains(NodeParent):
    def __init__(self, Text, Substring):
        self.Text = Text
        self.Substring = Substring

class Clamp(NodeParent):
    def __init__(self, Value, Min, Max):
        self.Value = Value
        self.Min = Min
        self.Max = Max
class DeepCopy(NodeParent):
    def __init__(self, Value):
        self.Value = Value
class HashValue(NodeParent):
    def __init__(self, Value):
        self.Value = Value
class BaseConvert(NodeParent):
    def __init__(self, Number, FromBase, ToBase):
        self.Number = Number
        self.FromBase = FromBase
        self.ToBase = ToBase

class DictionaryAssign(ValueParent):
    def __init__(self, Pairs):
        self.Pairs = Pairs
class DictGet(NodeParent):
    def __init__(self, Var, Key=ObjNONE(), SliceVal=ObjNONE(), GetKey=Boolean('False'), GetValues=Boolean('False'),\
        GetItems=Boolean('False'), HasKey=ObjNONE()):
        self.Key = Key
        self.Var = Var
        self.GetKey = GetKey
        self.GetItems = GetItems
        self.GetValues = GetValues
        self.SliceVal = SliceVal
        self.HasKey = HasKey
class DictItems(NodeParent):
    def __init__(self, ItemEditType, Var, Key, Value=ObjNONE()):
        self.Var = Var
        self.ItemEditType = ItemEditType
        self.Key = Key 
        self.Value = Value

class IsStringAffix(ValueParent):
    def __init__(self, Var, AffixCheckMode, AffixStr):
        self.Var = Var
        self.AffixCheckMode = AffixCheckMode
        self.AffixStr = AffixStr
class IsStringType(NodeParent):
    def __init__(self, Var, CheckMode):
        self.Var = Var
        self.CheckMode = CheckMode
class StringReplace(NodeParent):
    def __init__(self, Text, OldSubstring, NewSubstring):
        self.Text = Text
        self.OldSubstring = OldSubstring
        self.NewSubstring = NewSubstring
class FormattedString(NodeParent):
    def __init__(self, FormatString, Args=ListAssignment()):
        self.FormatString = FormatString
        self.Args = Args

class Slice(NodeParent):
    def __init__(self, Var, Start=ObjNONE(), End=ObjNONE(), Step=Integer(1)):
        self.Var = Var
        self.Start = Start 
        self.End = End  
        self.Step = Step
class Filter(NodeParent):
    def __init__(self, Iterable, Conditional, ResultName=ObjNONE()):
        self.Iterable = Iterable
        self.Conditional = Conditional
        self.ResultName = ResultName 
class YieldGenerator(FunctionParent):
    def __init__(self, Value):
        self.Value = Value
class StringSplit(NodeParent):
    def __init__(self, Str, Delimiter):
        self.Str = Str
        self.Delimiter = Delimiter
class TypeOf(NodeParent):
    def __init__(self, Value):
        self.Value = Value

class IsType(NodeParent):
    def __init__(self, Value, Type):
        self.Value = Value
        self.Type = Type
class ErrorCatch(IntepreterParent):
    def __init__(self, CatchedException, TryBody, ExceptBody, FinallyBody=ObjNONE()):
        self.CatchedException = CatchedException
        self.TryBody = TryBody
        self.ExceptBody = ExceptBody
        self.FinallyBody = FinallyBody
class Raise(NodeParent):
    def __init__(self, ErrorName, ErrorText=String('')):
        self.ErrorName = ErrorName
        self.ErrorText = ErrorText

class Comment(FunctionParent):
    def __init__(self, Text):
        self.Text = Text
class Exit(IntepreterParent):
    def __init__(self, Code=Integer(0)):
        self.Code = Code

class TupleAssign(ValueParent):
    def __init__(self, Elements):
        self.Elements = Elements
class TupleInspection(NodeParent):
    def __init__(self, TupleVar, Mode, Index=ObjNONE(), UnpackingTargets=ObjNONE()):
        self.TupleVar = TupleVar
        self.Mode = Mode
        self.Index = Index
        self.UnpackingTargets = UnpackingTargets
class Unique(NodeParent):
    def __init__(self, Items):
        self.Items = Items
class PauseExecution(FunctionParent):
    def __init__(self, Miliseconds):
        self.Miliseconds = Miliseconds

class DefineClass(FunctionParent):
    def __init__(self, Name, Body, Base=ObjNONE()):
        self.Name = Name
        self.Body = Body 
        self.Base = Base
class NewInstance(NodeParent):
    def __init__(self, ClassName, Args=[]):
        self.ClassName = ClassName
        self.Args = Args
class GetAttr(ValueParent):
    def __init__(self, Obj, Attr):
        self.Obj = Obj
        self.Attr = Attr
class SetAttr(NodeParent):
    def __init__(self, Obj, Attr, Value):
        self.Obj = Obj
        self.Attr = Attr
        self.Value = Value
class MethodCall(FunctionParent):
    def __init__(self, Obj, MethodName, Args=[]):
        self.Obj = Obj
        self.MethodName = MethodName
        self.Args = Args

class SuperClass(NodeParent):
    def __init__(self, ChildClassName, ParentClassName, Methods=ListAssignment(), Properties=ListAssignment()):
        self.ChildClassName = ChildClassName
        self.ParentClassName = ParentClassName 
        self.Methods = Methods 
        self.Properties = Properties  
class Super(NodeParent):
    def __init__(self, MethodName, Args=ListAssignment()):
        self.MethodName = MethodName  
        self.Args = Args
class IsInstanceOf(NodeParent):
    def __init__(self, Object, ClassName):
        self.Object = Object
        self.ClassName = ClassName

class Ord(NodeParent):
    def __init__(self, Str):
        self.Str = Str
class Chr(NodeParent):
    def __init__(self, Str):
        self.Str = Str

class FileRead(FunctionParent):
    def __init__(self, FilePath, Mode=String('r'), Encoding=String('utf-8')):
        self.FilePath = FilePath
        self.Mode = Mode
        self.Encoding = Encoding
class FileWrite(FunctionParent):
    def __init__(self, FilePath, Content, Mode=String('w'), Encoding=String('utf-8')):
        self.FilePath = FilePath
        self.Content = Content
        self.Mode = Mode
        self.Encoding = Encoding
class FileDelete(NodeParent):
    def __init__(self, FilePath):
        self.FilePath = FilePath
class FileSize(ValueParent):
    def __init__(self, FilePath):
        self.FilePath = FilePath
class ListFiles(IntepreterParent):
    def __init__(self, DirectoryPath, Pattern=String('*')):
        self.DirectoryPath = DirectoryPath
        self.Pattern = Pattern

class EvalExpression(IntepreterParent):
    def __init__(self, Expression, Globals=ObjNONE(), Locals=ObjNONE()):
        self.Expression = Expression
        self.Globals = Globals
        self.Locals = Locals
class ExecCode(IntepreterParent):
    def __init__(self, Code, Globals=ObjNONE(), Locals=ObjNONE()):
        self.Code = Code
        self.Globals = Globals
        self.Locals = Locals
class CallFunction(FunctionParent):
    def __init__(self, FunctionName, Args=ListAssignment(), Kwargs=DictionaryAssign([])):
        self.FunctionName = FunctionName
        self.Args = Args
        self.Kwargs = Kwargs
class Sort(NodeParent):
    def __init__(self, List, Reverse=Boolean('False'), Key=ObjNONE()):
        self.List = List
        self.Reverse = Reverse
        self.Key = Key
class Zip(FunctionParent):
    def __init__(self, *Lists):
        self.Lists = Lists
class Shuffle(NodeParent):
    def __init__(self, List):
        self.List = List
class Sample(NodeParent):
    def __init__(self, List, Count):
        self.List = List
        self.Count = Count
class Flatten(NodeParent):
    def __init__(self, List, Depth=Integer(1)):
        self.List = List
        self.Depth = Depth

class SetAssignment(ValueParent):
    def __init__(self, *Elements):
        self.Elements = Elements
class SetOperations(NodeParent):
    def __init__(self, Set1, Set2, Operation):
        self.Set1 = Set1
        self.Set2 = Set2
        self.Operation = Operation 
class SetMethods(NodeParent):
    def __init__(self, SetVar, Method, Element=ObjNONE()):
        self.SetVar = SetVar
        self.Method = Method
        self.Element = Element
class SetContains(NodeParent):
    def __init__(self, Set, Element):
        self.Set = Set
        self.Element = Element
class Split(FunctionParent):
    def __init__(self, Val, Delimiter):
        self.Val = Val
        self.Delimiter = Delimiter

class DateTime(NodeParent):
    def __init__(self, Year=ObjNONE(), Month=ObjNONE(), Day=ObjNONE(), Hour=Integer(0), Minute=Integer(0), Second=Integer(0)):
        self.Year = Year
        self.Month = Month
        self.Day = Day
        self.Hour = Hour
        self.Minute = Minute
        self.Second = Second
class DateTimeNow(NodeParent):
    def __init__(self):
        pass

class WarningRaise(NodeParent):
    def __init__(self, Message, Category=String('UserWarning')):
        self.Message = Message
        self.Category = Category
class ErrorContext(NodeParent):
    def __init__(self, Body, ErrorHandlers=ListAssignment()):
        self.Body = Body
        self.ErrorHandlers = ErrorHandlers
class CustomError(NodeParent):
    def __init__(self, Name, BaseError=String('Exception')):
        self.Name = Name
        self.BaseError = BaseError
class GetErrorInfo(NodeParent):
    def __init__(self, Error):
        self.Error = Error

class Statistics(NodeParent):
    def __init__(self, Data, Operation):
        self.Data = Data
        self.Operation = Operation 
class LinearAlgebra(NodeParent):
    def __init__(self, Matrix1, Matrix2=ObjNONE(), Operation=String('transpose')):
        self.Matrix1 = Matrix1
        self.Matrix2 = Matrix2
        self.Operation = Operation
class Matrix(ValueParent):
    def __init__(self, Rows):
        self.Rows = Rows
class Percentile(NodeParent):
    def __init__(self, Data, Percentage):
        self.Data = Data
        self.Percentage = Percentage
class StandardScore(NodeParent):
    def __init__(self, Value, Mean, StdDev):
        self.Value = Value
        self.Mean = Mean
        self.StdDev = StdDev
class Regression(NodeParent):
    def __init__(self, XData, YData, Type=String('linear')):
        self.XData = XData
        self.YData = YData
        self.Type = Type
class Calculate(ValueParent):
    def __init__(self, Expression):
        self.Expression = Expression

class InspectCode(IntepreterParent):
    def __init__(self, Object, Property=String('type')):
        self.Object = Object
        self.Property = Property
class Debugger(IntepreterParent):
    def __init__(self, Code, Breakpoints=ListAssignment()):
        self.Code = Code
        self.Breakpoints = Breakpoints
class StackTrace(IntepreterParent):
    def __init__(self, Depth=Integer(10)):
        self.Depth = Depth

class DataStream(NodeParent):
    def __init__(self, Source, BufferSize=Integer(1024)):
        self.Source = Source
        self.BufferSize = BufferSize
class StreamProcessor(NodeParent):
    def __init__(self, Stream, ProcessFunction, WindowSize=Integer(10)):
        self.Stream = Stream
        self.ProcessFunction = ProcessFunction
        self.WindowSize = WindowSize
class Pipeline(NodeParent):
    def __init__(self, Stages):
        self.Stages = Stages

class ArrayUtils(ValueParent):
    def __init__(self, Array, Operation, *Args):
        self.Array = Array
        self.Operation = Operation
        self.Args = Args
class Find(NodeParent):
    def __init__(self, Collection, Predicate, Mode=String('first')):
        self.Collection = Collection
        self.Predicate = Predicate
        self.Mode = Mode
class GroupBy(NodeParent):
    def __init__(self, Collection, KeyFunction):
        self.Collection = Collection
        self.KeyFunction = KeyFunction
class Partition(FunctionParent):
    def __init__(self, Collection, Predicate):
        self.Collection = Collection
        self.Predicate = Predicate
class Frequency(NodeParent):
    def __init__(self, Collection):
        self.Collection = Collection

class Assert(IntepreterParent):
    def __init__(self, Condition, Message=String('Assertion')):
        self.Condition = Condition
        self.Message = Message
class SafeCast(NodeParent):
    def __init__(self, Value, TargetType, DefaultValue=ObjNONE()):
        self.Value = Value
        self.TargetType = TargetType
        self.DefaultValue = DefaultValue
class RangeCheck(NodeParent):
    def __init__(self, Value, Min=ObjNONE(), Max=ObjNONE(), Inclusive=Boolean('True')):
        self.Value = Value
        self.Min = Min
        self.Max = Max
        self.Inclusive = Inclusive

class ForceStop(IntepreterParent):
    def __init__(self, Reason=String('')):
        self.Reason = Reason

class LoadHTTPDriver(IntepreterParent):
    def __init__(self, ReturnCode=Boolean('True')):
        self.ReturnCode = ReturnCode
class SendHTTPRequest(NodeParent):
    def __init__(self, Method, URL, Headers=None, Data=None):
        self.Method = Method
        self.URL = URL
        self.Headers = Headers
        self.Data = Data
class HTTPQueryParameters(NodeParent):
    def __init__(self, Params, URL):
        self.URL = URL
        self.Params = Params
primitive = (str, int, float, list, bool, dict, tuple)
class Evaluate(Stack):
    def evaluate(self, node, context):
        if isinstance(node, Exit):
            code = self.evaluate(node.Code, context)
            print(f"\n[IDE EXIT WITH CODE {code}]\n")
            import tkinter as tk
            for widget in tk._default_root.winfo_children():
                if isinstance(widget, tk.Toplevel):
                    widget.destroy()
            tk._default_root.quit()
            sys.exit(code)
        elif isinstance(node, type(...)):
            return None
        elif isinstance(node, type):
            print('[ERROR] Did not recieve arguments for function')
            return
        elif isinstance(node, primitive):
            return node
        elif isinstance(node, Comment):
            return
        elif isinstance(node, PrimitiveWrapper):
            return node.V
        elif isinstance(node, ObjNONE):
            return None
        elif isinstance(node, CastToValue):
            if isinstance(node.Var, Variable): 
                varname = node.Var.Name
            elif not isinstance(node.Var, Variable):
                varname = self.evaluate(node.Var, context)
            else: 
                raise Exception("CastToValue requires a valid node")
            value = self.evaluate(node.Var, context)
            match node.CastVal:
                case 'str':
                    casted = str(value)
                case 'int':
                    casted = int(value)
                case 'list':
                    casted = list(value)
                case 'tuple':
                    casted = tuple(value)
                case _: 
                    raise Exception(f"Unsupported cast: {node.CastVal}")
            
            context[varname] = casted
            return casted
        elif isinstance(node, Integer):
            if isinstance(node.Int, int):
                if node.Int >= 2**32:
                    raise OverflowError("Integer too large, expected 2^32")
                return node.Int
            return int(self.evaluate(node.Int, context))
        elif isinstance(node, Float):
            if isinstance(node.Flt, float):
                if node.Flt >= float(2^32):
                    raise OverflowError("Float too large, expected 2^32") 
                return node.Flt
            return float(self.evaluate(node.Flt, context))
        elif isinstance(node, Boolean):
            if node.Bool == 'True':
                return True
            elif node.Bool == 'False':
                return False
            else:
                return self.evaluate(node.Bool, context)
        elif isinstance(node, Variable):
            return context.get(node.Name)
        elif isinstance(node, String):
            if isinstance(node.Str, str):
                return node.Str
            return str(self.evaluate(node.Str, context))
        elif isinstance(node, ListAssignment):
            return [self.evaluate(elem, context) for elem in node.Lst]
        elif isinstance(node, ListCall):
            l = self.evaluate(node.ListName, context)
            i = self.evaluate(node.Index, context)
            return l[i]
        elif isinstance(node, FuncCall):
            if isinstance(node.Function, Print):
                contents = node.Function.Contents
                value = self.evaluate(contents, context)
    
                if str(value) == "Are you mad? That's a 12-year-old scotch!":
                    raise MemoryError('we opened it yesterday (Reference: Day After Tomorrow)')
                end_param = node.Function.End
                if isinstance(end_param, PrimitiveWrapper):
                    end_val = end_param.V
                else:
                    end_val = self.evaluate(end_param, context)
                
                if isinstance(value, str) and value in context:
                    print(context[value], end=end_val)
                else:
                    print(value, end=end_val)
                return None
        elif isinstance(node, ListEdit):
            mode = node.EditType
            valid_modes = {'append', 'del', 'clear', 'sort', 'pop', 'reverse'}
            if mode not in valid_modes:
                raise ValueError(f"Unsupported ListEdit mode: {mode}")
            
            if isinstance(node.Name, str):
                list_name = node.Name
                if list_name not in context:
                    raise NameError(f"List '{list_name}' is not defined in context")
                c = context.get(list_name)
            elif hasattr(node.Name, 'Name'):
                list_name = node.Name.Name
                if list_name not in context:
                    raise NameError(f"List '{list_name}' is not defined in context")
                c = context.get(list_name)
            else:
                c = self.evaluate(node.Name, context)
            
            if not isinstance(c, list):
                raise TypeError(f"ListEdit requires a list, got {type(c)}")
            
            if mode == 'append':
                apnd = self.evaluate(node.AppendVal, context)
                c.append(apnd)
            elif mode == 'del':
                if not isinstance(node.DelVal, ObjNONE):
                    Del = self.evaluate(node.DelVal, context)
                    if Del in c:
                        c.remove(Del)
                elif node.DelIndex:
                    delIndex = self.evaluate(node.DelIndex, context)
                    if 0 <= delIndex < len(c):
                        del c[delIndex]
            elif mode == 'clear':
                c.clear()
            elif mode == 'sort':
                c.sort(reverse=self.evaluate(node.ReversedSort, context))
            elif mode == 'pop':
                popi = self.evaluate(node.PopIndex, context)
                if 0 <= popi < len(c):
                    popped = c.pop(popi)
                    if list_name:
                        context[list_name] = c 
                    return popped
            elif mode == 'reverse':
                c.reverse()
            if list_name:
                context[list_name] = c
            
            return c
        elif isinstance(node, Range):
            bmin = self.evaluate(node.BoundMin, context)
            bmax = self.evaluate(node.BoundMax, context)
            step = self.evaluate(node.Step, context)
            return list(range(bmin, bmax + step, step))
        elif isinstance(node, InitVariable):
            context[node.Name] = None
            return
        elif isinstance(node, Operation):
            left_val = self.evaluate(node.Left, context)
            right_val = self.evaluate(node.Right, context)
            if node.Operator == "+":
                return left_val + right_val
            elif node.Operator == "-":
                return left_val - right_val
            elif node.Operator == "*":
                return left_val * right_val
            elif node.Operator == "/":
                return left_val / right_val
            elif node.Operator == '%':
                return left_val % right_val
            elif node.Operator == '//':
                return left_val // right_val
        elif isinstance(node, Assignment):
            value = self.evaluate(node.Val, context)
            context[node.Name] = value
            return value
        elif isinstance(node, Module):
            result = None
            for stmt in node.ModuleCode:
                result = self.evaluate(stmt, context)
            return result
        elif isinstance(node, FuncCall):
            if isinstance(node.Function, Print):
                contents = node.Function.Contents
                value = self.evaluate(contents, context)
                
                if isinstance(node.Function.End, PrimitiveWrapper):
                    end_val = node.Function.End.V
                else:
                    end_val = self.evaluate(node.Function.End, context)
                
                if isinstance(value, str) and value in context:
                    print(context[value], end=end_val)
                else:
                    print(value, end=end_val)
                return None
            elif isinstance(node.Function, Len):
                    var = self.evaluate(node.Function.Var, context)
                    return len(var)
            elif isinstance(node.Function, Max):
                    var = list(self.evaluate(node.Function.Var, context))
                    return max(var)
            elif isinstance(node.Function, Min):
                var = list(self.evaluate(node.Function.Var, context))
                return min(var)
        elif isinstance(node, Condition):
            left = self.evaluate(node.Left, context)
            right = self.evaluate(node.Right, context)
            if left is None or right is None:
                return
            match node.Operator:
                case '==':
                    return left == right
                case '!=':
                    return left != right
                case '>':
                    return left > right
                case '<':
                    return left < right
                case '>=':
                    return left >= right
                case '<=':
                    return left <= right
        elif isinstance(node, LogicalOperation):
            left = self.evaluate(node.LeftOp, context)
            right = self.evaluate(node.RightOp, context)
            if node.Op == 'and':
                return left and right
            if node.Op == 'or':
                return left or right
            if node.Op == 'contains':
                return left in right
            if node.Op == 'not':
                return not left 
        elif isinstance(node, IfCondition):
            if self.evaluate(node.Expression, context):
                for stmt in node.Body:
                    self.evaluate(stmt, context)
            elif self.evaluate(node.Elif, context):
                for stmt in node.ElifBody:
                    self.evaluate(stmt, context)
            elif self.evaluate(node.ElseBody, context):
                for stmt in node.ElseBody:
                    self.evaluate(stmt, context)
        elif isinstance(node, Switch):
            switch_val = self.evaluate(node.SwitchVar, context)
            matched = False

            for scenario in node.Scenarios:
                case_val = self.evaluate(scenario.Var, context)
                if switch_val == case_val:
                    for stmt in scenario.Body:
                        self.evaluate(stmt, context)
                    matched = True
                    if not scenario.Fallthrough.V:
                        break

            if not matched and node.Default:
                for stmt in node.Default:
                    self.evaluate(stmt, context)
        elif isinstance(node, cheesestick):
            print('You\'ve found an ASTLang easter egg: https://onecompiler.com/csharp/43w2q5euu')
        elif isinstance(node, Iterable):
            i = self.evaluate(node.Iter, context)
            return iter(i)
        elif isinstance(node, Factorial):
            v = self.evaluate(node.Value, context)
            if not isinstance(v, int) or v < 0:
                raise ValueError("Factorial requires a non-negative integer")
            return math.factorial(v)
        elif isinstance(node, Gcd):
            a = self.evaluate(node.A, context)
            b = self.evaluate(node.B, context)
            return math.gcd(a, b)
        elif isinstance(node, Lcm):
            a = self.evaluate(node.A, context)
            b = self.evaluate(node.B, context)
            return math.lcm(a, b)
        elif isinstance(node, Loop):
            if node.LoopType == 'for':
                iterable = self.evaluate(node.Iterable, context)
                for value in iterable:
                    if isinstance(node.ControlVar, list):
                        if isinstance(value, (list, tuple)):
                            if len(value) != len(node.ControlVar):
                                raise ValueError("Mismatch between control variables and iterable unpacking")
                            for var_name, var_value in zip(node.ControlVar, value):
                                context[var_name] = var_value
                        else:
                            if len(node.ControlVar) != 1:
                                raise ValueError("Mismatch between control variables and iterable unpacking")
                            context[node.ControlVar[0]] = value
                    else:  # single var
                        context[node.ControlVar] = value
                    try:
                        for stmt in node.Body:
                            self.evaluate(stmt, context)
                    except Continue:
                        continue
                    except Break:
                        break
            elif node.LoopType == 'while':
                while self.evaluate(node.Expression, context):
                    try:
                        for stmt in node.Body:
                            self.evaluate(stmt, context)
                    except Continue:
                        continue
                    except Break:
                        break
        elif isinstance(node, EnumerateObjects):
            Iter = iter(self.evaluate(node.Iterable, context))
            st = self.evaluate(node.Start, context)
            if not isinstance(st, int):
                raise TypeError("Start object must be an integer")
            return enumerate(Iter, start=st)
        elif isinstance(node, Join):
            delimiter = self.evaluate(node.Delimiter, context)
            items = self.evaluate(node.Items, context)
        
            if not isinstance(delimiter, str):
                raise TypeError("Join delimiter must be a string")
            if not isinstance(items, list) or not all(isinstance(i, str) for i in items):
                raise TypeError("Join items must be a list of strings")
        
            return delimiter.join(items)
        elif isinstance(node, InsertElement):
            var_name = self.evaluate(node.Name, context)
            v = self.evaluate(node.Var, context)
            pos = self.evaluate(node.IndexPos, context)
        
            if not isinstance(pos, int):
                raise TypeError("Index Position must be an integer")
            if not isinstance(var_name, str):
                raise TypeError("Variable name must be a string")
            lst = context.get(var_name)
            if not isinstance(lst, list):
                raise TypeError(f"Variable '{var_name}' must be a list")
        
            lst.insert(pos, v)
            context[var_name] = lst
            return lst
        elif isinstance(node, StringUpper):
            if isinstance(node.Str, Variable):
                var_name = node.Str.Name
                s = context.get(var_name)
                if not isinstance(s, str):
                    raise TypeError('StringUpper expects a string')
                result = s.upper()
                context[var_name] = result
                return result
            else:
                s = self.evaluate(node.Str, context)
                if not isinstance(s, str):
                    raise TypeError('StringUpper expects a string')
                return s.upper()
        elif isinstance(node, StringLower):
            if isinstance(node.Str, Variable):
                var_name = node.Str.Name
                s = context.get(var_name)
                if not isinstance(s, str):
                    raise TypeError('StringLower expects a string')
                result = s.lower()
                context[var_name] = result
                return result
            else:
                s = self.evaluate(node.Str, context)
                if not isinstance(s, str):
                    raise TypeError('StringLower expects a string')
                return s.lower()
        elif isinstance(node, Break):
            print(self.evaluate(node.ExitMessage, context))
            raise node
        elif isinstance(node, Continue):
            raise node
        elif isinstance(node, Return):
            v = self.evaluate(node.Value, context)
            return v
        elif isinstance(node, DisplayContext):
            print(context)
        elif isinstance(node, DefineFunction):
            context[node.Name] = node 
            return
        elif isinstance(node, UserFunction):
            func_def = context.get(node.FuncName)
            if not isinstance(func_def, DefineFunction):
                raise NameError(f"Function '{node.FuncName}' is not defined")

            local_context = context if self.evaluate(node.Global, context) else context.copy()

            if hasattr(node.Args, 'Lst'):
                args_list = node.Args.Lst
            elif isinstance(node.Args, list):
                args_list = node.Args
            else:
                args_list = [node.Args] if node.Args else []

            for param, arg in zip(func_def.Param, args_list):
                local_context[param] = self.evaluate(arg, context)
            
            if any(isinstance(stmt, YieldGenerator) for stmt in func_def.Body):
                def generator():
                    for stmt in func_def.Body:
                        if isinstance(stmt, YieldGenerator):
                            yielded = self.evaluate(stmt.Value, local_context)
                            if isinstance(yielded, list):
                                for v in yielded:
                                    yield v
                            else:
                                yield yielded
                    return
                return generator()
            
            result = None
            for stmt in func_def.Body:
                val = self.evaluate(stmt, local_context)
                if isinstance(stmt, Return):
                    return val
                result = val
            return result
        elif isinstance(node, DisplayCreditInfo):
            print(info)
            print('\n')
        elif isinstance(node, UserSTDIn):
            prompttxt = self.evaluate(node.Text, context)
            opt = get_user_input(prompt=prompttxt)
            if self.evaluate(node.Echo, context):
                print(opt)
                return opt
            else:
                return opt
        elif isinstance(node, ASTLangDir):
            for func in get_by_Id():
                print(func, end='\n')
        elif isinstance(node, DictionaryAssign):
            d = {}
            for k, v in node.Pairs:
                key = self.evaluate(k, context)
                val = self.evaluate(v, context)
                d[key] = val
            return d
        elif isinstance(node, DictGet):
            var_val = self.evaluate(node.Var, context)
            key = self.evaluate(node.Key, context) if node.Key else None
            get_keys = self.evaluate(node.GetKey, context) if getattr(node, "GetKey", False) else False
            get_values = self.evaluate(node.GetValues, context) if getattr(node, "GetValues", False) else False
            get_items = self.evaluate(node.GetItems, context) if getattr(node, "GetItems", False) else False
            slice_val = self.evaluate(node.SliceVal, context) if getattr(node, "SliceVal", None) else None
            has_key = self.evaluate(node.HasKey, context) if getattr(node, "HasKey", None) else None

            if isinstance(var_val, dict):
                if get_keys:
                    return list(var_val.keys())
                if get_items:
                    return list(var_val.items())
                if get_values:
                    return list(var_val.values())
                if key is not None:
                    return var_val.get(key, 0)
                if has_key:
                    return key in var_val
            elif isinstance(var_val, list):
                if slice_val:
                    start, stop, step = slice_val
                    return var_val[start:stop:step]
                if isinstance(key, int):
                    return var_val[key]
                else:
                    raise Exception("DictGet: list indices must be integers")
            else:
                raise Exception(f"DictGet: unsupported type {type(var_val).__name__}")
        elif isinstance(node, DictItems):
            k = self.evaluate(node.Key, context)
            v = self.evaluate(node.Value, context)
            d = self.evaluate(node.Var, context)
            if node.ItemEditType == 'add':
                d[k] = v
                if isinstance(node.Var, Variable):
                    context[node.Var.Name] = d
                return d 
            elif node.ItemEditType == 'remove':
                del d[k]
                if isinstance(node.Var, Variable):
                    context[node.Var.Name] = d
                return d
        elif isinstance(node, Abs):
            v = self.evaluate(node.Val, context)
            return abs(v)
        elif isinstance(node, Power):
            p = self.evaluate(node.Base, context)
            exp = self.evaluate(node.Exp, context)
            return pow(p, exp)
        elif isinstance(node, RandomInt):
            mx = self.evaluate(node.Max, context)
            mn = self.evaluate(node.Min, context)
            return randint(mn, mx)
        elif isinstance(node, RandomChoice):
            lst = self.evaluate(node.List, context)
            if not isinstance(lst, list):
                raise TypeError("RandomChoice List must evaluate to a list")
            if len(lst) == 0:
                raise ValueError("RandomChoice cannot choose from empty list")
            from random import choice
            return choice(lst)
        elif isinstance(node, AnyCondition):
            return any(self.evaluate(node.Condition, context))
        elif isinstance(node, AllCondition):
            return all(self.evaluate(node.Condition, context))
        elif isinstance(node, TupleAssign):
            return tuple(self.evaluate(elem, context) for elem in node.Elements)
        elif isinstance(node, TupleInspection):
            tup = self.evaluate(node.TupleVar, context)
            if node.Mode == "index":
                idx = self.evaluate(node.Index, context)
                return tup[idx]
            elif node.Mode == "unpack":
                if len(tup) != len(node.UnpackingTargets):
                    raise ValueError("Tuple unpack length mismatch")
                for target, value in zip(node.UnpackingTargets, tup):
                    context[target] = value
        elif isinstance(node, TestCode):
            sample = Module(
            InitVariable('score'),
            InitVariable('level'),
            Assignment(Name='Inventory', Val=DictionaryAssign([
                (String('Sword'), Integer(1)),
                (String('Shield'), Integer(1)),
                (String('Potion'), Integer(5))
            ])),
            DefineFunction(
                Name='PrintInventory',
                Param=['inv'],
                Body=[
                    FuncCall(Function=Print(Contents=Variable('inv'))),
                    Return(Value=PrimitiveWrapper(0))
                ]
            ),
            DefineFunction(
                Name='AddItem',
                Param=['inv', 'item', 'count'],
                Body=[
                            Assignment(
                    Name='current_count',
                    Val=Operation(
                        Left=DictGet(
                            Var=Variable('inv'),
                            Key=Variable('item'),
                            GetKey=Boolean(Bool=False)
                        ),
                        Operator='+',
                        Right=Variable('count')
                    )
                ),

                    DictItems(
                        ItemEditType='add',
                        Var=Variable('inv'),
                        Key=Variable('item'),
                        Value=Variable('current_count')
                    ),
                    Return(Value=PrimitiveWrapper(0))
                ]
            ),
            UserFunction(FuncName='AddItem', Args=[Variable('Inventory'), String('Potion'), Integer(3)], Global=PrimitiveWrapper(True)),
            UserFunction(FuncName='AddItem', Args=[Variable('Inventory'), String('Elixir'), Integer(1)], Global=PrimitiveWrapper(True)),
            DictItems(ItemEditType='remove', Var=Variable('Inventory'), Key=String('Shield')),
            Loop(
                LoopType='for',
                Iterable=Range(BoundMin=Integer(1), BoundMax=Integer(3)),
                ControlVar='i',
                Body=[
                    FuncCall(Function=Print(Contents=String('Loop iteration:'))),
                    FuncCall(Function=Print(Contents=Variable('i')))
                ]
            ),
            Assignment(Name='score', Val=Integer(60)),
            Assignment(Name='level', Val=Integer(1)),
            IfCondition(
                Expression=Condition(Left=Variable('score'), Operator='>=', Right=Integer(50)),
                Body=[FuncCall(Function=Print(Contents=String('You passed the level!')))],
                ElseBody=[FuncCall(Function=Print(Contents=String('Try again!')))]
            ),
            IfCondition(
                Expression=LogicalOperation(
                    LeftOp=Condition(Left=Variable('score'), Operator='>', Right=Integer(10)),
                    Op='and',
                    RightOp=Condition(Left=Variable('level'), Operator='==', Right=Integer(1))
                ),
                Body=[FuncCall(Function=Print(Contents=String('Early game progress')))]
            ),
            Switch(
                SwitchVar=Variable('level'),
                Scenarios=[
                    Scenario(Var=Integer(1), Body=[FuncCall(Function=Print(Contents=String('Level 1 unlocked!')))]),
                    Scenario(Var=Integer(2), Body=[FuncCall(Function=Print(Contents=String('Level 2 unlocked!')))])
                ],
                Default=[FuncCall(Function=Print(Contents=String('Unknown level')))]
            ),
            DefineFunction(
                Name='DoubleScore',
                Param=['points'],
                Body=[
                    Return(Value=Operation(
                        Left=Variable('points'),
                        Operator='*',
                        Right=Integer(2)
                    ))
                ]
            ),
            Assignment(Name='score', Val=UserFunction(FuncName='DoubleScore', Args=[Variable('score')], Global=PrimitiveWrapper(True))),
            Assignment(Name='player_name', Val=String('nan')),
            FuncCall(Function=Print(Contents=StringUpper(Str=Variable('player_name')))),
            FuncCall(Function=Print(Contents=StringLower(Str=Variable('player_name')))),
            Assignment(Name='joined_names', Val=Join(
                Delimiter=String(', '),
                Items=ListAssignment(String('Alice'), String('Bob'), String('Charlie'))
            )),
            FuncCall(Function=Print(Contents=Variable('joined_names'))),
            Loop(
                LoopType='for',
                Iterable=EnumerateObjects(
                    Iterable=ListAssignment(String('A'), String('B'), String('C')),
                    Start=Integer(1)
                ),
                ControlVar=['idx', 'val'],
                Body=[
                    FuncCall(Function=Print(Contents=Operation(
                        Left=Variable('idx'),
                        Operator='+',
                        Right=Integer(0)
                    )))
                ]
            ),
            UserFunction(FuncName='PrintInventory', Args=[Variable('Inventory')], Global=PrimitiveWrapper(True))
            )

            return self.evaluate(sample, context)
        elif isinstance(node, IsStringAffix):
            v = self.evaluate(node.Var, context)
            astr = self.evaluate(node.AffixStr, context)
            mode = node.AffixCheckMode
            if not isinstance(v, str):
                raise TypeError('IsStringAffix expects string "Var"')
            if mode == 'startswith':
                return v.startswith(astr)
            if mode == 'endswith':
                return v.endswith(astr)
        elif isinstance(node, IsStringType):
            v = self.evaluate(node.Var, context)
            if isinstance(v, str):
                if node.CheckMode == 'alpha':
                    return v.isalpha()
                elif node.CheckMode == 'upper':
                    return v.isupper()
                elif node.CheckMode == 'lower':
                    return v.islower()
        elif isinstance(node, Slice):
            seq = self.evaluate(node.Var, context)

            start = self.evaluate(node.Start, context) if node.Start else None
            end   = self.evaluate(node.End, context)   if node.End   else None
            step  = self.evaluate(node.Step, context)  if node.Step  else None

            if not isinstance(seq, (str, list, tuple)):
                raise Exception("Unsupported slicing type")

            return seq[start:end:step]
        elif isinstance(node, StringOperation):
            val = self.evaluate(node.Var, context)
            arg = self.evaluate(node.Arg, context) if node.Arg else None
            if node.OpType == 'reverse':
                return val[::-1]
            elif node.OpType == 'replace':
                old, new = arg
                return val.replace(old, new)
            elif node.OpType == 'split':
                return val.split(arg)
            elif node.OpType == 'sort':
                return sorted(val)
            else:
                raise Exception(f"Unknown StringOperation: {node.OpType}")
        elif isinstance(node, ErrorCatch):
            exc = node.CatchedException 
            result = None
            try:
                for stmt in node.TryBody:
                    result = self.evaluate(stmt, context)
            except exc:
                for stmt in node.ExceptBody:
                    result = self.evaluate(stmt, context)
            finally:
                if not isinstance(node.FinallyBody, ObjNONE):
                    for stmt in node.FinallyBody:
                        self.evaluate(stmt, context)
            return result
        elif isinstance(node, Sum):
            v = self.evaluate(node.Var, context)
            if not isinstance(v, list):
                raise Exception("Sum expects list argument")
            return sum(v)
        elif isinstance(node, Round):
            v = self.evaluate(node.Flt, context)
            decp = self.evaluate(node.DecPoints, context)
            if not isinstance(decp, int):
                raise Exception("DecPoints expects an integer value")
            return round(v, decp)
        elif isinstance(node, Filter):
            iterable = self.evaluate(node.Iterable, context)
            result = []
            for item in iterable:
                local_context = context.copy()
                local_context[node.ItemVar] = item
                condition_val = self.evaluate(node.Conditional, local_context)
                if condition_val:
                    result.append(item)
            if not isinstance(node.ResultName, ObjNONE):
                context[node.ResultName] = result
            return result
        elif isinstance(node, GetInfo):
            print(info)
        elif isinstance(node, YieldGenerator):
            value = self.evaluate(node.Value, context)
            if isinstance(value, list):
                def generatorx():
                    for v in value:
                        yield v
                return generatorx()
            def generatorxx():
                yield value
            return generatorxx()
        elif isinstance(node, StringSplit):
            s = self.evaluate(node.Str, context)
            d = self.evaluate(node.Delimiter, context)
            if not isinstance(s, str):
                raise TypeError("StringSplit Str must evaluate to a string")
            if not isinstance(d, str):
                raise TypeError("StringSplit Delimiter must evaluate to a string")
            return s.split(d)
        elif isinstance(node, Unique):
            items = self.evaluate(node.Items, context)
            if not isinstance(items, list):
                raise TypeError("Unique 'Items' must evaluate to a list")
            return list(dict.fromkeys(items))
        elif isinstance(node, Mean):
            lv = self.evaluate(node.List, context)
            if not isinstance(lv, list):
                raise TypeError('Mean expects list')
            return sum(lv)/len(lv)
        elif isinstance(node, Median):
            lv = self.evaluate(node.List, context)
            if not isinstance(lv, list):
                raise TypeError('Median expects list')
            mvar = sorted(lv)
            
            if len(mvar) % 2 == 1:
                median_index = len(mvar) // 2
                return mvar[median_index]
            else:
                mid1 = len(mvar) // 2 - 1
                mid2 = len(mvar) // 2
                return (mvar[mid1] + mvar[mid2]) / 2
        elif isinstance(node, Mode):
            lv = self.evaluate(node.List, context)
            if not isinstance(lv, list):
                raise TypeError('Mode expects list')
            if not lv:
                print('Undefined')
            counts = {x: lv.count(x) for x in lv}
            max_count = max(counts.values())
            for k, v in counts.items():
                if v == max_count:
                    return k
        elif isinstance(node, PauseExecution):
            time.sleep(self.evaluate(node.Miliseconds, context)/1000)
        elif isinstance(node, Raise):
            import builtins
            err_text = self.evaluate(node.ErrorText, context)
            err_name = self.evaluate(node.ErrorName, context)
            if isinstance(err_name, str):
                import builtins
                err_type = getattr(builtins, err_name, Exception)
            elif isinstance(err_name, type) and issubclass(err_name, BaseException):
                err_type = err_name
            else:
                err_type = Exception 

            raise err_type(err_text)
        elif isinstance(node, ListContains):
            return self.evaluate(node.List, context).count(self.evaluate(node.Element, context)) > 0
        elif isinstance(node, StringContains):
            return self.evaluate(node.Text, context).find(self.evaluate(node.Substring, context)) > -1
        elif isinstance(node, StringReplace):
            text = self.evaluate(node.Text, context)
            old_substring = self.evaluate(node.OldSubstring, context)
            new_substring = self.evaluate(node.NewSubstring, context)
            if not isinstance(text, str):
                raise TypeError("StringReplace Text must evaluate to a string")
            if not isinstance(old_substring, str):
                raise TypeError("StringReplace OldSubstring must evaluate to a string")
            if not isinstance(new_substring, str):
                raise TypeError("StringReplace NewSubstring must evaluate to a string")
            return text.replace(old_substring, new_substring)
        elif isinstance(node, TypeOf):
            value = self.evaluate(node.Value, context)
            return type(value).__name__
        elif isinstance(node, IsType):
            value = self.evaluate(node.Value, context)
            type_name = self.evaluate(node.Type, context)
            if isinstance(type_name, str):
                type_name = type_name.lower()
                if type_name in ['str', 'string']:
                    return isinstance(value, str)
                elif type_name in ['int', 'integer']:
                    return isinstance(value, int)
                elif type_name in ['float', 'number']:
                    return isinstance(value, (int, float))
                elif type_name in ['bool', 'boolean']:
                    return isinstance(value, bool)
                elif type_name in ['list']:
                    return isinstance(value, list)
                elif type_name in ['dict', 'dictionary']:
                    return isinstance(value, dict)
                elif type_name in ['tuple']:
                    return isinstance(value, tuple)
                elif type_name in ['none', 'null']:
                    return value is None
                else:
                    import builtins
                    try:
                        actual_type = getattr(builtins, type_name)
                        return isinstance(value, actual_type)
                    except AttributeError:
                        return False
            else:
                return isinstance(value, type_name)
                # Find the FormattedString evaluation and replace it with:
        elif isinstance(node, FormattedString):
            format_string = self.evaluate(node.FormatString, context)

            if hasattr(node.Args, 'Lst'): 
                args = [self.evaluate(arg, context) for arg in node.Args.Lst]
            elif isinstance(node.Args, list):
                args = [self.evaluate(arg, context) for arg in node.Args]
            else:
                args = [self.evaluate(node.Args, context)]
            
            if not isinstance(format_string, str):
                raise TypeError("FormattedString FormatString must evaluate to a string")
            return format_string.format(*args)
        elif isinstance(node, DefineClass):
            class_name = node.Name
            base_class = self.evaluate(node.Base, context) if not isinstance(node.Base, ObjNONE) else None
            
            class_def = {
                'type': 'class',
                'name': class_name,
                'methods': {},
                'properties': {},
                'constructor': None,
                'parent': base_class
            }
            
            for stmt in node.Body:
                if isinstance(stmt, DefineFunction):
                    if stmt.Name == '__init__':
                        class_def['constructor'] = {
                            'params': stmt.Param,
                            'body': stmt.Body
                        }
                    else:
                        class_def['methods'][stmt.Name] = {
                            'params': stmt.Param,
                            'body': stmt.Body
                        }
                elif isinstance(stmt, Assignment):
                    class_def['properties'][stmt.Name] = self.evaluate(stmt.Val, context)
            
            if base_class and base_class in context:
                parent_class = context[base_class]
                if isinstance(parent_class, dict) and parent_class.get('type') == 'class':
                    inherited_methods = parent_class.get('methods', {}).copy()
                    inherited_properties = parent_class.get('properties', {}).copy()
                    
                    inherited_methods.update(class_def['methods'])
                    inherited_properties.update(class_def['properties'])
                    
                    class_def['methods'] = inherited_methods
                    class_def['properties'] = inherited_properties
                    
                    if not class_def['constructor'] and parent_class.get('constructor'):
                        class_def['constructor'] = parent_class['constructor']
            
            # Store the class in context
            context[class_name] = class_def
            return class_def
        elif isinstance(node, NewInstance):
            class_name = node.ClassName
            class_def = context.get(class_name)
            
            if not class_def:
                raise NameError(f"Class '{class_name}' is not defined")
            
            if not isinstance(class_def, dict) or class_def.get('type') != 'class':
                raise TypeError(f"'{class_name}' is not a class")
            
            instance = {
                'class': class_name,
                'properties': class_def['properties'].copy()
            }
            
            for prop_name, prop_value in class_def['properties'].items():
                instance[prop_name] = prop_value
            
            if 'constructor' in class_def and class_def['constructor']:
                local_context = context.copy()
                local_context['self'] = instance
                
                constructor = class_def['constructor']
                
                if hasattr(node.Args, 'Lst'):
                    args_list = node.Args.Lst
                elif isinstance(node.Args, list):
                    args_list = node.Args
                else:
                    args_list = [node.Args] if node.Args else []
                
                constructor_params = constructor.get('params', [])
                
                expected_params = constructor_params[:]
                if expected_params and expected_params[0] == 'self':
                    expected_params = expected_params[1:]
                
                if len(args_list) != len(expected_params):
                    raise ValueError(f"Constructor expects {len(expected_params)} arguments, got {len(args_list)}")

                params_to_bind = constructor_params[:]
                if params_to_bind and params_to_bind[0] == 'self':
                    params_to_bind = params_to_bind[1:]
                    
                for param, arg in zip(params_to_bind, args_list):
                    local_context[param] = self.evaluate(arg, context)
                
                for stmt in constructor.get('body', []):
                    self.evaluate(stmt, local_context)
                    
                if 'self' in local_context:
                    instance.update(local_context['self'])
            
            return instance
        elif isinstance(node, MethodCall):
            obj = self.evaluate(node.Obj, context)
            method_name = node.MethodName
            
            if not isinstance(obj, dict) or 'class' not in obj:
                raise TypeError("MethodCall requires an object instance")
            
            class_name = obj['class']
            class_def = context.get(class_name)
            
            if not class_def:
                raise NameError(f"Class '{class_name}' is not defined")
            if method_name not in class_def['methods']:
                raise AttributeError(f"'{class_name}' object has no method '{method_name}'")
        
            method = class_def['methods'][method_name]
            local_context = context.copy()
            local_context['self'] = obj
            params = method.get('params', [])
            if params and params[0] == 'self':
                params = params[1:]
            if hasattr(node.Args, 'Lst'):
                args_list = node.Args.Lst
            elif isinstance(node.Args, list):
                args_list = node.Args
            else:
                args_list = [node.Args] if node.Args else []
            
            if len(args_list) != len(params):
                raise ValueError(f"Method '{method_name}' expects {len(params)} arguments, got {len(args_list)}")
            
            for param, arg in zip(params, args_list):
                local_context[param] = self.evaluate(arg, context)
            
            result = None
            for stmt in method.get('body', []):
                result = self.evaluate(stmt, local_context)
                if isinstance(stmt, Return):
                    break
            
            return result
        elif isinstance(node, GetAttr):
            obj = self.evaluate(node.Obj, context)
            return obj.get(node.Attr, None)
        elif isinstance(node, SetAttr):
            obj = self.evaluate(node.Obj, context)
            val = self.evaluate(node.Value, context)
            obj[node.Attr] = val
            return val
        elif isinstance(node, Floor):
            v = self.evaluate(node.Value, context)
            return math.floor(v)
        elif isinstance(node, Ceil):
            v = self.evaluate(node.Value, context)
            return math.ceil(v)
        elif isinstance(node, Sqrt):
            v = self.evaluate(node.Value, context)
            return math.sqrt(v)
        elif isinstance(node, Log):
            v = self.evaluate(node.Value, context)
            if isinstance(node.Base, ObjNONE):
                return math.log(v)
            else:
                base = self.evaluate(node.Base, context)
                return math.log(v, base)
        elif isinstance(node, Exp):
            v = self.evaluate(node.Value, context)
            return math.exp(v)
        elif isinstance(node, Sin):
            v = self.evaluate(node.Value, context)
            return math.sin(v)
        elif isinstance(node, Cos):
            v = self.evaluate(node.Value, context)
            return math.cos(v)
        elif isinstance(node, Tan):
            v = self.evaluate(node.Value, context)
            return math.tan(v)
        elif isinstance(node, Mod):
            value = self.evaluate(node.Value, context)
            divisor = self.evaluate(node.Divisor, context)
            return math.fmod(value, divisor)
        elif isinstance(node, MathConstants):
            const = self.evaluate(node.Constant, context)
            if const.lower() == 'pi':
                return math.pi
            elif const.lower() == 'e':
                return math.e
            elif const.lower() == 'tau':
                return math.tau
            elif const.lower() == 'inf':
                return math.inf
            else:
                raise ValueError(f"Unknown math constant: {const}")
        elif isinstance(node, Clamp):
            value = self.evaluate(node.Value, context)
            min_val = self.evaluate(node.Min, context)
            max_val = self.evaluate(node.Max, context)
            if not isinstance(value, (int, float)) or not isinstance(min_val, (int, float)) or not isinstance(max_val, (int, float)):
                raise TypeError("Clamp requires numeric values")
            return max(min_val, min(value, max_val))   
        elif isinstance(node, DeepCopy):
            import copy
            value = self.evaluate(node.Value, context)
            return copy.deepcopy(value)         
        elif isinstance(node, HashValue):
            value = self.evaluate(node.Value, context)
            try:
                return hash(value)
            except TypeError:
                return hash(str(value))                
        elif isinstance(node, BaseConvert):
            number = self.evaluate(node.Number, context)
            from_base = self.evaluate(node.FromBase, context)
            to_base = self.evaluate(node.ToBase, context)
            
            if not isinstance(from_base, int) or not isinstance(to_base, int):
                raise TypeError("BaseConvert bases must be integers")
            if from_base < 2 or from_base > 36 or to_base < 2 or to_base > 36:
                raise ValueError("BaseConvert bases must be between 2 and 36")

            if isinstance(number, str):
                try:
                    decimal = int(number, from_base)
                except ValueError:
                    raise ValueError(f"Invalid number '{number}' for base {from_base}")
            else:
                decimal = int(number)
            if to_base == 10:
                return decimal
            elif to_base == 2:
                return bin(decimal)[2:]
            elif to_base == 8:
                return oct(decimal)[2:]  
            elif to_base == 16:
                return hex(decimal)[2:]
            else:
                if decimal == 0:
                    return "0"
                digits = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
                result = ""
                negative = decimal < 0
                decimal = abs(decimal)
                while decimal > 0:
                    result = digits[decimal % to_base] + result
                    decimal //= to_base
                return ("-" if negative else "") + result
        elif isinstance(node, Ord):
            return ord(self.evaluate(node.Str, context))
        elif isinstance(node, Chr):
            return chr(self.evaluate(node.Str, context))
        elif isinstance(node, FileRead):
            filepath = self.evaluate(node.FilePath, context)
            mode = self.evaluate(node.Mode, context)
            encoding = self.evaluate(node.Encoding, context)
            
            if not isinstance(filepath, str):
                raise TypeError("FileRead FilePath must be a string")
            if not isinstance(mode, str):
                raise TypeError("FileRead Mode must be a string")
            if not isinstance(encoding, str):
                raise TypeError("FileRead Encoding must be a string")
                
            try:
                with open(filepath, mode, encoding=encoding) as f:
                    return f.read()
            except FileNotFoundError:
                raise FileNotFoundError(f"File '{filepath}' not found")
            except PermissionError:
                raise PermissionError(f"Permission denied accessing '{filepath}'")
            except Exception as e:
                raise Exception(f"Error reading file '{filepath}': {str(e)}")
        elif isinstance(node, FileWrite):
            filepath = self.evaluate(node.FilePath, context)
            content = self.evaluate(node.Content, context)
            mode = self.evaluate(node.Mode, context)
            encoding = self.evaluate(node.Encoding, context)
            
            if not isinstance(filepath, str):
                raise TypeError("FileWrite FilePath must be a string")
            if not isinstance(mode, str):
                raise TypeError("FileWrite Mode must be a string")
            if not isinstance(encoding, str):
                raise TypeError("FileWrite Encoding must be a string")
                
            try:
                with open(filepath, mode, encoding=encoding) as f:
                    f.write(str(content))
                    f.close()
                return f"Successfully wrote to '{filepath}' with '{content}'"
            except PermissionError:
                raise PermissionError(f"Permission denied writing to '{filepath}'")
            except Exception as e:
                raise Exception(f"Error writing to file '{filepath}': {str(e)}")                               
        elif isinstance(node, FileDelete):
            filepath = self.evaluate(node.FilePath, context)
            if not isinstance(filepath, str):
                raise TypeError("FileDelete FilePath must be a string")
            try:
                import os
                if os.path.exists(filepath):
                    os.remove(filepath)
                    return f"Successfully deleted '{filepath}'"
                else:
                    raise FileNotFoundError(f"File '{filepath}' not found")
            except PermissionError:
                raise PermissionError(f"Permission denied deleting '{filepath}'")
            except Exception as e:
                raise Exception(f"Error deleting file '{filepath}': {str(e)}")                
        elif isinstance(node, FileSize):
            filepath = self.evaluate(node.FilePath, context)
            if not isinstance(filepath, str):
                raise TypeError("FileSize FilePath must be a string")
            try:
                import os
                if os.path.exists(filepath):
                    return os.path.getsize(filepath)
                else:
                    raise FileNotFoundError(f"File '{filepath}' not found")
            except Exception as e:
                raise Exception(f"Error getting size of file '{filepath}': {str(e)}")               
        elif isinstance(node, ListFiles):
            dirpath = self.evaluate(node.DirectoryPath, context)
            pattern = self.evaluate(node.Pattern, context)
            
            if not isinstance(dirpath, str):
                raise TypeError("ListFiles DirectoryPath must be a string")
            if not isinstance(pattern, str):
                raise TypeError("ListFiles Pattern must be a string")
                
            try:
                import os
                import glob
                if not os.path.exists(dirpath):
                    raise FileNotFoundError(f"Directory '{dirpath}' not found")
                if not os.path.isdir(dirpath):
                    raise NotADirectoryError(f"'{dirpath}' is not a directory")
                    
                search_pattern = os.path.join(dirpath, pattern)
                files = glob.glob(search_pattern)
                return [os.path.basename(f) for f in files if os.path.isfile(f)]
            except Exception as e:
                raise Exception(f"Error listing files in '{dirpath}': {str(e)}")
        elif isinstance(node, Lambda):
            def lambda_func(*args):
                local_context = context.copy()

                if len(args) != len(node.Parameters):
                    raise ValueError(f"Lambda expects {len(node.Parameters)} arguments, got {len(args)}")
                
                for param, arg in zip(node.Parameters, args):
                    local_context[param] = arg
                return self.evaluate(node.Body, local_context)
            
            return lambda_func      
        elif isinstance(node, MapFunction):
            func = self.evaluate(node.Function, context)
            iterable = self.evaluate(node.Iterable, context)
            
            if not hasattr(iterable, '__iter__'):
                raise TypeError("MapFunction Iterable must be iterable")
            
            result = []
            for item in iterable:
                if callable(func):
                    result.append(func(item))
                elif isinstance(func, str):
                    func_def = context.get(func)
                    if isinstance(func_def, DefineFunction):
                        local_context = context.copy()
                        if len(func_def.Param) != 1:
                            raise ValueError(f"MapFunction expects function with 1 parameter, got {len(func_def.Param)}")
                        local_context[func_def.Param[0]] = item
                        func_result = None
                        for stmt in func_def.Body:
                            func_result = self.evaluate(stmt, local_context)
                            if isinstance(stmt, Return):
                                break
                        result.append(func_result)
                    else:
                        raise NameError(f"Function '{func}' is not defined")
                else:
                    raise TypeError("MapFunction Function must be callable or function name")

            return result 
        elif isinstance(node, FilterFunction):
            func = self.evaluate(node.Function, context)
            iterable = self.evaluate(node.Iterable, context)
            
            if not hasattr(iterable, '__iter__'):
                raise TypeError("FilterFunction Iterable must be iterable")
            
            result = []
            for item in iterable:
                should_include = False
                if callable(func):
                    should_include = func(item)
                elif isinstance(func, str):
                    func_def = context.get(func)
                    if isinstance(func_def, DefineFunction):
                        local_context = context.copy()
                        if len(func_def.Param) != 1:
                            raise ValueError(f"FilterFunction expects function with 1 parameter, got {len(func_def.Param)}")
                        local_context[func_def.Param[0]] = item
                        func_result = None
                        for stmt in func_def.Body:
                            func_result = self.evaluate(stmt, local_context)
                            if isinstance(stmt, Return):
                                break
                        should_include = func_result
                    else:
                        raise NameError(f"Function '{func}' is not defined")
                else:
                    raise TypeError("FilterFunction Function must be callable or function name")
                
                if should_include:
                    result.append(item)
            
            return result
        elif isinstance(node, ReduceFunction):
            func = self.evaluate(node.Function, context)
            iterable = self.evaluate(node.Iterable, context)
            
            if not hasattr(iterable, '__iter__'):
                raise TypeError("ReduceFunction Iterable must be iterable")
            
            items = list(iterable)
            if not items:
                if isinstance(node.InitialValue, ObjNONE):
                    raise ValueError("ReduceFunction of empty sequence with no initial value")
                return self.evaluate(node.InitialValue, context)
            if isinstance(node.InitialValue, ObjNONE):
                accumulator = items[0]
                items = items[1:]
            else:
                accumulator = self.evaluate(node.InitialValue, context)

            for item in items:
                if callable(func):
                    accumulator = func(accumulator, item)
                elif isinstance(func, str):
                    func_def = context.get(func)
                    if isinstance(func_def, DefineFunction):
                        local_context = context.copy()
                        if len(func_def.Param) != 2:
                            raise ValueError(f"ReduceFunction expects function with 2 parameters, got {len(func_def.Param)}")
                        local_context[func_def.Param[0]] = accumulator
                        local_context[func_def.Param[1]] = item
                        func_result = None
                        for stmt in func_def.Body:
                            func_result = self.evaluate(stmt, local_context)
                            if isinstance(stmt, Return):
                                break
                        accumulator = func_result
                    else:
                        raise NameError(f"Function '{func}' is not defined")
                else:
                    raise TypeError("ReduceFunction Function must be callable or function name")
            
            return accumulator
        elif isinstance(node, SuperClass):
            child_name = self.evaluate(node.ChildClassName, context)
            parent_name = self.evaluate(node.ParentClassName, context)
            
            if not isinstance(child_name, str) or not isinstance(parent_name, str):
                raise TypeError("SuperClass names must be strings")

            if parent_name not in context:
                raise NameError(f"Parent class '{parent_name}' is not defined")
            
            parent_class = context[parent_name]
            if not isinstance(parent_class, dict) or 'type' not in parent_class or parent_class['type'] != 'class':
                raise TypeError(f"'{parent_name}' is not a class")

            child_class = {
                'type': 'class',
                'parent': parent_name,
                'methods': parent_class['methods'].copy(),
                'properties': parent_class['properties'].copy(),
                'constructor': parent_class.get('constructor', []) 
            }
            
            additional_methods = self.evaluate(node.Methods, context)
            if isinstance(additional_methods, list):
                for method in additional_methods:
                    if isinstance(method, tuple) and len(method) == 2:
                        method_name, method_def = method
                        child_class['methods'][method_name] = method_def
            
            additional_props = self.evaluate(node.Properties, context)
            if isinstance(additional_props, list):
                for prop in additional_props:
                    if isinstance(prop, tuple) and len(prop) == 2:
                        prop_name, prop_value = prop
                        child_class['properties'][prop_name] = prop_value
            
            context[child_name] = child_class
            return f"Class '{child_name}' inherits from '{parent_name}'"
        elif isinstance(node, Super):
            method_name = self.evaluate(node.MethodName, context)
            args = self.evaluate(node.Args, context)
            if 'self' not in context:
                raise RuntimeError("Super() can only be called within a method")
            
            current_object = context['self']
            if 'class' not in current_object:
                raise RuntimeError("Current object has no class information")
            
            current_class_name = current_object['class']
            current_class = context[current_class_name]
            
            if 'parent' not in current_class:
                raise RuntimeError(f"Class '{current_class_name}' has no parent class")
            
            parent_class_name = current_class['parent']
            parent_class = context[parent_class_name]
            
            # call the parent method
            if method_name not in parent_class['methods']:
                raise AttributeError(f"Parent class '{parent_class_name}' has no method '{method_name}'")
            
            parent_method = parent_class['methods'][method_name]
            
            local_context = context.copy()
            local_context['self'] = current_object
            
            if len(args) != len(parent_method['params']):
                raise ValueError(f"Method '{method_name}' expects {len(parent_method['params'])} arguments, got {len(args)}")
            
            for param, arg in zip(parent_method['params'], args):
                local_context[param] = arg
            result = None
            for stmt in parent_method['body']:
                result = self.evaluate(stmt, local_context)
                if isinstance(stmt, Return):
                    break
            
            return result
        elif isinstance(node, IsInstanceOf):
            obj = self.evaluate(node.Object, context)
            class_name = self.evaluate(node.ClassName, context)
            
            if not isinstance(class_name, str):
                raise TypeError("ClassName must be a string")
            if not isinstance(obj, dict) or 'class' not in obj:
                return False
            if obj['class'] == class_name:
                return True
            current_class = context.get(obj['class'])
            while current_class and 'parent' in current_class:
                if current_class['parent'] == class_name:
                    return True
                current_class = context.get(current_class['parent'])
            
            return False
        elif isinstance(node, EvalExpression):
            expression = self.evaluate(node.Expression, context)
            globals_dict = self.evaluate(node.Globals, context) if not isinstance(node.Globals, ObjNONE) else globals()
            locals_dict = self.evaluate(node.Locals, context) if not isinstance(node.Locals, ObjNONE) else context
            
            if not isinstance(expression, str):
                raise TypeError("EvalExpression requires a string expression")
            
            try:
                return eval(expression, globals_dict, locals_dict)
            except Exception as e:
                raise Exception(f"Error evaluating expression '{expression}': {str(e)}")
        elif isinstance(node, ExecCode):
            code = self.evaluate(node.Code, context)
            globals_dict = self.evaluate(node.Globals, context) if not isinstance(node.Globals, ObjNONE) else globals()
            locals_dict = self.evaluate(node.Locals, context) if not isinstance(node.Locals, ObjNONE) else context
            
            if not isinstance(code, str):
                raise TypeError("ExecCode requires a string code")
            
            try:
                exec(code, globals_dict, locals_dict)
                if locals_dict is context:
                    context.update(locals_dict)
                return None
            except Exception as e:
                raise Exception(f"Error executing code: {str(e)}")
        elif isinstance(node, CallFunction):
            func_name = self.evaluate(node.FunctionName, context)
            args = self.evaluate(node.Args, context)
            kwargs = self.evaluate(node.Kwargs, context)
            
            # Retrieve appropriate function name to be refreneced by intepreter
            if callable(func_name):
                func = func_name
            elif isinstance(func_name, str) and func_name in context:
                func = context[func_name]
            elif isinstance(func_name, str):
                try:
                    func = eval(func_name, globals())
                except:
                    raise NameError(f"Function '{func_name}' not found")
            else:
                raise NameError(f"Function '{func_name}' not found")
            
            if not callable(func):
                raise TypeError(f"'{func_name}' is not callable")
            
            try:
                if isinstance(args, list) and isinstance(kwargs, dict):
                    return func(*args, **kwargs)
                elif isinstance(args, list):
                    return func(*args)
                else:
                    return func()
            except Exception as e:
                raise Exception(f"Error calling function '{func_name}': {str(e)}")
        elif isinstance(node, Sort):
            lst = self.evaluate(node.List, context)
            reverse = self.evaluate(node.Reverse, context)
            key_func = self.evaluate(node.Key, context) if not isinstance(node.Key, ObjNONE) else None
            
            if not isinstance(lst, list):
                raise TypeError("Sort expects a list")
            
            if key_func:
                if callable(key_func):
                    return sorted(lst, key=key_func, reverse=reverse)
                elif isinstance(key_func, str):
                    try:
                        key_func = eval(key_func, globals())
                        return sorted(lst, key=key_func, reverse=reverse)
                    except:
                        raise ValueError(f"Invalid key function: {key_func}")
            else:
                return sorted(lst, reverse=reverse)
        elif isinstance(node, Zip):
            lists = [self.evaluate(lst, context) for lst in node.Lists]
            return list(zip(*lists))
        elif isinstance(node, Shuffle):
            import random
            lst = self.evaluate(node.List, context).copy()
            random.shuffle(lst)
            return lst
        elif isinstance(node, Sample):
            import random
            lst = self.evaluate(node.List, context)
            count = self.evaluate(node.Count, context)
            return random.sample(lst, count)
        elif isinstance(node, Flatten):
            lst = self.evaluate(node.List, context)
            depth = self.evaluate(node.Depth, context)
            
            def flatten_list(l, d):
                if d <= 0:
                    return l
                result = []
                for item in l:
                    if isinstance(item, list):
                        result.extend(flatten_list(item, d-1))
                    else:
                        result.append(item)
                return result
            
            return flatten_list(lst, depth)
        elif isinstance(node, SetAssignment):
            return set(self.evaluate(elem, context) for elem in node.Elements)        
        elif isinstance(node, SetOperations):
            set1 = self.evaluate(node.Set1, context)
            set2 = self.evaluate(node.Set2, context)
            
            if not isinstance(set1, set) or not isinstance(set2, set):
                raise TypeError("SetOperations requires set arguments")
            
            if node.Operation == 'union':
                return set1.union(set2)
            elif node.Operation == 'intersection':
                return set1.intersection(set2)
            elif node.Operation == 'difference':
                return set1.difference(set2)
            elif node.Operation == 'symmetric_difference':
                return set1.symmetric_difference(set2)
            else:
                raise ValueError(f"Unknown set operation: {node.Operation}") 
        elif isinstance(node, SetMethods):
            set_var = self.evaluate(node.SetVar, context)
            if not isinstance(set_var, set):
                raise TypeError("SetMethods requires a set")
            
            if node.Method == 'add':
                element = self.evaluate(node.Element, context)
                set_var.add(element)
                return set_var
            elif node.Method == 'remove':
                element = self.evaluate(node.Element, context)
                set_var.remove(element)
                return set_var
            elif node.Method == 'discard':
                element = self.evaluate(node.Element, context)
                set_var.discard(element)
                return set_var
            elif node.Method == 'clear':
                set_var.clear()
                return set_var
            elif node.Method == 'copy':
                return set_var.copy()
            else:
                raise ValueError(f"Unknown set method: {node.Method}")
        elif isinstance(node, SetContains):
            set_val = self.evaluate(node.Set, context)
            element = self.evaluate(node.Element, context)
            return element in set_val
        elif isinstance(node, DateTime):
            from datetime import datetime
            
            year = self.evaluate(node.Year, context) if not isinstance(node.Year, ObjNONE) else datetime.now().year
            month = self.evaluate(node.Month, context) if not isinstance(node.Month, ObjNONE) else datetime.now().month
            day = self.evaluate(node.Day, context) if not isinstance(node.Day, ObjNONE) else datetime.now().day
            hour = self.evaluate(node.Hour, context)
            minute = self.evaluate(node.Minute, context)
            second = self.evaluate(node.Second, context)
            
            return datetime(year, month, day, hour, minute, second)
        elif isinstance(node, DateTimeNow):
            from datetime import datetime
            return datetime.now()
        elif isinstance(node, Statistics):
            data = self.evaluate(node.Data, context)
            operation = node.Operation
            
            if not isinstance(data, list) or not all(isinstance(x, (int, float)) for x in data):
                raise TypeError("Statistics requires a list of numbers")
            
            if not data:
                raise ValueError("Statistics requires non-empty data")
            
            if operation == 'variance':
                mean = sum(data) / len(data)
                return sum((x - mean) ** 2 for x in data) / len(data)
            elif operation == 'stdev':
                mean = sum(data) / len(data)
                variance = sum((x - mean) ** 2 for x in data) / len(data)
                return variance ** 0.5
            elif operation == 'correlation':
                if len(data) != 2 or not isinstance(data[0], list) or not isinstance(data[1], list):
                    raise ValueError("Correlation requires two lists of data")
                x_data, y_data = data
                if len(x_data) != len(y_data):
                    raise ValueError("Correlation requires equal length data sets")
                
                n = len(x_data)
                mean_x = sum(x_data) / n
                mean_y = sum(y_data) / n
                
                numerator = sum((x_data[i] - mean_x) * (y_data[i] - mean_y) for i in range(n))
                denominator_x = sum((x - mean_x) ** 2 for x in x_data) ** 0.5
                denominator_y = sum((y - mean_y) ** 2 for y in y_data) ** 0.5
                
                if denominator_x == 0 or denominator_y == 0:
                    return 0
                
                return numerator / (denominator_x * denominator_y)
            else:
                raise ValueError(f"Unknown statistics operation: {operation}")
        elif isinstance(node, Matrix):
            rows = self.evaluate(node.Rows, context)
            if not isinstance(rows, list) or not all(isinstance(row, list) for row in rows):
                raise TypeError("Matrix requires a list of lists")
            return rows
        elif isinstance(node, LinearAlgebra):
            matrix1 = self.evaluate(node.Matrix1, context)
            matrix2 = self.evaluate(node.Matrix2, context) if not isinstance(node.Matrix2, ObjNONE) else None
            operation = self.evaluate(node.Operation, context)
            
            if operation == 'transpose':
                if not isinstance(matrix1, list) or not all(isinstance(row, list) for row in matrix1):
                    raise TypeError("Transpose requires a matrix (list of lists)")
                return [[matrix1[j][i] for j in range(len(matrix1))] for i in range(len(matrix1[0]))]
            
            elif operation == 'multiply':
                if matrix2 is None:
                    raise ValueError("Matrix multiplication requires two matrices")
                
                # Matrix multiplication
                if len(matrix1[0]) != len(matrix2):
                    raise ValueError("Matrix dimensions incompatible for multiplication")
                
                result = []
                for i in range(len(matrix1)):
                    row = []
                    for j in range(len(matrix2[0])):
                        sum_val = 0
                        for k in range(len(matrix2)):
                            sum_val += matrix1[i][k] * matrix2[k][j]
                        row.append(sum_val)
                    result.append(row)
                return result
            
            elif operation == 'determinant':
                if len(matrix1) != len(matrix1[0]):
                    raise ValueError("Determinant requires a square matrix")
                
                def det(matrix):
                    if len(matrix) == 1:
                        return matrix[0][0]
                    if len(matrix) == 2:
                        return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]
                    
                    result = 0
                    for i in range(len(matrix)):
                        minor = [row[:i] + row[i+1:] for row in matrix[1:]]
                        result += ((-1) ** i) * matrix[0][i] * det(minor)
                    return result
                
                return det(matrix1)
            
            else:
                raise ValueError(f"Unknown linear algebra operation: {operation}")
        elif isinstance(node, Percentile):
            data = self.evaluate(node.Data, context)
            percentage = self.evaluate(node.Percentage, context)
            
            if not isinstance(data, list) or not all(isinstance(x, (int, float)) for x in data):
                raise TypeError("Percentile requires a list of numbers")
            
            sorted_data = sorted(data)
            k = (len(sorted_data) - 1) * (percentage / 100)
            f = math.floor(k)
            c = math.ceil(k)
            
            if f == c:
                return sorted_data[int(k)]
            
            return sorted_data[int(f)] * (c - k) + sorted_data[int(c)] * (k - f)
        elif isinstance(node, Assert):
            condition = self.evaluate(node.Condition, context)
            message = self.evaluate(node.Message, context)
            
            if not condition:
                raise AssertionError(message)
            return True
        elif isinstance(node, WarningRaise):
            import warnings
            message = self.evaluate(node.Message, context)
            category = self.evaluate(node.Category, context)
            
            if category == 'UserWarning':
                warnings.warn(message, UserWarning)
            elif category == 'DeprecationWarning':
                warnings.warn(message, DeprecationWarning)
            elif category == 'RuntimeWarning':
                warnings.warn(message, RuntimeWarning)
            else:
                warnings.warn(message)
            
            return None
        elif isinstance(node, CustomError):
            name = self.evaluate(node.Name, context)
            base_error = self.evaluate(node.BaseError, context)
            base_class = eval(base_error) if isinstance(base_error, str) else Exception
            
            custom_exception = type(name, (base_class,), {})
            context[name] = custom_exception
            
            return f"Custom error '{name}' created"

            try:
                import pygame
            except ImportError:
                raise ImportError("pygame is required for graphics functions. Install with: pip install pygame")
            filepath = self.evaluate(node.FilePath, context)
            volume = self.evaluate(node.Volume, context)
            
            try:
                sound = pygame.mixer.Sound(filepath)
                sound.set_volume(volume)
                sound.play()
                return f"Sound '{filepath}' played"
            except pygame.error as e:
                raise Exception(f"Could not play sound '{filepath}': {str(e)}")
        elif isinstance(node, InspectCode):
            import sys
            obj = self.evaluate(node.Object, context)
            property_name = self.evaluate(node.Property, context)
            
            if property_name == 'type':
                return type(obj).__name__
            elif property_name == 'methods':
                if hasattr(obj, '__dict__'):
                    methods = [attr for attr in dir(obj) if callable(getattr(obj, attr, None))]
                    return methods
                elif isinstance(obj, dict) and obj.get('type') == 'class':
                    return list(obj.get('methods', {}).keys())
                else:
                    return [attr for attr in dir(obj) if callable(getattr(obj, attr, None))]
            elif property_name == 'attributes':
                if hasattr(obj, '__dict__'):
                    return list(obj.__dict__.keys())
                elif isinstance(obj, dict):
                    return list(obj.keys())
                else:
                    return [attr for attr in dir(obj) if not callable(getattr(obj, attr, None))]
            elif property_name == 'source':
                import inspect
                try:
                    if callable(obj):
                        return inspect.getsource(obj)
                    else:
                        return f"Source not available for {type(obj).__name__}"
                except:
                    return "Source code not available"
            elif property_name == 'size':
                import sys
                return sys.getsizeof(obj)
            elif property_name == 'module':
                return getattr(obj, '__module__', 'unknown')
            elif property_name == 'doc':
                return getattr(obj, '__doc__', 'No documentation available')
            elif property_name == 'all':
                result = {
                    'type': type(obj).__name__,
                    'size': sys.getsizeof(obj),
                    'module': getattr(obj, '__module__', 'unknown'),
                    'doc': getattr(obj, '__doc__', 'No documentation')
                }
                if hasattr(obj, '__dict__'):
                    result['attributes'] = list(obj.__dict__.keys())
                    result['methods'] = [attr for attr in dir(obj) if callable(getattr(obj, attr, None))]
                return result
            else:
                raise ValueError(f"Unknown property: {property_name}")
        elif isinstance(node, Debugger):
            code = self.evaluate(node.Code, context)
            breakpoints = self.evaluate(node.Breakpoints, context)
            
            print(f"DEBUG MODE: Starting execution with {len(breakpoints)} breakpoints")

            debug_info = {
                'breakpoints': breakpoints,
                'current_line': 0,
                'variables': {},
                'call_stack': []
            }
            context['__debug_info__'] = debug_info
            
            def debug_evaluate(node, ctx, line_num=0):
                debug_info['current_line'] = line_num
                debug_info['variables'] = {k: v for k, v in ctx.items() if not k.startswith('__')}

                if line_num in breakpoints:
                    print(f"\nBREAKPOINT HIT at line {line_num}")
                    print(f"Current variables: {debug_info['variables']}")
                    print(f"Call Stack depth: {len(debug_info['call_stack'])}")
                    while True:
                        cmd = input("Debug> (c)ontinue, (s)tep, (v)ariables, (st)ack, (q)uit: ").strip().lower()
                        if cmd in ['c', 'continue']:
                            break
                        elif cmd in ['s', 'step']:
                            break
                        elif cmd in ['v', 'variables']:
                            for var, val in debug_info['variables'].items():
                                print(f"  {var} = {val}")
                        elif cmd in ['st', 'stack']:
                            print(f"Call stack: {debug_info['call_stack']}")
                        elif cmd in ['q', 'quit']:
                            raise KeyboardInterrupt("Debug session terminated")
                        else:
                            print("Unknown command. Use c, s, v, st, or q")
                
                return self.evaluate(node, ctx)
            
            try:
                if hasattr(code, 'ModuleCode'):
                    for i, stmt in enumerate(code.ModuleCode):
                        debug_info['call_stack'].append(f"Line {i+1}: {type(stmt).__name__}")
                        result = debug_evaluate(stmt, context, i+1)
                        debug_info['call_stack'].pop()
                else:
                    result = debug_evaluate(code, context, 1)
                
                print("Execution completed successfully")
                return result
                
            except Exception as e:
                print(f"DEBUG MODE: Exception at line {debug_info['current_line']}: {e}")
                print(f"Variables at crash: {debug_info['variables']}")
                raise
        elif isinstance(node, StackTrace):
            import inspect
            depth = self.evaluate(node.Depth, context)
            stack = inspect.stack()
            
            trace_info = []
            for i, frame in enumerate(stack[1:depth+1]):
                trace_info.append({
                    'frame': i+1,
                    'filename': frame.filename,
                    'function': frame.function,
                    'line': frame.lineno,
                    'code': frame.code_context[0].strip() if frame.code_context else 'N/A'
                })
            
            print("STACK TRACE:")
            for trace in trace_info:
                print(f"  Frame {trace['frame']}: {trace['function']}() in {trace['filename']}:{trace['line']}")
                print(f"    Code: {trace['code']}")
            
            return trace_info
        elif isinstance(node, DataStream):
            source = self.evaluate(node.Source, context)
            buffer_size = self.evaluate(node.BufferSize, context)
            
            class StreamIterator:
                def __init__(self, data, buffer_size):
                    self.data = data
                    self.buffer_size = buffer_size
                    self.position = 0
                
                def __iter__(self):
                    return self
                
                def __next__(self):
                    if isinstance(self.data, str):
                        if self.position >= len(self.data):
                            raise StopIteration
                        chunk = self.data[self.position:self.position + self.buffer_size]
                        self.position += self.buffer_size
                        return chunk
                    elif isinstance(self.data, list):
                        if self.position >= len(self.data):
                            raise StopIteration
                        chunk = self.data[self.position:self.position + self.buffer_size]
                        self.position += self.buffer_size
                        return chunk
                    elif hasattr(self.data, 'read'):  # File-like object
                        chunk = self.data.read(self.buffer_size)
                        if not chunk:
                            raise StopIteration
                        return chunk
                    else:
                        raise TypeError(f"Unsupported stream source type: {type(self.data)}")
                
                def reset(self):
                    self.position = 0
                
                def get_stats(self):
                    if isinstance(self.data, (str, list)):
                        total_size = len(self.data)
                        chunks_processed = self.position // self.buffer_size
                        progress = (self.position / total_size) * 100 if total_size > 0 else 100
                        return {
                            'total_size': total_size,
                            'position': self.position,
                            'chunks_processed': chunks_processed,
                            'progress_percent': progress,
                            'buffer_size': self.buffer_size
                        }
                    else:
                        return {
                            'position': self.position,
                            'chunks_processed': self.position // self.buffer_size,
                            'buffer_size': self.buffer_size
                        }
            
            stream = StreamIterator(source, buffer_size)
            stream_id = f"stream_{len([k for k in context.keys() if k.startswith('stream_')])}"
            context[stream_id] = stream
            
            return stream
        elif isinstance(node, StreamProcessor):
            stream = self.evaluate(node.Stream, context)
            process_function = self.evaluate(node.ProcessFunction, context)
            window_size = self.evaluate(node.WindowSize, context)
            
            if not hasattr(stream, '__iter__'):
                raise TypeError("StreamProcessor requires an iterable stream")
            
            results = []
            window = []
            
            for chunk in stream:
                if isinstance(chunk, list):
                    window.extend(chunk)
                else:
                    window.append(chunk)
                
                if len(window) >= window_size:
                    current_window = window[:window_size]
                    
                    if isinstance(process_function, str):
                        if process_function == 'sum':
                            processed = sum(current_window)
                        elif process_function == 'avg':
                            if all(isinstance(x, (int, float)) for x in current_window):
                                processed = sum(current_window) / len(current_window)
                            else:
                                raise TypeError("Average requires numeric values")
                        elif process_function == 'max':
                            processed = max(current_window)
                        elif process_function == 'min':
                            processed = min(current_window)
                        elif process_function == 'count':
                            processed = len(current_window)
                        else:
                            func_def = context.get(process_function)
                            if isinstance(func_def, DefineFunction):
                                local_context = context.copy()
                                if len(func_def.Param) != 1:
                                    raise ValueError("Stream processing function must take 1 parameter")
                                local_context[func_def.Param[0]] = current_window
                                
                                func_result = None
                                for stmt in func_def.Body:
                                    func_result = self.evaluate(stmt, local_context)
                                    if isinstance(stmt, Return):
                                        break
                                processed = func_result
                            else:
                                raise NameError(f"Function '{process_function}' not found")
                    elif callable(process_function):
                        processed = process_function(current_window)
                    else:
                        processed = current_window
                    
                    results.append(processed)
                
                    window = window[1:]
            if window:
                if isinstance(process_function, str):
                    if process_function == 'sum':
                        processed = sum(window)
                    elif process_function == 'avg':
                        if all(isinstance(x, (int, float)) for x in window):
                            processed = sum(window) / len(window)
                        else:
                            raise TypeError("Average requires numeric values")
                    elif process_function == 'max':
                        processed = max(window)
                    elif process_function == 'min':
                        processed = min(window)
                    elif process_function == 'count':
                        processed = len(window)
                    else:
                        func_def = context.get(process_function)
                        if isinstance(func_def, DefineFunction):
                            local_context = context.copy()
                            if len(func_def.Param) != 1:
                                raise ValueError("Stream processing function must take 1 parameter")
                            local_context[func_def.Param[0]] = window
                            
                            func_result = None
                            for stmt in func_def.Body:
                                func_result = self.evaluate(stmt, local_context)
                                if isinstance(stmt, Return):
                                    break
                            processed = func_result
                        else:
                            processed = window
                elif callable(process_function):
                    processed = process_function(window)
                else:
                    processed = window
                results.append(processed)
            
            return results
        elif isinstance(node, Pipeline):
            stages = self.evaluate(node.Stages, context)
            
            if not isinstance(stages, list):
                raise TypeError("Pipeline stages must be a list")
            
            def create_pipeline(*args):
                data = args[0] if args else None
                
                for i, stage in enumerate(stages):
                    try:
                        if callable(stage):
                            data = stage(data)
                        elif isinstance(stage, str):
                            func_def = context.get(stage)
                            if isinstance(func_def, DefineFunction):
                                local_context = context.copy()
                                if len(func_def.Param) != 1:
                                    raise ValueError(f"Pipeline stage {i+1} function must take 1 parameter")
                                local_context[func_def.Param[0]] = data
                                
                                func_result = None
                                for stmt in func_def.Body:
                                    func_result = self.evaluate(stmt, local_context)
                                    if isinstance(stmt, Return):
                                        break
                                data = func_result
                            else:
                                raise NameError(f"Pipeline stage {i+1}: Function '{stage}' not found")
                        else:
                            if hasattr(stage, 'evaluate'):
                                data = self.evaluate(stage, context)
                            else:
                                raise TypeError(f"Pipeline stage {i+1}: Invalid stage type {type(stage)}")
                    
                    except Exception as e:
                        raise Exception(f"Pipeline failed at stage {i+1}: {str(e)}")
                
                return data
            
            return create_pipeline
        elif isinstance(node, ArrayUtils):
            array = self.evaluate(node.Array, context)
            operation = self.evaluate(node.Operation, context)
            args = [self.evaluate(arg, context) for arg in node.Args]
            
            if not isinstance(array, list):
                raise TypeError("ArrayUtils requires a list")
            
            if operation == 'chunk':
                chunk_size = args[0] if args else 2
                if not isinstance(chunk_size, int) or chunk_size <= 0:
                    raise ValueError("Chunk size must be a positive integer")
                return [array[i:i + chunk_size] for i in range(0, len(array), chunk_size)]
            
            elif operation == 'rotate':
                steps = args[0] if args else 1
                if not isinstance(steps, int):
                    raise ValueError("Rotation steps must be an integer")
                if len(array) == 0:
                    return array
                steps = steps % len(array)
                return array[steps:] + array[:steps]
            
            elif operation == 'interleave':
                other_array = args[0] if args else []
                if not isinstance(other_array, list):
                    raise TypeError("Interleave requires another list")
                result = []
                max_len = max(len(array), len(other_array))
                for i in range(max_len):
                    if i < len(array):
                        result.append(array[i])
                    if i < len(other_array):
                        result.append(other_array[i])
                return result
            
            elif operation == 'difference':
                other_array = args[0] if args else []
                if not isinstance(other_array, list):
                    raise TypeError("Difference requires another list")
                return [item for item in array if item not in other_array]
            
            elif operation == 'flatten':
                depth = args[0] if args else 1
                def flatten_recursive(lst, d):
                    if d <= 0:
                        return lst
                    result = []
                    for item in lst:
                        if isinstance(item, list):
                            result.extend(flatten_recursive(item, d-1))
                        else:
                            result.append(item)
                    return result
                return flatten_recursive(array, depth)
            
            else:
                raise ValueError(f"Unknown ArrayUtils operation: {operation}")
        elif isinstance(node, Find):
            collection = self.evaluate(node.Collection, context)
            predicate = self.evaluate(node.Predicate, context)
            mode = self.evaluate(node.Mode, context)
            
            if not hasattr(collection, '__iter__'):
                raise TypeError("Find requires an iterable collection")
            
            matches = []
            indices = []
            
            for i, item in enumerate(collection):
                match = False
                
                if callable(predicate):
                    match = predicate(item)
                elif isinstance(predicate, str):
                    func_def = context.get(predicate)
                    if isinstance(func_def, DefineFunction):
                        local_context = context.copy()
                        if len(func_def.Param) != 1:
                            raise ValueError("Find predicate function must take 1 parameter")
                        local_context[func_def.Param[0]] = item
                        
                        func_result = None
                        for stmt in func_def.Body:
                            func_result = self.evaluate(stmt, local_context)
                            if isinstance(stmt, Return):
                                break
                        match = bool(func_result)
                    else:
                        match = str(item) == predicate
                else:
                    match = item == predicate
                
                if match:
                    matches.append(item)
                    indices.append(i)
            
            if mode == 'first':
                return matches[0] if matches else None
            elif mode == 'last':
                return matches[-1] if matches else None
            elif mode == 'all':
                return matches
            elif mode == 'index':
                return indices[0] if indices else -1
            else:
                raise ValueError(f"Unknown Find mode: {mode}")
        elif isinstance(node, GroupBy):
            collection = self.evaluate(node.Collection, context)
            key_function = self.evaluate(node.KeyFunction, context)
            
            if not hasattr(collection, '__iter__'):
                raise TypeError("GroupBy requires an iterable collection")
            
            groups = {}
            
            for item in collection:
                if callable(key_function):
                    key = key_function(item)
                elif isinstance(key_function, str):
                    func_def = context.get(key_function)
                    if isinstance(func_def, DefineFunction):
                        local_context = context.copy()
                        if len(func_def.Param) != 1:
                            raise ValueError("GroupBy key function must take 1 parameter")
                        local_context[func_def.Param[0]] = item
                        
                        func_result = None
                        for stmt in func_def.Body:
                            func_result = self.evaluate(stmt, local_context)
                            if isinstance(stmt, Return):
                                break
                        key = func_result
                    else:
                        if hasattr(item, key_function):
                            key = getattr(item, key_function)
                        elif isinstance(item, dict):
                            key = item.get(key_function)
                        else:
                            key = str(item)
                else:
                    key = key_function
                
                if key not in groups:
                    groups[key] = []
                groups[key].append(item)
            
            return groups
        elif isinstance(node, Partition):
            collection = self.evaluate(node.Collection, context)
            predicate = self.evaluate(node.Predicate, context)
            
            if not hasattr(collection, '__iter__'):
                raise TypeError("Partition requires an iterable collection")
            
            true_items = []
            false_items = []
            
            for item in collection:
                match = False
                
                if callable(predicate):
                    match = predicate(item)
                elif isinstance(predicate, str):
                    func_def = context.get(predicate)
                    if isinstance(func_def, DefineFunction):
                        local_context = context.copy()
                        if len(func_def.Param) != 1:
                            raise ValueError("Partition predicate function must take 1 parameter")
                        local_context[func_def.Param[0]] = item
                        
                        func_result = None
                        for stmt in func_def.Body:
                            func_result = self.evaluate(stmt, local_context)
                            if isinstance(stmt, Return):
                                break
                        match = bool(func_result)
                    else:
                        match = str(item) == predicate
                else:
                    match = item == predicate
                
                if match:
                    true_items.append(item)
                else:
                    false_items.append(item)
            
            return [true_items, false_items]
        elif isinstance(node, Frequency):
            collection = self.evaluate(node.Collection, context)
            
            if not hasattr(collection, '__iter__'):
                raise TypeError("Frequency requires an iterable collection")
            
            frequency_count = {}
            for item in collection:
                frequency_count[item] = frequency_count.get(item, 0) + 1
            
            return frequency_count
        elif isinstance(node, SafeCast):
            value = self.evaluate(node.Value, context)
            target_type = self.evaluate(node.TargetType, context)
            default_value = self.evaluate(node.DefaultValue, context) if not isinstance(node.DefaultValue, ObjNONE) else None
            
            try:
                if target_type == 'int':
                    return int(value)
                elif target_type == 'float':
                    return float(value)
                elif target_type == 'str':
                    return str(value)
                elif target_type == 'bool':
                    if isinstance(value, str):
                        return value.lower() in ('true', '1', 'yes', 'on')
                    return bool(value)
                elif target_type == 'list':
                    if isinstance(value, str):
                        try:
                            import json
                            return json.loads(value)
                        except:
                            return list(value)
                    return list(value)
                else:
                    raise ValueError(f"Unknown target type: {target_type}")
            
            except (ValueError, TypeError):
                if default_value is not None:
                    return default_value
                else:
                    raise ValueError(f"Cannot cast {value} to {target_type} and no default provided")
        elif isinstance(node, RangeCheck):
            value = self.evaluate(node.Value, context)
            min_val = self.evaluate(node.Min, context) if not isinstance(node.Min, ObjNONE) else None
            max_val = self.evaluate(node.Max, context) if not isinstance(node.Max, ObjNONE) else None
            inclusive = self.evaluate(node.Inclusive, context)
            
            if not isinstance(value, (int, float)):
                raise TypeError("RangeCheck requires a numeric value")
            
            result = {
                'value': value,
                'in_range': True,
                'violations': []
            }
            
            if min_val is not None:
                if inclusive:
                    if value < min_val:
                        result['in_range'] = False
                        result['violations'].append(f"Value {value} is less than minimum {min_val}")
                else:
                    if value <= min_val:
                        result['in_range'] = False
                        result['violations'].append(f"Value {value} is less than or equal to minimum {min_val}")
            
            if max_val is not None:
                if inclusive:
                    if value > max_val:
                        result['in_range'] = False
                        result['violations'].append(f"Value {value} is greater than maximum {max_val}")
                else:
                    if value >= max_val:
                        result['in_range'] = False
                        result['violations'].append(f"Value {value} is greater than or equal to maximum {max_val}")
            
            return result
        elif isinstance(node, Calculate):
            ex = self.evaluate(node.Expression, context)
            import re
            if not re.match(r'^[0-9+\-*/.() \t\n]+$', ex):
                raise ValueError(f"Calculate: Expression contains invalid characters: {ex}")
            danpattern = ['import', 'exec', 'eval', '__', 'open', 'file']
            for pattern in danpattern:
                if pattern in ex.lower():
                    raise ValueError(f"Calculate: Dangerous pattern '{pattern}' detected")
            
            try:
                result = eval(ex, {'__builtins__': {}}, {})
                return result
            except Exception as e:
                raise ValueError(f"Calculate: Error evaluating '{ex}': {str(e)}")
        elif isinstance(node, Split):
            text = str(self.evaluate(node.Val, context))
            delimiter = self.evaluate(node.Delimiter, context)
            
            if not isinstance(text, str):
                raise TypeError("Split requires a string to split")
            if not isinstance(delimiter, str):
                raise TypeError("Split delimiter must be a string")
            
            return text.split(delimiter)
        elif isinstance(node, AugAssignment):
            name = node.Name
            val = self.evaluate(node.Value, context)
            operation = node.Operator
            if operation in ['+', '-', '*', '/']:
                evaluated_value = self.evaluate(Operation(Variable(name), operation, val), context)
            else:
                raise ValueError("AugAssignment requires a valid mathematical operator")
            context[name] = evaluated_value
            return None
        elif isinstance(node, ForceStop):
            print('An unexpected stop code was detected and is unavoidable unless caught.')
            print('Code cannot return to proper use without loss of session.')
            print('\nThis error is usually used as a fallback. If you see this, it means a developer specifically triggered this stop for the reason below:')
            print('Reason: ', self.evaluate(node.Reason, context))
            raise StopIteration('An unavoidable system class error has occured.')
        elif isinstance(node, LoadHTTPDriver):
            try:
                global requests
                import requests
                return self.evaluate(node.ReturnCode, context)
            except ModuleNotFoundError:
                raise ModuleNotFoundError("The 'requests' module is required for HTTP operations. Install with: pip install requests via cmd")
        elif isinstance(node, SendHTTPRequest):
            try:   
                method = str(self.evaluate(node.Method, context))
                url = self.evaluate(node.URL, context)
                headers = self.evaluate(node.Headers, context)
                data = self.evaluate(node.Data, context)

                if method.upper() in ['GET', 'POST', 'PUT', 'DELETE', 'PATCH', 'HEAD', 'OPTIONS']:
                    response = requests.request(method.upper(), url=url, headers=headers, data=data)
                else:
                    raise ValueError("SendHTTPRequest: Unsupported HTTP method")
                return response.text
            except ModuleNotFoundError:
                raise ModuleNotFoundError('No HTTP Driver found')
        elif isinstance(node, HTTPQueryParameters):
            print('This function has not yet been developed. Please wait in future updates for this function.')
        else:
            if node is None:
                print("[WARNING]: Evaluated node is NoneType")
                return None
            elif isinstance(node, (str, int, float, bool, list, dict, tuple)):
                return node
            else:
                global runnable
                runnable = False
                print(f"[ERROR]: Unsupported node type: {type(node)}")
                print(f"[ERROR]: Node value: {node}")
                print(f"[ERROR]: Node repr: {repr(node)}")
                raise TypeError(f"Unsupported AST node type: {type(node)}")
E = Evaluate()
def show_result(output_queue=None, qw=100):
    global entry
    root2 = tk.Tk()
    root2.title('ASTLANG OUTPUT - REAL TIME')
    root2.geometry('1000x600')

    output_label = tk.Label(root2, text='OUTPUT:', font=('Consolas', 12,'italic bold'), width=20, justify='left')
    output_label.pack()

    main_frame = tk.Frame(root2)
    main_frame.pack(expand=True, fill='both', padx=10, pady=15)

    entry = tk.Text(main_frame, font=('Consolas',12,'bold'), width=qw, height=30,
                   background="#1E1E1E", foreground="#D4D4D4", insertbackground="white", state='disabled')
    entry.pack(expand=True, fill='both')
    
    entry.tag_configure("error", foreground="#FF0000", font=('Consolas', 12, 'bold'))
    entry.tag_configure("success", foreground="#00FF00", font=('Consolas', 12, 'bold'))
    entry.tag_configure("normal", foreground="#FFFFFF", font=('Consolas', 12, 'bold'))
    entry.tag_configure("warning", foreground="#FFA500", font=('Consolas', 12, 'bold'))

    button_frame = tk.Frame(root2)
    button_frame.pack(side='bottom', fill='x', padx=5, pady=5)
    
    execution_running = {'value': True}

    def insert_colored_text(text, tag="normal"):
        entry.config(state='normal')
        entry.insert(tk.END, text, tag)
        entry.config(state='disabled')
        entry.see(tk.END)

    if output_queue is None:
        entry.insert("1.0", "")
        entry.config(state='disabled')
        root2.mainloop()
        return
    
    def update_output():
        try:
            while not output_queue.empty():
                message = output_queue.get_nowait()
                
                if isinstance(message, dict):
                    text = message.get('text', '')
                    color = message.get('color', 'normal')
                    insert_colored_text(text, color)
                elif message == "__EXECUTION_COMPLETE__":
                    insert_colored_text("\n[EXECUTION COMPLETED]\n", "success")
                    execution_running['value'] = False
                elif message == "__EXECUTION_ERROR__":
                    insert_colored_text("\n[EXECUTION ERROR]\n", "error")
                    execution_running['value'] = False
                else:
                    if any(error_keyword in str(message) for error_keyword in 
                           ["[ERROR]"]):
                        insert_colored_text(str(message), "error")
                    elif any(info_keyword in str(message) for info_keyword in 
                            ["DEBUG MODE", "Starting execution"]):
                        insert_colored_text(str(message), "normal")
                    else:
                        insert_colored_text(str(message), "normal")
                
                root2.update_idletasks()
        except queue.Empty:
            pass

        if execution_running['value']:
            root2.after(50, update_output)

    update_output()

    def on_closing():
        execution_running['value'] = False
        root2.destroy()
    
    root2.protocol("WM_DELETE_WINDOW", on_closing)
    root2.mainloop()
def show_evaluate_output(code_content):
    if not code_content:
        print("No code content received!")
        return
    
    output_queue = queue.Queue()
    
    class RealTimeStdout:
        def __init__(self, queue):
            self.queue = queue
            
        def write(self, text):
            if text:
                if any(error_keyword in str(text) for error_keyword in 
                       ["FATAL ERROR AT"]):
                    self.queue.put({'text': text, 'color': 'error'})
                elif any(warning_keyword in str(text) for warning_keyword in 
                        ["WARNING", "Warning:", "[WARNING]"]):
                    self.queue.put({'text': text, 'color': 'warning'})
                else:
                    self.queue.put({'text': text, 'color': 'normal'})
        
        def flush(self):
            pass
    
    gui_thread = threading.Thread(target=lambda: show_result(output_queue), daemon=True)
    gui_thread.start()
    time.sleep(0.2)
    
    def execute_code():
        real_time_stdout = RealTimeStdout(output_queue)
        original_stdout = sys.stdout
        sys.stdout = real_time_stdout
        
        try:
            print("Starting execution...\n\n")
            
            class RealTimeEvaluate(Evaluate):
                def evaluate(self, node, context):
                    if isinstance(node, (Loop, IfCondition)):
                        time.sleep(0.001) 
                    return super().evaluate(node, context)
            
            rt_evaluator = RealTimeEvaluate()
            rt_evaluator.evaluate(code_content, context)
            
            output_queue.put("__EXECUTION_COMPLETE__")
            
        except Exception as e:
            output_queue.put({'text': f"\n[FATAL ERROR AT {Evaluate.__name__}]: {str(e)}\n", 'color': 'error'})
            import traceback
            output_queue.put({'text': traceback.format_exc(), 'color': 'error'})
            output_queue.put("__EXECUTION_ERROR__")
        finally:
            sys.stdout = original_stdout

    execution_thread = threading.Thread(target=execute_code, daemon=False)
    execution_thread.start()
    execution_thread.join()
    gui_thread.join()
def MAIN():
    if main:
        try:
            code_content = txteditor_ui() 
            if runnable and code_content:
                show_evaluate_output(code_content)
            else:
                return 1
        except tk.Tcl_AsyncDeleteError:
            pass
        except NameError:
            messagebox.showerror('ERROR', 'DID NOT RECIEVE ANY CODE FOR IDE')
            traceback.print_exc()
            MAIN()
        except SystemExit:
            pass
        except KeyboardInterrupt:
            pass
        except:
                traceback.print_exc()
                MAIN()
MAIN()
