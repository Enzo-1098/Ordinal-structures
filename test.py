import ordinal_structures as ord

ten = ord.Ordinal({"type": "finite", # finite number
                            "base": 10, # it's ten
                            "sub": 0, # ignored for finite numbers
                            "exp": 1, # default
                            "mul": 1, # default
                            "add": 0,}) # ignored for finite numbers

omega_plus_1 = ord.Ordinal({"type": "wainer", # Wainer hierarchy
                            "base": 0, # omega
                            "sub": 0, # ignored for omega
                            "exp": 1, # default
                            "mul": 1, # default
                            "add": 1,}) # plus 1