`ifndef PARAMS_UNDEFINE

`define PAR_GLB_DATA_BITS 7

`define PART_1 8'b1000_0001, 8'b0000_0001, 8'b1000_0000
`define PART_2 8'b0100_0010, 8'b0000_0010, 8'b0100_0000
`define PART_3 8'b0010_0100, 8'b0000_0100, 8'b0010_0000
`define PART_4 8'b0001_1000, 8'b0000_1000, 8'b0001_0000

`define PARTS `PART_1, `PART_2, \
`PART_3, `PART_4

`else // PARAMS_UNDEFINE

`undef PAR_GLB_DATA_BITS
`undef PART_1
`undef PART_2
`undef PART_3
`undef PART_4
`undef PARTS

`endif // PARAMS_UNDEFINE

