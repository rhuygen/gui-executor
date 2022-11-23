import contextlib
import importlib
from pathlib import Path
from typing import Callable
from typing import Dict
from typing import List
from typing import Tuple

from .exec import find_modules
from .exec import find_subpackages
from .exec import find_ui_button_functions
from .exec import find_ui_recurring_functions


class Model:
    def __init__(self, module_path: str):
        self._module_path: List = module_path

    @property
    def module_path(self) -> List:
        return self._module_path

    def reload_functions(self, mod):
        ...

    def get_ui_buttons_functions(self, mod: str) -> Dict[str, Callable]:
        return find_ui_button_functions(mod)

    def get_ui_recurring_functions(self, mod: str) -> Dict[str, Callable]:
        return find_ui_recurring_functions(mod)

    def get_ui_modules(self, module_path: List = None) -> Dict[str, Tuple[str, Path]]:
        module_path: List = module_path or self._module_path
        response = {}
        for mod_path in module_path:
            for name, path in find_modules(mod_path).items():
                with contextlib.suppress(ModuleNotFoundError):
                    mod = importlib.import_module(path)
                    display_name = getattr(mod, "UI_MODULE_DISPLAY_NAME", name)
                    response[name] = (display_name, path)
        return response

    def get_ui_subpackages(self, module_path: List = None) -> Dict[str, Tuple[str, Path]]:
        module_path: List = module_path or self._module_path
        response = {}
        for mod_path in module_path:
            for name, path in find_subpackages(mod_path).items():
                mod = importlib.import_module(f"{mod_path}.{name}")
                display_name = getattr(mod, "UI_TAB_DISPLAY_NAME", name)
                response[name] = (display_name, path)
        return response
