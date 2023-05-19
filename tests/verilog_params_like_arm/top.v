
`include "param.v"

module top
(
  input wire      ib_clk,
  input wire      [15:0] iv16_numA,
  input wire      [15:0] iv16_numB,
  input wire      [15:0] iv16_numC,
  output wire     [15:0] ov16_numA,
  output wire     [15:0] ov16_numB
);
  inst `PAR_INST_A i_inst_A (
    .ib_clk(ib_clk),
    .iv16_numA(iv16_numA),
    .iv16_numB(iv16_numB),
    .iv16_numC(iv16_numC),
    .ov16_num(ov16_numA)
  );
  inst `PAR_INST_B i_inst_B (
    .ib_clk(ib_clk),
    .iv16_numA(iv16_numA),
    .iv16_numB(iv16_numB),
    .iv16_numC(iv16_numC),
    .ov16_num(ov16_numB)
  );

endmodule

