def parsed(_measure):
    _measure = _measure.split(" ")
    feet = float(_measure[0])
    inches = float(_measure[1])
    return {'feet': feet, 'inches': inches}
