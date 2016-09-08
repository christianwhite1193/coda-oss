# This file was automatically generated by SWIG (http://www.swig.org).
# Version 3.0.10
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.





from sys import version_info as _swig_python_version_info
if _swig_python_version_info >= (2, 7, 0):
    def swig_import_helper():
        import importlib
        pkg = __name__.rpartition('.')[0]
        mname = '.'.join((pkg, '_coda_except')).lstrip('.')
        try:
            return importlib.import_module(mname)
        except ImportError:
            return importlib.import_module('_coda_except')
    _coda_except = swig_import_helper()
    del swig_import_helper
elif _swig_python_version_info >= (2, 6, 0):
    def swig_import_helper():
        from os.path import dirname
        import imp
        fp = None
        try:
            fp, pathname, description = imp.find_module('_coda_except', [dirname(__file__)])
        except ImportError:
            import _coda_except
            return _coda_except
        if fp is not None:
            try:
                _mod = imp.load_module('_coda_except', fp, pathname, description)
            finally:
                fp.close()
            return _mod
    _coda_except = swig_import_helper()
    del swig_import_helper
else:
    import _coda_except
del _swig_python_version_info
try:
    _swig_property = property
except NameError:
    pass  # Python < 2.2 doesn't have 'property'.

try:
    import builtins as __builtin__
except ImportError:
    import __builtin__

def _swig_setattr_nondynamic(self, class_type, name, value, static=1):
    if (name == "thisown"):
        return self.this.own(value)
    if (name == "this"):
        if type(value).__name__ == 'SwigPyObject':
            self.__dict__[name] = value
            return
    method = class_type.__swig_setmethods__.get(name, None)
    if method:
        return method(self, value)
    if (not static):
        if _newclass:
            object.__setattr__(self, name, value)
        else:
            self.__dict__[name] = value
    else:
        raise AttributeError("You cannot add attributes to %s" % self)


def _swig_setattr(self, class_type, name, value):
    return _swig_setattr_nondynamic(self, class_type, name, value, 0)


def _swig_getattr(self, class_type, name):
    if (name == "thisown"):
        return self.this.own()
    method = class_type.__swig_getmethods__.get(name, None)
    if method:
        return method(self)
    raise AttributeError("'%s' object has no attribute '%s'" % (class_type.__name__, name))


def _swig_repr(self):
    try:
        strthis = "proxy of " + self.this.__repr__()
    except __builtin__.Exception:
        strthis = ""
    return "<%s.%s; %s >" % (self.__class__.__module__, self.__class__.__name__, strthis,)

try:
    _object = object
    _newclass = 1
except __builtin__.Exception:
    class _object:
        pass
    _newclass = 0

class Context(_object):
    """Proxy of C++ except::Context class."""

    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, Context, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, Context, name)
    __repr__ = _swig_repr

    def __init__(self, *args):
        """
        __init__(except::Context self, std::string const & file, int line, std::string const & func, std::string const & time, std::string const & message) -> Context
        __init__(except::Context self, Context c) -> Context
        """
        this = _coda_except.new_Context(*args)
        try:
            self.this.append(this)
        except __builtin__.Exception:
            self.this = this

    def getMessage(self):
        """getMessage(Context self) -> std::string const &"""
        return _coda_except.Context_getMessage(self)


    def getTime(self):
        """getTime(Context self) -> std::string const &"""
        return _coda_except.Context_getTime(self)


    def getFunction(self):
        """getFunction(Context self) -> std::string const &"""
        return _coda_except.Context_getFunction(self)


    def getFile(self):
        """getFile(Context self) -> std::string const &"""
        return _coda_except.Context_getFile(self)


    def getLine(self):
        """getLine(Context self) -> int"""
        return _coda_except.Context_getLine(self)

    __swig_setmethods__["mMessage"] = _coda_except.Context_mMessage_set
    __swig_getmethods__["mMessage"] = _coda_except.Context_mMessage_get
    if _newclass:
        mMessage = _swig_property(_coda_except.Context_mMessage_get, _coda_except.Context_mMessage_set)
    __swig_setmethods__["mTime"] = _coda_except.Context_mTime_set
    __swig_getmethods__["mTime"] = _coda_except.Context_mTime_get
    if _newclass:
        mTime = _swig_property(_coda_except.Context_mTime_get, _coda_except.Context_mTime_set)
    __swig_setmethods__["mFunc"] = _coda_except.Context_mFunc_set
    __swig_getmethods__["mFunc"] = _coda_except.Context_mFunc_get
    if _newclass:
        mFunc = _swig_property(_coda_except.Context_mFunc_get, _coda_except.Context_mFunc_set)
    __swig_setmethods__["mFile"] = _coda_except.Context_mFile_set
    __swig_getmethods__["mFile"] = _coda_except.Context_mFile_get
    if _newclass:
        mFile = _swig_property(_coda_except.Context_mFile_get, _coda_except.Context_mFile_set)
    __swig_setmethods__["mLine"] = _coda_except.Context_mLine_set
    __swig_getmethods__["mLine"] = _coda_except.Context_mLine_get
    if _newclass:
        mLine = _swig_property(_coda_except.Context_mLine_get, _coda_except.Context_mLine_set)
    __swig_destroy__ = _coda_except.delete_Context
    __del__ = lambda self: None
