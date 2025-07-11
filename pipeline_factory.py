import importlib.util
import os
from pipeline_registry import manual_register

PIPELINE_DIR = "pipeline"

def load_pipeline_modules():
    loaded_modules = {}
    for filename in os.listdir(PIPELINE_DIR):
        if filename.endswith(".py") and filename != "__init__.py":
            module_name = filename[:-3]
            file_path = os.path.join(PIPELINE_DIR, filename)

            spec = importlib.util.spec_from_file_location(f"{PIPELINE_DIR}.{module_name}", file_path)
            module = importlib.util.module_from_spec(spec)
            spec.loader.exec_module(module)
            loaded_modules[module_name] = module
    return loaded_modules

def build_pipeline():
    modules = load_pipeline_modules()

    manual_register(modules["addition"].add_numbers, priority=1)
    manual_register(modules["modulo"].check_addition_result, priority=2)

    manual_register(modules["multiplication"].multiply_numbers, priority=3)
    manual_register(modules["modulo"].check_multiplication_result, priority=4)
    manual_register(modules["division"].divide_numbers, priority=5)

    return modules
