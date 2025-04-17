# Assignment3test
 KISS – Keep It Simple, Stupid
I kept all aspects direct and easy to understand. All functions remain brief and easy to understand. Each check within the requisition system (such as whether the total amount is below a certain threshold) depends on a single if statement without any unnecessary additional programming.

 DRY – Don’t Repeat Yourself
Depictions of identical logics were eliminated from my codebase. Each printing of requisition information requires a single function to carry out treatment. The function exists in one location for all print modifications so I do not need to update it multiple times.

 SRP – Single Responsibility Principle
The application programming code contains functions consisting of single tasks. The function responsible for approval validations prevents printing operations. The function dedicated to displaying info is separate from both total computation and approval verification. Each one sticks to its role.

 Open/Closed Principle
This code contains features that let it handle new functions effectively as it expands. The system enables me to create new functions containing approval rules without making any changes to existing functions.

 Composition Over Inheritance 
I adopted a similar approach in my project despite not applying actual classes since I split tasks into small components which used reusable functions rather than grouping everything within one area.

 Separation of Concerns
Each script functions for an explicit reason. Each script has a dedicated function that either performs approvals or works with display logic or input processing or calculation functions. Fixes or updates performed on a single part become easier because they do not require modifications throughout the entire program.

The principle YAGNI dictates that we only create what we need now because extra features are unnecessary.
All the features I integrated served direct purposes I would use. No extra functions, no unused variables. The exact tools which perfectly suited my current work requirements.

 Avoid Premature Optimization
The logic needed to function properly before any optimization attempts focusing on speedup or output reduction were made. I finished program testing before improving its readability through code reorganization for better appearance and comprehension.

 Refactor and Clean Code
I returned to modify the code I had already written. The code received its naming improvements and unnecessary lines got removed while maintaining proper organization. I adopted names which offer effortless understanding for any person who reviews the code.
