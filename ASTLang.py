import io, sys, time, traceback, inspect, math
from tkinter import messagebox
import tkinter as tk
from random import randint
context: dict[str, object] = dict()

info = """
DEFAULT MESSAGE FROM IDE:
'NTMDev ...'
Note from NTMDev: ASTLang 25 is now unsupported
----------------------------------------------------------------------------------------------------------------
ASTLang for PC, Local based (IDE)
Supports IDE usuage and file saving with .astlang

Designed with GitHub Copilot
Created by NTMDev (2025)

Packages used: traceback, random, ast, re, pickle, tkinter, sys, io, time, builtins, inspect, math

ASTLang Version 28 [PRE-DEV]

Currently Known Bugs:
- None

Functions (COMING SOON): FileOperation(), FileEdit()

Adding: 
- superclass inheritance (coming ASTLang 27)
- File I/O operations (coming ASTLang 27)

Added: Clamp(), DeepCopy(), HashValue(), Ord(), Chr(), BaseConvert()
Updated: None
----------------------------------------------------------------------------------------------------------------
"""
print(info)
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
        global content
        raw_text = code_text.get("1.0", tk.END).strip()
        try:
            content = eval(raw_text, globals())
        except Exception as e:
            print(f"Error: {e}")
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
            sig = str(inspect.signature(obj))
            return f"{name}{sig}"
        except Exception:
            return None
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
            font=('Consolas', 12)
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
    tk.Button(button_frame, text="RUN ASTLANG PROGRAM", command=submit,
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
    code_text.pack(expand=True, fill='both')
    code_text.insert(tk.END, initial)
    scrollbar.config(command=on_scroll)

    def safe_update_ui():
        try:
            if code_text.winfo_exists():
                update_line_numbers()
                highlight()
                handle_autocomplete()
                handle_signature()
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
    popup = tk.Toplevel()
    popup.title("User Input")
    popup.geometry("400x200")
    popup.grab_set() 
    if prompt:
        tk.Label(popup, text=prompt, font=("Consolas", 12)).pack(pady=5)
    text_widget = tk.Text(popup, height=5, font=("Consolas", 12))
    text_widget.pack(expand=True, fill="both", padx=5, pady=5)
    def submit():
        result["value"] = text_widget.get("1.0", "end-1c") 
        popup.destroy()
        root2.destroy()
    submit_btn = tk.Button(popup, text="Submit", command=submit, font=("Consolas", 12))
    submit_btn.pack(pady=5)
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

class FuncCall(FunctionParent): #Simple Function Call
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
    def __init__(self, FormatString, *Args):
        self.FormatString = FormatString
        self.Args = Args

class Slice(NodeParent):
    def __init__(self, Var, Start=ObjNONE(), End=ObjNONE(), Step=ObjNONE()):
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

class Ord(NodeParent):
    def __init__(self, Str):
        self.Str = Str
class Chr(NodeParent):
    def __init__(self, Str):
        self.Str = Str

primitive = (str, int, float, list, bool, dict, tuple)
class Evaluate():
    def evaluate(self, node, context):
        if isinstance(node, Exit):
            code = self.evaluate(node.Code, context)
            sys.exit(code)
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
            else: 
                raise Exception("CastToValue requires a Variable node")
            value = self.evaluate(node.Var, context)
            if node.CastVal == 'str': 
                casted = str(value)
            elif node.CastVal == 'int': 
                casted = int(value)
            elif node.CastVal == 'list': 
                casted = list(value)
            else: 
                raise Exception(f"Unsupported cast: {node.CastVal}")
            
            context[varname] = casted
            return casted
        elif isinstance(node, Integer):
            if isinstance(node.Int, int):
                return node.Int
            return int(self.evaluate(node.Int, context))
        elif isinstance(node, Float):
            if isinstance(node.Flt, float):
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
        elif isinstance(node, ListEdit):
            mode = node.EditType
            valid_modes = {'append', 'del', 'clear', 'sort', 'pop', 'reverse'}
            if mode not in valid_modes:
                raise ValueError(f"Unsupported ListEdit mode: {mode}")
            list_name = self.evaluate(node.Name, context)
            if not isinstance(list_name, str):
                raise TypeError(f"ListEdit Name must evaluate to a string, got {type(list_name)}")
            if list_name not in context:
                raise NameError(f"List '{list_name}' is not defined in context")
            c = list(context.get(list_name))
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
                    if delIndex in range(0, len(c)):
                        del c[delIndex]
            elif mode == 'clear':
                c.clear()
            elif mode == 'sort':
                c.sort(reverse=node.ReversedSort)
            elif mode == 'pop':
                popi = self.evaluate(node.PopIndex, context)
                if popi in range(0, len(c)):
                    popped = c.pop(popi)
                    context[list_name] = c 
                    return popped
            elif mode == 'reverse':
                c.reverse()
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
                  
                end_val = node.Function.End
                end_val = self.evaluate(end_val, context) if not isinstance(end_val, primitive) else end_val
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
            if node.Operator == '==':
                return left == right
            elif node.Operator == '!=':
                return left != right
            elif node.Operator == '>':
                return left > right
            elif node.Operator == '<':
                return left < right
            elif node.Operator == '>=':
                return left >= right
            elif node.Operator == '<=':
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

            for param, arg in zip(func_def.Param, node.Args):
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
                raise Exception("DictGet: no key specified for dictionary lookup")
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
                if node.FinallyBody:
                    for stmt in node.FinallyBody:
                        self.evaluate(stmt, context)
            return result
        elif isinstance(node, Sum):
            v = self.evaluate(node.Var, context)
            if not isinstance(v, str):
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
            MedianIndice = None
            if len(mvar) % 2 == 1:
                MedianIndice = len(mvar)//2
            else:
                MedianIndice = (mvar[len(mvar)//2-1] + mvar[len(mvar)//2])/2
            return mvar[MedianIndice]
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
            time.sleep(self.evaluate(node.Miliseconds)/1000)
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
        elif isinstance(node, FormattedString):
            format_string = self.evaluate(node.FormatString, context)
            args = [self.evaluate(arg, context) for arg in node.Args]
            if not isinstance(format_string, str):
                raise TypeError("FormattedString FormatString must evaluate to a string")
            return format_string.format(*args)
        elif isinstance(node, DefineClass):
            class_def = {
                "name": node.Name,
                "body": node.Body,
                "base": self.evaluate(node.Base, context) if not isinstance(node.Base, ObjNONE) else None
            }
            context[node.Name] = class_def
            return class_def
        elif isinstance(node, NewInstance):
            class_def = context.get(node.ClassName)
            if not class_def:
                raise NameError(f"Class '{node.ClassName}' is not defined")

            instance = {"__class__": class_def["name"]}
            for stmt in class_def["body"]:
                if isinstance(stmt, Assignment):
                    instance[stmt.Name] = self.evaluate(stmt.Val, context)
                elif isinstance(stmt, DefineFunction) and stmt.Name == "__init__":
                    local_context = context.copy()
                    local_context["self"] = instance
                    for param, arg in zip(stmt.Param[1:], node.Args):
                        local_context[param] = self.evaluate(arg, context)
                    for s in stmt.Body:
                        self.evaluate(s, local_context)
            return instance
        elif isinstance(node, MethodCall):
            obj = self.evaluate(node.Obj, context)
            class_def = context.get(obj["__class__"])
            if not class_def:
                raise NameError(f"Class '{obj['__class__']}' is not defined")

            method = None
            for stmt in class_def["body"]:
                if isinstance(stmt, DefineFunction) and stmt.Name == node.MethodName:
                    method = stmt
                    break
            if not method:
                raise NameError(f"Method '{node.MethodName}' is not defined in class '{obj['__class__']}'")
            local_context = context.copy()
            local_context["self"] = obj
            for param, arg in zip(method.Param[1:], node.Args):
                local_context[param] = self.evaluate(arg, context)
            result = None
            for s in method.Body:
                result = self.evaluate(s, local_context)
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
        else:
            global runnable
            runnable = False
            raise TypeError(f"{type(node)}")

E = Evaluate()
def show_result(output, qw):
    root2 = tk.Tk()
    root2.title('ASTLANG OUTPUT')

    output_label = tk.Label(root2, text='OUTPUT:', font=('Consolas', 12,'italic bold'), width=20, justify='left')
    output_label.pack()

    entry = tk.Text(root2, font=('Consolas',12,'bold'), width=qw)
    entry.pack(padx=10, pady=15)

    entry.insert("1.0", output)
    entry.config(state='disabled') 

    root2.mainloop()
def show_evaluate_output():
    buffer = io.StringIO()
    old_stdout = sys.stdout
    sys.stdout = buffer
    try:
        E.evaluate(content, context)
    finally:
        sys.stdout = old_stdout
    output = buffer.getvalue()
    show_result(output, 100)
    output = ''
ran = False
def MAIN():
    if main:
        try:
            while True:
                txteditor_ui()
                if runnable:
                    show_evaluate_output()
                else:
                    return
        except NameError:
            messagebox.showerror('ERROR', 'DID NOT RECIEVE ANY CODE FOR IDE')
            traceback.print_exc()
            MAIN()
        except tk.TclError:
            messagebox.showerror('ERROR', 'NO CODE OUTPUT, CANNOT DISPLAY')
            traceback.print_exc()
            MAIN()
        except SystemExit:
            pass
        except KeyboardInterrupt:
            pass
        except:
            traceback.print_exc()
            MAIN()
if not ran:
    MAIN()
    ran = True
