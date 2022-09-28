import ordinal_structures as ord

omega_plus_1 = ord.Ordinal({"type": "wainer", # Wainer hierarchy
                            "base": 0, # omega
                            "sub": 0, # ignored for omega
                            "exp": 1, # default
                            "mul": 1, # default
                            "add": 1,}) # plus 1