Context_swigregister = _coda_except.Context_swigregister
Context_swigregister(Context)

class Throwable(_object):
    """Proxy of C++ except::Throwable class."""

    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, Throwable, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, Throwable, name)
    __repr__ = _swig_repr

    def __init__(self, *args):
        """
        __init__(except::Throwable self) -> Throwable
        __init__(except::Throwable self, std::string const & message) -> Throwable
        __init__(except::Throwable self, Context c) -> Throwable
        __init__(except::Throwable self, Throwable t, Context c) -> Throwable
        """
        this = _coda_except.new_Throwable(*args)
        try:
            self.this.append(this)
        except __builtin__.Exception:
            self.this = this
    __swig_destroy__ = _coda_except.delete_Throwable
    __del__ = lambda self: None

    def getMessage(self):
        """getMessage(Throwable self) -> std::string"""
        return _coda_except.Throwable_getMessage(self)


    def getTrace(self, *args):
        """
        getTrace(Throwable self) -> Trace const
        getTrace(Throwable self) -> Trace &
        """
        return _coda_except.Throwable_getTrace(self, *args)


    def getType(self):
        """getType(Throwable self) -> std::string"""
        return _coda_except.Throwable_getType(self)


    def toString(self):
        """toString(Throwable self) -> std::string"""
        return _coda_except.Throwable_toString(self)

Throwable_swigregister = _coda_except.Throwable_swigregister
Throwable_swigregister(Throwable)

class Exception(Throwable):
    """Proxy of C++ except::Exception class."""

    __swig_setmethods__ = {}
    for _s in [Throwable]:
        __swig_setmethods__.update(getattr(_s, '__swig_setmethods__', {}))
    __setattr__ = lambda self, name, value: _swig_setattr(self, Exception, name, value)
    __swig_getmethods__ = {}
    for _s in [Throwable]:
        __swig_getmethods__.update(getattr(_s, '__swig_getmethods__', {}))
    __getattr__ = lambda self, name: _swig_getattr(self, Exception, name)
    __repr__ = _swig_repr

    def __init__(self, *args):
        """
        __init__(except::Exception self) -> Exception
        __init__(except::Exception self, Context c) -> Exception
        __init__(except::Exception self, Throwable t, Context c) -> Exception
        __init__(except::Exception self, std::string const & message) -> Exception
        """
        this = _coda_except.new_Exception(*args)
        try:
            self.this.append(this)
        except __builtin__.Exception:
            self.this = this
    __swig_destroy__ = _coda_except.delete_Exception
    __del__ = lambda self: None

    def getType(self):
        """getType(Exception self) -> std::string"""
        return _coda_except.Exception_getType(self)

Exception_swigregister = _coda_except.Exception_swigregister
Exception_swigregister(Exception)

