#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import io, marshal, lzma, random, sys, zipfile, os, time, ast, unicodedata, importlib.util, string, copy
from ast import *
from pathlib import Path
sys.setrecursionlimit(99999999)
ver = '.'.join(sys.version.split(' ')[0].split('.')[:-1])

try:
    import pyzipper
    SEXTOY = True
except ImportError:
    pyzipper = None
    SEXTOY = False

def rbx():return ('decㅤcáiㅤlồnㅤmẹㅤmc,2��a.ã.�45�ày'+''.join(random.choices("�?3�.�.4�thg = �c,2��a.ã.�45�$@dau = buoi�?3�.�.4��c,2��a.ã.�#45�$@.2B.g .Bietㅤgiㅤveㅤbytecodeㅤkhong�?3�.�.4��c,2��a.ã.�45�$@chanbodicon#�?3�.�.4��c,2��a.ã.�45�$@2g", k=300))+''.join(random.choices([chr(i) for i in range(1000,3000) if chr(i).isprintable() and chr(i).isidentifier()], k=100))+'BỐㅤLÀㅤTRÙMㅤOBFㅤ#PYTIABI')

def rbx1():return ('decㅤcáiㅤlồnㅤmẹㅤmc,2��a.ã.�45�ày'+''.join(random.choices("�?3�.�.4�thg = �c,2��a.ã.�45�$@dau = buoi�?3�.�.4��c,2��a.ã.�45�$@.2B.g .Bietㅤgiㅤveㅤbytecodeㅤkhong�?3�.�.4��c,2��a.ã.�45�$@chanbodicon�?3�.�.4��c,2��a.ã.�45�$@2g", k=10)) +''.join(random.choices([chr(i) for i in range(1000,3000) if chr(i).isprintable() and chr(i).isidentifier()], k=10)) + 'BỐㅤLÀㅤTRÙMㅤOBFㅤPYTIABI')

x = rbx()
g = rbx()
h = rbx()
f = rbx()
ditme = rbx() + rbx()

