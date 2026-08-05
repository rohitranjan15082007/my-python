physic = int(input("Enter your physics marks: "))
chemistry = int(input("Enter your chemistry marks: "))
biology = int(input("Enter your biology marks: "))
if physic >=45 and chemistry >=45 and biology >=45:
    print("You are pass in all subjects.")
elif physic < 45 and chemistry >=45 and biology >=45:
    print("You are fail in physics.")
elif physic >=45 and chemistry < 45 and biology >=45:
    print("You are fail in chemistry.")
elif physic >=45 and chemistry >=45 and biology < 45:
    print("You are fail in biology.")
elif physic < 45 and chemistry < 45 and biology >=45:
    print("You are fail in physics and chemistry.")
elif physic < 45 and chemistry >=45 and biology < 45:
    print("You are fail in physics and biology.")
elif physic >=45 and chemistry < 45 and biology < 45:
    print("You are fail in chemistry and biology.")
elif physic < 45 and chemistry < 45 and biology < 45:
    print("You are fail in all subjects.")