class IOException(Exception):
    """Proxy of C++ except::IOException class."""

    __swig_setmethods__ = {}
    for _s in [Exception]:
        __swig_setmethods__.update(getattr(_s, '__swig_setmethods__', {}))
    __setattr__ = lambda self, name, value: _swig_setattr(self, IOException, name, value)
    __swig_getmethods__ = {}
    for _s in [Exception]:
        __swig_getmethods__.update(getattr(_s, '__swig_getmethods__', {}))
    __getattr__ = lambda self, name: _swig_getattr(self, IOException, name)
    __repr__ = _swig_repr

    def __init__(self, *args):
        """
        __init__(except::IOException self) -> IOException
        __init__(except::IOException self, Context c) -> IOException
        __init__(except::IOException self, std::string const & msg) -> IOException
        __init__(except::IOException self, Throwable t, Context c) -> IOException
        """
        this = _coda_except.new_IOException(*args)
        try:
            self.this.append(this)
        except __builtin__.Exception:
            self.this = this
    __swig_destroy__ = _coda_except.delete_IOException
    __del__ = lambda self: None

    def getType(self):
        """getType(IOException self) -> std::string"""
        return _coda_except.IOException_getType(self)

IOException_swigregister = _coda_except.IOException_swigregister
IOException_swigregister(IOException)

class FileNotFoundException(IOException):
    """Proxy of C++ except::FileNotFoundException class."""

    __swig_setmethods__ = {}
    for _s in [IOException]:
        __swig_setmethods__.update(getattr(_s, '__swig_setmethods__', {}))
    __setattr__ = lambda self, name, value: _swig_setattr(self, FileNotFoundException, name, value)
    __swig_getmethods__ = {}
    for _s in [IOException]:
        __swig_getmethods__.update(getattr(_s, '__swig_getmethods__', {}))
    __getattr__ = lambda self, name: _swig_getattr(self, FileNotFoundException, name)
    __repr__ = _swig_repr

    def __init__(self, *args):
        """
        __init__(except::FileNotFoundException self) -> FileNotFoundException
        __init__(except::FileNotFoundException self, Context c) -> FileNotFoundException
        __init__(except::FileNotFoundException self, std::string const & msg) -> FileNotFoundException
        __init__(except::FileNotFoundException self, Throwable t, Context c) -> FileNotFoundException
        """
        this = _coda_except.new_FileNotFoundException(*args)
        try:
            self.this.append(this)
        except __builtin__.Exception:
            self.this = this
    __swig_destroy__ = _coda_except.delete_FileNotFoundException
    __del__ = lambda self: None

    def getType(self):
        """getType(FileNotFoundException self) -> std::string"""
        return _coda_except.FileNotFoundException_getType(self)

FileNotFoundException_swigregister = _coda_except.FileNotFoundException_swigregister
FileNotFoundException_swigregister(FileNotFoundException)

class BadCastException(Exception):
    """Proxy of C++ except::BadCastException class."""

    __swig_setmethods__ = {}
    for _s in [Exception]:
        __swig_setmethods__.update(getattr(_s, '__swig_setmethods__', {}))
    __setattr__ = lambda self, name, value: _swig_setattr(self, BadCastException, name, value)
    __swig_getmethods__ = {}
    for _s in [Exception]:
        __swig_getmethods__.update(getattr(_s, '__swig_getmethods__', {}))
    __getattr__ = lambda self, name: _swig_getattr(self, BadCastException, name)
    __repr__ = _swig_repr

    def __init__(self, *args):
        """
        __init__(except::BadCastException self) -> BadCastException
        __init__(except::BadCastException self, Context c) -> BadCastException
        __init__(except::BadCastException self, std::string const & msg) -> BadCastException
        __init__(except::BadCastException self, Throwable t, Context c) -> BadCastException
        """
        this = _coda_except.new_BadCastException(*args)
        try:
            self.this.append(this)
        except __builtin__.Exception:
            self.this = this
    __swig_destroy__ = _coda_except.delete_BadCastException
    __del__ = lambda self: None

    def getType(self):
        """getType(BadCastException self) -> std::string"""
        return _coda_except.BadCastException_getType(self)

BadCastException_swigregister = _coda_except.BadCastException_swigregister
BadCastException_swigregister(BadCastException)

