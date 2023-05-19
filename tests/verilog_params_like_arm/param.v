
`define PAR_A 6

`define PAR_DECL #( parameter PAR_A = 1, \
                    parameter PAR_B = 2, \
                    parameter PAR_C = 0)

`define PAR_INST_A #( .PAR_A   (`PAR_A), \
                      .PAR_B   (8), \
                      .PAR_C   (`PAR_C))

`define PAR_INST_B #( .PAR_A   (`PAR_C), \
                      .PAR_B   (`PAR_C), \
                      .PAR_C   (`PAR_A))

`define PAR_C 4

