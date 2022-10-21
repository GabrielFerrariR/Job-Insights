from src.sorting import sort_by

# essa função cria uma lista de jobs, porém por algum motivo o test
# nao consegue acessar os jobs
# def create_job(value):
#     return {
#         "min_salary": value * 20,
#         "max_salary": value * 200,
#         "date_posted": f"200{value}-01-01"
#     }


# jobs = [create_job(i) for i in range(1, 4)]
# print(jobs)

jobs = [
    {"min_salary": 20, "max_salary": 200, "date_posted": "2001-01-01"},
    {"min_salary": 40, "max_salary": 400, "date_posted": "2002-01-01"},
    {"min_salary": 60, "max_salary": 600, "date_posted": "2003-01-01"},
]


def test_sort_by_criteria():
    sort_by(jobs, "max_salary")
    assert jobs[0]["max_salary"] == 600
    sort_by(jobs, "min_salary")
    assert jobs[0]["min_salary"] == 20
    sort_by(jobs, "date_posted")
    assert jobs[0]["date_posted"] == "2003-01-01"
