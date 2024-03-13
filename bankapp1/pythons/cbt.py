import time


class ChemistryExam:
    '''A class to represent a Chemistry CBT Exam System.'''

    def __init__(self, questions, student_name,time_limit):
        
        self.questions = questions
        self.student_name = student_name
        self.score = 0
        self.total_questions = len(questions)
        self.time_limit = time_limit * 60

    def take_exam(self):
        '''Simulate taking the exam by asking each question and checking the answers.'''
        for question in self.questions:
            print(question['question'])
            answer = input('Enter your answer: ')
            if answer.lower() == question['answer'].lower():
                self.score += 1
        self.display_score()

    def display_score(self):
        '''Display the student's score after completing the exam.'''
        print(f"{self.student_name}, your score is {self.score}/{self.total_questions}.")

def main():
   
    questions = [
     {'question': 'What is the atomic number of hydrogen?', 'answer': '1'},
     {'question': 'What is the formula for water?', 'answer': 'H2O'},
     {'question': 'What is the pH level of a neutral substance?', 'answer': '7'},
     {'question': 'What is the chemical symbol for sodium?', 'answer': 'Na'},
     {'question': 'What type of bond is formed when electrons are shared between atoms?', 'answer': 'Covalent bond'},
     {'question': 'What is the molar mass of carbon dioxide (CO2)?', 'answer': '44.01 g/mol'},
     {'question': 'What is the main component of natural gas?', 'answer': 'Methane'},
     {'question': 'What is the name given to the elements in Group 1 of the periodic table?', 'answer': 'Alkali metals'},
     {'question': 'What is the standard state of oxygen at room temperature?', 'answer': 'Gas'},
     {'question': 'What is the common name for dihydrogen monoxide?', 'answer': 'Water'},
     {'question': 'What is the name of the process where solid turns directly into gas?', 'answer': 'Sublimation'},
     {'question': 'What is the main type of intermolecular force in water?', 'answer': 'Hydrogen bonding'},
     {'question': 'What is the chemical formula for ammonia?', 'answer': 'NH3'},
     {'question': 'What is the principle quantum number?', 'answer': 'It indicates the main energy level occupied by the electron'},
     {'question': 'What is the term for the amount of substance that contains as many particles as there are atoms in 12g of carbon-12?', 'answer': 'Mole'},
     {'question': 'What is the name given to the electrons in the outermost shell of an atom?', 'answer': 'Valence electrons'},
     {'question': 'What is the pH of a solution with a hydrogen ion concentration of 1 x 10^-4 M?', 'answer': '4'},
     {'question': 'What is the name of the compound with the formula NaHCO3?', 'answer': 'Sodium bicarbonate'},
     {'question': 'What type of reaction occurs when an acid reacts with a base?', 'answer': 'Neutralization'},
     {'question': 'What is the law that states that mass is neither created nor destroyed in a chemical reaction?', 'answer': 'Law of Conservation of Mass'},
     {'question': 'What is the name of the compound with the formula \( KNO_3 \)?', 'answer': 'Potassium nitrate'},
     {'question': 'What is the term for the smallest particle of a compound that retains the properties of the compound?', 'answer': 'Molecule'},
     {'question': 'What is the name of the \( -OH \) functional group in organic chemistry?', 'answer': 'Hydroxyl group'},
     {'question': 'What is the name of the process by which plants convert carbon dioxide and water into glucose and oxygen?', 'answer': 'Photosynthesis'},
     {'question': 'What is the chemical formula for glucose?', 'answer': 'C6H12O6'},
     {'question': 'What is the name of the law that states that the total pressure of a mixture of gases is equal to the sum of the pressures of each individual gas?', 'answer': 'Dalton\'s law of partial pressures'},
     {'question': 'What is the term for a reaction in which an element displaces another element in a compound?', 'answer': 'Single displacement reaction'},
     {'question': 'What is the name of the \( SiO_2 \) compound, commonly found in sand?', 'answer': 'Silicon dioxide'},
     {'question': 'What is the term for the amount of energy required to raise the temperature of one gram of water by one degree Celsius?', 'answer': 'Calorie'},
     {'question': 'What is the name of the \( H_2SO_4 \) compound?', 'answer': 'Sulfuric acid'},
     {'question': 'What is the name of the \( C_6H_6 \) compound?', 'answer': 'Benzene'},
     {'question': 'What is the term for the separation of a chemical compound into its individual ions in water?', 'answer': 'Dissociation'},
     {'question': 'What is the name of the \( HNO_3 \) compound?', 'answer': 'Nitric acid'},
     {'question': 'What is the term for the amount of solute needed to make a saturated solution in a given quantity of solvent at a certain temperature?', 'answer': 'Solubility'},
     {'question': 'What is the name of the \( CH_4 \) compound?', 'answer': 'Methane'},
     {'question': 'What is the term for the mass of one mole of a substance?', 'answer': 'Molar mass'},
     {'question': 'What is the name of the \( CH_3COOH \) compound?', 'answer': 'Acetic acid'},
     {'question': 'What is the term for the number of protons in the nucleus of an atom?', 'answer': 'Atomic number'},
     {'question': 'What is the name of the \( NaCl \) compound?', 'answer': 'Sodium chloride'},
     {'question': 'What is the term for the simplest whole number ratio of atoms in a compound?', 'answer': 'Empirical formula'},
     {'question': 'What is the name of the \( CaCO_3 \) compound?', 'answer': 'Calcium carbonate'},
     {'question': 'What is the term for the energy change that occurs when an electron is added to a neutral atom?', 'answer': 'Electron affinity'},
     {'question': 'What is the name of the \( C_2H_5OH \) compound?', 'answer': 'Ethanol'},
     {'question': 'What is the term for the temperature and pressure at which a substance can exist in equilibrium in the liquid, solid, and gaseous states?', 'answer': 'Triple point'},
     {'question': 'What is the name of the \( H_2O_2 \) compound?', 'answer': 'Hydrogen peroxide'},
     {'question': 'What is the term for the spontaneous emission of radiation from the nucleus of an unstable atom?', 'answer': 'Radioactivity'},
     {'question': 'What is the name of the \( CO \) compound?', 'answer': 'Carbon monoxide'},
     {'question': 'What is the term for the measure of the disorder or randomness in a system?', 'answer': 'Entropy'},
     {'question': 'What is the name of the \( HCl \) compound?', 'answer': 'Hydrochloric acid'},
     {'question': 'What is the term for the reaction in which energy is absorbed?', 'answer': 'Endothermic reaction'}
]



  



    student_name = input('Enter your name: ')
    exam = ChemistryExam(questions, student_name, time_limit=20)

    print("Welcome to the Chemistry CBT Exam. You have 20 minutes to complete 50 questions.")
    exam.take_exam()

if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"An error occurred: {e}")