class InvalidFormatException(Exception):
    """Proxy of C++ except::InvalidFormatException class."""

    __swig_setmethods__ = {}
    for _s in [Exception]:
        __swig_setmethods__.update(getattr(_s, '__swig_setmethods__', {}))
    __setattr__ = lambda self, name, value: _swig_setattr(self, InvalidFormatException, name, value)
    __swig_getmethods__ = {}
    for _s in [Exception]:
        __swig_getmethods__.update(getattr(_s, '__swig_getmethods__', {}))
    __getattr__ = lambda self, name: _swig_getattr(self, InvalidFormatException, name)
    __repr__ = _swig_repr

    def __init__(self, *args):
        """
        __init__(except::InvalidFormatException self) -> InvalidFormatException
        __init__(except::InvalidFormatException self, Context c) -> InvalidFormatException
        __init__(except::InvalidFormatException self, std::string const & msg) -> InvalidFormatException
        __init__(except::InvalidFormatException self, Throwable t, Context c) -> InvalidFormatException
        """
        this = _coda_except.new_InvalidFormatException(*args)
        try:
            self.this.append(this)
        except __builtin__.Exception:
            self.this = this
    __swig_destroy__ = _coda_except.delete_InvalidFormatException
    __del__ = lambda self: None

    def getType(self):
        """getType(InvalidFormatException self) -> std::string"""
        return _coda_except.InvalidFormatException_getType(self)

InvalidFormatException_swigregister = _coda_except.InvalidFormatException_swigregister
InvalidFormatException_swigregister(InvalidFormatException)

class IndexOutOfRangeException(Exception):
    """Proxy of C++ except::IndexOutOfRangeException class."""

    __swig_setmethods__ = {}
    for _s in [Exception]:
        __swig_setmethods__.update(getattr(_s, '__swig_setmethods__', {}))
    __setattr__ = lambda self, name, value: _swig_setattr(self, IndexOutOfRangeException, name, value)
    __swig_getmethods__ = {}
    for _s in [Exception]:
        __swig_getmethods__.update(getattr(_s, '__swig_getmethods__', {}))
    __getattr__ = lambda self, name: _swig_getattr(self, IndexOutOfRangeException, name)
    __repr__ = _swig_repr

    def __init__(self, *args):
        """
        __init__(except::IndexOutOfRangeException self) -> IndexOutOfRangeException
        __init__(except::IndexOutOfRangeException self, Context c) -> IndexOutOfRangeException
        __init__(except::IndexOutOfRangeException self, std::string const & msg) -> IndexOutOfRangeException
        __init__(except::IndexOutOfRangeException self, Throwable t, Context c) -> IndexOutOfRangeException
        """
        this = _coda_except.new_IndexOutOfRangeException(*args)
        try:
            self.this.append(this)
        except __builtin__.Exception:
            self.this = this
    __swig_destroy__ = _coda_except.delete_IndexOutOfRangeException
    __del__ = lambda self: None

    def getType(self):
        """getType(IndexOutOfRangeException self) -> std::string"""
        return _coda_except.IndexOutOfRangeException_getType(self)

IndexOutOfRangeException_swigregister = _coda_except.IndexOutOfRangeException_swigregister
IndexOutOfRangeException_swigregister(IndexOutOfRangeException)

class OutOfMemoryException(Exception):
    """Proxy of C++ except::OutOfMemoryException class."""

    __swig_setmethods__ = {}
    for _s in [Exception]:
        __swig_setmethods__.update(getattr(_s, '__swig_setmethods__', {}))
    __setattr__ = lambda self, name, value: _swig_setattr(self, OutOfMemoryException, name, value)
    __swig_getmethods__ = {}
    for _s in [Exception]:
        __swig_getmethods__.update(getattr(_s, '__swig_getmethods__', {}))
    __getattr__ = lambda self, name: _swig_getattr(self, OutOfMemoryException, name)
    __repr__ = _swig_repr

    def __init__(self, *args):
        """
        __init__(except::OutOfMemoryException self) -> OutOfMemoryException
        __init__(except::OutOfMemoryException self, Context c) -> OutOfMemoryException
        __init__(except::OutOfMemoryException self, std::string const & msg) -> OutOfMemoryException
        __init__(except::OutOfMemoryException self, Throwable t, Context c) -> OutOfMemoryException
        """
        this = _coda_except.new_OutOfMemoryException(*args)
        try:
            self.this.append(this)
        except __builtin__.Exception:
            self.this = this
    __swig_destroy__ = _coda_except.delete_OutOfMemoryException
    __del__ = lambda self: None

    def getType(self):
        """getType(OutOfMemoryException self) -> std::string"""
        return _coda_except.OutOfMemoryException_getType(self)

