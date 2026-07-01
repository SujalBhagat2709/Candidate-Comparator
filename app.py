from comparator import CandidateComparator


class CandidateComparatorApp:

    def __init__(self):

        self.engine = CandidateComparator()

    def menu(self):

        while True:

            print("\n")

            print("=" * 40)

            print("      CANDIDATE COMPARATOR")

            print("=" * 40)

            print("1. Add Candidate")

            print("2. View Candidates")

            print("3. Compare Candidates")

            print("4. Remove Candidate")

            print("5. Exit")

            choice = input("\nEnter Choice: ")

            if choice == "1":

                try:

                    self.engine.add_candidate()

                except ValueError:

                    print("\nInvalid Input.")

            elif choice == "2":

                self.engine.view_candidates()

            elif choice == "3":

                self.engine.compare_candidates()

            elif choice == "4":

                self.engine.remove_candidate()

            elif choice == "5":

                print("\nThank You!")

                break

            else:

                print("\nInvalid Choice.")


if __name__ == "__main__":

    app = CandidateComparatorApp()

    app.menu()