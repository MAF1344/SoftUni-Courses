def tags(tag_name):
    def decorator(func):
        def wrapper(*args, **kwargs):
            return f"<{tag_name}>{func(*args, **kwargs)}</{tag_name}>"
        return wrapper
    return decorator

@tags('p')
def join_strings(*args):
    return "".join(args)

@tags('h1')
def to_upper(text):
    return text.upper()