OutOfMemoryException_swigregister = _coda_except.OutOfMemoryException_swigregister
OutOfMemoryException_swigregister(OutOfMemoryException)

class NullPointerReferenceException(Exception):
    """Proxy of C++ except::NullPointerReferenceException class."""

    __swig_setmethods__ = {}
    for _s in [Exception]:
        __swig_setmethods__.update(getattr(_s, '__swig_setmethods__', {}))
    __setattr__ = lambda self, name, value: _swig_setattr(self, NullPointerReferenceException, name, value)
    __swig_getmethods__ = {}
    for _s in [Exception]:
        __swig_getmethods__.update(getattr(_s, '__swig_getmethods__', {}))
    __getattr__ = lambda self, name: _swig_getattr(self, NullPointerReferenceException, name)
    __repr__ = _swig_repr

    def __init__(self, *args):
        """
        __init__(except::NullPointerReferenceException self) -> NullPointerReferenceException
        __init__(except::NullPointerReferenceException self, Context c) -> NullPointerReferenceException
        __init__(except::NullPointerReferenceException self, std::string const & msg) -> NullPointerReferenceException
        __init__(except::NullPointerReferenceException self, Throwable t, Context c) -> NullPointerReferenceException
        """
        this = _coda_except.new_NullPointerReferenceException(*args)
        try:
            self.this.append(this)
        except __builtin__.Exception:
            self.this = this
    __swig_destroy__ = _coda_except.delete_NullPointerReferenceException
    __del__ = lambda self: None

    def getType(self):
        """getType(NullPointerReferenceException self) -> std::string"""
        return _coda_except.NullPointerReferenceException_getType(self)

NullPointerReferenceException_swigregister = _coda_except.NullPointerReferenceException_swigregister
NullPointerReferenceException_swigregister(NullPointerReferenceException)

class NoSuchKeyException(Exception):
    """Proxy of C++ except::NoSuchKeyException class."""

    __swig_setmethods__ = {}
    for _s in [Exception]:
        __swig_setmethods__.update(getattr(_s, '__swig_setmethods__', {}))
    __setattr__ = lambda self, name, value: _swig_setattr(self, NoSuchKeyException, name, value)
    __swig_getmethods__ = {}
    for _s in [Exception]:
        __swig_getmethods__.update(getattr(_s, '__swig_getmethods__', {}))
    __getattr__ = lambda self, name: _swig_getattr(self, NoSuchKeyException, name)
    __repr__ = _swig_repr

    def __init__(self, *args):
        """
        __init__(except::NoSuchKeyException self) -> NoSuchKeyException
        __init__(except::NoSuchKeyException self, Context c) -> NoSuchKeyException
        __init__(except::NoSuchKeyException self, std::string const & msg) -> NoSuchKeyException
        __init__(except::NoSuchKeyException self, Throwable t, Context c) -> NoSuchKeyException
        """
        this = _coda_except.new_NoSuchKeyException(*args)
        try:
            self.this.append(this)
        except __builtin__.Exception:
            self.this = this
    __swig_destroy__ = _coda_except.delete_NoSuchKeyException
    __del__ = lambda self: None

    def getType(self):
        """getType(NoSuchKeyException self) -> std::string"""
        return _coda_except.NoSuchKeyException_getType(self)

NoSuchKeyException_swigregister = _coda_except.NoSuchKeyException_swigregister
NoSuchKeyException_swigregister(NoSuchKeyException)

class NoSuchReferenceException(Exception):
    """Proxy of C++ except::NoSuchReferenceException class."""

    __swig_setmethods__ = {}
    for _s in [Exception]:
        __swig_setmethods__.update(getattr(_s, '__swig_setmethods__', {}))
    __setattr__ = lambda self, name, value: _swig_setattr(self, NoSuchReferenceException, name, value)
    __swig_getmethods__ = {}
    for _s in [Exception]:
        __swig_getmethods__.update(getattr(_s, '__swig_getmethods__', {}))
    __getattr__ = lambda self, name: _swig_getattr(self, NoSuchReferenceException, name)
    __repr__ = _swig_repr

    def __init__(self, *args):
        """
        __init__(except::NoSuchReferenceException self) -> NoSuchReferenceException
        __init__(except::NoSuchReferenceException self, Context c) -> NoSuchReferenceException
        __init__(except::NoSuchReferenceException self, std::string const & msg) -> NoSuchReferenceException
        __init__(except::NoSuchReferenceException self, Throwable t, Context c) -> NoSuchReferenceException
        """
        this = _coda_except.new_NoSuchReferenceException(*args)
        try:
            self.this.append(this)
        except __builtin__.Exception:
            self.this = this
    __swig_destroy__ = _coda_except.delete_NoSuchReferenceException
    __del__ = lambda self: None

    def getType(self):
        """getType(NoSuchReferenceException self) -> std::string"""
        return _coda_except.NoSuchReferenceException_getType(self)

