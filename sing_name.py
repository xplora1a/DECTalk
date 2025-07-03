#! /bin/python3

def sing_name(name: str) -> str:
    """
    Generate a DECTalk command to string sing a name.
    
    Args:
        name (str): The name to be sung.
        
    Returns:
        str: A DECTalk command string to sing the name.
    """
    # Ensure the name is a string and strip any leading/trailing whitespace
    name = str(name).strip()
    name = name.lower()
    # divide into two parts and add the note encoding
    sing = "["+name[:(len(name)+1)//2] + "<600,14>" + name[(len(name)-1)//2:] + "<600,12>]"

    return sing

# Example usage:
if __name__ == "__main__":
    print(f"DECTalk command to sing Peter: {sing_name('Peter')}")
    print(f"DECTalk command to sing John: {sing_name('John')}")
    print(f"DECTalk command to sing Alice: {sing_name('Alice')}")

    # Output: DECTalk command to sing 'John': [Jo<600,14>hn<600,12>]