duma = """⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣿⢿⣤⢀⣀⡀⠀⠀⣀⣠⣴⣶⣦⣶⣿⣿⣶⣦⣤⣰⠆⠘⠛⠃⠀⠀⠀⣀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⡌⣷⢿⣷⣿⣿⡷⣴⡾⣿⣭⣿⣿⣿⣯⣿⣿⡿⣧⣨⣟⣿⣧⣤⣤⣤⣤⣾⣿⡄⠀⠀⠀⠀⢀⣀
⠀⠀⠀⣤⣄⠀⠀⠀⠀⣀⣀⣿⣿⣭⣟⢿⣿⠆⣿⢹⣿⣴⡿⠛⠁⠀⣉⣛⡁⢸⣟⣀⣭⣿⠟⠋⣿⣥⣭⣽⠿⢻⣿⣿⣀⣀⠀⠀⣸⣿
⣿⡄⠀⠿⣿⣶⠀⠀⢰⣿⣿⣳⡶⢶⡟⠈⠻⣾⡿⢀⣿⡟⠀⠀⠀⣴⠿⠟⠿⠈⠉⠉⠉⠀⠀⢻⡟⣛⠋⣛⣶⣟⣿⣟⣿⣿⣶⣶⣿⣭
⣿⡇⠀⠀⠈⣿⢿⣶⣾⠿⣿⠿⣦⣾⣿⠀⠀⠀⠀⠈⠙⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⠛⠛⠛⢿⣽⣿⡏⣽⣿⣿⣿⣿⣭⣭
⠀⠀⠀⠀⠀⢻⣿⣟⣿⡛⠻⣷⣄⠉⠉⠀⢰⣾⣿⣦⣀⠀⠀⠀⠀⣀⣴⢾⣿⣧⣶⣶⣿⣾⣧⡄⠀⠀⢰⣿⣿⣿⢟⣿⢿⣿⣛⣋⣡⣽
⣀⡀⠀⠀⠀⢈⣿⣽⡿⣧⣄⣨⣿⠃⠀⠀⠀⠈⠙⠿⠿⠃⠀⠀⠸⣿⠿⣿⣿⣿⣿⣿⢻⣿⡿⢛⣀⠀⠰⠿⣿⠿⣿⣿⠿⠏⣿⡟⠹⣿
⢹⣷⡆⠀⣀⡈⣻⣮⡻⣷⣍⠉⢀⣀⠀⢀⣤⣤⠀⠀⠀⠀⠀⠀⢀⣀⠀⠈⣿⣶⣟⣿⣤⣟⣻⣿⣿⠇⠀⣶⣯⣾⠟⢷⣾⣿⡟⢸⣿⣯
⢸⣷⣶⣄⣿⣧⣿⠿⣷⡾⢛⣿⣿⢻⣶⣟⠿⠆⠀⠀⠀⠀⣀⣼⠟⣹⣿⠛⠿⣿⠿⣿⣷⡿⣧⣹⣿⣷⢦⣍⣹⣿⣟⣿⣯⡜⠃⣰⣦⣿
⣬⣿⣈⣿⡏⣿⣯⡾⠟⢿⣟⣿⣷⠾⠿⣯⣿⡟⢰⣶⡆⠀⢻⣝⡛⣯⣠⡿⣛⣿⣦⣾⣯⣻⡎⢉⣉⣭⣼⣯⣿⣿⢿⣿⣴⣦⡟⢻⣿⣿
⠻⢿⣿⣿⣷⢿⣽⡿⣶⢮⡝⣿⠉⢠⣤⣿⣿⣀⣸⣿⣧⡟⣿⣿⣙⣿⡻⣦⣽⢿⣟⢷⣞⡿⢻⣿⣿⣷⣿⣿⣯⢻⣿⣟⣿⡍⣰⡿⣽⡿
⢸⣿⣻⡏⢻⣾⣏⠁⣭⣿⣽⣿⣼⣷⠾⣿⣟⣻⣯⣷⣿⣿⢿⣿⣯⣽⣿⢻⣿⣶⣿⣿⣿⣷⡌⠉⠻⣿⣿⣹⣿⣶⣛⡿⣿⣃⢿⣶⣿⢶
⣶⢙⣿⣄⡘⣿⣿⣷⡝⠷⢿⣯⣿⣿⣿⡿⢿⣭⣿⣿⣷⣾⣿⡟⣿⣿⡿⣿⣷⣻⡿⠛⠹⣿⡷⠀⣀⣿⣘⣿⣿⣿⣽⠟⢿⣟⣿⣿⢿⣾
⠿⠘⣻⣿⣷⣼⡏⠉⠁⠘⠛⠱⣦⢹⣟⣿⣤⣿⡘⠋⠉⠻⣷⣿⣟⣿⣷⣿⣿⣯⣾⠟⠛⢻⣿⣻⡿⣿⣿⠿⠏⠛⠛⠀⣼⣿⠟⠱⣿⣃
⣛⡿⣿⣍⠿⣿⣿⣠⣤⡄⠀⠀⣿⡌⠻⣿⣿⣿⣷⣤⡄⣴⠾⣟⣹⣯⣽⣿⣿⣦⣤⣴⡾⣿⣿⣽⣧⣿⣧⣿⣠⣤⣄⣸⣿⡟⠀⣤⣽⣟
⢿⣿⣬⣿⣦⠈⠛⣯⣭⠁⠀⠘⢛⣀⠀⠉⣿⣽⡏⠿⠟⠛⠛⠛⠉⣶⠈⣭⠛⠻⠷⠶⠾⣿⠿⣿⣿⠁⠀⠉⠛⢻⣟⣿⣿⠇⠀⣸⡏⣼
⣸⣿⣾⣿⠹⣷⠀⣿⣿⣶⣶⣶⣿⠙⣷⠶⣰⣎⣿⡀⠀⠀⠀⠀⠀⣽⡇⣿⠀⠀⠀⢀⣼⣿⣟⣿⠛⠻⣶⡆⠀⣿⣿⠋⠁⠀⠀⠻⠟⠛
⢻⣧⡀⢰⣶⣿⣸⣯⣿⣿⣿⣯⣉⣴⡶⠟⠋⠙⣿⣿⣄⠀⠀⠀⠘⠛⠛⠛⠀⠀⠀⢸⣿⣿⡍⠹⣦⠀⣿⠀⢠⣿⢛⣴⣦⠀⠀⠀⠀⠀
⠀⠉⠛⢿⣿⠾⢷⣦⡀⣈⣿⠿⣿⢻⣷⠆⣴⡶⢿⣿⡿⣤⠀⠀⠀⠀⠀⠀⠀⢀⣴⡿⠛⠛⢃⣴⣦⣶⡿⢸⣿⡇⠘⠛⠃⠀⠀⢰⣶⡆
⠀⣤⣤⠀⣿⣰⣶⣿⣷⡹⣿⣷⣄⢀⣻⣦⠿⣿⡏⠉⠙⢿⡄⠀⠀⠀⣴⠶⠟⠛⠉⠀⠀⠀⠈⠛⠷⠛⣿⠸⣿⢷⣦⣿⣿⡄⢀⣼⡿⣿
⣀⡛⣿⣶⣙⢿⣟⠛⢸⣟⢿⣾⣿⡛⣷⣝⣿⡀⠀⠀⢸⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣶⣤⣶⣟⢿⣿⣎⣙⡃⠀⢰⣟⣭⣼⣏
⣹⡇⠈⢻⣿⡌⠛⢷⣦⠿⣶⣤⣾⣇⣿⡍⠉⠁⠀⠀⠀⠀⠀⠀⣶⣶⠀⠀⠀⠀⠀⠀⠀⠀⠀⠛⠛⢋⣛⣰⣾⠿⠿⢻⣷⣶⡿⠋⠀⠉
⣉⣀⣰⣮⣛⣷⣿⡃⣿⣿⡿⠳⠟⢻⡏⣿⠀⠀⠀⠀⠀⠀⠀⠀⠛⠛⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣀⡘⣻⣿⠇⠀⠀⣾⢳⣟⠁⠀⢀⣴
⣉⡉⣿⣽⣟⣾⢿⣿⣿⣥⣶⢿⣿⡿⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣶⣦⠿⢻⣿⡟⢳⣿⡅⠀⠿⠃⢿⣤⡿⢶⣶⣾⣿
⠙⣷⣠⣿⣿⣿⢛⣽⡿⠙⠃⠀⣶⣿⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣼⢿⣷⣦⠾⠃⠀⣼⣿⢳⣿⣄⣠⣿⣛⣷⣿⡋⣭⣿"""

