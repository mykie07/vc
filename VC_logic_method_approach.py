from constraint import *

problem = Problem()
def create_chars():
    problem.addVariable("VC_CHR_GRAPHIC_CARD", ["N-Graphic", "A-Graphic", "Onboard"])
    problem.addVariable("VC_CHR_TYPE", ["Laptop", "Office", "Gaming", "Server"])
    problem.addVariable("VC_CHR_CPU", ["A-CPU", "I-CPU"])
    problem.addVariable("VC_CHR_MAIN_MEMORY", ["2", "4", "8", "16"])
    problem.addVariable("VC_MAT_EQU_SOUND", ["Yes", "No", ])
    problem.addVariable("VC_MAT_EQU_TV", ["Yes", "No", ])
    problem.addVariable("VC_MAT_EQU_MODEM", ["Yes", "No", ])

def create_constraints(VC_CHR_GRAPHIC_CARD=None,
                       VC_CHR_TYPE=None,
                       VC_CHR_CPU=None,
                       VC_CHR_MAIN_MEMORY=None,
                       VC_MAT_EQU_SOUND=None,
                       VC_MAT_EQU_TV=None,
                       VC_MAT_EQU_MODEM=None):
#VC_EX_CON1
    # if VC_MAT_EQU_SOUND == "Yes" or VC_MAT_EQU_TV == "Yes" or VC_MAT_EQU_MODEM == "Yes":
    #     problem.addConstraint(lambda sound, tv, modem, typ:
    #                           (sound == "Yes" or tv == "Yes" or modem == "Yes") and
    #                           (typ != "Server" and typ != "Laptop"),
    #                           ("VC_MAT_EQU_SOUND", "VC_MAT_EQU_TV", "VC_MAT_EQU_MODEM", "VC_CHR_TYPE"))
    #

    #VERSION 2

    if VC_MAT_EQU_SOUND == "Yes" or VC_MAT_EQU_TV == "Yes" or VC_MAT_EQU_MODEM == "Yes":
        problem.addConstraint(lambda xx, typ:

                              (typ != "Server" and typ != "Laptop"),
                              ("VC_MAT_EQU_SOUND","VC_CHR_TYPE")
                              )



#VC_EX_CON2
    # if VC_CHR_MAIN_MEMORY == "8" or VC_CHR_MAIN_MEMORY == "16" or VC_CHR_CPU == "A-CPU":
    #     problem.addConstraint(
    #         lambda memory, cpu, typ:
    #         (memory == "8" or memory == "16" or cpu == "A-CPU") and
    #         typ == "Server",
    #         ("VC_CHR_MAIN_MEMORY", "VC_CHR_CPU", "VC_CHR_TYPE")
    #
    #     )

    #VERSION 2

    if (VC_CHR_MAIN_MEMORY == "8" or VC_CHR_MAIN_MEMORY == "16") and VC_CHR_CPU == "A-CPU":
        problem.addConstraint(
            lambda xx, typ:

            typ == "Server",
            ("VC_CHR_CPU", "VC_CHR_TYPE")


            )

#VC_EX_CON3


    #VERSION 2
    if VC_CHR_GRAPHIC_CARD == "N-Graphic" or VC_CHR_GRAPHIC_CARD == "A-Graphic":
        problem.addConstraint(
            lambda xx, typ:

            typ== "Gaming" or typ == "Laptop",
            ("VC_CHR_CPU", "VC_CHR_TYPE")

        )



#VC_EX_CON4
    if VC_CHR_GRAPHIC_CARD == "Onboard":
        problem.addConstraint(
            lambda xx, typ :

            typ == "Server" or typ == "Office",
            ("VC_CHR_CPU", "VC_CHR_TYPE")

        )







if __name__ == "__main__":
    create_chars()
    create_constraints(
                    VC_CHR_GRAPHIC_CARD="N-Graphic",
                    VC_CHR_TYPE=None,
                    VC_CHR_CPU="A-CPU",
                    VC_CHR_MAIN_MEMORY="8",
                    VC_MAT_EQU_SOUND="Yes",
                    VC_MAT_EQU_TV=None,
                    VC_MAT_EQU_MODEM=None)

    results = problem.getSolutions()

    for x in results[:]:
        print(x)

    print(len(results))
