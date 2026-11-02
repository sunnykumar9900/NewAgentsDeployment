from app.agents.job_agent import search_jobs

if __name__ == "__main__":
    skills = input("Enter your skills: ")

    result = search_jobs(skills)

    print("\n===== JOB SEARCH RESULTS =====\n")
    print(result)