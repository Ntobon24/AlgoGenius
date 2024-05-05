def bucket_sort(arr, key):
    # Crear un diccionario para almacenar las cubetas
    buckets = {}

    # Agregar elementos a las cubetas
    for item in arr:
        bucket_key = item[key]
        if bucket_key in buckets:
            buckets[bucket_key].append(item)
        else:
            buckets[bucket_key] = [item]

    # Ordenar las cubetas y concatenarlas
    sorted_arr = []
    for bucket_key in sorted(buckets.keys()):
        sorted_arr.extend(buckets[bucket_key])

    # Actualizar la lista original
    arr[:] = sorted_arr