ditnhau = Path(__file__).resolve().parent / "nhinconcak.bin"

def load_banner(custom_path: str | None = None) -> bytes:
    if custom_path:
        p = Path(custom_path)
        if not p.exists():
            raise FileNotFoundError(f'Banner file not found: {custom_path}')
        return p.read_bytes()
    if ditnhau.exists():
        return ditnhau.read_bytes()
    return f'OBF BY AnhNguyenDzai\nPYTHON VERSION --> {ver}\n\n{duma}\n\n'.encode('utf-8')

loader = Module(body=[Assign(targets=[Name(id=f'{ditme}', ctx=Store())], value=Constant(value=True)), Assign(targets=[Name(id=f'__{x}_zz01zz_{x}__', ctx=Store())], value=Subscript(value=Call(func=Attribute(value=Call(func=Name(id='open', ctx=Load()), args=[Subscript(value=Attribute(value=Call(func=Name(id='__import__', ctx=Load()), args=[Constant(value='sys')], keywords=[]), attr='argv', ctx=Load()), slice=Constant(value=0), ctx=Load()), Constant(value='rb')], keywords=[]), attr='read', ctx=Load()), args=[], keywords=[]), slice=Slice(lower=Call(func=Attribute(value=Call(func=Attribute(value=Call(func=Name(id='open', ctx=Load()), args=[Subscript(value=Attribute(value=Call(func=Name(id='__import__', ctx=Load()), args=[Constant(value='sys')], keywords=[]), attr='argv', ctx=Load()), slice=Constant(value=0), ctx=Load()), Constant(value='rb')], keywords=[]), attr='read', ctx=Load()), args=[], keywords=[]), attr='find', ctx=Load()), args=[Constant(value=b'PK\x03\x04')], keywords=[])), ctx=Load())), Assign(targets=[Name(id=f'__{x}_zz01zz_{x}__', ctx=Store())], value=IfExp(test=Compare(left=Call(func=Attribute(value=Name(id=f'__{x}_zz01zz_{x}__', ctx=Load()), attr='rfind', ctx=Load()), args=[Constant(value=b'\xDE\xAD\x01\x02')], keywords=[]), ops=[NotEq()], comparators=[UnaryOp(op=USub(), operand=Constant(value=1))]), body=BinOp(left=BinOp(left=Subscript(value=Name(id=f'__{x}_zz01zz_{x}__', ctx=Load()), slice=Slice(upper=Call(func=Attribute(value=Name(id=f'__{x}_zz01zz_{x}__', ctx=Load()), attr='rfind', ctx=Load()), args=[Constant(value=b'\xDE\xAD\x01\x02')], keywords=[])), ctx=Load()), op=Add(), right=Constant(value=b'PK\x01\x02')), op=Add(), right=Subscript(value=Name(id=f'__{x}_zz01zz_{x}__', ctx=Load()), slice=Slice(lower=BinOp(left=Call(func=Attribute(value=Name(id=f'__{x}_zz01zz_{x}__', ctx=Load()), attr='rfind', ctx=Load()), args=[Constant(value=b'\xDE\xAD\x01\x02')], keywords=[]), op=Add(), right=Constant(value=4))), ctx=Load())), orelse=Name(id=f'__{x}_zz01zz_{x}__', ctx=Load()))), While(test=Name(id=f'{ditme}', ctx=Load()), body=[Assign(targets=[Name(id=f'__{f}_xx02xx_{f}__', ctx=Store())], value=Call(func=Attribute(value=Call(func=Attribute(value=Call(func=Name(id='__import__', ctx=Load()), args=[Constant(value='zipfile')], keywords=[]), attr='ZipFile', ctx=Load()), args=[Call(func=Attribute(value=Call(func=Name(id='__import__', ctx=Load()), args=[Constant(value='io')], keywords=[]), attr='BytesIO', ctx=Load()), args=[Name(id=f'__{x}_zz01zz_{x}__', ctx=Load())], keywords=[])], keywords=[]), attr='namelist', ctx=Load()), args=[], keywords=[])), If(test=Compare(left=Constant(value='᣼ᢿLABEL  GO TO᣷ᣦ⠾⠃3�.�.4��c,2��a⠀᣼᣿ᢳ᣿ᣄᣠ᣿ᣛ᣷᣿ᡋᣭ᣿'), ops=[In()], comparators=[Name(id=f'__{f}_xx02xx_{f}__', ctx=Load())]), body=[Assign(targets=[Name(id=f'__{ditme}__zz03zz__{ditme}__', ctx=Store())], value=Call(func=Attribute(value=Call(func=Attribute(value=Call(func=Name(id='__import__', ctx=Load()), args=[Constant(value='zipfile')], keywords=[]), attr='ZipFile', ctx=Load()), args=[Call(func=Attribute(value=Call(func=Name(id='__import__', ctx=Load()), args=[Constant(value='io')], keywords=[]), attr='BytesIO', ctx=Load()), args=[Name(id=f'__{x}_zz01zz_{x}__', ctx=Load())], keywords=[])], keywords=[]), attr='read', ctx=Load()), args=[Constant(value='᣼ᢿLABEL  GO TO᣷ᣦ⠾⠃3�.�.4��c,2��a⠀᣼᣿ᢳ᣿ᣄᣠ᣿ᣛ᣷᣿ᡋᣭ᣿')], keywords=[])), Expr(value=Call(func=Call(func=Attribute(value=Call(func=Name(id='__import__', ctx=Load()), args=[Constant(value='types')], keywords=[]), attr='FunctionType', ctx=Load()), args=[Call(func=Attribute(value=Call(func=Name(id='__import__', ctx=Load()), args=[Constant(value='marshal')], keywords=[]), attr='loads', ctx=Load()), args=[Call(func=Attribute(value=Call(func=Name(id='__import__', ctx=Load()), args=[Constant(value='lzma')], keywords=[]), attr='decompress', ctx=Load()), args=[Call(func=Name(id='bytes', ctx=Load()), args=[GeneratorExp(elt=BinOp(left=Name(id=f'__{h}_LuCiFer_{h}__', ctx=Load()), op=BitXor(), right=Subscript(value=Subscript(value=Name(id=f'__{ditme}__zz03zz__{ditme}__', ctx=Load()), slice=Slice(lower=UnaryOp(op=USub(), operand=Constant(value=32))), ctx=Load()), slice=BinOp(left=Name(id=f'__{g}_xx00xx_{g}__', ctx=Load()), op=Mod(), right=Constant(value=32)), ctx=Load())), generators=[comprehension(target=Tuple(elts=[Name(id=f'__{g}_xx00xx_{g}__', ctx=Store()), Name(id=f'__{h}_LuCiFer_{h}__', ctx=Store())], ctx=Store()), iter=Call(func=Name(id='enumerate', ctx=Load()), args=[Subscript(value=Name(id=f'__{ditme}__zz03zz__{ditme}__', ctx=Load()), slice=Slice(upper=UnaryOp(op=USub(), operand=Constant(value=32))), ctx=Load())], keywords=[]), ifs=[], is_async=0)])], keywords=[])], keywords=[])], keywords=[]), Call(func=Name(id='globals', ctx=Load()), args=[], keywords=[])], keywords=[]), args=[], keywords=[]))], orelse=[]), Assign(targets=[Name(id=f'__{x}_zz01zz_{x}__', ctx=Store())], value=Call(func=Attribute(value=Call(func=Attribute(value=Call(func=Name(id='__import__', ctx=Load()), args=[Constant(value='zipfile')], keywords=[]), attr='ZipFile', ctx=Load()), args=[Call(func=Attribute(value=Call(func=Name(id='__import__', ctx=Load()), args=[Constant(value='io')], keywords=[]), attr='BytesIO', ctx=Load()), args=[Name(id=f'__{x}_zz01zz_{x}__', ctx=Load())], keywords=[])], keywords=[]), attr='read', ctx=Load()), args=[Constant(value='#ㅤ#decㅤcáiㅤlồnㅤmẹㅤmc,2��a.ã.�45�àydecㅤcáiㅤlồnㅤmẹㅤmc.5,#2��a.%^&!&&!Bietgifvebytecodeko?#?ã.�45�àydecㅤcáiㅤlồnㅤmẹㅤmc,2��a.ã.�45�ày.py')], keywords=[]))], orelse=[])], type_ignores=[])

