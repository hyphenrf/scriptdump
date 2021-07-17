#!/usr/bin/env python3

st = "g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj."


# this functional pipeline (without imports):
def transl(s, n):
    
    def decyph(c):
        
        asc = [ chr(i) for i in range(97,123) ]
        dec = ord(c)+n
        dec = dec-123 if dec > 122 else dec-97
        
        return asc[dec] if dec in range(27) else c
    
    return "".join([ i for i in map(decyph, s) ])


trans_st = transl(st, 2)


#is equal to:
from string import ascii_lowercase as asc
trans_st_2 = st.translate(
                st.maketrans(
                        asc, asc[2:]+asc[:2] # a +2 shift
                )
             )

print(
        f"first pipeline:\n\"{trans_st}\"",
         "",
        f"second pipeline:\n\"{trans_st_2}\"",
        sep="\n"
)
