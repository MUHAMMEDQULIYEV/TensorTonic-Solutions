

def encode(text: str, merges: list[list[int]]) -> list[int]:
    """
    Returns token IDs after applying the ordered merge rules.
"""
    text_tokenize=list(text.encode("utf-8"))
    for left, right, new_id in merges:
       i=0
       ids=[]
       while i<len(text_tokenize):
          if i<len(text_tokenize)-1 and (text_tokenize[i],text_tokenize[i+1])==(left,right):
            ids.append(new_id)
            i+=2
            
          else:
            ids.append(text_tokenize[i])
            i+=1
       text_tokenize=ids    
    return text_tokenize
        
def decode(ids: list[int], vocab: dict[int, list[int]]) -> str:
    """
    Returns the text reconstructed from the token bytes.
    """
    ls=[]
    for i in ids:
        ls=ls+vocab[i]
    return bytes(ls).decode("utf-8")
