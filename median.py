def checkio(data): 
    while len(data) > 2:
      max_value = max(data)
      min_value = min(data)
      data.remove(max_value)
      data.remove(min_value)
    if len(data) == 2:
        return (data[0] + data[1]) / 2.0
    return data[0]