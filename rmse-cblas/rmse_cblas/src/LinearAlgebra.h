#pragma once

#include <vector>

class LinearAlgebra {
public:
  static double
  rmseBlas(const std::vector<double> &a,
             const std::vector<double> &b);
};
