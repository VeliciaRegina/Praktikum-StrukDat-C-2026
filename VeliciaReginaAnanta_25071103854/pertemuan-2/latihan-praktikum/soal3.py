tim_frontend = {"HTML", "CSS", "JavaScript", "React"}
tim_backend = {"Python", "JavaScript", "SQL",
"NodeJS"}

keahlian = tim_frontend.intersection(tim_backend)
print(keahlian)

onlyBackEnd = tim_backend.difference(tim_frontend)
print(onlyBackEnd)

set3 = tim_frontend.union(tim_backend)
print(set3)