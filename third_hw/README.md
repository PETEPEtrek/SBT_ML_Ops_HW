Отчет по модели distilber-base-case (output_dim=96)

Всего FLOPS: 2720759808
Backbone: 2720464896 FLOPS - ограничен памятью до batch_size = 11
FC layer: 294912 FLOPS - ограничен памятью до batch_size = 78





Различия между эмбеддингами .plan и .onnx:

FP16: 0.00062
FP32: 0.00010
INT8: 0.31913
BEST: 0.00062




Throughout и latency:

ONNX:
Inferences/Second vs. Client Average Batch Latency
Concurrency: 1, throughput: 452.866 infer/sec, latency 2206 usec
Concurrency: 2, throughput: 597.334 infer/sec, latency 3346 usec
Concurrency: 3, throughput: 603.644 infer/sec, latency 4967 usec
Concurrency: 4, throughput: 612.276 infer/sec, latency 6530 usec
Concurrency: 5, throughput: 605.86 infer/sec, latency 8250 usec
Concurrency: 6, throughput: 596.501 infer/sec, latency 10056 usec
Concurrency: 7, throughput: 589.377 infer/sec, latency 11875 usec
Concurrency: 8, throughput: 574.044 infer/sec, latency 13935 usec
Concurrency: 9, throughput: 605.491 infer/sec, latency 14862 usec
Concurrency: 10, throughput: 610.146 infer/sec, latency 16386 usec
Concurrency: 11, throughput: 622.489 infer/sec, latency 17668 usec
Concurrency: 12, throughput: 625.655 infer/sec, latency 19176 usec
Concurrency: 13, throughput: 615.384 infer/sec, latency 21123 usec
Concurrency: 14, throughput: 605.18 infer/sec, latency 23130 usec
Concurrency: 15, throughput: 607.167 infer/sec, latency 24701 usec
Concurrency: 16, throughput: 605.967 infer/sec, latency 26401 usec
Concurrency: 17, throughput: 600.06 infer/sec, latency 28325 usec
Concurrency: 18, throughput: 604.06 infer/sec, latency 29795 usec
Concurrency: 19, throughput: 613.589 infer/sec, latency 30961 usec
Concurrency: 20, throughput: 608.969 infer/sec, latency 32836 usec
Concurrency: 21, throughput: 590.925 infer/sec, latency 35533 usec
Concurrency: 22, throughput: 598.259 infer/sec, latency 36768 usec
Concurrency: 23, throughput: 605.554 infer/sec, latency 37975 usec
Concurrency: 24, throughput: 586.053 infer/sec, latency 40941 usec
Concurrency: 25, throughput: 583.339 infer/sec, latency 42852 usec
Concurrency: 26, throughput: 586.92 infer/sec, latency 44291 usec
Concurrency: 27, throughput: 592.826 infer/sec, latency 45540 usec
Concurrency: 28, throughput: 587.813 infer/sec, latency 47630 usec
Concurrency: 29, throughput: 607.159 infer/sec, latency 47760 usec
Concurrency: 30, throughput: 602.371 infer/sec, latency 49801 usec
Concurrency: 31, throughput: 605.28 infer/sec, latency 51207 usec
Concurrency: 32, throughput: 606.921 infer/sec, latency 52714 usec

FP32:
Inferences/Second vs. Client Average Batch Latency
Concurrency: 1, throughput: 772.947 infer/sec, latency 1292 usec
Concurrency: 2, throughput: 1251.12 infer/sec, latency 1597 usec
Concurrency: 3, throughput: 1728.41 infer/sec, latency 1733 usec
Concurrency: 4, throughput: 2313.71 infer/sec, latency 1727 usec
Concurrency: 5, throughput: 2784.55 infer/sec, latency 1794 usec
Concurrency: 6, throughput: 3302.72 infer/sec, latency 1815 usec
Concurrency: 7, throughput: 3899.32 infer/sec, latency 1793 usec
Concurrency: 8, throughput: 3916 infer/sec, latency 2041 usec
Concurrency: 9, throughput: 4082.87 infer/sec, latency 2202 usec
Concurrency: 10, throughput: 4273.75 infer/sec, latency 2338 usec
Concurrency: 11, throughput: 4343.8 infer/sec, latency 2530 usec
Concurrency: 12, throughput: 4772.58 infer/sec, latency 2512 usec
Concurrency: 13, throughput: 5067.36 infer/sec, latency 2563 usec
Concurrency: 14, throughput: 5503.68 infer/sec, latency 2542 usec
Concurrency: 15, throughput: 5806.13 infer/sec, latency 2582 usec
Concurrency: 16, throughput: 6539.57 infer/sec, latency 2445 usec
Concurrency: 17, throughput: 6575.95 infer/sec, latency 2583 usec
Concurrency: 18, throughput: 6520.46 infer/sec, latency 2758 usec
Concurrency: 19, throughput: 6523.06 infer/sec, latency 2911 usec
Concurrency: 20, throughput: 6459.09 infer/sec, latency 3094 usec
Concurrency: 21, throughput: 6559.34 infer/sec, latency 3200 usec
Concurrency: 22, throughput: 6461.57 infer/sec, latency 3403 usec
Concurrency: 23, throughput: 6463.3 infer/sec, latency 3556 usec
Concurrency: 24, throughput: 6389.8 infer/sec, latency 3754 usec
Concurrency: 25, throughput: 6394.46 infer/sec, latency 3907 usec
Concurrency: 26, throughput: 6505.9 infer/sec, latency 3994 usec
Concurrency: 27, throughput: 6472.54 infer/sec, latency 4169 usec
Concurrency: 28, throughput: 6436.24 infer/sec, latency 4348 usec
Concurrency: 29, throughput: 6454.85 infer/sec, latency 4491 usec
Concurrency: 30, throughput: 6462.6 infer/sec, latency 4640 usec
Concurrency: 31, throughput: 6401.62 infer/sec, latency 4840 usec
Concurrency: 32, throughput: 6460.57 infer/sec, latency 4951 usec