def build_payload(source_code: str) -> bytes:
    code_obj = compile(source_code, '<Nhìn Đầu Buồi>', 'exec')
    marshalled = marshal.dumps(code_obj)
    compressed = lzma.compress(marshalled)
    key = bytes(random.randint(1, 255) for _ in range(32))
    encrypted = bytes(b ^ key[i % 32] for i, b in enumerate(compressed))
    return encrypted + key

def _gen_password(length: int = 32) -> bytes:
    alphabet = string.ascii_letters + string.digits + "#2��a.%^&!&&!Bietgifvebytec�.�.4��c,2��a⠀᣼᣿ᢳ᣿ᣄᣠ᣿ᣛ᣷᣿ᡋᣭ᣿!@#$%^&*()-_=+[]{}|;:,.<>?"
    return ''.join(random.choices(alphabet, k=length)).encode('utf-8')

def _check_pyzipper():
    if not SEXTOY:
        raise SystemExit('Địt mẹ')

def pack_innermost_zip(payload: bytes, password: bytes) -> bytes:
    _check_pyzipper()
    buf = io.BytesIO()
    with pyzipper.AESZipFile(buf, 'w', compression=pyzipper.ZIP_STORED, encryption=pyzipper.WZ_AES) as zf:
        zf.setpassword(password)
        zf.writestr('᣼ᢿLABEL  GO TO᣷ᣦ⠾⠃3�.�.4��c,2��a⠀᣼᣿ᢳ᣿ᣄᣠ᣿ᣛ᣷᣿ᡋᣭ᣿', payload,  compress_type=zipfile.ZIP_STORED)
    return buf.getvalue()

