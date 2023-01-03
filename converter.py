import json

# For now we will assume that the JSON is pulled manually

raw_problems = open("leetcode_problem_info.json", "r")
problems_json = json.loads(raw_problems.read())
raw_problems.close()

problems_formatted = open("leetcode_problem_dictionary.json", "w")
problems_formatted.write("{")

stat_sets = problems_json["stat_status_pairs"]

for problem in stat_sets:
    id = problem["stat"]["question_id"]
    title = problem["stat"]["question__title"]
    title_slug = problem["stat"]["question__title_slug"]
    difficulty = problem["difficulty"]["level"]
    
    json_slug = f'"{id}": {{"title": "{title}","title_slug": "{title_slug}","difficulty_level": {difficulty}}},'

    # Remove comma from final problem 
    if id == 1:
        json_slug = json_slug[:-1]

    problems_formatted.write(json_slug)

problems_formatted.write("}")
problems_formatted.close()
    

