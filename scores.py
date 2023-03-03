def read_scores_file(filename):
    # Define the weights for each category
    exam_weight = 0.25
    assignment_weight = 0.25
    midterm_weight = 0.25
    final_weight = 0.25
    
    # Read the file line by line
    with open(filename) as f:
        lines = f.readlines()
    
    # Parse the lines and calculate the total score for each student
    scores = []
    for line in lines:
        # Split the line into fields
        fields = line.strip().split(",")
        name = fields[0]
        exams = sorted([float(x) for x in fields[1:7]])[2:]
        assignments = sorted([float(x) for x in fields[7:11]])[1:]
        midterm = float(fields[11])
        final = float(fields[12])
        
        # Calculate the category scores
        exam_score = sum(exams) / len(exams) * 100 * exam_weight
        assignment_score = sum(assignments) / len(assignments) * 100 * assignment_weight
        midterm_score = midterm * 100 * midterm_weight
        final_score = final * 100 * final_weight
        
        # Calculate the total score from 100 point score!
        total_score = (exam_score + assignment_score + midterm_score + final_score)/20
        
        # Add the score to the list
        scores.append((name, total_score))
    
    return scores

scores = read_scores_file("c:/Users/Hossein/Desktop/py/scores.txt")
for name, score in scores:
    if score<60:
        print(f"{name}: {score} , Failed!")
    else:
        print(f"{name}: {score} , Pass!")