FP16:
Inferences/Second vs. Client Average Batch Latency
Concurrency: 1, throughput: 1024.46 infer/sec, latency 975 usec
Concurrency: 2, throughput: 1852.62 infer/sec, latency 1078 usec
Concurrency: 3, throughput: 2644.07 infer/sec, latency 1133 usec
Concurrency: 4, throughput: 3460.49 infer/sec, latency 1154 usec
Concurrency: 5, throughput: 3941.02 infer/sec, latency 1267 usec
Concurrency: 6, throughput: 4744.1 infer/sec, latency 1263 usec
Concurrency: 7, throughput: 5159.18 infer/sec, latency 1355 usec
Concurrency: 8, throughput: 5750.92 infer/sec, latency 1389 usec
Concurrency: 9, throughput: 6080.96 infer/sec, latency 1478 usec
Concurrency: 10, throughput: 6776.27 infer/sec, latency 1474 usec
Concurrency: 11, throughput: 6890.92 infer/sec, latency 1595 usec
Concurrency: 12, throughput: 7681.44 infer/sec, latency 1560 usec
Concurrency: 13, throughput: 7999.64 infer/sec, latency 1623 usec
Concurrency: 14, throughput: 8745.48 infer/sec, latency 1599 usec
Concurrency: 15, throughput: 9059.09 infer/sec, latency 1654 usec
Concurrency: 16, throughput: 10095.6 infer/sec, latency 1583 usec
Concurrency: 17, throughput: 10358.4 infer/sec, latency 1639 usec
Concurrency: 18, throughput: 10592.5 infer/sec, latency 1698 usec
Concurrency: 19, throughput: 10527.9 infer/sec, latency 1803 usec
Concurrency: 20, throughput: 10646.9 infer/sec, latency 1877 usec
Concurrency: 21, throughput: 10782.6 infer/sec, latency 1946 usec
Concurrency: 22, throughput: 10845.8 infer/sec, latency 2027 usec
Concurrency: 23, throughput: 10805.7 infer/sec, latency 2127 usec
Concurrency: 24, throughput: 10860.8 infer/sec, latency 2208 usec
Concurrency: 25, throughput: 10862.3 infer/sec, latency 2300 usec
Concurrency: 26, throughput: 10898.9 infer/sec, latency 2384 usec
Concurrency: 27, throughput: 10960.6 infer/sec, latency 2462 usec
Concurrency: 28, throughput: 10876.2 infer/sec, latency 2573 usec
Concurrency: 29, throughput: 10774.6 infer/sec, latency 2690 usec
Concurrency: 30, throughput: 10953.3 infer/sec, latency 2737 usec
Concurrency: 31, throughput: 10919.9 infer/sec, latency 2837 usec
Concurrency: 32, throughput: 11034.3 infer/sec, latency 2898 usec