NoSuchReferenceException_swigregister = _coda_except.NoSuchReferenceException_swigregister
NoSuchReferenceException_swigregister(NoSuchReferenceException)

class KeyAlreadyExistsException(Exception):
    """Proxy of C++ except::KeyAlreadyExistsException class."""

    __swig_setmethods__ = {}
    for _s in [Exception]:
        __swig_setmethods__.update(getattr(_s, '__swig_setmethods__', {}))
    __setattr__ = lambda self, name, value: _swig_setattr(self, KeyAlreadyExistsException, name, value)
    __swig_getmethods__ = {}
    for _s in [Exception]:
        __swig_getmethods__.update(getattr(_s, '__swig_getmethods__', {}))
    __getattr__ = lambda self, name: _swig_getattr(self, KeyAlreadyExistsException, name)
    __repr__ = _swig_repr

    def __init__(self, *args):
        """
        __init__(except::KeyAlreadyExistsException self) -> KeyAlreadyExistsException
        __init__(except::KeyAlreadyExistsException self, Context c) -> KeyAlreadyExistsException
        __init__(except::KeyAlreadyExistsException self, std::string const & msg) -> KeyAlreadyExistsException
        __init__(except::KeyAlreadyExistsException self, Throwable t, Context c) -> KeyAlreadyExistsException
        """
        this = _coda_except.new_KeyAlreadyExistsException(*args)
        try:
            self.this.append(this)
        except __builtin__.Exception:
            self.this = this
    __swig_destroy__ = _coda_except.delete_KeyAlreadyExistsException
    __del__ = lambda self: None

    def getType(self):
        """getType(KeyAlreadyExistsException self) -> std::string"""
        return _coda_except.KeyAlreadyExistsException_getType(self)

KeyAlreadyExistsException_swigregister = _coda_except.KeyAlreadyExistsException_swigregister
KeyAlreadyExistsException_swigregister(KeyAlreadyExistsException)

class NotImplementedException(Exception):
    """Proxy of C++ except::NotImplementedException class."""

    __swig_setmethods__ = {}
    for _s in [Exception]:
        __swig_setmethods__.update(getattr(_s, '__swig_setmethods__', {}))
    __setattr__ = lambda self, name, value: _swig_setattr(self, NotImplementedException, name, value)
    __swig_getmethods__ = {}
    for _s in [Exception]:
        __swig_getmethods__.update(getattr(_s, '__swig_getmethods__', {}))
    __getattr__ = lambda self, name: _swig_getattr(self, NotImplementedException, name)
    __repr__ = _swig_repr

    def __init__(self, *args):
        """
        __init__(except::NotImplementedException self) -> NotImplementedException
        __init__(except::NotImplementedException self, Context c) -> NotImplementedException
        __init__(except::NotImplementedException self, std::string const & msg) -> NotImplementedException
        __init__(except::NotImplementedException self, Throwable t, Context c) -> NotImplementedException
        """
        this = _coda_except.new_NotImplementedException(*args)
        try:
            self.this.append(this)
        except __builtin__.Exception:
            self.this = this
    __swig_destroy__ = _coda_except.delete_NotImplementedException
    __del__ = lambda self: None

    def getType(self):
        """getType(NotImplementedException self) -> std::string"""
        return _coda_except.NotImplementedException_getType(self)

NotImplementedException_swigregister = _coda_except.NotImplementedException_swigregister
NotImplementedException_swigregister(NotImplementedException)

