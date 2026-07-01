import json
import os


class CandidateComparator:

    def __init__(self):

        self.file_name = "candidates.json"

        self.candidates = []

        self.load_data()

    def load_data(self):

        if os.path.exists(self.file_name):

            try:

                with open(

                    self.file_name,

                    "r",

                    encoding="utf-8"

                ) as file:

                    self.candidates = json.load(file)

            except:

                self.candidates = []

    def save_data(self):

        with open(

            self.file_name,

            "w",

            encoding="utf-8"

        ) as file:

            json.dump(

                self.candidates,

                file,

                indent=4

            )

    def calculate_score(

        self,

        experience,

        skills,

        projects,

        education

    ):

        score = 0

        score += min(

            experience * 10,

            40

        )

        score += min(

            skills * 5,

            30

        )

        score += min(

            projects * 3,

            20

        )

        education = education.lower()

        if education == "phd":

            score += 10

        elif education == "masters":

            score += 8

        elif education == "bachelors":

            score += 6

        else:

            score += 4

        return score

    def add_candidate(self):

        print("\nAdd Candidate\n")

        name = input(

            "Name: "

        )

        experience = int(

            input(

                "Experience (Years): "

            )

        )

        skills = int(

            input(

                "Number of Skills: "

            )

        )

        projects = int(

            input(

                "Projects Completed: "

            )

        )

        education = input(

            "Education (Diploma/Bachelors/Masters/PhD): "

        )

        score = self.calculate_score(

            experience,

            skills,

            projects,

            education

        )

        candidate = {

            "name": name,

            "experience": experience,

            "skills": skills,

            "projects": projects,

            "education": education,

            "score": score

        }

        self.candidates.append(

            candidate

        )

        self.save_data()

        print(

            "\nCandidate Added Successfully."

        )

    def view_candidates(self):

        if not self.candidates:

            print(

                "\nNo Candidates Found."

            )

            return

        print(

            "\n========== CANDIDATES ==========\n"

        )

        for candidate in self.candidates:

            print(

                "Name        :",

                candidate["name"]

            )

            print(

                "Experience  :",

                candidate["experience"],

                "Years"

            )

            print(

                "Skills      :",

                candidate["skills"]

            )

            print(

                "Projects    :",

                candidate["projects"]

            )

            print(

                "Education   :",

                candidate["education"]

            )

            print(

                "Score       :",

                candidate["score"]

            )

            print(

                "-" * 40

            )

    def compare_candidates(self):

        if len(self.candidates) < 2:

            print(

                "\nAdd at least two candidates."

            )

            return

        ranking = sorted(

            self.candidates,

            key=lambda x: x["score"],

            reverse=True

        )

        print(

            "\n========== RANKING ==========\n"

        )

        for index, candidate in enumerate(

            ranking,

            start=1

        ):

            print(

                f"Rank {index}"

            )

            print(

                "Name :", candidate["name"]

            )

            print(

                "Score:", candidate["score"]

            )

            print(

                "-" * 30

            )

    def remove_candidate(self):

        if not self.candidates:

            print(

                "\nNo Candidates Available."

            )

            return

        name = input(

            "\nCandidate Name: "

        )

        for candidate in self.candidates:

            if candidate["name"].lower() == name.lower():

                self.candidates.remove(

                    candidate

                )

                self.save_data()

                print(

                    "\nCandidate Removed."

                )

                return

        print(

            "\nCandidate Not Found."
        )