INT8:
Inferences/Second vs. Client Average Batch Latency
Concurrency: 1, throughput: 654.26 infer/sec, latency 1527 usec
Concurrency: 2, throughput: 1108.77 infer/sec, latency 1802 usec
Concurrency: 3, throughput: 286.262 infer/sec, latency 10474 usec
Concurrency: 4, throughput: 384.83 infer/sec, latency 10388 usec
Concurrency: 5, throughput: 478.81 infer/sec, latency 10441 usec
Concurrency: 6, throughput: 564.359 infer/sec, latency 10629 usec
Concurrency: 7, throughput: 686.537 infer/sec, latency 10197 usec
Concurrency: 8, throughput: 761.961 infer/sec, latency 10496 usec
Concurrency: 9, throughput: 889.787 infer/sec, latency 10112 usec
Concurrency: 10, throughput: 957.239 infer/sec, latency 10446 usec
Concurrency: 11, throughput: 1092.44 infer/sec, latency 10067 usec
Concurrency: 12, throughput: 1134.94 infer/sec, latency 10573 usec
Concurrency: 13, throughput: 1211.86 infer/sec, latency 10726 usec
Concurrency: 14, throughput: 1272.86 infer/sec, latency 10994 usec
Concurrency: 15, throughput: 1367.96 infer/sec, latency 10961 usec
Concurrency: 16, throughput: 5734.83 infer/sec, latency 2789 usec
Concurrency: 17, throughput: 6426.91 infer/sec, latency 2643 usec
Concurrency: 18, throughput: 7339 infer/sec, latency 2451 usec
Concurrency: 19, throughput: 7187.73 infer/sec, latency 2642 usec
Concurrency: 20, throughput: 6961.16 infer/sec, latency 2871 usec
Concurrency: 21, throughput: 7268.08 infer/sec, latency 2888 usec
Concurrency: 22, throughput: 7741.77 infer/sec, latency 2840 usec
Concurrency: 23, throughput: 7882.45 infer/sec, latency 2916 usec
Concurrency: 24, throughput: 7493.44 infer/sec, latency 3201 usec
Concurrency: 25, throughput: 7791.44 infer/sec, latency 3207 usec
Concurrency: 26, throughput: 7824.36 infer/sec, latency 3321 usec
Concurrency: 27, throughput: 7702.83 infer/sec, latency 3503 usec
Concurrency: 28, throughput: 7924.59 infer/sec, latency 3531 usec
Concurrency: 29, throughput: 8027.71 infer/sec, latency 3611 usec
Concurrency: 30, throughput: 7971.93 infer/sec, latency 3761 usec
Concurrency: 31, throughput: 8100.36 infer/sec, latency 3825 usec
Concurrency: 32, throughput: 8079.96 infer/sec, latency 3959 usec

BEST:
Inferences/Second vs. Client Average Batch Latency
Concurrency: 1, throughput: 940.876 infer/sec, latency 1061 usec
Concurrency: 2, throughput: 1885.98 infer/sec, latency 1059 usec
Concurrency: 3, throughput: 2550.93 infer/sec, latency 1174 usec
Concurrency: 4, throughput: 3561.57 infer/sec, latency 1121 usec
Concurrency: 5, throughput: 4253.61 infer/sec, latency 1174 usec
Concurrency: 6, throughput: 5017.61 infer/sec, latency 1194 usec
Concurrency: 7, throughput: 5649.86 infer/sec, latency 1237 usec
Concurrency: 8, throughput: 6372.52 infer/sec, latency 1254 usec
Concurrency: 9, throughput: 6541.65 infer/sec, latency 1374 usec
Concurrency: 10, throughput: 7115.18 infer/sec, latency 1404 usec
Concurrency: 11, throughput: 7464.06 infer/sec, latency 1472 usec
Concurrency: 12, throughput: 8227.77 infer/sec, latency 1457 usec
Concurrency: 13, throughput: 8428.55 infer/sec, latency 1541 usec
Concurrency: 14, throughput: 9159.84 infer/sec, latency 1527 usec
Concurrency: 15, throughput: 9461.63 infer/sec, latency 1584 usec
Concurrency: 16, throughput: 10249.6 infer/sec, latency 1559 usec
Concurrency: 17, throughput: 10537.2 infer/sec, latency 1611 usec
Concurrency: 18, throughput: 10812 infer/sec, latency 1663 usec
Concurrency: 19, throughput: 10696.2 infer/sec, latency 1774 usec
Concurrency: 20, throughput: 10860.2 infer/sec, latency 1840 usec
Concurrency: 21, throughput: 10886.5 infer/sec, latency 1927 usec
Concurrency: 22, throughput: 10808.5 infer/sec, latency 2034 usec
Concurrency: 23, throughput: 10840.7 infer/sec, latency 2120 usec
Concurrency: 24, throughput: 10719.5 infer/sec, latency 2237 usec
Concurrency: 25, throughput: 10745.8 infer/sec, latency 2325 usec
Concurrency: 26, throughput: 10883.5 infer/sec, latency 2387 usec
Concurrency: 27, throughput: 11088.9 infer/sec, latency 2433 usec
Concurrency: 28, throughput: 11164 infer/sec, latency 2506 usec
Concurrency: 29, throughput: 10945.7 infer/sec, latency 2648 usec
Concurrency: 30, throughput: 11157.1 infer/sec, latency 2687 usec
Concurrency: 31, throughput: 11217.9 infer/sec, latency 2762 usec
Concurrency: 32, throughput: 10860.2 infer/sec, latency 2945 usec