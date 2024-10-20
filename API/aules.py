def aula_schema(classroom) -> dict:
    return {"IdAula": classroom[0],
            "DescAula": classroom[1],
            "Edifici": classroom[2],
            "Pis": classroom[3],
            "CreatedAt": classroom[4],
            "UpdatedAt": classroom[5] 
            }

def aules_schema(classrooms) -> dict:
    return [aula_schema(classroom) for classroom in classrooms]