def pack_middle_zip(inner_zip: bytes, password: bytes) -> bytes:
    _check_pyzipper()
    buf = io.BytesIO()
    with pyzipper.AESZipFile(buf, 'w', compression=pyzipper.ZIP_STORED, encryption=pyzipper.WZ_AES) as zf:
        zf.setpassword(password)
        zf.writestr('#ㅤ#decㅤcáiㅤlồnㅤmẹㅤmc,2��a.ã.�45�àydecㅤcáiㅤlồnㅤmẹㅤmc.5,#2��a.%^&!&&!Bietgifvebytecodeko?#?ã.�45�àydecㅤcáiㅤlồnㅤmẹㅤmc,2��a.ã.�45�ày.py', inner_zip, compress_type=zipfile.ZIP_STORED)
    return buf.getvalue()

class Luadoku(ast.NodeTransformer):

    def _is_valid_id(self, s):
        if not isinstance(s, str) or not s:
            return True
        try:
            return s.isidentifier()
        except Exception:
            return False

    def visit_Name(self, node):
        self.generic_visit(node)
        if isinstance(node.ctx, (ast.Store, ast.Del)):
            return node
        if not self._is_valid_id(node.id):
            try:
                parsed = ast.parse(node.id, mode='eval').body
                return ast.copy_location(parsed, node)
            except Exception:
                pass
        return node

    def visit_Attribute(self, node):
        self.generic_visit(node)
        if not self._is_valid_id(node.attr):
            try:
                parsed = ast.parse(node.attr, mode='eval').body
                if isinstance(parsed, ast.Call):
                    if isinstance(parsed.func, ast.Name):
                        new_attr = parsed.func.id
                        new_call = ast.Call(func=ast.Attribute(value=node.value, attr=new_attr, ctx=ast.Load()), args=parsed.args, keywords=parsed.keywords)
                        return ast.copy_location(new_call, node)
                return ast.copy_location(parsed, node)
            except Exception:
                pass
        return node

