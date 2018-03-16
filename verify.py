# PURPOSE: Verify numerical representations of binary operators form
# groups with a given set. Report which group properties pass and fail.
# AUTHOR: Andre' Green

import convert as cnvt
S = [0,1,2,3,4]
base = len(S)

# Multiple functions can be entered. Here, one which forms a group with the set,
# and one that comes close but doesn't satisfy associativity.
fns = ['0123412340234013401240123','0123412340234113401240123']
for fn in fns:

    # Closure: All outputs of fn are elements of S.
    closure = all([int(e) in S for e in fn])

    # Associativity: For all a,b,c in S,
    # fn(a,fn(b,c)) = fn(fn(a,b),c))
    associative = True
    for a in S:
        for b in S:
            for c in S:
                ab = str(a)+str(b)
                fn_ab = fn[ cnvt.s2n(ab,base) ]
                fn_fn_ab_c = fn[ cnvt.s2n(fn_ab+str(c),base) ]
                ab_c = fn_fn_ab_c

                bc = str(b)+str(c)
                fn_bc = fn[ cnvt.s2n(bc,base) ]
                fn_a_fn_bc = fn[ cnvt.s2n(str(a)+fn_bc,base) ]
                a_bc = fn_a_fn_bc

                if ab_c != a_bc:
                    associative = False

    # Identity: For all a in S, there exists k
    # s.t. fn(a,k) = fn(k,a) = a
    has_identity = False
    for p_i in S: # Potential identity
        p_i_works = True
        for a in S:
            p_ia = fn[ cnvt.s2n(str(p_i)+str(a), base) ]
            ap_i = fn[ cnvt.s2n(str(a)+str(p_i), base) ]
            if cnvt.s2n(p_ia,base) != a or cnvt.s2n(ap_i,base) != a:
                p_i_works = False
        if p_i_works:
            has_identity = True
            identity = p_i
            break

    # Inverses: For all a in S, there exists B such that
    # fn(a,b) = fn(b,a) = k, where k is the identity.
    invertible = has_identity
    if has_identity:
        for a in S:
            a_has_identity = False
            for b in S:
                ab = fn[ cnvt.s2n(str(a)+str(b),base)]
                ba = fn[ cnvt.s2n(str(b)+str(a),base)]
                if cnvt.s2n(ab,base) == identity and cnvt.s2n(ba,base) == identity:
                    a_has_identity = True
            if not a_has_identity:
                invertible = False
                break

    # Print the function in its natural base.
    properties = [closure,associative,has_identity,invertible]
    print(fn,'\t',properties,"\t*" if all(properties) else "")
