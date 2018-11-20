from typing import Any, Optional, Protocol, Iterable, Text
from wsgiref.types import WSGIEnvironment, InputStream

def responder(f): ...
def get_current_url(environ, root_only: bool = ..., strip_querystring: bool = ..., host_only: bool = ...,
                    trusted_hosts: Optional[Any] = ...): ...
def host_is_trusted(hostname, trusted_list): ...
def get_host(environ, trusted_hosts: Optional[Any] = ...): ...
def get_content_length(environ: WSGIEnvironment) -> Optional[int]: ...
def get_input_stream(environ: WSGIEnvironment, safe_fallback: bool = ...) -> InputStream: ...
def get_query_string(environ): ...
def get_path_info(environ, charset: Text = ..., errors: Text = ...): ...
def get_script_name(environ, charset: Text = ..., errors: Text = ...): ...
def pop_path_info(environ, charset: Text = ..., errors: Text = ...): ...
def peek_path_info(environ, charset: Text = ..., errors: Text = ...): ...
def extract_path_info(environ_or_baseurl, path_or_url, charset: Text = ..., errors: Text = ...,
                      collapse_http_schemes: bool = ...): ...

class SharedDataMiddleware:
    app = ...  # type: Any
    exports = ...  # type: Any
    cache = ...  # type: Any
    cache_timeout = ...  # type: Any
    fallback_mimetype = ...  # type: Any
    def __init__(self, app, exports, disallow: Optional[Any] = ..., cache: bool = ..., cache_timeout=...,
                 fallback_mimetype: str = ...): ...
    def is_allowed(self, filename): ...
    def get_file_loader(self, filename): ...
    def get_package_loader(self, package, package_path): ...
    def get_directory_loader(self, directory): ...
    def generate_etag(self, mtime, file_size, real_filename): ...
    def __call__(self, environ, start_response): ...

class DispatcherMiddleware:
    app = ...  # type: Any
    mounts = ...  # type: Any
    def __init__(self, app, mounts: Optional[Any] = ...): ...
    def __call__(self, environ, start_response): ...

class ClosingIterator:
    def __init__(self, iterable, callbacks: Optional[Any] = ...): ...
    def __iter__(self): ...
    def __next__(self): ...
    def close(self): ...

class _Readable(Protocol):
    def read(self, size: int = ...) -> bytes: ...

def wrap_file(environ: WSGIEnvironment, file: _Readable, buffer_size: int = ...) -> Iterable[bytes]: ...

class FileWrapper:
    file: _Readable
    buffer_size: int
    def __init__(self, file: _Readable, buffer_size: int = ...) -> None: ...
    def close(self) -> None: ...
    def seekable(self) -> bool: ...
    def seek(self, offset: int, whence: int = ...) -> None: ...
    def tell(self) -> Optional[int]: ...
    def __iter__(self) -> FileWrapper: ...
    def __next__(self) -> bytes: ...

class _RangeWrapper:
    iterable = ...  # type: Any
    byte_range = ...  # type: Any
    start_byte = ...  # type: Any
    end_byte = ...  # type: Any
    read_length = ...  # type: Any
    seekable = ...  # type: Any
    end_reached = ...  # type: Any
    def __init__(self, iterable, start_byte: int = ..., byte_range: Optional[Any] = ...): ...
    def __iter__(self): ...
    def __next__(self): ...
    def close(self): ...

def make_line_iter(stream, limit: Optional[Any] = ..., buffer_size=..., cap_at_buffer: bool = ...): ...
def make_chunk_iter(stream, separator, limit: Optional[Any] = ..., buffer_size=..., cap_at_buffer: bool = ...): ...

class LimitedStream:
    limit = ...  # type: Any
    def __init__(self, stream, limit): ...
    def __iter__(self): ...
    @property
    def is_exhausted(self): ...
    def on_exhausted(self): ...
    def on_disconnect(self): ...
    def exhaust(self, chunk_size=...): ...
    def read(self, size: Optional[Any] = ...): ...
    def readline(self, size: Optional[Any] = ...): ...
    def readlines(self, size: Optional[Any] = ...): ...
    def tell(self): ...
    def __next__(self): ...