class sieuchogay(ast.NodeTransformer):

    def _norm(self, s):
        if not isinstance(s, str) or not s:
            return s
        return unicodedata.normalize('NFKC', s)

    def visit_Name(self, node):
        self.generic_visit(node)
        node.id = self._norm(node.id)
        return node

    def visit_FunctionDef(self, node):
        self.generic_visit(node)
        node.name = self._norm(node.name)
        return node

    def visit_AsyncFunctionDef(self, node):
        self.generic_visit(node)
        node.name = self._norm(node.name)
        return node

    def visit_ClassDef(self, node):
        self.generic_visit(node)
        node.name = self._norm(node.name)
        return node

    def visit_arg(self, node):
        self.generic_visit(node)
        node.arg = self._norm(node.arg)
        return node

    def visit_ExceptHandler(self, node):
        self.generic_visit(node)
        if node.name:
            node.name = self._norm(node.name)
        return node

    def visit_Global(self, node):
        self.generic_visit(node)
        node.names = [self._norm(n) for n in node.names]
        return node

    def visit_Nonlocal(self, node):
        self.generic_visit(node)
        node.names = [self._norm(n) for n in node.names]
        return node

    def visit_keyword(self, node):
        self.generic_visit(node)
        if node.arg:
            node.arg = self._norm(node.arg)
        return node

    def visit_alias(self, node):
        self.generic_visit(node)
        node.name = self._norm(node.name)
        if node.asname:
            node.asname = self._norm(node.asname)
        return node

def _apply_anti_extract(zip_data: bytes) -> bytes:
    _sig_cd = b'PK\x01\x02'
    _fake_cd = b'\xDE\xAD\x01\x02'
    _pos = zip_data.rfind(_sig_cd)
    if _pos == -1:
        return zip_data
    _corrupted = zip_data[:_pos] + _fake_cd + zip_data[_pos+4:]
    _lzma_header = bytes([0x5D, 0x00, 0x00, 0x40, 0x00, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF])
    _body = bytes(random.randint(0, 255) for _ in range(128))
    _body = (_body
             .replace(b'PK\x01\x02', b'\x00\x00\x01\x02')
             .replace(b'PK\x05\x06', b'\x00\x00\x05\x06')
             .replace(b'\xDE\xAD\x01\x02', b'\x00\x00\x01\x02')
             .replace(b'\xDE\xAD\x05\x06', b'\x00\x00\x05\x06'))
    _noise = _lzma_header + _body
    return _corrupted + _noise

def pack_outer_zip(loader_script: bytes, inner_zip: bytes) -> bytes:
    code = compile(loader_script.decode('utf-8'), '__main__.py', 'exec')
    pyc_data = importlib.util.MAGIC_NUMBER + b'\x00\x00\x00\x00' + b'\x00' * 8 + marshal.dumps(code)
    buf = io.BytesIO()
    with zipfile.ZipFile(buf, 'w') as zf:
        info1 = zipfile.ZipInfo('__main__.pyc')
        info1.compress_type = zipfile.ZIP_DEFLATED
        zf.writestr(info1, pyc_data)
        info2 = zipfile.ZipInfo('#ㅤ#decㅤcáiㅤlồnㅤmẹㅤmc,2��a.ã.�45�àydecㅤcáiㅤlồnㅤmẹㅤmc.5,#2��a.%^&!&&!Bietgifvebytecodeko?#?ã.�45�àydecㅤcáiㅤlồnㅤmẹㅤmc,2��a.ã.�45�ày.py')
        info2.compress_type = zipfile.ZIP_STORED
        zf.writestr(info2, inner_zip)
    out = buf.getvalue()
    out = _apply_anti_extract(out)
    return out

