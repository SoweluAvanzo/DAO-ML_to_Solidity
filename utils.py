def camel_case( s):
    # Join the string, ensuring the first letter is lowercase
    return s.title().replace(" ", "").replace("-", "").replace("_", "")

def to_keyword(name:str):
    return name.replace(" ", "_").lower()
