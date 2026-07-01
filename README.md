# Candidate Comparator

## Overview

Candidate Comparator is a terminal-based Python application that helps recruiters compare multiple candidates based on experience, skills, projects, and education.

The application automatically calculates a score, ranks candidates, and stores all candidate information in a JSON file.

---

## Features

- Add Candidate
- Automatic Candidate Scoring
- Compare Multiple Candidates
- Candidate Ranking
- View Candidate Details
- Remove Candidate
- Automatic JSON Storage

---

## Project Structure

candidate-comparator/

├── comparator.py

├── app.py

├── README.md

└── .gitignore

---

## Requirements

Python 3.x

No external libraries required.

---

## Run

```bash
python app.py
```

---

## Menu

```
1. Add Candidate

2. View Candidates

3. Compare Candidates

4. Remove Candidate

5. Exit
```

---

## Example

Candidate 1

```
Name : Rahul

Experience : 4

Skills : 8

Projects : 5

Education : Bachelors
```

Score

```
91
```

Candidate 2

```
Name : Priya

Experience : 6

Skills : 10

Projects : 7

Education : Masters
```

Score

```
98
```

---

## Ranking

```
Rank 1

Priya

Score : 98

----------------------

Rank 2

Rahul

Score : 91
```

---

## Generated File

```
candidates.json
```

Example

```json
[
    {
        "name":"Rahul",
        "experience":4,
        "skills":8,
        "projects":5,
        "education":"Bachelors",
        "score":91
    },
    {
        "name":"Priya",
        "experience":6,
        "skills":10,
        "projects":7,
        "education":"Masters",
        "score":98
    }
]
```

---

## Scoring Logic

| Category | Maximum Score |
|-----------|--------------:|
| Experience | 40 |
| Skills | 30 |
| Projects | 20 |
| Education | 10 |

Maximum Score = **100**

---

## Future Improvements

- Resume PDF Parsing
- Job Description Matching
- Missing Skill Detection
- Candidate Filtering
- Candidate Search
- CSV Import / Export
- Recruiter Notes
- AI Skill Recommendation
- Interview Recommendation
- ATS Score
- Recruiter Dashboard

---

## License

MIT License