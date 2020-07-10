particles = open("particles.txt", 'r')

def Magic(question):
    for particle in particles:
        question = question.replace(particle, "")
    return question
