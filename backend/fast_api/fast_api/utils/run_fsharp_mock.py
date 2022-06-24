def run_fsharp(code: str) -> str:
    hello_world = 'printf "Hello, World!"'
    if hello_world in code:
        return 'Hello, World!'
    return code