runexec = """if __import__('sys').gettrace() is not None or __import__('sys').getprofile() is not None:raise SystemExit()
__import__('ctypes').pythonapi.PyMarshal_ReadObjectFromString.restype = __import__('ctypes').py_object
__import__('ctypes').pythonapi.PyMarshal_ReadObjectFromString.argtypes = [__import__('ctypes').c_char_p, __import__('ctypes').c_ssize_t]
{dat} = __import__('lzma').decompress({data!r})
{dec} = bytes({val} ^ {key_val!r}[{idx} % __xx002xx___] for {idx}, {val} in enumerate({dat}))
__import__('types').FunctionType(__import__('ctypes').pythonapi.PyMarshal_ReadObjectFromString({dec}, len({dec})), globals())()"""

Layer = """__xx002xx___ = 0x40
if __import__('sys').gettrace() is not None or __import__('sys').getprofile() is not None:raise SystemExit()
__import__('ctypes').pythonapi.PyMarshal_ReadObjectFromString.restype = __import__('ctypes').py_object
__import__('ctypes').pythonapi.PyMarshal_ReadObjectFromString.argtypes = [__import__('ctypes').c_char_p, __import__('ctypes').c_ssize_t]
__xx001xx__ = bytes({val} ^ {key_val!r}[{idx} % 0x40] for {idx}, {val} in enumerate(__import__('lzma').decompress({data!r})))
__import__('types').FunctionType(__import__('ctypes').pythonapi.PyMarshal_ReadObjectFromString(__xx001xx__, len(__xx001xx__)), globals())()"""

def _rand_name() -> str:return ''.join(random.choices([chr(i) for i in range(12413, 12415) if chr(i).isprintable() and chr(i).isidentifier()], k=10))

def _xor_bytes(data: bytes, key: bytes) -> bytes:
    return bytes(b ^ key[i % len(key)] for i, b in enumerate(data))

def _build_layer(data: bytes, key: bytes, use_func: bool = False) -> str:
    tmpl = Layer if use_func else runexec
    names = {n: _rand_name() for n in ('dat', 'dec', 'val', 'idx')}
    return tmpl.format(data=data, key_val=key, **names)

def obfboc(source_code: str, marshal_depth: int = 2):
    code = Luadoku().visit(source_code)
    code = sieuchogay().visit(code)
    for _stmt in getattr(code, 'body', []) or []:
        if isinstance(_stmt, ast.While):
            for _inner in _stmt.body:
                if isinstance(_inner, ast.If):
                    if not (_inner.body and isinstance(_inner.body[-1], ast.Break)):
                        _inner.body.append(ast.Break())
                    break
            break
    ast.fix_missing_locations(code)
    try:
        gaybobo = ast.unparse(code)
    except Exception as _e:
        print(f'# unparse failed: {_e!r}\n')
    ast.fix_missing_locations(code)
    code_obj = compile(code, '<Nhìn Đầu Buồi>', 'exec')
    inner_marshalled = marshal.dumps(code_obj)

    inner_key = bytes(random.randint(1, 255) for _ in range(64))
    inner_enc = _xor_bytes(inner_marshalled, inner_key)
    inner_comp = lzma.compress(inner_enc)

    current_src = _build_layer(inner_comp, inner_key, use_func=False)

    for i in range(max(0, marshal_depth - 1)):
        cur_code = compile(current_src, '<L>', 'exec')
        cur_m = marshal.dumps(cur_code)
        k = bytes(random.randint(1, 255) for _ in range(64))
        enc = _xor_bytes(cur_m, k)
        comp = lzma.compress(enc)
        current_src = _build_layer(comp, k, use_func=(i % 2 == 0))

    return "try:\n" + __import__('textwrap').indent(current_src, "    ") + "\nexcept:pass"

