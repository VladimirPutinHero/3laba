def Rere(filename):
    with open(filename, 'r') as file:
        gl = 0
        sgl = 0
        for char in filename:
            if char.isalpha():
                if char.lower() in "eyuioa":
                    gl +=1
            if char.lower() in "qwrtpsdfghjklzxcvbnm":
                sgl +=1

        print("sogl - " + str(sgl) + " shtyk")
        print("glasn - " + str(gl) + " shtyk")