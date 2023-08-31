def pipe(*funcs):
    def pipeline(data):
        for func in funcs:
            data = func(data)
            if data is None:
                break
        return data

    return pipeline
