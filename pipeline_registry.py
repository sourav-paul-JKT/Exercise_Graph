PIPELINE = []

# def register_step(priority=0):
#     def decorator(func):
#         PIPELINE.append((priority, func))
#         return func
#     return decorator

def manual_register(func, priority):
    PIPELINE.append((priority, func))

def get_ordered_pipeline():
    return [func for _, func in sorted(PIPELINE, key=lambda x: x[0])]
