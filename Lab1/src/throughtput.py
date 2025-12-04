last_arrival_time = None
total_time_ms = 0
total_payload_size = 0

stats = open("stats.txt", "r").readlines()
stats = [eval(x) for x in stats]
for json_data in stats:
    arrivalTimeMs = json_data["arrival_time_ms"]
    payloadSize = json_data["payload_size"]

    total_payload_size += int(payloadSize)
    if last_arrival_time is None:
        last_arrival_time = arrivalTimeMs
    total_time_ms += arrivalTimeMs - last_arrival_time
    last_arrival_time = arrivalTimeMs

print(total_payload_size * 1000 / total_time_ms) # bytes per ms