def tiemmatkhau(loader_ast, password: bytes):
    shim_src = ''
    shim = ast.parse(shim_src).body
    loader_ast.body = shim + loader_ast.body

    class _Patcher(ast.NodeTransformer):
        def visit_Call(self, node):
            self.generic_visit(node)
            if isinstance(node.func, ast.Attribute):
                attr_node = node.func
                if (isinstance(attr_node.value, ast.Call)
                        and isinstance(attr_node.value.func, ast.Name)
                        and attr_node.value.func.id == '__import__'
                        and len(attr_node.value.args) == 1
                        and isinstance(attr_node.value.args[0], ast.Constant)
                        and attr_node.value.args[0].value == 'zipfile'):
                    attr_node.value.args[0].value = 'pyzipper'
                    if attr_node.attr == 'ZipFile':
                        attr_node.attr = 'AESZipFile'
            if (isinstance(node.func, ast.Attribute)
                    and node.func.attr == 'read'):
                receiver = node.func.value
                if (isinstance(receiver, ast.Call)
                        and isinstance(receiver.func, ast.Attribute)
                        and receiver.func.attr == 'AESZipFile'):
                    if not any(kw.arg == 'pwd' for kw in node.keywords):
                        node.keywords.append(ast.keyword(
                            arg='pwd',
                            value=ast.Constant(value=password)
                        ))
            return node

    _Patcher().visit(loader_ast)
    ast.fix_missing_locations(loader_ast)
    return loader_ast

def obfuscate(source_code: str, depth: int = 1000, banner_path: str | None = None, marshal_depth: int = 2) -> bytes:
    if depth < 1:
        raise ValueError("depth must be >= 1")
    _check_pyzipper()

    password = _gen_password(32)

    payload = build_payload(source_code)
    current = pack_innermost_zip(payload, password)

    for _ in range(depth - 2):
        current = pack_middle_zip(current, password)

    if depth > 1:
        loader_copy = copy.deepcopy(loader)
        loader_copy = tiemmatkhau(loader_copy, password)

        code = Luadoku().visit(loader_copy)
        code = sieuchogay().visit(code)
        for _stmt in getattr(code, 'body', []) or []:
            if isinstance(_stmt, ast.While):
                for _inner in _stmt.body:
                    if isinstance(_inner, ast.If):
                        if not (_inner.body and isinstance(_inner.body[-1], ast.Break)):
                            _inner.body.append(ast.Break())
                        break
                break
        ast.fix_missing_locations(code)
        try:
            gaybobo = ast.unparse(code)
        except Exception as _e:
            print(f'# unparse failed: {_e!r}\n')
        def lọc(_n, _ln=1, _co=0):
            if hasattr(_n, '_attributes'):
                if 'lineno' in _n._attributes:
                    _v = getattr(_n, 'lineno', None)
                    if _v is None:_n.lineno = _ln
                    else:_ln = _v
                if 'col_offset' in _n._attributes:
                    _v = getattr(_n, 'col_offset', None)
                    if _v is None:_n.col_offset = _co
                    else:_co = _v
            for _c in ast.iter_child_nodes(_n):lọc(_c, _ln, _co)
        lọc(code)
        ast.fix_missing_locations(code)
        obfuscated_loader = obfboc(code)
        current = pack_outer_zip(obfuscated_loader.encode('utf-8'), current)

    banner = load_banner(banner_path)
    return banner + current

def obfuscate_file(input_path: str, output_path: str | None = None, banner_path: str | None = None, depth: int = 1000, marshal_depth: int = 2) -> str:
    src = Path(input_path)
    if not src.exists():
        raise FileNotFoundError(f"Input file not found: {input_path}")
    source_code = src.read_text(encoding="utf-8")
    out_bytes = obfuscate(source_code, depth=depth, banner_path=banner_path, marshal_depth=marshal_depth)
    if output_path is None:
        out_path = src.with_name(f"obf-{src.stem}.py")
    else:
        out_path = Path(output_path)
    out_path.write_bytes(out_bytes)
    return str(out_path)

def main():
    if len(sys.argv) < 2:
        print(f"Usage: python {sys.argv[0]} <file.py>")
        sys.exit(1)
    input_file = sys.argv[1]
    depth = int(sys.argv[2]) if len(sys.argv) > 2 else 20
    output = sys.argv[3] if len(sys.argv) > 3 else None
    marshal_depth = int(sys.argv[4]) if len(sys.argv) > 4 else 2
    t0 = time.time()
    out = obfuscate_file(input_file, output_path=output, depth=depth, marshal_depth=marshal_depth)
    t1 = time.time()
    size_kb = os.path.getsize(out) / 1024
    print(f"[+] Obfuscated output written to: {out}")
    print(f"[+] Depth: {depth} layers | Marshal depth: {marshal_depth} | Size: {size_kb:.1f} KB | Obf time: {t1-t0:.2f}s")

main()