class InvalidArgumentException(Exception):
    """Proxy of C++ except::InvalidArgumentException class."""

    __swig_setmethods__ = {}
    for _s in [Exception]:
        __swig_setmethods__.update(getattr(_s, '__swig_setmethods__', {}))
    __setattr__ = lambda self, name, value: _swig_setattr(self, InvalidArgumentException, name, value)
    __swig_getmethods__ = {}
    for _s in [Exception]:
        __swig_getmethods__.update(getattr(_s, '__swig_getmethods__', {}))
    __getattr__ = lambda self, name: _swig_getattr(self, InvalidArgumentException, name)
    __repr__ = _swig_repr

    def __init__(self, *args):
        """
        __init__(except::InvalidArgumentException self) -> InvalidArgumentException
        __init__(except::InvalidArgumentException self, Context c) -> InvalidArgumentException
        __init__(except::InvalidArgumentException self, std::string const & msg) -> InvalidArgumentException
        __init__(except::InvalidArgumentException self, Throwable t, Context c) -> InvalidArgumentException
        """
        this = _coda_except.new_InvalidArgumentException(*args)
        try:
            self.this.append(this)
        except __builtin__.Exception:
            self.this = this
    __swig_destroy__ = _coda_except.delete_InvalidArgumentException
    __del__ = lambda self: None

    def getType(self):
        """getType(InvalidArgumentException self) -> std::string"""
        return _coda_except.InvalidArgumentException_getType(self)

InvalidArgumentException_swigregister = _coda_except.InvalidArgumentException_swigregister
InvalidArgumentException_swigregister(InvalidArgumentException)

class SerializationException(IOException):
    """Proxy of C++ except::SerializationException class."""

    __swig_setmethods__ = {}
    for _s in [IOException]:
        __swig_setmethods__.update(getattr(_s, '__swig_setmethods__', {}))
    __setattr__ = lambda self, name, value: _swig_setattr(self, SerializationException, name, value)
    __swig_getmethods__ = {}
    for _s in [IOException]:
        __swig_getmethods__.update(getattr(_s, '__swig_getmethods__', {}))
    __getattr__ = lambda self, name: _swig_getattr(self, SerializationException, name)
    __repr__ = _swig_repr

    def __init__(self, *args):
        """
        __init__(except::SerializationException self) -> SerializationException
        __init__(except::SerializationException self, Context c) -> SerializationException
        __init__(except::SerializationException self, std::string const & msg) -> SerializationException
        __init__(except::SerializationException self, Throwable t, Context c) -> SerializationException
        """
        this = _coda_except.new_SerializationException(*args)
        try:
            self.this.append(this)
        except __builtin__.Exception:
            self.this = this
    __swig_destroy__ = _coda_except.delete_SerializationException
    __del__ = lambda self: None

    def getType(self):
        """getType(SerializationException self) -> std::string"""
        return _coda_except.SerializationException_getType(self)

SerializationException_swigregister = _coda_except.SerializationException_swigregister
SerializationException_swigregister(SerializationException)

class ParseException(IOException):
    """Proxy of C++ except::ParseException class."""

    __swig_setmethods__ = {}
    for _s in [IOException]:
        __swig_setmethods__.update(getattr(_s, '__swig_setmethods__', {}))
    __setattr__ = lambda self, name, value: _swig_setattr(self, ParseException, name, value)
    __swig_getmethods__ = {}
    for _s in [IOException]:
        __swig_getmethods__.update(getattr(_s, '__swig_getmethods__', {}))
    __getattr__ = lambda self, name: _swig_getattr(self, ParseException, name)
    __repr__ = _swig_repr

    def __init__(self, *args):
        """
        __init__(except::ParseException self) -> ParseException
        __init__(except::ParseException self, Context c) -> ParseException
        __init__(except::ParseException self, std::string const & msg) -> ParseException
        __init__(except::ParseException self, Throwable t, Context c) -> ParseException
        """
        this = _coda_except.new_ParseException(*args)
        try:
            self.this.append(this)
        except __builtin__.Exception:
            self.this = this
    __swig_destroy__ = _coda_except.delete_ParseException
    __del__ = lambda self: None

    def getType(self):
        """getType(ParseException self) -> std::string"""
        return _coda_except.ParseException_getType(self)

ParseException_swigregister = _coda_except.ParseException_swigregister
ParseException_swigregister(ParseException)

# This file is compatible with both classic and new-style classes.


