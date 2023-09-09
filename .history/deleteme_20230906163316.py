


def parse(filter_obj):
    
    if type(filter_obj) is not dict:
        return filter_obj
        
    for key in filter_obj:
        condition = parse(filter_obj[key])
    
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
    parse({"categories":{"name":{"_eq": "HELLO"}}})
)