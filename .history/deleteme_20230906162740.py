


def parse(filter_obj):
    if type(filter_obj) == dict:
        for key in filter_obj:
            
            if type(filter_obj) is not dict:
                if filter_obj[key][0] == "_":
                    return filter_obj[key]
            
            condition = parse(filter_obj[key])
            for key in condition:
                if key == "_eq":
                    return f"[?{key}=='{filter_obj[key]}']"
                elif key == "_in":
                    conditions = []
                    for val in filter_obj[key]:
                        conditions.append(f"{key}=='{val}'")
                    condition = " || ".join(conditions)
                    return f"[?{condition}]"

            res = "[].%s%s" % (key, parse(filter_obj[key]))
            return res
        
        
print(
    parse({"categories":{"controls":{"name":{"_eq": "HELLO"}}}})
)