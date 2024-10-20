def alumne_schema(student) -> dict:
    return {"NomAlumne": student[0],
            "Cicle": student[1],
            "Curs": student[2],
            "Grup": student[3],
            "DescAula": student[4]
            }


def alumnes_schema(alumnes) -> dict:
    return [alumne_schema(alumne) for alumne in alumnes]