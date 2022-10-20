from src.jobs import read


def get_unique_job_types(path):
    jobList = read(path)
    jobTypeSet = {jobs["job_type"] for jobs in jobList}
    # jobTypeSet = set()
    # for jobs in jobList:
    #     jobTypeSet.add(jobs['job_type'])
    return jobTypeSet


def filter_by_job_type(jobs, job_type):
    return [job for job in jobs if job["job_type"] == job_type]


def get_unique_industries(path):
    jobList = read(path)
    jobIndustries = {
        jobs["industry"] for jobs in jobList if len(jobs["industry"]) > 0
    }
    # print(jobIndustries)
    return jobIndustries


def filter_by_industry(jobs, industry):
    return [job for job in jobs if job["industry"] == industry]


def get_max_salary(path):
    jobList = read(path)
    jobSalaries = [
        int(salary["max_salary"])
        for salary in jobList
        if len(salary["max_salary"]) > 0 and salary["max_salary"] != "invalid"
    ]
    return max(jobSalaries)


def get_min_salary(path):
    jobList = read(path)
    jobSalaries = [
        int(salary["min_salary"])
        for salary in jobList
        if len(salary["min_salary"]) > 0 and salary["min_salary"] != "invalid"
    ]
    return min(jobSalaries)


def it_min_and_max_salary_exists(job):
    if "min_salary" not in job or "max_salary" not in job:
        raise ValueError("One of the ranges doesn't exists")


def is_numeric_value_range_salary(job):
    if (
        not str(job["min_salary"]).isnumeric()
        or not str(job["max_salary"]).isnumeric()
    ):
        raise ValueError("One of the ranges is non-numeric")


def does_salary_range_makes_sense(job):
    if job["min_salary"] > job["max_salary"]:
        raise ValueError("Min value is greater than max")


def is_numeric_value_salary(salary):
    if type(salary) != int:
        raise ValueError("Non numeric salary")


def matches_salary_range(job, salary):
    """Checks if a given salary is in the salary range of a given job

    Parameters
    ----------
    job : dict
        The job with `min_salary` and `max_salary` keys
    salary : int
        The salary to check if matches with salary range of the job

    Returns
    -------
    bool
        True if the salary is in the salary range of the job, False otherwise

    Raises
    ------
    ValueError
        If `job["min_salary"]` or `job["max_salary"]` doesn't exists
        If `job["min_salary"]` or `job["max_salary"]` aren't valid integers
        If `job["min_salary"]` is greather than `job["max_salary"]`
        If `salary` isn't a valid integer
    """
    it_min_and_max_salary_exists(job)
    is_numeric_value_range_salary(job)
    does_salary_range_makes_sense(job)
    is_numeric_value_salary(salary)
    if job["min_salary"] <= salary <= job["max_salary"]:
        return True
    return False


def filter_by_salary_range(jobs, salary):
    """Filters a list of jobs by salary range

    Parameters
    ----------
    jobs : list
        The jobs to be filtered
    salary : int
        The salary to be used as filter

    Returns
    -------
    list
        Jobs whose salary range contains `salary`
    """
    return []
